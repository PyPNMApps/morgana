# Local save workflow

Review all staged, unstaged and untracked changes, architecture and checklist.
`commit-msg` requests a prepared command, not execution.

```bash
tools/git/git-save.sh --commit-msg "Feature: Preserve MORGANA foundation checkpoint
- Add upstream LDPC scaffold and local agent guidance
- Keep incomplete PHY validation explicit
- Tests: Workspace tests, formatting and Clippy pass"
```

The local helper includes all non-ignored working changes and existing staged
content, runs `scripts/validate.sh`, checks the candidate and commits locally.
On failure the staged candidate remains available for review. It rejects a changed
HEAD/index, unstaged changes created during validation, nested Gitlinks, whitespace
errors and an empty candidate. It never pushes, tags or bumps a version.

No push/release helper is implemented. Adding a remote, tagging and publication
require separate explicit instructions. VERSION is canonical; workspace package
versions and Cargo.lock must agree before a future release.
