# Requirements, architecture and software development checklist

[Skill](../SKILL.md) · [Requirements template](../../../templates/project/requirements.md) ·
[Architecture template](../../../templates/project/architecture.md) ·
[Checklist template](../../../templates/project/checklist.md)

## Inputs and outputs

Use the repository's current requirements, architecture, official checklist and
validation records. Keep established paths and identifiers in an existing project.
For a new project, instantiate the local templates. The output is one canonical,
dependency-ordered checklist plus navigable requirement/architecture references;
a second competing completion list is not a substitute.

## Required flow

**Requirements → Architecture → Checklist → Implementation → Validation → reconciliation.**

1. Give each requirement a stable ID, observable behavior and acceptance criterion.
   Use SHALL/MUST for obligations and SHALL NOT/MUST NOT for prohibitions. Resolve
   advisory proposals into mandatory behavior, explicit exclusion or deferred scope;
   record unresolved decisions and prevent dependent implementation until resolved.
   Preserve external specifications' actual normative force separately.
2. Give requirements stable section headings or explicit anchors. Keep architecture
   stage/owner anchors stable and record actual planned implementation/test paths.
   New-project templates use heading anchors; table-based existing documents can
   add explicit ID anchors without renumbering requirements or rewriting contracts.
3. Derive small implementation tasks from both requirements and architecture.
   Every active task MUST identify its stable task ID, direct requirement links,
   canonical architecture links, prerequisite task IDs and observable acceptance.
   Name the owner/code/test paths locally or through the linked architecture path
   table. Shared algorithms keep one owner, including across language adapters.
4. Order prerequisites before dependent tasks. Spell out dependency edges rather
   than treating every earlier row as required. Separate source/design decisions,
   core implementation, integration, adapters, validation and deferred extensions.
   A parent milestone stays unchecked until all its required children pass.
5. Preserve existing task IDs, completed evidence and partial status when updating
   a checklist. Clearly separate completed design/setup records from unfinished
   implementation; do not mark runtime acceptance complete because a section exists.
   Cross-cutting lifecycle, error, resource, compatibility and documentation
   requirements need explicit tasks, not only a general reminder.
6. Add reverse navigation: requirements name delivery task IDs; checklist items
   link back to the precise requirement and architecture. Reconcile mappings on
   renames, splits or scope changes. Every in-scope requirement MUST have a task
   or an explicit deferred/out-of-scope decision with its future acceptance gate.
7. At completion, record actual validation commands, outcomes and limitations in
   the feature record. Reconcile requirement scope, architecture, task status and
   user guidance. Documentation planning does not authorize implementation,
   commits, publication or installation.

## Worked example

A requirement R1 states that cancelling an import SHALL preserve the previously
accepted document. Its architecture defines candidate validation and atomic
adoption. A suitable task is:

```text
TASK-02: Integrate atomic import adoption and cancellation.
Requirements: R1 (link to its exact requirement section).
Architecture: candidate/adoption owner (link to its exact design section).
Depends on: TASK-01 (bounded candidate parsing).
Paths: owner and regression-test files in the architecture path table.
Acceptance: cancellation before/during/after parsing preserves accepted identity
and contents, and a late completion cannot replace the accepted document.
```

The adopting checklist uses real relative Markdown links, not these prose link
instructions. A task saying only 'finish importer' with no acceptance or owner is
incomplete. A test task links the same requirement, rather than inventing a second
requirement for the same behavior.

## Failure cases and acceptance checks

Check file existence AND section targets, including explicit anchors if used.
Detect duplicate requirement/task IDs, stale links, omitted requirements, unknown
prerequisites and dependency cycles. Verify that new stage tasks cover the complete
architecture stage inventory. Check one complete requirement → task → owner/test
chain, one cross-cutting requirement, one deferred case and one failed/partial item.

For an existing project, compare old/new IDs and statuses and preserve unrelated
index/worktree changes. For a new project, verify the template's local links work
without another checkout. Missing evidence leaves an item unchecked; an unresolved
prerequisite is a recorded gap, not a reason to implement unrelated work.
