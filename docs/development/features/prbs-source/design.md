# PRBS block design

Status: architecture defined; SOURCE-01 implementation remains planned.
Scope: PRBS-TX source and independent PRBS-RX comparison. No scientific code, Qt
implementation, Python bindings or reference-project links are introduced.

## Requirements

| ID | Requirement | Owner and acceptance |
| --- | --- | --- |
| PRBS-01 | Explicit PRBS15 recurrence, seed/emission order, period and continuous absolute identity. | Rust source; independent literal vectors, all nonzero states and continuity across chunk/grant/codeword/period boundaries. |
| PRBS-02 | Request exact meaningful payload lengths from accepted upstream grants; separate fill, shortening and padding. | TX grant framing plus orchestration ledger; source counts and comparison exclude non-source bits. |
| PRBS-03 | Independently compare actual received decisions, preserving decoder failure outcomes. | Rust verifier outside CMTS-US-RX; exact injected mismatch counts and a parity-valid wrong payload. |
| PRBS-04 | Bound work/memory and preserve accepted state on invalid input or overflow. | Generator/verifier constructors and operations; zero-count, invalid seed/bits, oversized chunk and counter-boundary cases. |
| PRBS-05 | Detect incomplete/discontinuous recovery without hidden phase search or gap skipping. | Source association/verification coverage; missing, duplicate, reordered, wrong-run and wrong-length ranges retain prior totals and report incomplete status. |
| PRBS-06 | Freeze settings per run; pause/resume preserves state and restart resets with a new identity. | Orchestration; equivalent resumed stream, partial cancellation results and observer neutrality. |
| PRBS-07 | Present draft/accepted PRBS-TX settings and independent PRBS-RX readiness/results. | Future presentation adapter; Apply/Cancel, invalid drafts and readiness before any results exist. |
| PRBS-08 | Keep shared behavior in Rust with matching future native Python semantics. | Public facade/adapters; bounds, binary representation, owned results and absent-value/error parity. |

## Architecture and reference decisions

The canonical [PRBS block section](../../../architecture.md#prbs-block-architecture)
contains the complete sequence, stage-interface, comparison, lifecycle and UI
contracts. Keep those details there rather than maintaining a competing design.
Its section-level path table names planned `crates/phy/src/source/prbs15.rs`,
`crates/phy/src/source/verifier.rs`, shared `crates/phy/src/types/bits.rs`,
the simulation ledger/comparison adapters and their acceptance test files.
See the [directory overview](../../../architecture.md#planned-code-layout) for
module registration and future facade/adapter placement. All remain planned.
The future source module belongs to the proposed Rust PHY crate; the codec stays
independent of source generation. Neither the seed nor expected bits enter the
CMTS receiver. A grant/source ledger associates receiver grant/codeword output
with meaningful source positions outside receiver recovery.

Read-only reference inspection used revision
`096d5a476194d4f2e016863d723b225257bb6037` of MERLIN. This record has no links to
that repository; all required behavior is stated locally.

| Reference behavior | Decision for this block |
| --- | --- |
| Explicit nonzero 15-bit seed and recurrence/emission order | Reuse the mathematical contract, including initial draft seed `0x7fff`. |
| Separate generator/verifier state and actual mismatch totals | Reuse; keep expected truth outside receiver processing. |
| Bounded generation/comparison and rejected-call invariance | Reuse a proposed 1,048,576-bit per-call work limit with checked `u64` positions. |
| Fixed downstream payload helper | Replace with lengths from validated upstream grant/codeword selection; no downstream BCH constants. |
| Contiguous comparison supplied by the caller | Preserve; add explicit orchestration association/coverage requirements before claiming complete recovery. No implicit gap-aware verifier is assumed. |
| Parameter/Value editor with draft/accepted settings | Reuse the interaction contract; actual Qt implementation is separate. |
| File sources and optional finite PRBS fill | Defer; this block's first source choice is continuous PRBS15. |
| Existing deterministic ChaCha8 fixture | Preserve its current label/API; it does not become PRBS by documentation or renaming. |

This task copies no implementation code or presentation assets. Any future code
adaptation must preserve original copyright/license and modification notices.

## Dependency-ordered checklist

- [x] ARCH-PRBS-01: Inspect reference contracts and define the complete local block.
- [x] Reconcile canonical architecture, development navigation and official checklist.
- [x] Backfill concrete source/verifier, association and validation file paths.
- [ ] SOURCE-01a: Implement bounded PRBS generation and independent verifier with
  literal recurrence/period, rejected-call and overflow checks after plan approval.
- [ ] SOURCE-01b: Integrate validated grant-driven payload requests, source ledger
  and comparison coverage after PHY-01 provides accepted upstream grant lengths.
- [ ] SOURCE-01c: Validate failures, pause/resume, cancellation, restart and passive
  observations through the bounded closed loop; retain earlier completed results.
- [ ] API-PRBS-01: Expose source selection/results through the shared Rust facade;
  version exported report additions and implement/test future Python parity.
- [ ] UI-PRBS-01: Implement PRBS-TX editor and PRBS-RX acceptance/results after the
  scientific contracts and application adapter exist.

The official dependency order still starts with LDPC source validation. A
standalone source algorithm can be tested independently, but its grant integration
and full-waveform acceptance cannot bypass PHY-01 or the TX/channel/RX milestones.
Architecture approval and implementation authorization remain separate.

## Validation scope

Documentation checks cover local navigation/anchors, terminology, stage ownership,
reference-link exclusion and Git whitespace. Reference source and tests were
inspected; no reference test run or new PRBS runtime behavior is claimed.
MORGANA still implements the standalone LDPC checkpoint only. The pending LDPC
matrix-source finding remains unchanged and unchecked in the official checklist.

`python3 tools/validation/check.py` passed 20 skills and 252 local links.
Focused documentation checks resolved the new local section anchors and confirmed
that the new block/design contain no external repository links or workstation
paths. `git diff --check` passed. `scripts/validate.sh` passed the existing 23 Rust,
19 setup and 5 Git tests plus formatting and Clippy; these are checkpoint
regression results, not tests of an implemented PRBS block.
