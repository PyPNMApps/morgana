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
