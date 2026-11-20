#!/usr/bin/env python3
# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Build/test the optional native adapter locally without installation or DSP.

All generated files stay under ignored target/. Requires an existing Python
interpreter/header toolchain; never installs packages or changes the Git index.
"""
from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys
import sysconfig

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    """Compile locked Rust, stage a private import tree and execute native tests.

    No arguments. Uses the running interpreter and preserves build caches;
    required failures propagate rather than becoming skipped passing checks.
    """
    native_env = dict(os.environ, CARGO_TARGET_DIR=str(ROOT / "target/python"), PYO3_PYTHON=sys.executable)
    subprocess.run(["scripts/cargo-local.sh", "build", "--locked", "--manifest-path", "bindings/python/Cargo.toml"], cwd=ROOT, env=native_env, stdin=subprocess.DEVNULL, check=True, timeout=300)
    package = ROOT / "target/python-runtime/morgana"
    package.mkdir(parents=True, exist_ok=True)
    source = ROOT / "bindings/python/python/morgana"
    for name in ["__init__.py", "__init__.pyi", "py.typed"]:
        destination = package / name
        if not destination.resolve().is_relative_to((ROOT / "target").resolve()):
            raise RuntimeError("Native staging escaped the ignored project target")
        shutil.copyfile(source / name, destination)
    library = ROOT / "target/python/debug/lib_native.so"
    destination = package / ("_native" + str(sysconfig.get_config_var("EXT_SUFFIX")))
    if not destination.resolve().is_relative_to((ROOT / "target").resolve()):
        raise RuntimeError("Native extension staging escaped project target")
    shutil.copyfile(library, destination)
    reference = subprocess.run(["scripts/cargo-local.sh", "run", "-p", "morgana", "--example", "upstream_loop", "--locked"], cwd=ROOT, stdin=subprocess.DEVNULL, capture_output=True, check=True, timeout=60)
    reference_path = ROOT / "target/python-runtime/rust-reference.json"
    reference_path.write_bytes(reference.stdout)
    measurement = subprocess.run(["scripts/cargo-local.sh", "run", "-p", "morgana", "--example", "upstream_measurements", "--locked"], cwd=ROOT, stdin=subprocess.DEVNULL, capture_output=True, check=True, timeout=60)
    measurement_path = ROOT / "target/python-runtime/rust-measurements.json"
    measurement_path.write_bytes(measurement.stdout)
    document = subprocess.run(["scripts/cargo-local.sh", "run", "-p", "morgana", "--example", "upstream_document", "--locked"], cwd=ROOT, stdin=subprocess.DEVNULL, capture_output=True, check=True, timeout=60)
    document_path = ROOT / "target/python-runtime/rust-document.json"
    document_path.write_bytes(document.stdout)
    synthetic = subprocess.run(["scripts/cargo-local.sh", "run", "-p", "morgana", "--example", "upstream_document", "--locked", "--", "synthetic"], cwd=ROOT, stdin=subprocess.DEVNULL, capture_output=True, check=True, timeout=60)
    synthetic_path = ROOT / "target/python-runtime/rust-synthetic-document.json"
    synthetic_path.write_bytes(synthetic.stdout)
    capture = subprocess.run(["scripts/cargo-local.sh", "run", "-p", "morgana", "--example", "inspect_ucd", "--locked"], cwd=ROOT, stdin=subprocess.DEVNULL, capture_output=True, check=True, timeout=60)
    capture_path = ROOT / "target/python-runtime/rust-ucd.json"
    capture_path.write_bytes(capture.stdout)
    rxmer = subprocess.run(["scripts/cargo-local.sh", "run", "-p", "morgana", "--example", "inspect_rxmer", "--locked"], cwd=ROOT, stdin=subprocess.DEVNULL, capture_output=True, check=True, timeout=60)
    rxmer_path = ROOT / "target/python-runtime/rust-rxmer.json"
    rxmer_path.write_bytes(rxmer.stdout)
    env = dict(os.environ, MORGANA_RUST_RXMER_JSON=str(rxmer_path), MORGANA_RUST_UCD_JSON=str(capture_path), MORGANA_RUST_SYNTHETIC_JSON=str(synthetic_path), MORGANA_RUST_DOCUMENT_JSON=str(document_path), MORGANA_RUST_MEASUREMENTS_JSON=str(measurement_path), PYTHONPATH=str(package.parent), MORGANA_RUST_REFERENCE_JSON=str(reference_path))
    subprocess.run([sys.executable, "-B", "-m", "unittest", "discover", "-s", "bindings/python/tests", "-v"], cwd=ROOT, env=env, stdin=subprocess.DEVNULL, check=True, timeout=120)


if __name__ == "__main__":
    main()
