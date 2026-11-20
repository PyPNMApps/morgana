# CMTS-US-RX block and stage design

Status: receiver block overview, processing chart, stage navigation and planned
file ownership defined. Detailed RX-01..09 contracts and scientific implementation
remain planned. Scope is architecture documentation in this repository.

## Requirements

| ID | Requirement | Owner / acceptance |
| --- | --- | --- |
| RX-ARCH-01 | Use CMTS-US-RX and show the nine ordered receiver stages. | Canonical block architecture, one processing chart and matching local stage index. |
| RX-NAV-01 | Link every overview/output label to its corresponding section and back to the index. | Nine unique stage targets, 18 linked overview/output rows and major-section contents links. |
| RX-PATH-01 | Name implementation/shared numerical/test files per stage with create/reuse disposition. | Existing codec reuse is verified; proposed PHY files remain absent and algorithms have one owner. |
| RX-INPUT-01 | Recover from received samples and a receiver-specific accepted configuration. | No injected H/C, RxMER target, channel seed, original bits or PRBS truth in normal recovery. |
| RX-STATE-01 | Bound work/state and preserve completed outcomes on pause/cancel/failure. | Receiver composition; per-stage contexts, partial status, no silent gap filling or restart on inspection. |
| RX-DOMAIN-01 | Separate samples, physical/equalized cells, soft bits and decoded information. | Stage boundaries and passive SA/QAM/LLR/FEC inspection; source association/comparison outside RX. |
| RX-SCOPE-01 | Keep scheduled-data/configured-timing scope and stage design status explicit. | No blind acquisition, ranging/probe processing, downstream BCH/PLC/NCP or implementation claim. |

## Architecture and reuse

The [CMTS-US-RX block](../../../architecture.md#cmts-us-rx-block-architecture)
owns the chart, input/result/lifecycle contract and stage path tables.
The [receiver stage sequence](../../../architecture.md#receiver-stage-sequence)
is the linked index. Shared numerical/resource owners remain those proposed by
CM-US-TX; adapters use independent receiver state. The already implemented
`crates/ldpc/src/codec.rs` is reused only after source-validation prerequisites;
its existence does not make RX-08 or the integrated receiver implemented.

Read-only reference review used MERLIN revision
`096d5a476194d4f2e016863d723b225257bb6037`: receiver composition, owned timing/
transform/extraction boundaries, received-pilot estimation and retained stage
observations. Its supplied-H reference path, fixed downstream geometry and
PLC/NCP/BCH owners are not this receiver's normal inputs or processing chain.
No reference code, capture or presentation asset is copied or linked here.

| Local owner / disposition | Contract |
| --- | --- |
| Planned `crates/phy/src/receiver/mod.rs`, `crates/phy/src/receiver/result.rs` | Focused sequencing and owned outcomes; no numerical monolith or original-source comparison. |
| Planned `crates/phy/src/configuration/receiver.rs` | Receiver-specific policies/limits, composing accepted grant/profile/waveform settings without whole-run channel truth. |
| Planned shared transform/QAM/randomizer/resources/grant owners | Reuse the same conventions/labels/plans, with separately owned RX contexts and independent acceptance vectors. |
| Planned `crates/phy/src/signal_processing/channel_estimation.rs`, `crates/phy/src/signal_processing/equalization.rs` | Received-pilot estimate/correction owners; details belong to ARCH-RX-04. |
| Planned `crates/phy/src/signal_processing/demapping.rs` | Soft-demapping numerical owner using shared label/scale tables; details belong to ARCH-RX-06. |
| Existing `crates/ldpc/src/codec.rs` | Standalone codec reuse; keep LDPC-01/02 source/milestone gaps visible and no BCH dependency. |

The receiver order is a local engineering decomposition of the accepted upstream
path. Controlling upstream evidence remains CM-SP-PHYv3.1-I20-230419 §7.4.1,
§7.4.3–7, §7.4.9–11 and §7.4.16–17. Corresponding TX sections record their
source/figure reviews; this overview adds no new source-table transcription or
numerical receiver algorithm. Detailed stage work must verify the applicable
source conventions and independent tests before claiming complete contracts.
The [publisher's pinned PHY I20](https://account.cablelabs.com/server/alfresco/4eb470eb-aca3-4e64-af88-773b8c594fbd)
was checked for revision/section identity. Real MAC message parsing needs separate
MULPI evidence; existing probe RxMER input does not implement a probe receiver.

## Dependency-ordered checklist

- [x] ARCH-RX-00: Define the CMTS-US-RX block, chart, nine stage roles, input/
  result boundaries, lifecycle and inspection overview.
- [x] ARCH-RX-NAV: Link all nine overview/output rows to local stage sections,
  with index backlinks and contents/development navigation.
- [x] ARCH-RX-PATH: Add planned code/test paths for every RX section and identify
  actual codec reuse; no empty modules or new Cargo member.
- [ ] ARCH-RX-01: Expand configured-timing framing, indexed input admission,
  bounded buffering, discontinuities, completion and independent acceptance.
- [ ] ARCH-RX-02: Expand useful-window selection, CP/overlap boundaries and
  sample identity/validity without receiver access to TX samples.
- [ ] ARCH-RX-03: Expand centered unitary FFT admission/metadata and independent
  forward vectors, sharing the TX-07 numerical owner.
- [ ] ARCH-RX-04: Expand upstream pilot references, effective C×H estimation,
  coverage/reliability, correction and null/failure behavior.
- [ ] ARCH-RX-05: Expand resource extraction and exact inverse visits across
  blocks/frames, preserving loading/roles and bit/cell conservation.
- [ ] ARCH-RX-06: Expand MSB-first soft metrics, label/scale/noise-confidence
  semantics, hard-decision observations and independent acceptance.
- [ ] ARCH-RX-07: Expand grant mask regeneration on LLRs, codeword ordering,
  pad removal and chunk/offset state.
- [ ] ARCH-RX-08: Expand shortening restoration, codec admission and separate
  convergence/syndrome/known-zero/decision/iteration outcomes.
- [ ] ARCH-RX-09: Expand receiver-known information deframing and partial output,
  preserving independent source association/comparison outside the block.
- [ ] WAVE-RX-01: Implement approved receiver stages after source/TX/unity-channel
  prerequisites and compare actual recovered bits in the separate verifier.

Next detailed architecture section: RX-01. No stage is marked complete merely
because its heading, file table or diagram exists. Stage IDs remain RX-01..09;
the enclosing block's full name is CMTS-US-RX.

## Validation

Check section fragments, unique targets, stage order, overview/output/backlink
coverage, planned-path absence and actual reused-path existence. Run the local
validation gate for checkpoint regression. These checks do not execute the
proposed receiver, prove source matrices or establish Rust/Python/UI parity.

On the Ubuntu 22.04.5 LTS checkout, `scripts/validate.sh` passed in 3.20 seconds:
20 skills, 315 local links, 23 existing Rust tests, 19 setup tests, 5 Git tests,
formatting and Clippy. Focused checks resolved 129 section links in the six
changed/new documents, all 18 RX overview/output links to nine unique stage
targets, nine index backlinks and the major-section contents. All 38 unique
proposed receiver/shared paths remain absent; the one reused codec path exists.
TX/channel navigation remains intact. RX-01..09 detailed designs and scientific
milestones remain unchecked. `git diff --check` passed. No receiver processing,
new numerical algorithm, Python binding or native UI was executed by this work.
