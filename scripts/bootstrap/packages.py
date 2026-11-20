# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""One deduplicated apt transaction for minimal Rust development prerequisites."""
from __future__ import annotations

from pathlib import Path

from common import SetupError, command, require_success

# Host tools only: no Qt, Python simulation runtime, services or packaging SDKs.
PACKAGES = ("ca-certificates", "git", "build-essential", "python3")


def missing_packages(root: Path, packages: tuple[str, ...] = PACKAGES) -> tuple[str, ...]:
    """Query deduplicated package state without refreshing indexes or installing.

    Accepts the command working root and package names. Returns names whose dpkg
    status is not 'install ok installed'. Unexpected query failures raise SetupError.
    """
    missing = []
    for package in dict.fromkeys(packages):
        result = command(["dpkg-query", "-W", "-f=${Status}", package], root)
        if result.returncode not in (0, 1):
            raise SetupError(f"Cannot inspect package {package}")
        if result.returncode != 0 or result.stdout.strip() != "install ok installed":
            missing.append(package)
    return tuple(missing)


def install_missing(root: Path, packages: tuple[str, ...]) -> None:
    """Install only missing packages, using sudo only for apt transactions.

    Accepts an admitted root and resolved missing names. Empty input is a no-op.
    Retains apt's normal confirmation and configured repositories. Command or
    unavailable-package failures raise SetupError; caller must be a normal user.
    """
    if not packages:
        return
    require_success(command(["sudo", "apt-get", "update"], root, capture=False, timeout=900), "apt update")
    for package in packages:
        require_success(command(["apt-cache", "show", package], root), f"package candidate {package}")
    require_success(command(["sudo", "apt-get", "install", "--", *packages], root,
                            capture=False, timeout=1800), "apt install")
