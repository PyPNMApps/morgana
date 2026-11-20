---
name: development-workflow
description: Plan new projects and existing-code features through requirements, architecture and implementation checklists.
---

# Development Workflow

Choose new or existing codebase explicitly. Write requirements first: observable behavior, IDs, acceptance criteria, scope and non-goals. Then architecture: owners, interfaces, lifecycle, failure handling and validation. Then a dependency-ordered checklist tracing requirement IDs to code and checks. Keep records proportional to the task; short sections are sufficient for small changes.

For a new codebase, establish the smallest foundation satisfying the requirements. For existing code, read current architecture and software facts, verify the active checkout and follow [reuse-first changes](../reuse-first-changes/SKILL.md). Do not substitute a new architecture for understanding the current one.

Keep completed, partial and planned work distinct. At completion reconcile requirements, architecture and checklist with actual evidence. Use the [feature templates](../../templates/project/README.md).

[Skill catalog](../README.md)

## Architecture navigation

Link every block/stage label in overview tables to its canonical local section.
Give diagrams a companion linked index when their labels cannot be navigated
reliably. Keep stage IDs stable and label future sections as placeholders;
a working link does not mean the design or implementation is complete.
Use the [navigation procedure](references/procedure.md#architecture-navigation)
when adding stages or renaming headings.

## Standalone procedure

Read the [operational guide](references/procedure.md) for inputs, implementation
steps, examples, failure cases and acceptance checks. Required resources are in
the foundation; no other repository is required or referenced by the procedure.

## Changeable guidance

When this task relies on external APIs, tooling, platform support or other changing
contracts, apply [knowledge-freshness](../knowledge-freshness/SKILL.md) and update
affected local guidance from verified official evidence as part of the task.

When changes originate outside the current reviewed session, apply
[external-change-review](../external-change-review/SKILL.md) before adoption or handoff.
