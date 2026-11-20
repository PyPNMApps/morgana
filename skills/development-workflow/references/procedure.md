# Architecture through implementation

## Inputs and first decision

Read the requested goal, constraints, current instructions/revision and existing
architecture/requirements/status records. Classify the task as a new codebase or
existing behavior. A feature in an existing application uses the existing-code
path. A planning request stops after architecture, requirements and checklist;
these documents do not authorize implementation or external actions.

## Procedure

1. Define or update the architecture first. For existing code inspect owners,
   callers, tests and build registration before proposing changes. Record the
   design/data/lifecycle/error boundaries, reuse decisions and validation approach.
2. Define the software layout in that architecture. Name concrete repository-relative
   implementation/test/registration files and label add (planned), edit (existing)
   or reuse (unchanged). Check existing paths before assigning their disposition.
   Use the target project's naming conventions; this workflow assumes no language.
3. Derive complete observable requirements from the architecture. Each stable ID
   uses MUST, MUST NOT, SHALL or SHALL NOT, has acceptance criteria and links to
   the relevant design section. Record constraints, exclusions and unresolved
   decisions explicitly; an advisory proposal needs a mandatory/excluded/deferred
   decision before baseline acceptance or dependent implementation.
4. Build the developer checklist from those requirements and design owners.
   Each task links its requirement, names dependencies and acceptance, and links
   architecture whenever design, ownership or file placement applies. Document
   why architecture does not apply for a task with no design impact. Put prerequisite
   tasks before consumers; combined milestones stay pending until their parts pass.
5. Implement and validate an authorized slice. If requirements expose a missing
   design decision, revise the architecture, reconcile requirements and refresh
   dependent tasks before code; do not implement against contradictory records.
6. Reconcile architecture, requirements, checklist, actual validation and affected
   user guidance. Preserve stable IDs/history while reopening invalidated acceptance.
   Report commands, outcomes and unsupported environments accurately.

## Architecture navigation

1. Inventory the blocks/stages in each overview and reuse their existing canonical
   sections. Link each overview label to the appropriate local heading or explicit
   anchor; do the same in stage-output tables. For diagrams whose labels are not
   reliably clickable, provide a companion Markdown table or index.
2. Keep stage IDs and target anchors stable. If a stage has no detailed design yet,
   add a short section with its responsibility and explicit planned/placeholder
   status. Leave its design and implementation checklist items pending.
3. Link detailed sections back to the overview when useful for a long staged design.
   On a rename or move, update every incoming link and check for duplicate anchors.
4. Verify fragment targets as well as file existence. A file-only link checker
   cannot prove that a section exists. Review all overview rows against the section
   inventory and confirm that links land on the intended stage.

For example, the following neutral overview links to an actual section below:

| Stage | Status |
| --- | --- |
| [STAGE-01: Transform](#stage-01-transform) | Placeholder; design pending. |

### STAGE-01: Transform

Placeholder: converts the accepted input representation to the next stage's
representation. Detailed contracts and implementation remain planned.
[Return to the overview](#architecture-navigation).

Acceptance: every overview stage resolves to one intended local section, section
IDs remain unique, and placeholders retain pending status. In a new project,
start with the linked architecture template; in an existing project, add links to
current owners without duplicating their design. Missing fragments, renamed
headings, duplicate section IDs and placeholders marked complete are failures.

## Code layout per section

During architecture, inspect the current tree and name the concrete files each
block/stage will create, reuse or extend. Put a compact path table in that section,
covering implementation, module/build registration, adapters and meaningful tests
where applicable. A directory-only owner or a global tree without per-section
mapping does not show where the work will land.

Use full repository-relative paths. For existing files, verify their role and
existence; for proposed files, say create (planned). Use code formatting for paths
that do not exist yet, and links only for existing targets. A planned file table
does not authorize creating empty code or imply implemented behavior.

The following filename convention is language-independent. Angle-bracket
segments are template placeholders; replace every segment with concrete target
paths and dispositions before publishing the adopting architecture:

| Path | Disposition | Responsibility |
| --- | --- | --- |
| `<source-root>/<component>/<operation>.<source-extension>` | Add (planned) | Operation and validated domain inputs. |
| `<build-or-registration-file>` | Add or edit after inspection | Register the focused component when the project requires it. |
| `<test-root>/<component>/<operation>.<test-extension>` | Add or edit after inspection | Independent expected-output and invalid-input cases. |

Name a shared algorithm's same canonical path in each consuming stage and identify
stage-specific adapters separately. Backfill previously written sections when the
rule is introduced; keep a directory overview for scanning and reconcile it with
the section tables when placement changes. If a placement is undecided, record the
open decision and its owner rather than presenting a placeholder as settled.

Acceptance: each block/stage has explicit file paths and dispositions, existing
paths resolve, planned files are not falsely linked or created, and sections agree
on shared ownership. Verify one new section and one backfilled existing section.
Missing filenames, two competing algorithm owners, stale paths and an existing
file mislabeled as new are failures. Design-only sections with no code change
MUST state that explicitly rather than inventing implementation files.

## Filename conventions

The generic workflow does not select a programming language or file extension.
Use descriptive names for a component's responsibility and preserve the target
repository's established capitalization, separators, extensions and directory
structure. Record full repository-relative paths, not workstation paths.

Architecture file tables MUST distinguish Add (new planned file), Edit (existing
file to change) and Reuse (existing unchanged file). State the responsibility of
each implementation, registration/build and test file. Verify existing files and
resolve template placeholders to concrete filenames before implementation. Language
or framework rules belong in their separate applicable skills, not this workflow.

## Worked example

Architecture: a transformation owner builds a bounded candidate and validates it
before atomic publication, with cancellation/stale-generation checks and named
implementation/test files to add or edit.
Requirement R1: a cancelled/failed transformation SHALL preserve the accepted
result; success SHALL publish a validated result atomically. Link R1 to that owner.
Checklist: establish the owner → implement cancellation/publication → independently
validate success/failure/stale results → reconcile documentation. Each task links
R1 and its applicable architecture section.

## Deliverables and failure cases

Use the local [requirements](../../../templates/project/requirements.md),
[architecture](../../../templates/project/architecture.md) and
[checklist](../../../templates/project/checklist.md) templates. A small task can
combine these sections in one file. Missing acceptance criteria or an unknown
ownership boundary is a design gap to resolve, not permission for broad refactoring.


[Skill](../SKILL.md)

## Traceable software development checklist

Apply the [requirements/checklist procedure](checklist-traceability.md) when
creating or updating delivery tasks. It defines direct links, dependencies,
acceptance, bidirectional coverage and the distinction between design and runtime.
