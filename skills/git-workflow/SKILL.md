---
name: git-workflow
description: Review staged, unstaged and untracked changes and prepare guarded local save commands; commit-msg is command preparation unless execution is explicit.
---

# Local Git workflow

Read the [procedure](references/procedure.md), [Git guide](../../docs/git.md),
architecture and checklist before drafting messages. Use the project-owned
`tools/git/git-save.sh --commit-msg` entrypoint. It includes all non-ignored
changes and existing staged content, with no staged-content opt-in flag.

Prepare commands unless execution is explicit. Use Feature:, BugFix: or
Documentation:, detail lines and a Tests: line, each at most 60 characters.
Saving never implies push, tagging, publication or a version bump. Push/release
automation is not implemented in this checkpoint. Preserve the user's index
while reviewing; do not stage or reset merely to prepare the command.
