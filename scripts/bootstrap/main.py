# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
"""Compose validated development inspection, planning and explicitly selected apply."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

from common import SetupError, command, require_success
from host import detect_host
from packages import install_missing, missing_packages
import toolchain

ROOT = Path(__file__).resolve().parents[2]


def run(arguments: list[str], root: Path = ROOT) -> int:
    """Dispatch explicit setup with documented statuses and no implicit installs.

    Takes literal CLI arguments and a repository root. Returns 0 for ready/valid
    plan, 1 for missing prerequisites and 2 for invalid/unsupported/failed setup.
    Check/plan never write; only explicit --development without inspection applies.
    """
    parser = argparse.ArgumentParser(description="Prepare Ubuntu 22.04/24.04 amd64 Rust development prerequisites.")
    parser.add_argument("--development", "-d", action="store_true", help="explicitly select development setup")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true", help="read-only readiness; exit 1 when missing")
    modes.add_argument("--dry-run", action="store_true", help="read-only resolved setup plan")
    options = parser.parse_args(arguments)
    if not options.development:
        parser.print_help()
        return 2
    try:
        host = detect_host()
        version = toolchain.rust_version(root)
        environment = toolchain.local_environment(root)
        # Validate destination ownership and lock presence before any transaction.
        toolchain.tool_bin(root, version)
        if not (root / "Cargo.toml").is_file() or not (root / "Cargo.lock").is_file():
            raise SetupError("Cargo.toml and committed Cargo.lock are required")
        missing = missing_packages(root)
        rust_ready = toolchain.ready(root, version, environment)
        print(f"Host: Ubuntu {host.release} amd64")
        print(f"Missing apt packages: {', '.join(missing) or 'none'}")
        print(f"Local Rust {version} with rustfmt/Clippy ready: {rust_ready}")
        print("Cargo source-cache completeness is not checked by inspection.")
        if options.check:
            return int(bool(missing) or not rust_ready)
        if options.dry_run:
            print("Would install missing apt packages only; preserve existing tools/configuration.")
            print(f"Would prepare pinned local Rust {version} if missing; bootstrap SHA-256 verified.")
            print(f"Would cargo fetch --locked --target {host.target}; no builds, tests or application install.")
            return 0
        if os.geteuid() == 0:
            raise SetupError("Run as your normal user; sudo is used only for missing apt packages")
        install_missing(root, missing)
        toolchain.install(root, version, environment)
        fetch_environment = dict(environment, CARGO_NET_OFFLINE="false", RUSTUP_TOOLCHAIN=version)
        cargo = toolchain.tool_bin(root, version) / "cargo"
        require_success(command([str(cargo), "fetch", "--manifest-path", str(root / "Cargo.toml"),
                                 "--locked", "--target", host.target], root, fetch_environment,
                                capture=False, timeout=900), "locked Cargo source fetch")
        if missing_packages(root) or not toolchain.ready(root, version, environment):
            raise SetupError("Development prerequisites remain incomplete after setup")
        print("Development prerequisites ready. Run scripts/validate.sh separately.")
        return 0
    except SetupError as error:
        print(f"setup: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1:]))
