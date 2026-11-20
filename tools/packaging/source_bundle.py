#!/usr/bin/env python3
# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Build a scientific-only source archive with explicit ownership and inventory.

Run from any directory. Creates a new ignored archive, never overwrites exports,
publishes, stages or vendors dependencies. Private instructional material stays
outside this distribution; root repository publication has separate obligations.
"""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[2]
FILES = {"Cargo.toml", "Cargo.lock", "VERSION", "rust-toolchain.toml", "LICENSE", "NOTICE", "install.sh", "scripts/cargo-local.sh"}
PREFIXES = ("crates/", "bindings/python/src/", "bindings/python/python/morgana/", "bindings/python/tests/", "examples/", "docs/user/", "scripts/bootstrap/", "tools/python/", "tools/packaging/")
FILES |= {"bindings/python/Cargo.toml", "bindings/python/Cargo.lock", "bindings/python/pyproject.toml"}
FILES.add("tools/validation/ldpc_source_reference.rs")
EXCLUDED_PARTS = {"target", "local", "__pycache__", ".git", ".venv", "wheel-notices"}


def selected_paths() -> list[Path]:
    """Return reviewed existing scientific candidate files without following links.

    Reads staged, tracked and untracked names together. Symlinks and unreviewed
    binary/generated/private content reject; the Git index is never modified.
    """
    listed = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT).decode().split("\0")
    paths = []
    for name in sorted(set(listed)-{""}):
        if name not in FILES and not name.startswith(PREFIXES):
            continue
        path = ROOT / name
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise ValueError(f"Redirected scientific source: {name}")
        if not path.is_file():
            continue
        if EXCLUDED_PARTS.intersection(path.relative_to(ROOT).parts) or path.suffix.lower() in {".pdf", ".whl", ".pyc", ".so"}:
            raise ValueError(f"Unreviewed private/generated scientific path: {name}")
        paths.append(path)
    if not FILES.issubset({str(path.relative_to(ROOT)) for path in paths}):
        raise ValueError("Scientific source package is missing required inputs")
    return paths


def build(destination: Path) -> tuple[str, int]:
    """Create a new bounded tar.gz from the reviewed candidate and inspect it.

    destination must be under ignored target/source-packages and not exist.
    Returns SHA-256 and member count. Includes exact source hashes and notices;
    archive metadata is normalized, but gzip timestamps are not reproducible.
    """
    directory = ROOT / "target/source-packages"
    if directory.is_symlink() or not directory.resolve().is_relative_to(ROOT / "target") or destination.parent.resolve() != directory.resolve() or destination.exists():
        raise ValueError("Source export must be a new owned target/source-packages file")
    paths = selected_paths()
    version = (ROOT / "VERSION").read_text().strip()
    prefix = f"morgana-{version}"
    files = {str(path.relative_to(ROOT)): path.read_bytes() for path in paths}
    if sum(map(len, files.values())) > 64*1024*1024:
        raise ValueError("Scientific source archive exceeds64MiB")
    files["SOURCE-README.md"] = b"""# MORGANA scientific source distribution

Apache-2.0 scientific core, CLI and optional native Python. Dependency downloads
are resolved by the included exact Cargo locks; no dependency sources are vendored.
Use the pinned Rust version with rustfmt/Clippy and native build prerequisites:

    scripts/cargo-local.sh test --workspace --locked
    scripts/cargo-local.sh clippy --workspace --all-targets --locked -- -D warnings
    scripts/cargo-local.sh run --locked -p morgana --example upstream_captures

See docs/user/ for Rust/Python inputs, controls and limits. Original capture-driven
examples are authored fixtures, not modem recordings. Private engineering guidance,
specification corpora, build outputs and repository automation are excluded. Root
repository publication and other platforms have separate acceptance. LICENSE,
NOTICE and crates/phy/resources/qam-table retain actual reused-material terms.
"""
    inventory = {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}
    files["SOURCE-MANIFEST.json"] = (json.dumps({"format":"morgana.scientific-source","schema_version":1,"version":version,"files_sha256":inventory},indent=2)+"\n").encode()
    directory.mkdir(parents=True, exist_ok=True)
    with destination.open("xb") as output, tarfile.open(fileobj=output, mode="w:gz") as archive:
        for name, data in sorted(files.items()):
            entry = tarfile.TarInfo(f"{prefix}/{name}")
            entry.size = len(data)
            entry.mode = 0o755 if name in {"install.sh", "scripts/cargo-local.sh"} else 0o644
            archive.addfile(entry, io.BytesIO(data))
    with tarfile.open(destination) as archive:
        members = archive.getmembers()
        if len(members) != len(files) or any(not member.isfile() for member in members):
            raise ValueError("Unexpected scientific archive members")
        for name, expected in inventory.items():
            if hashlib.sha256(archive.extractfile(f"{prefix}/{name}").read()).hexdigest() != expected:
                raise ValueError(f"Changed source archive entry: {name}")
    return hashlib.sha256(destination.read_bytes()).hexdigest(), len(files)


if __name__ == "__main__":
    version = (ROOT / "VERSION").read_text().strip()
    target = ROOT / f"target/source-packages/morgana-{version}-scientific.tar.gz"
    digest, count = build(target)
    print(f"Verified {count} source entries: {target.relative_to(ROOT)} SHA256 {digest}")
