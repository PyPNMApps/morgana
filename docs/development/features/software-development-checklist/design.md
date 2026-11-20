# Software development checklist and traceability

Status: checklist/guidance documentation only. Scientific implementation remains
subject to the current approval boundary. No source/runtime/module work occurs.

## Requirements

| ID | Required behavior | Acceptance |
| --- | --- | --- |
| TRACE-01 | The official checklist SHALL derive tasks from requirements and architecture with direct stable links. | All 59 baseline requirements map to active tasks; every task has requirement/architecture targets, dependencies and observable acceptance. |
| TRACE-02 | Existing task identifiers and completion evidence MUST be preserved. | All 67 prior IDs and statuses survive; completed design/tooling records remain separate from unimplemented science. |
| TRACE-03 | Prerequisites SHALL precede dependent implementation and cover each stage. | Eight TX contracts, six channel contracts and nine RX contracts map to stage work; known source/format/decision gaps remain pending; dependency graph has no unknown IDs or cycles. |
| TRACE-04 | Workflow guidance SHALL define the same traceability in the local bundle and generic foundation. | Self-contained skill procedure and working local templates cover both new/existing projects, explicit requirement decisions, links, evidence, coverage and failure cases. |

## Ownership and scope

| Path / disposition | Responsibility |
| --- | --- |
| `docs/development/checklist.md` / extend existing | Canonical ordered software tasks, retained historical records and complete requirement coverage table. |
| `docs/requirements.md` / extend existing | Explicit per-ID table anchors and reverse coverage navigation; obligation IDs/behavior stay stable. |
| `docs/architecture.md`, `docs/development/README.md`, `AGENTS.md` / extend existing | Discover the canonical checklist and require linked traceability before implementation. |
| `skills/development-workflow/SKILL.md`, `references/procedure.md` / extend existing | Route to the detailed reusable workflow. |
| `skills/development-workflow/references/checklist-traceability.md` / create | Generic inputs, workflow, example, decisions, failure cases and acceptance checks. |
| `templates/project/requirements.md`, `templates/project/checklist.md` / extend existing | Linked requirement/architecture/checklist examples that work within the bundle. |

Reuse the established official checklist instead of adding a competing completion
list. Existing parent milestones remain pending until their stage acceptance is
complete. The first scientific prerequisite is still LDPC-01, including its known
matrix discrepancy. Configuration JSON/PNM/native/GUI acceptance remains pending.
Dependencies are explicit edges; later presentation/measurement sections do not
become implicit prerequisites for an accepted typed reference experiment.

PDE changes are explicitly authorized for this task and use generic wording;
the foundation owns its separate change record. Its existing unrelated dirty
worktree and index are preserved. No source checkout links are introduced into
MORGANA or the generic procedures.

## Completion and validation

- [x] TRACE-01: Create direct requirement anchors, linked tasks and coverage.
- [x] TRACE-02: Preserve existing IDs/status and separate historical records.
- [x] TRACE-03: Define ordered tasks and explicit stage/dependency acceptance.
- [x] TRACE-04: Update local and generic workflow procedures/templates.
- [x] Validate links, IDs/status preservation, coverage and dependency graph;
  run both repositories' required checks and record results before handoff.

## Validation

`bash scripts/validate.sh` passed: 20 skills, 825 local file links, 23 Rust tests,
19 setup tests, 5 Git-helper tests, doctests, formatting and Clippy. Reported
durations were 0.896 seconds for Git tests, 1.018 seconds for setup and 0.41
seconds for the 21 LDPC cases; the two facade cases reported 0.00 seconds.
These are existing checkpoint checks, not new scientific acceptance.

Focused checks passed for 67 retained task IDs/statuses, 58 active tasks, all
59 requirements, eight TX/six CH/nine RX contracts, known ordered dependencies
without cycles, and 785 local links/section targets across the scoped bundles.
Both updated skills passed skill-creator metadata validation. The generic
requirement/checklist templates resolve within their own local bundles.
Planned PHY/API/binding source directories remain absent. Git whitespace checks
passed. No new runtime, source-table, format, native Python, GUI, provisioning,
hosted CI or publication evidence is claimed.

PDE's whole-checkout guidance/portability checker and all 31 existing tests passed;
its separate feature record captures the prior dirty-state preservation boundary.
No index changes, staging, commits, pushes or system installation occurred.

## Generic workflow review

Review scope: the staged checklist/requirements guidance and reusable workflow
templates, plus the corresponding PDE bundle. Project-specific scientific
requirements stay in project documents; reusable rules have no such dependency.
The existing staged index is preserved during review.

Three issues were corrected in both bundles:

- Requirement/checklist examples described an import while their architecture
  target described a transform. All three now use one fictional transformation
  with isolated candidate state, validated atomic publication and stale/cancelled
  generation rejection.
- Language-specific filenames could be mistaken for a required technology/layout.
  The templates now use language-independent filename placeholders and require
  concrete target-specific paths before implementation.
- A single-checklist/status-preservation rule could be misread as forbidding
  scoped feature checklists or reopening invalidated acceptance. Guidance now
  declares one status owner per scope, permits indexed feature checklists and
  requires evidence-based reopening with retained history.

The requested canonical sequence is now Architecture → Requirements → Developer
checklist → Implementation → Validation. Architecture defines responsibility and
software layout with files to Add, Edit or Reuse; every requirement uses MUST,
MUST NOT, SHALL or SHALL NOT and links its architecture owner. Developer tasks
link requirements and applicable design, with dependencies and acceptance.
The generic filename convention uses descriptive target-specific names and
extensions; language-specific examples/rules are excluded from this workflow.
Active skills, templates and entrypoints are reconciled to this sequence;
previous feature records remain historical evidence rather than current policy.

Review validation passed: the workflow skill, procedure and three templates are
language-independent and consistent in both bundles. Both relocated three-template
examples resolved all 40 relative links/fragments without another checkout.
Focused checks retained all 97 IDs/statuses in the saved checklist checkpoint,
58 active tasks, all 59 requirement mappings and ordered acyclic dependencies.
Both skills passed metadata validation. `bash scripts/validate.sh` passed with
20 skills, 829 local links, 23 Rust tests, 19 setup tests, 5 Git-helper tests,
doctests, formatting and Clippy. PDE's maintained-guidance checks and 31 tests
also passed. Generic naming rules impose no source language or extension.

During review, the original staged checklist checkpoint became commit `52bccec`
through an external action; direct ancestry and its unchanged index were verified.
The remaining review corrections are unstaged and no Git mutation was executed
by this work. Both existing indexes were preserved. PDE's 23 unrelated baseline
files remain byte-identical; additional edits are limited to the authorized
workflow-order guidance and templates. Historical validation paragraphs above
describe their original task boundary, not the subsequent external commit.
