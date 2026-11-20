# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Explicit Ubuntu package mappings; no installation during module import."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import platform
import shlex
import sys

from common import SetupError

SUPPORTED_UBUNTU = ("22.04", "24.04")
HOST_TARGET = "x86_64-unknown-linux-gnu"


@dataclass(frozen=True)
class Host:
    """An admitted Ubuntu amd64 development host; not provisioning evidence."""

    release: str
    target: str = HOST_TARGET


def validate_host(system: str, machine: str, release_text: str) -> Host:
    """Validate explicit OS/CPU metadata without executing its contents.

    Takes the kernel system/machine and os-release text. Returns an immutable
    admitted host. Unsupported/malformed platform or Python versions raise
    SetupError before any package/tool mutation.
    """
    if sys.version_info < (3, 10):
        raise SetupError("Python 3.10+ is required")
    values: dict[str, str] = {}
    try:
        for line in release_text.splitlines():
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            tokens = shlex.split(value)
            values[key] = tokens[0] if len(tokens) == 1 else ""
    except ValueError as error:
        raise SetupError("Invalid os-release metadata") from error
    if (system != "Linux" or machine != "x86_64" or values.get("ID") != "ubuntu"
            or values.get("VERSION_ID") not in SUPPORTED_UBUNTU):
        raise SetupError("Development setup supports Ubuntu 22.04/24.04 amd64 only")
    return Host(values["VERSION_ID"])


def detect_host() -> Host:
    """Read host metadata and return an admitted platform without changing state.

    Reads /etc/os-release and kernel identity. Missing/unsupported metadata raises
    SetupError. No package manager, network or configuration write is invoked.
    """
    try:
        release_text = Path("/etc/os-release").read_text()
    except OSError as error:
        raise SetupError("Cannot read /etc/os-release") from error
    return validate_host(platform.system(), platform.machine(), release_text)
