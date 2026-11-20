---
name: development-workflow
description: Define architecture and software layout, derive mandatory linked requirements, then build a developer checklist for new or existing projects.
---

# Development Workflow

Choose new or existing codebase explicitly. Start from the requested goal and
constraints, then define architecture: owners, interfaces, lifecycle, failures,
validation and the software layout with files to add, edit or reuse. Derive the
requirements from that architecture using MUST, MUST NOT, SHALL or SHALL NOT;
each requirement links its relevant architecture section. Then build the
developer checklist: ordered tasks linked to requirements and, where relevant,
architecture owners/file plans, with dependencies and acceptance evidence.
Keep records proportional to the task; short sections are sufficient for small changes.

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

## Code layout per section

Every architecture block/stage section names its repository-relative directories,
implementation files and validation files, with responsibilities and disposition:
create (planned), reuse (existing) or extend (existing). Backfill earlier sections
when adopting this rule. Keep shared algorithms at one named path; mark unresolved
placement explicitly. See the [file-layout procedure](references/procedure.md#code-layout-per-section).

## Requirements and checklist traceability

Use the [traceability procedure](references/checklist-traceability.md) for the full
Architecture → Requirements → Developer checklist → Implementation → Validation flow.
Every active task MUST link its requirement, identify dependency IDs and
acceptance evidence, and link architecture when design/ownership/layout applies.
Resolve implementation/test placement through that architecture owner.
Preserve stable IDs/history and keep status evidence-based; cover every in-scope
requirement or record an explicit deferred decision. Declare the canonical status
owner for each project/feature scope. Verify anchors and dependency cycles.

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
