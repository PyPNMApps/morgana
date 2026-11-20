#!/usr/bin/env bash
# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
# Run Cargo at the workspace root, preferring an optional isolated local toolchain.
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -x "${project_dir}/local/cargo/bin/cargo" ]]; then
    export CARGO_HOME="${CARGO_HOME:-${project_dir}/local/cargo}"
    export RUSTUP_HOME="${RUSTUP_HOME:-${project_dir}/local/rustup}"
    export PATH="${project_dir}/local/cargo/bin:${PATH}"
fi
if ! command -v cargo >/dev/null 2>&1; then
    echo 'Cargo is missing; see docs/development/build.md.' >&2
    exit 1
fi
cd "${project_dir}"
exec cargo "$@"
