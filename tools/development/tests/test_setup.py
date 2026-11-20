# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Validate development setup with isolated roots and fake package/tool commands."""
from __future__ import annotations

import hashlib
import importlib.util
import io
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts/bootstrap"))
import common
import host
import packages
import toolchain

SPEC = importlib.util.spec_from_file_location("morgana_setup", ROOT / "scripts/bootstrap/main.py")
assert SPEC is not None and SPEC.loader is not None
setup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(setup)


def result(status: int = 0, output: str = "") -> subprocess.CompletedProcess[str]:
    """Return a controlled command result with no process or host side effects."""
    return subprocess.CompletedProcess([], status, stdout=output, stderr="")


def snapshot(root: Path) -> dict[str, tuple[object, ...]]:
    """Snapshot names, contents, modes and modification times without mutating data."""
    values = {}
    for path in root.rglob("*"):
        state = path.lstat()
        content = path.readlink() if path.is_symlink() else path.read_bytes() if path.is_file() else None
        values[str(path.relative_to(root))] = (state.st_mode, state.st_mtime_ns, content)
    return values


class Response(io.BytesIO):
    """In-memory HTTPS response used instead of contacting a download server."""

    def geturl(self) -> str:
        """Return the synthetic response's HTTPS origin without network access."""
        return toolchain.RUSTUP_URL


