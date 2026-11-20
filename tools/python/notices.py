#!/usr/bin/env python3
# Copyright 2026 DOCSIS OFDM Channel Sim contributors
# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
# Adapted from MERLIN tools/packaging/notices.py at
# 096d5a476194d4f2e016863d723b225257bb6037.
# Modifications: host-reachable graph walk, exact shared VCS check, hashes,
# explicit generated-directory ownership and independent optional adapter scope.
"""Collect full pinned host-reachable dependency notices for a scientific wheel."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess


def notice_files(directory: Path) -> list[Path]:
    """Find actual root/license-directory notices without inventing license text.

    directory is a pinned unpacked Cargo package. Returns files; rejects redirected
    license directories. REUSE README attribution is preserved with its texts.
    """
    selected = [path for path in directory.iterdir() if path.is_file() and path.name.upper().startswith(("LICENSE", "LICENCE", "COPYING", "NOTICE", "COPYRIGHT", "UNLICENSE"))]
    licenses = directory / "LICENSES"
    if licenses.is_symlink():
        raise ValueError("Refuse redirected dependency licenses")
    if licenses.is_dir():
        selected.extend(path for path in licenses.rglob("*") if path.is_file())
        if (directory / "README.md").is_file():
            selected.append(directory / "README.md")
    return sorted(set(selected))


def collect_notices(root: Path, destination: Path) -> int:
    """Collect the locked Linux adapter graph and full source notices with hashes.

    root is the project checkout; destination is a generated internal directory.
    Returns third-party package count; missing/unsafe source attribution fails.
    Exact same-repository/commit peer evidence is required for the one archive gap.
    """
    if destination.is_symlink() or not destination.resolve().is_relative_to((root / "bindings/python/python/wheel-notices").resolve()):
        raise ValueError("Notice staging escaped private generated scope")
    if destination.exists():
        if not (destination / "manifest.json").is_file() or any(path.is_symlink() for path in destination.rglob("*")):
            raise ValueError("Refuse unrecognized/redirected generated notice staging")
        shutil.rmtree(destination)
    information = subprocess.check_output(["scripts/cargo-local.sh", "-vV"], cwd=root, text=True)
    host = next(line.removeprefix("host: ") for line in information.splitlines() if line.startswith("host: "))
    metadata = json.loads(subprocess.check_output(["scripts/cargo-local.sh", "metadata", "--manifest-path", "bindings/python/Cargo.toml", "--locked", "--offline", "--filter-platform", host, "--format-version", "1"], cwd=root, text=True))
    nodes = {node["id"]: node for node in metadata["resolve"]["nodes"]}
    included: set[str] = set()
    pending = [metadata["resolve"]["root"]]
    while pending:
        identity = pending.pop()
        if identity in included:
            continue
        included.add(identity)
        pending.extend(dependency["pkg"] for dependency in nodes[identity]["deps"])
    packages = [package for package in metadata["packages"] if package["id"] in included and package["source"]]
    destination.mkdir(parents=True)
    records = []
    for package in sorted(packages, key=lambda item: (item["name"], item["version"])):
        directory = Path(package["manifest_path"]).parent
        source = package
        source_directory = directory
        files = notice_files(directory)
        if not files and (package["name"], package["version"]) == ("termination_attrib", "0.1.1"):
            source = next(item for item in packages if (item["name"], item["version"]) == ("termination", "0.1.2"))
            source_directory = Path(source["manifest_path"]).parent
            original_vcs = json.loads((directory / ".cargo_vcs_info.json").read_text())
            source_vcs = json.loads((source_directory / ".cargo_vcs_info.json").read_text())
            if source["repository"] != package["repository"] or source["license"] != package["license"] or original_vcs["git"]["sha1"] != source_vcs["git"]["sha1"]:
                raise ValueError("Pinned shared dependency notice source changed")
            files = notice_files(source_directory)
        if not files or not package["license"]:
            raise ValueError(f"Missing reviewed full dependency notice: {package['name']}")
        target = destination / f"{package['name']}-{package['version']}"
        target.mkdir()
        hashes = {}
        for path in files:
            if path.is_symlink() or path.stat().st_size > 1024 * 1024:
                raise ValueError("Unsafe dependency notice source")
            relative = path.relative_to(source_directory)
            copied = target / relative
            copied.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, copied)
            hashes[str(relative)] = hashlib.sha256(copied.read_bytes()).hexdigest()
        if (source_directory / "LICENSES").is_dir():
            authors = set(package.get("authors", []))
            for path in directory.rglob("*.rs"):
                for line in path.read_bytes()[:8192].decode("utf-8", errors="replace").splitlines():
                    if "SPDX-FileCopyrightText:" in line:
                        authors.add(line.partition("SPDX-FileCopyrightText:")[2].strip())
            (target / "AUTHOR-NOTICES").write_text("\n".join(sorted(authors)) + "\n")
        records.append(dict(name=package["name"], version=package["version"], license=package["license"], repository=package["repository"], notice_source=f"{source['name']}-{source['version']}", files_sha256=hashes))
    (destination / "manifest.json").write_text(json.dumps(dict(host=host, packages=records), indent=2) + "\n")
    return len(records)
