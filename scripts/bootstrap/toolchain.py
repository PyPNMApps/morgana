# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Exact local Rust readiness and explicitly requested verified installation."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import re
import tempfile
import time
import urllib.request

from common import SetupError, command, require_success
from host import HOST_TARGET

RUSTUP_VERSION = "1.28.2"
RUSTUP_URL = f"https://static.rust-lang.org/rustup/archive/{RUSTUP_VERSION}/{HOST_TARGET}/rustup-init"
RUSTUP_SHA256 = "20a06e644b0d9bd2fbdbfd52d42540bdde820ea7df86e92e533c073da0cdd43c"
MAX_BOOTSTRAP_BYTES = 32 * 1024 * 1024
DOWNLOAD_TIMEOUT_SECONDS = 120


def rust_version(root: Path) -> str:
    """Read the exact toolchain pin before permitting setup operations.

    Takes the repository root and returns its numeric major.minor.patch channel.
    Requires the project's minimal profile and rustfmt/Clippy components; malformed
    or unpinned manifests raise SetupError. This operation never changes the file.
    """
    try:
        text = (root / "rust-toolchain.toml").read_text()
    except OSError as error:
        raise SetupError("Missing rust-toolchain.toml") from error
    # Whole-line pin extraction: channel = "1.85.1" captures 1.85.1 only.
    # Floating channels, comments inside the quoted value and duplicate pins fail.
    versions = re.findall(r'^channel\s*=\s*"([0-9]+\.[0-9]+\.[0-9]+)"\s*$', text, re.MULTILINE)
    if (len(versions) != 1 or '[toolchain]' not in text or 'profile = "minimal"' not in text
            or '"rustfmt"' not in text or '"clippy"' not in text):
        raise SetupError("Expected one exact Rust pin, minimal profile and rustfmt/Clippy components")
    return versions[0]


def local_environment(root: Path) -> dict[str, str]:
    """Validate owned tool roots and prepare a process-local isolated environment.

    Takes the root and returns an environment copy. No directories are created.
    Rejects external root/proxy redirection or conflicting Cargo/rustup overrides.
    Auto-install/update checks and Cargo networking are disabled for inspection.
    """
    root = root.resolve()
    for relative in ("local", "local/cargo", "local/rustup", "local/cargo/bin",
                     "local/rustup/toolchains", "local/cargo/bin/rustup", "local/cargo/bin/cargo"):
        if not (root / relative).resolve().is_relative_to(root):
            raise SetupError(f"Refusing redirected local tool path: {relative}")
    environment = os.environ.copy()
    for key, relative in (("CARGO_HOME", "local/cargo"), ("RUSTUP_HOME", "local/rustup")):
        destination = root / relative
        if key in environment and Path(environment[key]).resolve() != destination.resolve():
            raise SetupError(f"Unset conflicting {key} before project-local setup")
        environment[key] = str(destination)
    environment.update(RUSTUP_AUTO_INSTALL="0", RUSTUP_NO_UPDATE_CHECK="1", CARGO_NET_OFFLINE="true")
    environment["PATH"] = str(root / "local/cargo/bin") + os.pathsep + environment.get("PATH", "")
    return environment


def tool_bin(root: Path, version: str) -> Path:
    """Return the pinned local tool directory without creating it.

    Accepts validated root/version and returns the expected Linux toolchain bin
    path. Redirected toolchain destinations raise SetupError before execution.
    """
    directory = root / f"local/rustup/toolchains/{version}-{HOST_TARGET}/bin"
    if not directory.resolve().is_relative_to(root.resolve()):
        raise SetupError("Refusing redirected pinned toolchain")
    return directory


def ready(root: Path, version: str, environment: dict[str, str]) -> bool:
    """Check exact installed binaries directly, avoiding rustup's lazy downloads.

    Takes validated root/pin/environment and returns readiness for rustc, Cargo,
    rustfmt and Clippy plus the local manager/proxy. Missing tools return false.
    Unexpected command failures are unready; no installation or writes occur.
    """
    for relative in ("local/cargo/bin/rustup", "local/cargo/bin/cargo"):
        if not os.access(root / relative, os.X_OK):
            return False
    directory = tool_bin(root, version)
    for executable in ("rustc", "cargo", "rustfmt", "clippy-driver"):
        binary = directory / executable
        if not binary.resolve().is_relative_to(root.resolve()):
            raise SetupError("Refusing redirected tool executable")
        if not os.access(binary, os.X_OK):
            return False
        result = command([str(binary), "--version"], root, environment, timeout=10)
        if result.returncode != 0 or (executable == "rustc" and not result.stdout.startswith(f"rustc {version} ")):
            return False
    return True


def download_bootstrap(destination: Path) -> None:
    """Download the pinned HTTPS bootstrap into a new operation-owned file.

    Takes a new temporary destination. Streams at most MAX_BOOTSTRAP_BYTES with a
    finite network timeout and verifies the tracked SHA-256 before executable mode.
    HTTP/size/digest/output failures raise SetupError; nothing is executed here.
    """
    try:
        deadline = time.monotonic() + DOWNLOAD_TIMEOUT_SECONDS
        with urllib.request.urlopen(RUSTUP_URL, timeout=15) as response:
            if not response.geturl().startswith("https://"):
                raise SetupError("Rustup bootstrap redirected away from HTTPS")
            digest = hashlib.sha256()
            size = 0
            with destination.open("xb") as output:
                while True:
                    if time.monotonic() > deadline:
                        raise SetupError("Rustup bootstrap exceeded its download deadline")
                    chunk = response.read(64 * 1024)
                    if not chunk:
                        break
                    size += len(chunk)
                    if size > MAX_BOOTSTRAP_BYTES:
                        raise SetupError("Rustup bootstrap exceeds download bound")
                    digest.update(chunk)
                    output.write(chunk)
        if digest.hexdigest() != RUSTUP_SHA256:
            raise SetupError("Rustup bootstrap SHA-256 mismatch")
        destination.chmod(0o700)
    except (OSError, ValueError) as error:
        raise SetupError(f"Cannot download verified rustup bootstrap: {error}") from error


def install(root: Path, version: str, environment: dict[str, str]) -> None:
    """Install only missing pinned local Rust; preserve external/user toolchains.

    Accepts validated root/version/environment after host packages are ready.
    Uses an operation-owned temporary directory and verified bootstrap only if
    the local manager is absent. Failures raise SetupError; retained tools/caches
    are never deleted, and no shell startup file or application is installed.
    """
    if ready(root, version, environment):
        return
    local = root / "local"
    local.mkdir(exist_ok=True)
    manager = local / "cargo/bin/rustup"
    if not os.access(manager, os.X_OK):
        with tempfile.TemporaryDirectory(prefix="development-setup-", dir=local) as temporary:
            bootstrap = Path(temporary) / "rustup-init"
            download_bootstrap(bootstrap)
            require_success(command([str(bootstrap), "-y", "--no-modify-path", "--profile", "minimal",
                                     "--default-toolchain", "none"], root, environment,
                                    capture=False, timeout=300), "local rustup bootstrap")
    require_success(command([str(manager), "toolchain", "install", version, "--profile", "minimal",
                             "--component", "rustfmt", "--component", "clippy", "--no-self-update"],
                            root, environment, capture=False, timeout=1800), "pinned Rust installation")
    if not ready(root, version, environment):
        raise SetupError("Pinned Rust/components remain incomplete after setup")
