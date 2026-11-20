#!/usr/bin/env bash
# Copyright 2026 MORGANA contributors
# SPDX-License-Identifier: Apache-2.0
# Save all non-ignored working changes, including staged content, locally.
# Arguments: --commit-msg followed by one literal multiline message.
# Runs the local gate; failures retain the staged candidate for inspection.
# No push, tag, remote access, version bump or index cleanup is performed.
set -euo pipefail

project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
if [[ "${1:-}" == --help && $# -eq 1 ]]; then
    echo 'Usage: tools/git/git-save.sh --commit-msg MESSAGE'
    exit 0
fi
if [[ $# -ne 2 || "$1" != --commit-msg || -z "$2" ]]; then
    echo 'Use --commit-msg MESSAGE; save includes all non-ignored changes.' >&2
    exit 1
fi
message="$2"
cd -- "${project_dir}"
if [[ "$(git rev-parse --show-toplevel)" != "${project_dir}" ]]; then
    echo 'Initialize Git at the project root before saving.' >&2
    exit 1
fi
git symbolic-ref -q HEAD >/dev/null
if [[ -e "$(git rev-parse --git-path MERGE_HEAD)" ||
      -d "$(git rev-parse --git-path rebase-merge)" ||
      -d "$(git rev-parse --git-path rebase-apply)" ||
      -n "$(git ls-files --unmerged)" ]]; then
    echo 'Finish the merge/rebase or resolve conflicts before saving.' >&2
    exit 1
fi

head_before="$(git rev-parse --verify HEAD 2>/dev/null || true)"
git add --all
if git ls-files --stage | awk '$1 == "160000" { found = 1 } END { exit !found }'; then
    echo 'Nested Gitlinks are outside the local save contract.' >&2
    exit 1
fi
git diff --cached --check
if git diff --cached --quiet; then
    echo 'No changes to commit.' >&2
    exit 1
fi
candidate_before="$(git write-tree)"
bash scripts/validate.sh
if [[ "$(git rev-parse --verify HEAD 2>/dev/null || true)" != "${head_before}" ||
      "$(git write-tree)" != "${candidate_before}" ]]; then
    echo 'HEAD or the staged candidate changed during validation; review before retry.' >&2
    exit 1
fi
if ! git diff --quiet || [[ -n "$(git ls-files --others --exclude-standard)" ]]; then
    echo 'Working files changed during validation; review before retry.' >&2
    exit 1
fi
git diff --cached --check
git diff --cached --stat
git commit -m "${message}"
