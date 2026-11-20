# Accepted backend delivery plan

Current execution status: bounded synthetic stage science, generic source JSON
and native APIs are recorded in the [backend validation](../backend-stages/validation.md).
The design history below is retained; capture/import, broader PHY and presentation
items do not gain runtime acceptance from completed design checkboxes.

Subsequent status, 2026-11-20: the user authorized starting this plan. The
[source audit and standalone codec acceptance](../ldpc-source-audit/validation.md)
close LDPC-01/02. The original decision-only record follows; remaining runtime
work stays in the [official checklist](../../checklist.md).

Status: six scope/order decisions accepted; implementation and scientific
acceptance remain pending. This task records the decisions and reconciles
architecture → requirements → developer checklist. It adds no source modules,
dependencies, bindings, schemas or capture importers and does not start coding.

## Accepted decisions and traceability

The canonical [architecture decisions](../../../architecture.md#accepted-backend-delivery-decisions)
own the milestone boundary and planned file dispositions. The requirements
retain their 59 existing IDs; these are refinements rather than a second baseline.

| Decision | Accepted direction | Requirements / active tasks |
| --- | --- | --- |
| BACKEND-01 | Audit/correct/independently validate all three LDPC families first. | [REQ-TX-02](../../../requirements.md#req-tx-02), [REQ-SYS-05](../../../requirements.md#req-sys-05); LDPC-01/02 before waveform work. |
| BACKEND-02 | Keep MORGANA standalone and borrow suitable reviewed source into local owners, with attribution and upstream acceptance. | [REQ-NFR-02](../../../requirements.md#req-nfr-02), [REQ-SYS-03](../../../requirements.md#req-sys-03); DEV-CORE-01, DEV-LICENSE-01. |
| BACKEND-03 | Deliver bounded cancellation/partial results first; pause/resume follows the reference milestone and its own state-preservation checks. | [REQ-LIFE-02](../../../requirements.md#req-life-02), [REQ-LIFE-03](../../../requirements.md#req-life-03); DEV-RUN-01, DEV-PAUSE-01. |
| BACKEND-04 | Establish independent source-checked expectations before implementing each stage; build them stage by stage. | [REQ-SYS-05](../../../requirements.md#req-sys-05); LDPC and each TX/CH/RX stage acceptance. |
| BACKEND-05 | Typed synthetic configuration drives the first loop; JSON and verified PNM loaders follow. Retain full applicable MULPI delivery. | [REQ-CFG-05](../../../requirements.md#req-cfg-05), [REQ-CFG-04](../../../requirements.md#req-cfg-04), [REQ-PNM-01](../../../requirements.md#req-pnm-01); DEV-LOOP-01 before JSON-loader/PNM integration. |
| BACKEND-06 | Build the Rust API with the backend, exercise the unity loop through it, then implement native Python. | [REQ-API-01](../../../requirements.md#req-api-01), [REQ-API-02](../../../requirements.md#req-api-02); API-RUST/INPUT-01 → API-RUN-01 → DEV-LOOP-01 → API-PY/STUB-01. |

Standalone means no dependency on another application crate, checkout or runtime.
Source adaptation preserves origin/revision/licenses and uses independently
checked upstream contracts. It is not an instruction to copy every reference
module or assume downstream numerology/labels are suitable. Existing local
sparse-encoder adaptation and pinned external Rust dependencies remain valid;
no new external numerical library or shared cross-project crate is selected.
Reference checkout inspection remains read-only.

## First milestone and later work

First delivery is a bounded Rust API experiment using typed synthetic US
Configuration and PRBS → CM-US-TX → exact unity CH-SIM → configured-timing
CMTS-US-RX → independent comparison. Real cancellation retains completed and
explicit incomplete outcomes. Every stage has independent expectations before
its implementation; source-table checks remain required even if round trips pass.

Pause/resume, JSON loading, capture import, impairments and native Python remain
later capabilities. Separate tasks enforce their dependencies; the later pause
task does not block the initial loop, loaders or initial wrapper. Python controls
stay unavailable until corresponding Rust behavior and native parity are verified.
Full later requirements are retained rather than converted to optional obligations.

## Layout and status changes

| Existing document / disposition | Change |
| --- | --- |
| `docs/architecture.md` / edit | Six accepted decisions, first/later milestones and concrete implementation-owner paths with add/edit/reuse status; API order and reuse strategy reconciled. |
| `docs/requirements.md` / edit | Mandatory clauses refine the existing source/testing, codec, configuration, API, lifecycle and reuse requirements; no renumbering. |
| `docs/development/checklist.md` / edit | Move the Rust session task alongside typed configuration and Rust run integration before the loop; explicit loader/Python gates; add pending DEV-PAUSE-01. |
| `docs/development/features/public-api/design.md` / edit | Match the accepted Rust-first/native-Python-after-loop milestone. |
| `docs/development/features/foundation/design.md` / edit | Record local adaptation as the selected standalone strategy, with no shared cross-project crate selected. |
| `docs/development/README.md`, `AGENTS.md` / edit | Discover and apply the accepted milestone decisions. |

Scientific code/test files remain those in each architecture stage/API section;
this documentation task creates none of them. Completed design records and all
existing task IDs/statuses are preserved. The known matrix discrepancy remains
open under LDPC-01. Concrete cumulative job budgets, individual code/dependency
admissions, source vectors, schema field coverage and capture formats still need
their specified audits/decisions before dependent implementation.

## Completion and validation

- [x] Record the six accepted architectural decisions and planned owners.
- [x] Refine mandatory requirements and retain their IDs and broader obligations.
- [x] Reconcile dependency ordering and retain incomplete scientific status.
- [x] Validate links, coverage, old IDs/statuses and the dependency graph; run the
  required existing gate and record actual evidence before handoff.

## Validation

`bash scripts/validate.sh` passed: 20 skills, 856 local links, 23 existing Rust
tests, 19 setup tests, 5 Git-helper tests, doctests, formatting and Clippy. Test
durations reported 0.737 seconds for Git tooling, 0.884 seconds for setup and
0.39 seconds for the 21 LDPC cases; two facade cases reported 0.00 seconds.
These validate the existing checkpoint, not source-table or waveform acceptance.

Focused checks preserved all 97 existing task IDs/statuses and 59 requirement
IDs/anchors. All requirements map to the 59 pending tasks, including the new
DEV-PAUSE-01. Dependencies are known, ordered and acyclic; Rust run integration
precedes reference-loop acceptance, loaders/Python follow it, and pause is not
a prerequisite for those initial capabilities. All 714 local links/fragments in
the eight Markdown-only changed/new files resolved. Git whitespace checks passed;
planned PHY/API/binding source directories remain absent.

No scientific implementation, table correction, new dependency, source import,
native Python execution or external interoperability validation occurred. No
staging, commit, push or system installation was performed. Reference repositories
and generic PDE guidance were not modified by these project-specific decisions.
