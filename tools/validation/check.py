#!/usr/bin/env python3
# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Validate local resource closure, canonical skill discovery and version identity.

This development-only check reads the Git candidate and Cargo metadata. It does
not perform scientific calculations, install prerequisites or stage source files.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]

# Extract inline Markdown destinations, excluding the label. For [x](guide.md#h)
# group 1 is guide.md#h; external URLs/anchors are filtered before local lookup.
MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")


def main() -> None:
    """Check candidate paths and local guidance, raising on incomplete resources.

    Reads repository/Cargo metadata and prints aggregate check counts. No source
    files or Git index entries are changed; a failed invariant exits nonzero.
    """
    listed = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
    ).decode().split("\0")
    paths = [ROOT / name for name in set(listed) if name]
    forbidden = (ROOT / "local", ROOT / "target", ROOT / "docs/development/local")
    for path in paths:
        if any(path.is_relative_to(directory) for directory in forbidden):
            raise SystemExit(f"Private/generated path is in candidate: {path.relative_to(ROOT)}")
        if path.suffix.lower() == ".pdf":
            raise SystemExit(f"Specification PDF is in candidate: {path.relative_to(ROOT)}")

    canonical = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    for skill in canonical:
        entry = skill / "SKILL.md"
        content = entry.read_text()
        if not content.startswith("---\n"):
            raise SystemExit(f"Missing skill frontmatter: {entry.relative_to(ROOT)}")
        metadata = content.split("---", 2)[1]
        fields = dict(line.split(":", 1) for line in metadata.splitlines() if ":" in line)
        if fields.get("name", "").strip() != skill.name or not fields.get("description", "").strip():
            raise SystemExit(f"Invalid skill name/description: {entry.relative_to(ROOT)}")
        if "/home/" in content or "/Projects/" in content:
            raise SystemExit(f"Workstation dependency in skill: {entry.relative_to(ROOT)}")
        for discovery in (".agents/skills", ".claude/skills"):
            link = ROOT / discovery / skill.name
            if not link.is_symlink() or link.readlink().is_absolute() or link.resolve() != skill:
                raise SystemExit(f"Invalid skill discovery link: {link.relative_to(ROOT)}")

    checked_links = 0
    for path in paths:
        if path.suffix != ".md" or not path.is_file():
            continue
        for destination in MARKDOWN_LINK.findall(path.read_text()):
            if destination.startswith(("http:", "https:", "mailto:", "#")):
                continue
            local = destination.split("#", 1)[0]
            target = (path.parent / local).resolve()
            if not target.is_relative_to(ROOT):
                raise SystemExit(f"External checkout dependency: {path.relative_to(ROOT)} -> {destination}")
            # Optional private evidence is supplied locally, never shipped with a clone.
            if target.is_relative_to(ROOT / "docs/development/local"):
                continue
            if not target.exists():
                raise SystemExit(f"Broken local link: {path.relative_to(ROOT)} -> {destination}")
            checked_links += 1

    metadata = json.loads(subprocess.check_output(
        [str(ROOT / "scripts/cargo-local.sh"), "metadata", "--locked", "--no-deps", "--format-version", "1"],
        cwd=ROOT,
    ))
    version = (ROOT / "VERSION").read_text().strip()
    if any(package["version"] != version for package in metadata["packages"]):
        raise SystemExit("VERSION and workspace package versions disagree")
    print(f"Guidance checks passed: {len(canonical)} skills, {checked_links} local links; version {version}.")


if __name__ == "__main__":
    main()
