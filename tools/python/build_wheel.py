#!/usr/bin/env python3
# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Build/review a local Linux native wheel without installation or publication.

Requires existing pinned maturin 1.8.3. Generated notices/wheels/import trees stay
under ignored project target directories. No system dependency is installed.
"""
from __future__ import annotations

import importlib.metadata
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import zipfile
from notices import collect_notices

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    """Build locked native code, inventory attribution and test the actual wheel.

    No arguments. Raises on missing/wrong tools, package scope or native failures;
    output is a local host wheel and never a portability/publication assertion.
    """
    if sys.platform != "linux" or importlib.metadata.version("maturin") != "1.8.3":
        raise RuntimeError("This local Linux gate requires existing maturin 1.8.3")
    executable = Path(importlib.metadata.distribution("maturin").locate_file("bin/maturin"))
    if not executable.is_file():
        executable = Path(shutil.which("maturin") or "")
    if not executable.is_file() or subprocess.check_output([str(executable), "--version"], text=True).strip() != "maturin 1.8.3":
        raise RuntimeError("Cannot locate the pinned maturin executable")
    notices = ROOT / "bindings/python/python/wheel-notices"
    notices.mkdir(parents=True, exist_ok=True)
    for name in ["LICENSE", "NOTICE"]:
        shutil.copyfile(ROOT / name, notices / name)
    resources = notices / "qam-table"
    resources.mkdir(exist_ok=True)
    for name in ["LICENSE", "NOTICE", "provenance.json"]:
        shutil.copyfile(ROOT / "crates/phy/resources/qam-table" / name, resources / name)
    dependencies = collect_notices(ROOT, notices / "dependencies")
    output = ROOT / "target/python-wheels"
    output.mkdir(parents=True, exist_ok=True)
    environment = dict(os.environ, CARGO_TARGET_DIR=str(ROOT / "target/python"), PYO3_PYTHON=sys.executable)
    # The same isolated Cargo wrapper/toolchain is used by maturin's Cargo child.
    cargo = subprocess.check_output(["scripts/cargo-local.sh", "--version"], cwd=ROOT, text=True)
    if "cargo 1.85.1" not in cargo:
        raise RuntimeError("Expected the project-pinned Cargo toolchain")
    environment["CARGO_HOME"] = str(ROOT / "local/cargo")
    environment["RUSTUP_HOME"] = str(ROOT / "local/rustup")
    environment["PATH"] = os.pathsep.join([str(ROOT / "local/cargo/bin"), str(Path(importlib.metadata.distribution("maturin").locate_file("bin"))), environment["PATH"]])
    subprocess.run([str(executable), "build", "--manifest-path", "bindings/python/Cargo.toml", "--locked", "--release", "--compatibility", "linux", "--interpreter", sys.executable, "--out", str(output)], cwd=ROOT, env=environment, stdin=subprocess.DEVNULL, check=True, timeout=600)
    version = (ROOT / "VERSION").read_text().strip()
    wheels = list(output.glob(f"morgana_ofdma-{version}-cp{sys.version_info.major}{sys.version_info.minor}-*-linux_*.whl"))
    if len(wheels) != 1:
        raise RuntimeError("Expected exactly one local host/version wheel")
    runtime = ROOT / "target/python-wheel-runtime"
    runtime.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(wheels[0]) as archive:
        names = archive.namelist()
        for name in names:
            path = PurePosixPath(name)
            if path.is_absolute() or ".." in path.parts:
                raise RuntimeError("Wheel path escaped private runtime")
            if any(part in {"skills", "local", ".git", "__pycache__"} for part in path.parts) or name.endswith(".pdf"):
                raise RuntimeError("Private/guidance files entered scientific wheel")
        for suffix in ["morgana/__init__.py", "morgana/__init__.pyi", "morgana/py.typed", "wheel-notices/LICENSE", "wheel-notices/NOTICE", "wheel-notices/qam-table/provenance.json", "wheel-notices/dependencies/manifest.json"]:
            if not any(name.endswith(suffix) for name in names):
                raise RuntimeError(f"Required native/attribution asset missing: {suffix}")
        for name in ["LICENSE", "NOTICE"]:
            if archive.read(f"wheel-notices/{name}") != (ROOT / name).read_bytes():
                raise RuntimeError("Packaged root license/notice differs from its reviewed source")
        for name in ["LICENSE", "NOTICE", "provenance.json"]:
            if archive.read(f"wheel-notices/qam-table/{name}") != (ROOT / "crates/phy/resources/qam-table" / name).read_bytes():
                raise RuntimeError("Packaged QAM attribution differs from its reviewed source")
        manifest_name = next(name for name in names if name.endswith("wheel-notices/dependencies/manifest.json"))
        import json, hashlib
        inventory = json.loads(archive.read(manifest_name))
        if len(inventory["packages"]) != dependencies:
            raise RuntimeError("Dependency attribution inventory changed")
        for package in inventory["packages"]:
            for name, expected in package["files_sha256"].items():
                entry = f"wheel-notices/dependencies/{package['name']}-{package['version']}/{name}"
                if hashlib.sha256(archive.read(entry)).hexdigest() != expected:
                    raise RuntimeError("Packaged dependency notice changed")
        archive.extractall(runtime)
    environment = dict(os.environ, PYTHONPATH=str(runtime))
    environment["MORGANA_RUST_CAPTURES_JSON"] = str(ROOT / "target/python-runtime/rust-captures.json")
    environment["MORGANA_RUST_CAPTURES25_JSON"] = str(ROOT / "target/python-runtime/rust-captures25.json")
    for setting, name in [("MORGANA_RUST_RXMER_JSON", "rust-rxmer.json"), ("MORGANA_RUST_UCD_JSON", "rust-ucd.json"), ("MORGANA_RUST_REFERENCE_JSON", "rust-reference.json"), ("MORGANA_RUST_MEASUREMENTS_JSON", "rust-measurements.json"), ("MORGANA_RUST_DOCUMENT_JSON", "rust-document.json"), ("MORGANA_RUST_SYNTHETIC_JSON", "rust-synthetic-document.json")]:
        environment[setting] = str(ROOT / "target/python-runtime" / name)
    subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "bindings/python/tests", "-v"], cwd=ROOT, env=environment, stdin=subprocess.DEVNULL, check=True, timeout=120)
    print(f"Verified local Linux wheel: {wheels[0].relative_to(ROOT)}; {len(names)} package entries, {dependencies} attributed dependencies")


if __name__ == "__main__":
    main()
