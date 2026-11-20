---
name: reuse-first-changes
description: Extend or rework existing code with minimal coherent changes and evidence-backed reuse.
---

# Reuse First Changes

Trace existing entrypoints, owners, callers, tests, build registration and failure paths before proposing code. Record a reuse table: path/symbol, current contract, requirement gap, disposition (reuse, extend, candidate or reject), and evidence. A matching name is not proof of matching semantics.

Check lifecycle, cancellation, concurrency, units, persistence and external callers. Prefer an existing owner or extension point; avoid parallel parsers, schedulers, validation or logging. Introduce a module or abstraction only for a concrete responsibility. Preserve public imports and data contracts where required. Missing local callers do not establish that an interface is unused.

Minimize behavioral scope, not line count. A necessary refactor should state its reason, compatibility impact and tests. Keep unrelated cleanup separate. Record discovered behavior through [software facts](../software-facts/SKILL.md).

[Skill catalog](../README.md)

## Standalone procedure

Read the [operational guide](references/procedure.md) for inputs, implementation
steps, examples, failure cases and acceptance checks. Required resources are in
the foundation; no other repository is required or referenced by the procedure.

## Changeable guidance

When this task relies on external APIs, tooling, platform support or other changing
contracts, apply [knowledge-freshness](../knowledge-freshness/SKILL.md) and update
affected local guidance from verified official evidence as part of the task.
