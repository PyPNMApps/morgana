---
name: software-facts
description: Capture and refresh evidence-backed codebase knowledge to avoid repeated investigation.
---

# Software Facts

Read the project's facts index before investigation; verify drift-prone claims against the active checkout. Store one question/topic per Markdown file. Lead with a direct answer, then exact source paths and symbols, revision/date, supporting tests or observations, limitations and refresh triggers.

Distinguish source-confirmed behavior, runtime observations, inference and unknowns. Proposed implementation belongs in feature designs, not confirmed facts. A passed unit test does not establish installed or hardware behavior. Update affected facts in the same change that invalidates them; preserve a superseded note when historical context matters.

Keep project facts in that project's repository. Promote only reusable methods and sanitized lessons into this foundation. Link new facts from the index and relevant source-navigation guidance. Use the [fact template](../../templates/project/software-fact.md).

[Skill catalog](../README.md)

## Standalone procedure

Read the [operational guide](references/procedure.md) for inputs, implementation
steps, examples, failure cases and acceptance checks. Required resources are in
the foundation; no other repository is required or referenced by the procedure.

## Changeable guidance

When this task relies on external APIs, tooling, platform support or other changing
contracts, apply [knowledge-freshness](../knowledge-freshness/SKILL.md) and update
affected local guidance from verified official evidence as part of the task.
