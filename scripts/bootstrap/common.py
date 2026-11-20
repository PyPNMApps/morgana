# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Bounded development commands and explicit prerequisite failures."""
from __future__ import annotations

from pathlib import Path
import subprocess


class SetupError(RuntimeError):
    """Expected invalid host/input or failed prerequisite operation."""


def command(
    arguments: list[str],
    root: Path,
    environment: dict[str, str] | None = None,
    *,
    capture: bool = True,
    timeout: int = 30,
) -> subprocess.CompletedProcess[str]:
    """Run literal arguments with a finite timeout and no shell interpretation.

    Arguments select the command, working root and optional child environment.
    Capture returns stdout/stderr; interactive apt steps inherit the terminal.
    Returns the actual exit status; missing executables/timeouts raise SetupError.
    """
    try:
        return subprocess.run(
            arguments, cwd=root, env=environment, text=True, capture_output=capture,
            timeout=timeout, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SetupError(f"Cannot run {arguments[0]}: {error}") from error


def require_success(result: subprocess.CompletedProcess[str], operation: str) -> None:
    """Raise a concise operation failure while preserving a successful result.

    Accepts a completed command and human operation label. No retries, writes or
    cleanup occur; nonzero status raises SetupError and stops later setup stages.
    """
    if result.returncode != 0:
        raise SetupError(f"{operation} failed with status {result.returncode}")
