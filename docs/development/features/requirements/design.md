# Architecture-derived requirements baseline

Status: documentation consolidation only. No scientific source, API module,
binding, schema or capture importer is implemented by this work.

## Request and procedure

Create a project-wide requirements document from the existing architecture.
Apply the local development-workflow skill and requirements template: observable
behavior with stable IDs, scope/non-goals, acceptance criteria, constraints,
unknowns and requirement-to-owner-to-validation traceability. This is the
existing-code workflow; current behavior and pending design must remain distinct.

The [requirements baseline](../../../requirements.md) consolidates existing
contracts without reopening source tables or adding standard-derived behavior.
Source/algorithm detail stays in the architecture and linked feature records.
All referenced specification claims retain their existing evidence boundaries;
no new PDF/specification audit is asserted.

## Document ownership and reuse

| Document / disposition | Responsibility |
| --- | --- |
| `docs/requirements.md` / create | Stable project-wide REQ IDs, behavior, acceptance, scope and explicit open decisions. |
| `docs/architecture.md` / extend navigation | Canonical scientific/API design, owner boundaries, exact algorithms, planned implementation/test paths; link requirements without duplicating design. |
| `docs/development/checklist.md` / extend | Official runtime/source/delivery status; completion of this documentation does not complete scientific/API gates. |
| `docs/development/features/*/design.md` / reuse | Existing feature-local requirement IDs, detailed acceptance and actual validation records; preserve their traceability. |
| `templates/project/requirements.md` / reuse | Local requirements structure: purpose/scope, ID/behavior/acceptance and constraints/open questions. |
| `README.md`, `AGENTS.md`, `docs/development/README.md` / extend | Discover the baseline and read requirements before architecture/checklist/implementation. |

Requirements rows link to the canonical stage/block or feature owner and name
existing delivery IDs. Architecture links supply the concrete implementation and
test paths. Requirement IDs are new stable project identifiers, not replacements
for TX/RX/feature IDs or instructions to renumber existing records.

## Completion checklist

- [x] REQ-BASELINE-01: Consolidate system/configuration/source, eight TX stages,
  six channel stages, nine RX stages, PNM inputs, instruments, paired APIs and
  lifecycle/nonfunctional requirements with acceptance and traceability.
- [x] Distinguish current FEC/tooling evidence, unity-loop delivery, later
  measurement/impairment features, planned presentation and unresolved formats.
- [x] Link the baseline from architecture, development index, README and agent
  instructions; retain pending source/runtime milestones in the official checklist.
- [x] Validate navigation, coverage, stable IDs and the required existing gate;
  record actual results below before handoff.

## Validation

`bash scripts/validate.sh` passed in the local checkout: 20 skills, 454 local
file links, 23 existing Rust unit tests, 19 setup tests, 5 Git-helper tests,
doctests, formatting and Clippy. Reported test durations were 0.782 seconds
for Git tooling, 0.964 seconds for setup and 0.40 seconds for the 21 LDPC cases;
the two facade cases reported 0.00 seconds. These checks cover existing behavior,
not new waveform/API implementation or unresolved matrix-source acceptance.

Focused document checks confirmed 59 unique requirement IDs, complete coverage
of eight TX, six channel and nine RX stages, acceptance and owner/delivery fields
for every requirement, and valid section links across all seven Markdown-only
changes. A PRBS lifecycle link with slash punctuation was corrected during the
navigation check. Planned PHY/API/binding source directories remain absent.
`git diff --check` passed.

No future requirement is satisfied merely by these document checks. No new
scientific/runtime, capture-format, native Python, hosted/platform or provisioning
acceptance was executed. Source/specification gaps remain pending. The save
command is prepared only; no staging, commit, push or installation occurred.

## Mandatory requirement wording

The baseline uses uppercase SHALL and MUST for obligations, and SHALL NOT and
MUST NOT for prohibitions. Advisory requirements are prohibited; a recommendation
requires an explicit mandatory, excluded or deferred decision before baseline
acceptance. Unresolved design choices require a decision before dependent work.
Optional field/capability applicability and consumer installation choices remain
distinct from mandatory delivery and acceptance obligations. All 59 requirement
IDs and architecture/checklist links are retained.

`bash scripts/validate.sh` passed again: 20 skills, 454 local file links,
23 Rust tests, 19 setup tests, 5 Git-helper tests, doctests, formatting and Clippy.
Focused checks preserved all 59 requirement IDs and all prior document links,
confirmed uppercase mandatory keywords and found no advisory keyword. Git
whitespace checks passed. Scientific/API implementation status is unchanged.
