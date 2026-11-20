#!/usr/bin/env bash
# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
# Dispatch explicit development setup from any working directory.
# Arguments and exit status pass through unchanged; Python must already be present.
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if ! command -v python3 >/dev/null 2>&1; then
    echo 'Python 3.10+ is required to inspect/setup development prerequisites.' >&2
    exit 2
fi
exec python3 -B "${project_dir}/scripts/bootstrap/main.py" "$@"
