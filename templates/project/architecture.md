# Feature architecture

Start from the requested goal and constraints. Define this architecture and
software layout first, then derive [mandatory requirements](requirements.md) and
the [developer checklist](checklist.md). Reconcile all three when the design changes.

## Current behavior and reuse

| Path / symbol | Verified contract | Requirement gap | Reuse / extend / candidate / reject |
| --- | --- | --- | --- |

## Proposed ownership and interfaces

Describe data flow, lifecycle, errors, concurrency and compatibility.

### Stage overview

For a staged design, link every block/stage label to its canonical local section.
Keep IDs/anchors stable and update incoming links when a heading changes. Add rows
and sections as needed; a diagram can use this table as its navigation index.

| Stage | Responsibility | Status |
| --- | --- | --- |
| [STAGE-01: Transform](#stage-01-transform) | Convert the accepted input for the next stage. | Placeholder; design and implementation pending. |

### STAGE-01: Transform

Placeholder: replace with the stage's inputs, outputs, owner, lifecycle, failure
behavior and acceptance checks as its design is developed. Keep its checklist
pending until the corresponding acceptance criteria are met.

Worked example for [R1](requirements.md#r1): a transformation owner builds a
bounded candidate result separately from the accepted result. It validates the
candidate before atomic publication. Failure or cancellation before publication
preserves accepted identity/content; stale cancelled generations cannot publish.
Successful completion adopts the validated result. Check these cases in the
stage regression tests. This is a fictional example, not implemented behavior.

#### Planned code paths

Use repository-relative filenames in each block/stage section, including existing
reuse/extension points and planned tests or registration changes. The paths below
use language-independent filename placeholders. Replace every placeholder
with actual target paths and the project's naming/extension conventions.
Use Add for a new planned file, Edit for an existing file to change, and Reuse
for an existing unchanged file. Verify existing paths before labeling them; keep
planned paths as code-formatted text until they exist.

| Path | Disposition | Responsibility |
| --- | --- | --- |
| `<source-root>/<component>/<operation>.<source-extension>` | Add (planned) | Stage algorithm and input validation. |
| `<build-or-registration-file>` | Add or edit after inspection | Component/build registration when needed. |
| `<test-root>/<component>/<operation>.<test-extension>` | Add or edit after inspection | Independent stage acceptance checks. |

[Return to stage overview](#stage-overview).

## Requirement mapping and validation

Map each requirement to an owner and a planned check. Record unresolved evidence.
