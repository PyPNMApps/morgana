#!/usr/bin/env bash
# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
# Validate the local checkpoint without installing, committing or publishing.
# No arguments. Required failures propagate; caches and source inputs are retained.
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "${project_dir}"
python3 tools/validation/check.py
python3 -m unittest discover -s tools/git/tests -p 'test_*.py' -v
python3 -B -m unittest discover -s tools/development/tests -p 'test_*.py' -v
bash -n scripts/cargo-local.sh scripts/validate.sh tools/git/git-save.sh
bash -n install.sh
scripts/cargo-local.sh fmt --all -- --check
scripts/cargo-local.sh test --workspace --locked
scripts/cargo-local.sh clippy --workspace --all-targets --locked -- -D warnings