class SetupTests(unittest.TestCase):
    """Own one temporary checkout; tests never install on the actual host."""

    def setUp(self) -> None:
        """Create source/command fixtures and isolate caller tool-root overrides."""
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for relative in ("install.sh", "rust-toolchain.toml", "Cargo.toml", "Cargo.lock"):
            shutil.copyfile(ROOT / relative, self.root / relative)
        shutil.copytree(ROOT / "scripts/bootstrap", self.root / "scripts/bootstrap",
                        ignore=shutil.ignore_patterns("__pycache__"))
        self.bin = self.root / "fake-bin"
        self.bin.mkdir()
        self.fake("dpkg-query", "printf 'install ok installed'")
        for name in ("sudo", "apt-get", "curl"):
            self.fake(name, 'echo "forbidden mutator invoked" >&2; exit 99')
        self.environment = dict(os.environ, PATH=f"{self.bin}:{os.environ['PATH']}", PYTHONDONTWRITEBYTECODE="1")
        self.environment.pop("CARGO_HOME", None)
        self.environment.pop("RUSTUP_HOME", None)
        self.environment_patch = patch.dict(os.environ, self.environment, clear=True)
        self.environment_patch.start()
        self.addCleanup(self.environment_patch.stop)

    def fake(self, name: str, body: str) -> None:
        """Write an executable command only into this fixture's fake PATH."""
        path = self.bin / name
        path.write_text(f"#!/bin/bash\n{body}\n")
        path.chmod(0o755)

    def ready_tools(self) -> Path:
        """Create passive pinned binaries and managers that fail if probed lazily."""
        proxy = self.root / "local/cargo/bin"
        proxy.mkdir(parents=True)
        for name in ("rustup", "cargo"):
            path = proxy / name
            path.write_text('#!/bin/bash\necho lazy > "' + str(self.root / "forbidden") + '"\nexit 99\n')
            path.chmod(0o755)
        directory = toolchain.tool_bin(self.root, "1.85.1")
        directory.mkdir(parents=True)
        for name in ("rustc", "cargo", "rustfmt", "clippy-driver"):
            path = directory / name
            path.write_text(f"#!/bin/bash\nprintf '{name} 1.85.1 (fixture)\\n'\n")
            path.chmod(0o755)
        return directory

    def cli(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        """Run the public dispatcher from outside its checkout with a finite timeout."""
        return subprocess.run(["bash", str(self.root / "install.sh"), *arguments],
                              cwd=ROOT, env=self.environment, text=True, capture_output=True, timeout=20)

    def admitted(self):
        """Mock only platform admission for portable control-flow tests."""
        return patch.object(setup, "detect_host", return_value=host.Host("22.04"))

    def test_help_and_invalid_arguments_never_write(self) -> None:
        """No action, unknown/conflicting flags and help preserve the entire fixture."""
        before = snapshot(self.root)
        self.assertEqual(self.cli("--help").returncode, 0)
        for arguments in ((), ("--check",), ("--unknown",),
                          ("--development", "--check", "--dry-run"), ("--development", "--unknown")):
            self.assertEqual(self.cli(*arguments).returncode, 2)
        self.assertEqual(snapshot(self.root), before)

    def test_missing_tools_inspection_never_writes_or_installs(self) -> None:
        """Empty local roots yield missing/plan statuses without lazy setup."""
        self.fake("dpkg-query", "exit 1")
        before = snapshot(self.root)
        with self.admitted():
            self.assertEqual(setup.run(["--development", "--check"], self.root), 1)
            self.assertEqual(setup.run(["--development", "--dry-run"], self.root), 0)
        self.assertEqual(snapshot(self.root), before)

    def test_public_ready_check_and_plan_use_only_installed_binaries(self) -> None:
        """Configured Ubuntu host inspection bypasses rustup/proxy auto-install paths."""
        if sys.platform != "linux" or 'ID=ubuntu' not in Path('/etc/os-release').read_text():
            self.skipTest("public fixture admission is an Ubuntu integration case")
        self.ready_tools()
        before = snapshot(self.root)
        for flag in ("--check", "--dry-run"):
            completed = self.cli("--development", flag)
            self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(snapshot(self.root), before)
        self.assertFalse((self.root / "forbidden").exists())

    def test_component_missing_and_wrong_rust_version_are_unready(self) -> None:
        """File presence alone cannot establish the pinned compiler/component contract."""
        directory = self.ready_tools()
        environment = toolchain.local_environment(self.root)
        self.assertTrue(toolchain.ready(self.root, "1.85.1", environment))
        (directory / "rustfmt").unlink()
        self.assertFalse(toolchain.ready(self.root, "1.85.1", environment))
        (directory / "rustc").write_text("#!/bin/bash\necho 'rustc 1.84.0 (wrong)'\n")
        self.assertFalse(toolchain.ready(self.root, "1.85.1", environment))

    def test_host_mapping_requires_explicit_supported_platform(self) -> None:
        """Both Ubuntu mappings admit; unsupported kernel/CPU/distro/version reject."""
        for release in ("22.04", "24.04"):
            self.assertEqual(host.validate_host("Linux", "x86_64", f'ID=ubuntu\nVERSION_ID="{release}"').release, release)
        for system, machine, text in (("Darwin", "x86_64", "ID=ubuntu\nVERSION_ID=22.04"),
                                      ("Linux", "aarch64", "ID=ubuntu\nVERSION_ID=22.04"),
                                      ("Linux", "x86_64", "ID=debian\nVERSION_ID=22.04"),
                                      ("Linux", "x86_64", "ID=ubuntu\nVERSION_ID=26.04")):
            with self.assertRaises(common.SetupError):
                host.validate_host(system, machine, text)

    def test_redirected_local_roots_reject_without_external_writes(self) -> None:
        """A symlinked destination cannot redirect an installer into another checkout."""
        with tempfile.TemporaryDirectory() as outside:
            self.root.joinpath("local").symlink_to(outside, target_is_directory=True)
            before = snapshot(Path(outside))
            with self.assertRaises(common.SetupError):
                toolchain.local_environment(self.root)
            self.assertEqual(snapshot(Path(outside)), before)

    def test_conflicting_environment_root_is_rejected(self) -> None:
        """Setup does not silently use or overwrite a caller's unrelated Cargo root."""
        with patch.dict(os.environ, CARGO_HOME=str(self.root / "external-cargo")):
            with self.assertRaises(common.SetupError):
                toolchain.local_environment(self.root)

    def test_missing_or_floating_toolchain_pin_rejects_before_transactions(self) -> None:
        """Invalid pin and missing locks cannot reach package installation."""
        (self.root / "rust-toolchain.toml").write_text('[toolchain]\nchannel = "stable"\n')
        with self.admitted(), patch.object(setup, "install_missing") as install:
            self.assertEqual(setup.run(["--development"], self.root), 2)
            install.assert_not_called()
        shutil.copyfile(ROOT / "rust-toolchain.toml", self.root / "rust-toolchain.toml")
        (self.root / "Cargo.lock").unlink()
        with self.admitted(), patch.object(setup, "missing_packages") as inspect:
            self.assertEqual(setup.run(["--development"], self.root), 2)
            inspect.assert_not_called()

    def test_package_queries_are_deduplicated_and_unexpected_failures_propagate(self) -> None:
        """One query per package; a broken package database is not reported ready."""
        with patch.object(packages, "command", return_value=result(1)) as query:
            self.assertEqual(packages.missing_packages(self.root, ("git", "git", "python3")), ("git", "python3"))
            self.assertEqual(query.call_count, 2)
        with patch.object(packages, "command", return_value=result(2)):
            with self.assertRaises(common.SetupError):
                packages.missing_packages(self.root)

    def test_no_missing_packages_skips_all_package_transactions(self) -> None:
        """Repeated complete package setup does not refresh indexes or elevate."""
        with patch.object(packages, "command") as execute:
            packages.install_missing(self.root, ())
            execute.assert_not_called()

    def test_package_failure_stops_before_install_transaction(self) -> None:
        """An unavailable candidate stops after index refresh, before apt install."""
        with patch.object(packages, "command", side_effect=[result(), result(1)]) as execute:
            with self.assertRaises(common.SetupError):
                packages.install_missing(self.root, ("git",))
            self.assertEqual(execute.call_count, 2)
            self.assertEqual(execute.call_args_list[0].args[0], ["sudo", "apt-get", "update"])

    def test_ready_toolchain_install_is_a_noop(self) -> None:
        """An already-complete pin does not bootstrap, install or create roots."""
        before = snapshot(self.root)
        with patch.object(toolchain, "ready", return_value=True), patch.object(toolchain, "command") as execute:
            toolchain.install(self.root, "1.85.1", toolchain.local_environment(self.root))
            execute.assert_not_called()
        self.assertEqual(snapshot(self.root), before)

    def test_missing_toolchain_uses_verified_bootstrap_and_exact_pin(self) -> None:
        """Mocked local install verifies bootstrap first and requests exact components."""
        environment = toolchain.local_environment(self.root)
        with patch.object(toolchain, "ready", side_effect=[False, True]), \
                patch.object(toolchain, "download_bootstrap") as download, \
                patch.object(toolchain, "command", return_value=result()) as execute:
            toolchain.install(self.root, "1.85.1", environment)
            download.assert_called_once()
            self.assertEqual(execute.call_count, 2)
            bootstrap = execute.call_args_list[0].args[0]
            self.assertIn("--no-modify-path", bootstrap)
            self.assertEqual(bootstrap[-2:], ["--default-toolchain", "none"])
            selected = execute.call_args_list[1].args[0]
            self.assertEqual(selected[1:4], ["toolchain", "install", "1.85.1"])
            self.assertIn("rustfmt", selected)
            self.assertIn("clippy", selected)
            self.assertIn("--no-self-update", selected)
        self.assertEqual(list((self.root / "local").glob("development-setup-*")), [])

    def test_bootstrap_verification_failure_prevents_any_execution(self) -> None:
        """An unverified bootstrap is never run and operation temporary data is cleaned."""
        environment = toolchain.local_environment(self.root)
        with patch.object(toolchain, "ready", return_value=False), \
                patch.object(toolchain, "download_bootstrap", side_effect=common.SetupError("digest mismatch")), \
                patch.object(toolchain, "command") as execute:
            with self.assertRaises(common.SetupError):
                toolchain.install(self.root, "1.85.1", environment)
            execute.assert_not_called()
        self.assertEqual(list((self.root / "local").glob("development-setup-*")), [])

    def test_apply_order_keeps_locked_fetch_separate_from_builds(self) -> None:
        """Mocked apply installs requirements then fetches the exact locked host target."""
        with self.admitted(), patch.object(setup.os, "geteuid", return_value=1000), \
                patch.object(setup, "missing_packages", side_effect=[("git",), ()]), \
                patch.object(toolchain, "ready", side_effect=[False, True]), \
                patch.object(setup, "install_missing") as apt, \
                patch.object(toolchain, "install") as rust, \
                patch.object(setup, "command", return_value=result()) as fetch:
            self.assertEqual(setup.run(["--development"], self.root), 0)
            apt.assert_called_once_with(self.root, ("git",))
            rust.assert_called_once()
            arguments = fetch.call_args.args[0]
            self.assertIn("--locked", arguments)
            self.assertEqual(arguments[-2:], ["--target", host.HOST_TARGET])
            self.assertEqual(arguments[1], "fetch")
            self.assertEqual(fetch.call_args.args[2]["CARGO_NET_OFFLINE"], "false")

    def test_root_apply_and_failed_fetch_stop_with_nonzero_status(self) -> None:
        """Root installation and failed dependency acquisition cannot report success."""
        with self.admitted(), patch.object(setup, "missing_packages", return_value=()), \
                patch.object(toolchain, "ready", return_value=True), \
                patch.object(setup.os, "geteuid", return_value=0), patch.object(setup, "install_missing") as apt:
            self.assertEqual(setup.run(["--development"], self.root), 2)
            apt.assert_not_called()
        with self.admitted(), patch.object(setup, "missing_packages", return_value=()), \
                patch.object(toolchain, "ready", return_value=True), \
                patch.object(setup.os, "geteuid", return_value=1000), \
                patch.object(setup, "install_missing"), patch.object(toolchain, "install"), \
                patch.object(setup, "command", return_value=result(7)):
            self.assertEqual(setup.run(["--development"], self.root), 2)

    def test_verified_bootstrap_and_checksum_rejection(self) -> None:
        """Only matching fixture bytes become executable; mismatches remain untrusted."""
        content = b"synthetic bootstrap, never executed"
        destination = self.root / "bootstrap"
        with patch.object(toolchain.urllib.request, "urlopen", return_value=Response(content)), \
                patch.object(toolchain, "RUSTUP_SHA256", hashlib.sha256(content).hexdigest()):
            toolchain.download_bootstrap(destination)
        self.assertEqual(destination.read_bytes(), content)
        self.assertTrue(os.access(destination, os.X_OK))
        bad = self.root / "bad-bootstrap"
        with patch.object(toolchain.urllib.request, "urlopen", return_value=Response(content)):
            with self.assertRaises(common.SetupError):
                toolchain.download_bootstrap(bad)
        self.assertFalse(os.access(bad, os.X_OK))

    def test_bootstrap_size_deadline_and_no_clobber_bounds(self) -> None:
        """Oversized/slow/existing download destinations cannot be promoted or overwritten."""
        with patch.object(toolchain.urllib.request, "urlopen", return_value=Response(b"12345")), \
                patch.object(toolchain, "MAX_BOOTSTRAP_BYTES", 4):
            with self.assertRaises(common.SetupError):
                toolchain.download_bootstrap(self.root / "too-big")
        with patch.object(toolchain.urllib.request, "urlopen", return_value=Response(b"12345")), \
                patch.object(toolchain.time, "monotonic", side_effect=[0, 121]):
            with self.assertRaises(common.SetupError):
                toolchain.download_bootstrap(self.root / "too-slow")
        existing = self.root / "keep"
        existing.write_bytes(b"original")
        with patch.object(toolchain.urllib.request, "urlopen", return_value=Response(b"new")):
            with self.assertRaises(common.SetupError):
                toolchain.download_bootstrap(existing)
        self.assertEqual(existing.read_bytes(), b"original")

    def test_subprocess_timeout_is_a_setup_failure(self) -> None:
        """Bounded command failures remain explicit without implicit retry."""
        with patch.object(common.subprocess, "run", side_effect=subprocess.TimeoutExpired("fixture", 1)):
            with self.assertRaises(common.SetupError):
                common.command(["fixture"], self.root, timeout=1)


if __name__ == "__main__":
    unittest.main()
