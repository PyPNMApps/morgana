# Architecture, requirements and developer checklist

[Skill](../SKILL.md) · [Requirements template](../../../templates/project/requirements.md) ·
[Architecture template](../../../templates/project/architecture.md) ·
[Checklist template](../../../templates/project/checklist.md)

## Inputs and outputs

Use the repository's current requirements, architecture, official checklist and
validation records. Keep established paths and identifiers in an existing project.
For a new project, instantiate the local templates. Declare the delivery scope
(project, feature or release) and its canonical checklist. Large projects can
link scoped feature checklists from an index; each task has one authoritative
status owner. Preserve that hierarchy rather than duplicating competing statuses.

## Required flow

**Architecture → Requirements → Developer checklist → Implementation → Validation → reconciliation.**

1. Define architecture from the requested goal and constraints. Identify owners,
   interfaces, data/lifecycle/error boundaries and the software layout. Name concrete
   implementation/test/build files to add, edit or reuse, with inspected dispositions.
   Use the target project's filename/extension conventions; no language is prescribed.
2. Derive all requirements from that design. Each stable requirement ID MUST use
   MUST, MUST NOT, SHALL or SHALL NOT, define observable acceptance and link its
   relevant architecture section. Resolve advisory proposals into mandatory,
   excluded or deferred scope; preserve external specifications' actual force.
   Use stable heading/ID anchors without renumbering existing requirements.
3. Derive small developer tasks from requirements. Every active task MUST identify
   its stable task ID, direct requirement links, prerequisite IDs and acceptance.
   Link architecture when design, ownership or file placement applies; otherwise
   record why there is no design impact. Resolve actual owner/test paths through
   that architecture. Shared behavior keeps one owner across its consumers.
4. Order prerequisites before dependent tasks. Spell out dependency edges rather
   than treating every earlier row as required. Separate source/design decisions,
   core implementation, integration, adapters, validation and deferred extensions.
   A parent milestone stays unchecked until all its required children pass.
5. Preserve existing task IDs, completion history and evidence when updating
   a checklist. Reopen a task if changed behavior or new evidence invalidates its
   acceptance; record the reason rather than retaining an inaccurate checked state.
   Clearly separate completed design/setup records from unfinished implementation;
   do not mark runtime acceptance complete because a section exists.
   Cross-cutting lifecycle, error, resource, compatibility and documentation
   requirements need explicit tasks, not only a general reminder.
6. Add reverse navigation: requirements name delivery task IDs; checklist items
   link back to the precise requirement and applicable architecture. Reconcile mappings on
   renames, splits or scope changes. Every in-scope requirement MUST have a task
   or an explicit deferred/out-of-scope decision with its future acceptance gate.
7. At completion, record actual validation commands, outcomes and limitations in
   the feature record. Reconcile requirement scope, architecture, task status and
   user guidance. Documentation planning does not authorize implementation,
   commits, publication or installation.

## Worked example

Requirement R1 states that a cancelled or failed transformation SHALL preserve
the accepted result, while successful completion SHALL publish a validated result
atomically. Its architecture owns candidate validation and publication. A task is:

```text
TASK-02: Integrate atomic result publication and cancellation.
Requirements: R1 (link to its exact requirement section).
Architecture: transformation/publication owner (link to its exact design section).
Depends on: TASK-01 (bounded candidate transformation).
Paths: owner and regression-test files in the architecture path table.
Acceptance: failure or cancellation before/during/immediately before publication
preserves accepted identity/content; successful completion publishes the validated
result, and a late cancelled generation cannot replace it.
```

Derive R1 from the architecture before writing TASK-02. The adopting checklist
uses real relative Markdown links, not these prose link
instructions. A task saying only 'finish transform' with no acceptance or owner is
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
