# Requirements through implementation

## Inputs and first decision

Read the target's instructions, current revision/status, existing architecture and
active requirement records. Classify the task as new codebase or existing behavior.
A new feature in an existing application uses the existing-code path. If the user
requested only a plan, stop after the design/checklist; documents do not authorize code.

## Procedure

1. Write observable requirements with stable IDs, acceptance criteria, constraints
   and non-goals. Separate unknowns from accepted behavior. Avoid implementation
   choices disguised as requirements (for example, a class name).
2. For existing code trace entrypoints, owners and tests, then write the behavioral
   delta. For new code identify the minimal public operation and data model needed
   to demonstrate the first requirement.
3. Design responsibility/data/lifecycle/error boundaries. Record alternatives only
   where they explain the decision. Name the existing extension point or justify a
   new owner. Include a requirement-to-owner-to-test mapping.
4. Create dependency-ordered checklist items small enough to verify independently.
   Put prerequisites ahead of dependent UI or adapters. Mark blocked/partial items
   honestly; a combined item stays unchecked until all acceptance checks pass.
5. Implement a vertical slice, validate it, then continue. Update the design if the
   actual contract changes; do not leave an abandoned plan described as implemented.
6. At handoff reconcile requirements, architecture, checklist, user guidance and
   software facts. Report actual commands/results and any unsupported environment.

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

A fictional project's transform section might contain:

| Path | Disposition | Responsibility |
| --- | --- | --- |
| `src/processing/transform.rs` | Create (planned) | Transform algorithm and validated domain inputs. |
| `src/processing/mod.rs` | Extend (existing in the example project) | Register the focused module. |
| `tests/transform.rs` | Create (planned) | Independent expected-output and invalid-input cases. |

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
should state that explicitly rather than inventing implementation files.

## Worked example

R1: cancelling an import leaves the previous accepted document usable.
Architecture: importer creates a candidate; document owner replaces accepted state
only after full validation. Cancellation invalidates the candidate generation.
Checklist: add candidate owner → cancellation checks → controller integration →
late-result regression → user help. Acceptance: cancel before parse, during parse
and immediately before completion; accepted document identity/content remain equal.

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
