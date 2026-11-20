---
name: external-change-review
description: Review changes made outside the current session using Git and semantic evidence, preserving existing work and applying relevant repository skills before adoption or handoff.
---

# Review externally produced changes

Apply when another AI/chat session, developer, editor, generator or imported patch
has changed the repository since the last reviewed baseline. Also apply when a
resumed task discovers unfamiliar changes. Treat chat summaries as leads; the
actual checkout, requirements and implementation are the review evidence.

Read the [procedure](references/procedure.md) and use the
[review record](../../templates/project/external-change-review.md). Separate staged,
unstaged, untracked and already committed changes. Do not assume Git identifies
who made an uncommitted edit. Preserve existing work and index state.

Review complete changed behavior against applicable skills, make authorized focused
fixes, and report findings, validation and remaining limits. For reusable guidance
apply [generic-guidance](../generic-guidance/SKILL.md); for copied material preserve
[third-party notices](../third-party-reuse/SKILL.md). A review does not authorize
committing, publishing, resetting or rewriting someone else's work.
