# Official software development checklist

This is the canonical delivery checklist derived from the
[requirements](../requirements.md) and [architecture](../architecture.md).
Current authorization remains documentation/tooling and explicit development
setup; further scientific implementation awaits plan approval. No task grants
commit, push, publication, provisioning or GUI implementation authorization.

## How to use this checklist

Follow Requirements → Architecture → Checklist → Implementation → Validation.
Every active task links precise requirement anchors and canonical design owners;
those architecture sections specify implementation/test files and dispositions.
Dependencies are explicit task IDs, not every preceding item. Work on the first
unfinished authorized prerequisite. Completed design/history records are kept
separately below and do not satisfy corresponding runtime requirements.

A task SHALL remain unchecked until its implementation and acceptance evidence
pass. Record actual commands/outcomes/limits in its feature record. Aggregate
milestones MUST NOT close before their required stage tasks. Resolve advisory
choices into mandatory behavior or an explicit excluded/deferred decision before
dependent work. Preserve task IDs and requirement links across refinements.

The deferred section tracks design gates, not a promise of immediate support.
Core synthetic inputs do not require all later PNM formats. Shared contracts
MUST still be source-audited within their declared supported scope before use.

**Contents**

- [1. Source evidence and core admission](#1-source-evidence-and-core-admission)
- [2. Source and grant planning](#2-source-and-grant-planning)
- [3. CM-US-TX implementation and acceptance](#3-cm-us-tx-implementation-and-acceptance)
- [4. Unity CH-SIM boundary](#4-unity-ch-sim-boundary)
- [5. CMTS-US-RX implementation and acceptance](#5-cmts-us-rx-implementation-and-acceptance)
- [6. Closed loop, controls, instruments and results](#6-closed-loop-controls-instruments-and-results)
- [7. Complete configuration JSON and PNM admission](#7-complete-configuration-json-and-pnm-admission)
- [8. Supported channel impairment extensions](#8-supported-channel-impairment-extensions)
- [9. High-level Rust and native Python delivery](#9-high-level-rust-and-native-python-delivery)
- [10. Foundation delivery and deferred design gates](#10-foundation-delivery-and-deferred-design-gates)
- [Requirement coverage](#requirement-coverage)
- [Completed design and tooling records](#completed-design-and-tooling-records)

## 1. Source evidence and core admission

First scientific work remains LDPC-01 after implementation authorization. Shared types and supported reference configuration precede waveform stages.

- [ ] LDPC-01: Resolve the recorded matrix discrepancy and independently audit every upstream matrix/order.<br>
  Requirements: [REQ-SYS-05](../requirements.md#req-sys-05), [REQ-TX-02](../requirements.md#req-tx-02), [REQ-RX-08](../requirements.md#req-rx-08). Architecture: [design/owner](../architecture.md#tx-02-ldpc-encoding-and-shortening).<br>
  Depends on: none.<br>
  Acceptance: Original-page fixtures resolve the long matrix fifth-row, zero-based column-20 value (-1 in code versus 12 in the recorded PDF review); every family is checked independently of production constants.
- [ ] LDPC-02: Complete source-verified standalone codec acceptance.<br>
  Requirements: [REQ-TX-02](../requirements.md#req-tx-02), [REQ-RX-08](../requirements.md#req-rx-08), [REQ-SYS-05](../requirements.md#req-sys-05). Architecture: [design/owner](../architecture.md#tx-02-ldpc-encoding-and-shortening).<br>
  Depends on: LDPC-01.<br>
  Acceptance: All families pass independent parity/shortening, controlled errors, failed decisions and actual-iteration cases. The existing 23 tests alone do not close source acceptance; no external-interoperability claim.
- [ ] DEV-CORE-01: Register the reviewed PHY owners, shared typed boundaries and explicit resource/error contracts.<br>
  Requirements: [REQ-SYS-03](../requirements.md#req-sys-03), [REQ-NFR-01](../requirements.md#req-nfr-01), [REQ-LIFE-01](../requirements.md#req-life-01). Architecture: [design/owner](../architecture.md#planned-code-layout).<br>
  Depends on: LDPC-02.<br>
  Acceptance: Rust-only checks cover units, finite/index/size bounds, checked arithmetic and run/configuration identities; no Python/Qt dependency, duplicate scientific owner or empty executable placeholder.
- [ ] US-CONFIG-01: Implement the supported typed reference configuration, inventory/selection and legitimate TX/RX projections.<br>
  Requirements: [REQ-CFG-01](../requirements.md#req-cfg-01), [REQ-CFG-02](../requirements.md#req-cfg-02), [REQ-CFG-05](../requirements.md#req-cfg-05), [REQ-SYS-04](../requirements.md#req-sys-04). Architecture: [design/owner](../architecture.md#us-configuration).<br>
  Depends on: DEV-CORE-01.<br>
  Acceptance: Audit each reference-scope field before use; invalid settings preserve accepted state, all retained entries are discoverable, and normal RX excludes simulator truth. Full JSON/MULPI coverage stays separately pending.

## 2. Source and grant planning

These tasks use the accepted shared resource/configuration contract; source verification remains outside normal RX.

- [ ] PHY-01: Implement TX-01 resource capacity, grant/codeword selection and fill/pad accounting.<br>
  Requirements: [REQ-TX-01](../requirements.md#req-tx-01), [REQ-CFG-05](../requirements.md#req-cfg-05), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#tx-01-grant-framing-and-fec-selection).<br>
  Depends on: US-CONFIG-01.<br>
  Acceptance: Independent capacity/threshold/borrowing/byte-residue cases conserve source/fill/shortening/parity/pad counts; RX independently derives the same plan and invalid planning does not consume source.
- [ ] SOURCE-01: Implement continuous PRBS15, independent verification and source associations.<br>
  Requirements: [REQ-PRBS-01](../requirements.md#req-prbs-01), [REQ-PRBS-02](../requirements.md#req-prbs-02), [REQ-PRBS-03](../requirements.md#req-prbs-03), [REQ-PRBS-04](../requirements.md#req-prbs-04). Architecture: [design/owner](../architecture.md#prbs-block-architecture).<br>
  Depends on: DEV-CORE-01.<br>
  Acceptance: Literal seeds/period/chunk tests pass; invalid inputs and backpressure preserve state; wrong valid words count errors, gaps stop contiguous comparison, and no-payload BER is unavailable.

## 3. CM-US-TX implementation and acceptance

TX-01 is PHY-01 above. Each remaining task includes its independent stage checks; WAVE-TX-01 is the aggregate transmitter gate.

- [ ] DEV-TX-02: Integrate exact upstream LDPC encoding/shortening and ordered grant assembly.<br>
  Requirements: [REQ-TX-02](../requirements.md#req-tx-02). Architecture: [design/owner](../architecture.md#tx-02-ldpc-encoding-and-shortening).<br>
  Depends on: PHY-01, SOURCE-01, LDPC-02.<br>
  Acceptance: Independent full/shortened words, ordering and exact source/fill/parity/pad conservation pass without BCH or assumed puncturing.
- [ ] DEV-TX-03: Implement grant-seeded PHY randomization.<br>
  Requirements: [REQ-TX-03](../requirements.md#req-tx-03). Architecture: [design/owner](../architecture.md#tx-03-grant-seeded-phy-randomization).<br>
  Depends on: DEV-TX-02.<br>
  Acceptance: Literal first-mask/reset/chunk cases pass over every transmitted position, with no clocks for omitted shortening or pilots.
- [ ] DEV-TX-04: Implement MSB-first role-dependent QAM mapping.<br>
  Requirements: [REQ-TX-04](../requirements.md#req-tx-04). Architecture: [design/owner](../architecture.md#tx-04-cell-word-construction-and-qam-mapping).<br>
  Depends on: DEV-TX-03.<br>
  Acceptance: Independent upstream label/energy vectors cover the declared supported orders; mixed loading/inactive cells conserve visit order and bits.
- [ ] DEV-TX-05: Implement exact pilot roles/signs, block partitioning and joint address generation.<br>
  Requirements: [REQ-TX-05](../requirements.md#req-tx-05). Architecture: [design/owner](../architecture.md#tx-05-pilots-ofdma-framing-and-interleaving).<br>
  Depends on: DEV-TX-04.<br>
  Acceptance: Independent masks, permutations, edge/body/exclusion/zero-resource/boost cases pass; shared pure resource owners drive capacity and inverse RX expectations.
- [ ] DEV-TX-06: Implement accepted static Pre-EQ admission/defaults and carrier application.<br>
  Requirements: [REQ-TX-06](../requirements.md#req-tx-06). Architecture: [design/owner](../architecture.md#tx-06-cm-pre-eq).<br>
  Depends on: DEV-TX-05.<br>
  Acceptance: Independent normalization/complex/default/reset tests pass; excluded zeros and grid identity persist, C stays separate from H, and invalid/stale banks reject atomically.
- [ ] DEV-TX-07: Implement the accepted centered unitary upstream IFFT.<br>
  Requirements: [REQ-TX-07](../requirements.md#req-tx-07). Architecture: [design/owner](../architecture.md#tx-07-ifft).<br>
  Depends on: DEV-TX-06.<br>
  Acceptance: Independent direct-sum/tone/impulse/energy checks establish 2K/4K signs/bin order/scaling and exact useful sample metadata.
- [ ] DEV-TX-08: Implement CP/RP extension, taper, overlap, burst tails and explicit guards.<br>
  Requirements: [REQ-TX-08](../requirements.md#req-tx-08). Architecture: [design/owner](../architecture.md#tx-08-sample-assembly).<br>
  Depends on: DEV-TX-07.<br>
  Acceptance: Independent coefficient/numbered-sample/adjacent-symbol cases establish origins, complete length and chunk/backpressure invariance; partial cancellation is explicit.
- [ ] WAVE-TX-01: Complete one source-verified scheduled-data burst across all eight TX stages.<br>
  Requirements: [REQ-TX-01](../requirements.md#req-tx-01), [REQ-TX-02](../requirements.md#req-tx-02), [REQ-TX-03](../requirements.md#req-tx-03), [REQ-TX-04](../requirements.md#req-tx-04), [REQ-TX-05](../requirements.md#req-tx-05), [REQ-TX-06](../requirements.md#req-tx-06), [REQ-TX-07](../requirements.md#req-tx-07), [REQ-TX-08](../requirements.md#req-tx-08). Architecture: [design/owner](../architecture.md#cm-us-tx-block-architecture).<br>
  Depends on: DEV-TX-08.<br>
  Acceptance: Integrated bit/cell/sample accounting, independent source checks and passive stage taps agree; every required TX stage acceptance passes.

## 4. Unity CH-SIM boundary

No impairment is required for the initial closed loop. CH-03/04/05 are later extension tasks.

- [ ] DEV-CH-01: Implement indexed sample admission and bounded pipeline preflight.<br>
  Requirements: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design/owner](../architecture.md#ch-01-input-admission).<br>
  Depends on: WAVE-TX-01.<br>
  Acceptance: Finite clock/identity/continuity/overflow and capacity tests reject atomically; empty blocks do not finish the stream.
- [ ] DEV-CH-02: Implement exact unity transport and zero-effect bypass.<br>
  Requirements: [REQ-CH-02](../requirements.md#req-ch-02). Architecture: [design/owner](../architecture.md#ch-02-unity-transport).<br>
  Depends on: DEV-CH-01.<br>
  Acceptance: Signed zero/subnormal/sample bits and all metadata survive arbitrary chunking; no random draws or add-zero/multiply-one recomputation.
- [ ] DEV-CH-06: Implement channel output validity and passive bounded observation routing.<br>
  Requirements: [REQ-CH-06](../requirements.md#req-ch-06), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#ch-06-output-and-observations).<br>
  Depends on: DEV-CH-02.<br>
  Acceptance: Tail/guard/partial/index metadata remains correct; disabled/full observers do not change output or expose truth as RX corrections.
- [ ] WAVE-CH-01: Accept the complete bounded unity channel boundary.<br>
  Requirements: [REQ-CH-01](../requirements.md#req-ch-01), [REQ-CH-02](../requirements.md#req-ch-02), [REQ-CH-06](../requirements.md#req-ch-06). Architecture: [design/owner](../architecture.md#channel-simulator-unity-stub-first).<br>
  Depends on: DEV-CH-06.<br>
  Acceptance: Every initial channel task passes independently and integrated TX samples/metadata are delivered bit-identically to the RX boundary.

## 5. CMTS-US-RX implementation and acceptance

Configured timing and frame-based pilot estimates are the initial policies. Each RX stage uses legitimate configuration and separately owned state.

- [ ] DEV-RX-01: Implement RX-01: Burst framing and indexed available/missing sample intervals.<br>
  Requirements: [REQ-RX-01](../requirements.md#req-rx-01), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#rx-01-burst-framing-and-timing).<br>
  Depends on: WAVE-CH-01.<br>
  Acceptance: Literal origin/stride/gap/identity/overflow tests retain declared coverage and reject unexplained gaps without hidden acquisition.
- [ ] DEV-RX-02: Implement RX-02: Exact useful-window extraction and unavailable-symbol outcomes.<br>
  Requirements: [REQ-RX-02](../requirements.md#req-rx-02), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#rx-02-useful-symbol-extraction).<br>
  Depends on: DEV-RX-01.<br>
  Acceptance: Numbered windows distinguish available zeros from missing samples; incomplete windows are never silently zero-filled.
- [ ] DEV-RX-03: Implement RX-03: Centered unitary FFT and raw physical-bin results.<br>
  Requirements: [REQ-RX-03](../requirements.md#req-rx-03), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#rx-03-fft).<br>
  Depends on: DEV-RX-02.<br>
  Acceptance: Independent signed tones/direct sums/impulses establish sign/order/scaling and preserve raw validity.
- [ ] DEV-RX-04: Implement RX-04: Received-pilot C×H estimation and declared zero-forcing correction.<br>
  Requirements: [REQ-RX-04](../requirements.md#req-rx-04), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#rx-04-channel-estimation-and-equalization).<br>
  Depends on: DEV-RX-03.<br>
  Acceptance: Independent complex-anchor/interpolation/notch tests cover FrameFlatLs/FramePilotLinear, known pilot gain and explicit unavailable estimates; no injected H or fast tracking.
- [ ] DEV-RX-05: Implement RX-05: Resource extraction and inverse joint ordering.<br>
  Requirements: [REQ-RX-05](../requirements.md#req-rx-05), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#rx-05-resource-extraction-and-inverse-interleaving).<br>
  Depends on: DEV-RX-04.<br>
  Acceptance: Independent mixed-loading/permutation/boost cases preserve unavailable scheduled cells and exact bit positions without compaction.
- [ ] DEV-RX-06: Implement RX-06: Finite MSB-first MaxLog LLRs and erasures.<br>
  Requirements: [REQ-RX-06](../requirements.md#req-rx-06), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#rx-06-soft-qam-demapping).<br>
  Depends on: DEV-RX-05.<br>
  Acceptance: Independent labels/distances validate P(0)/P(1) signs, positive ReferenceVariance, clipping/ties and zero-confidence erasures.
- [ ] DEV-RX-07: Implement RX-07: Independent grant-mask soft derandomization and pad separation.<br>
  Requirements: [REQ-RX-07](../requirements.md#req-rx-07), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#rx-07-phy-soft-derandomization).<br>
  Depends on: DEV-RX-06.<br>
  Acceptance: Mask-one signs reverse without magnitude changes; erasure/pad clocks, omitted positions, word order and resets match independent vectors.
- [ ] DEV-RX-08: Implement RX-08: Codec integration with exactly-once shortening restoration.<br>
  Requirements: [REQ-RX-08](../requirements.md#req-rx-08), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#rx-08-shortening-restoration-and-ldpc-decoding).<br>
  Depends on: DEV-RX-07, LDPC-02.<br>
  Acceptance: Retained-length inputs, 1..100 iteration limits, failed decisions and separate convergence/parity/known-zero outcomes pass; cancellation respects indivisible codec calls.
- [ ] DEV-RX-09: Implement RX-09: Information deframing with actual failed/partial payload coverage.<br>
  Requirements: [REQ-RX-09](../requirements.md#req-rx-09), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#rx-09-information-deframing).<br>
  Depends on: DEV-RX-08.<br>
  Acceptance: Independent byte/fill/short-word cases preserve decision positions and continuity; source association/comparison stays outside RX.
- [ ] WAVE-RX-01: Accept the full configured-timing received-only receiver.<br>
  Requirements: [REQ-RX-01](../requirements.md#req-rx-01), [REQ-RX-02](../requirements.md#req-rx-02), [REQ-RX-03](../requirements.md#req-rx-03), [REQ-RX-04](../requirements.md#req-rx-04), [REQ-RX-05](../requirements.md#req-rx-05), [REQ-RX-06](../requirements.md#req-rx-06), [REQ-RX-07](../requirements.md#req-rx-07), [REQ-RX-08](../requirements.md#req-rx-08), [REQ-RX-09](../requirements.md#req-rx-09), [REQ-SYS-02](../requirements.md#req-sys-02). Architecture: [design/owner](../architecture.md#cmts-us-rx-block-architecture).<br>
  Depends on: DEV-RX-09.<br>
  Acceptance: All nine stage cases and integrated noiseless recovery pass without source/channel truth in normal receiver inputs.

## 6. Closed loop, controls, instruments and results

Passive taps accompany stage work. These aggregate tasks prove lifecycle and complete experiment behavior before measurement extensions or full language adapters.

- [ ] DEV-RUN-01: Implement frozen run settings, identities, cumulative budgets and cancellation with retained completed science.<br>
  Requirements: [REQ-LIFE-01](../requirements.md#req-life-01), [REQ-LIFE-02](../requirements.md#req-life-02), [REQ-LIFE-03](../requirements.md#req-life-03), [REQ-NFR-01](../requirements.md#req-nfr-01). Architecture: [design/owner](../architecture.md#ownership-results-and-acceptance).<br>
  Depends on: WAVE-RX-01.<br>
  Acceptance: Resolve job-wide limits/safe boundaries before execution; test bounded cancellation, pending tails/ranges and reproducibility. Pause/resume stays unavailable until state/time/stop semantics pass actual tests.
- [ ] INSTRUMENTS-01: Implement shared bounded QAM/SA collectors and queryable matched taps.<br>
  Requirements: [REQ-OBS-01](../requirements.md#req-obs-01), [REQ-CH-06](../requirements.md#req-ch-06). Architecture: [design/owner](../architecture.md#shared-qam-analyzer-and-spectrum-analyzer).<br>
  Depends on: WAVE-RX-01.<br>
  Acceptance: Tests identify tap/units/grid/run/retention, preserve unavailable history and prove disabled/full/query observers leave samples/RNG/decoder behavior unchanged.
- [ ] DEV-RESULTS-01: Implement owned experiment reports and independent source/decoder/metric accounting.<br>
  Requirements: [REQ-OBS-02](../requirements.md#req-obs-02), [REQ-PRBS-03](../requirements.md#req-prbs-03), [REQ-PRBS-04](../requirements.md#req-prbs-04), [REQ-API-06](../requirements.md#req-api-06). Architecture: [design/owner](../architecture.md#ownership-results-and-acceptance).<br>
  Depends on: DEV-RUN-01, INSTRUMENTS-01.<br>
  Acceptance: Reports retain failed/partial science, true iterations, generated/compared/unverified coverage, provenance and explicit unavailable/unbounded metric states; configuration and report schemas remain distinct.
- [ ] DEV-LOOP-01: Accept the complete source-to-recovered-bits reference unity experiment.<br>
  Requirements: [REQ-SYS-01](../requirements.md#req-sys-01), [REQ-SYS-02](../requirements.md#req-sys-02), [REQ-SYS-04](../requirements.md#req-sys-04), [REQ-LIFE-01](../requirements.md#req-life-01), [REQ-LIFE-02](../requirements.md#req-life-02). Architecture: [design/owner](../architecture.md#ownership-results-and-acceptance).<br>
  Depends on: DEV-RESULTS-01.<br>
  Acceptance: Completed/drained runs have exact meaningful-bit counts, full contiguous coverage and zero mismatches; destructive/truncated/cancelled/no-payload cases cannot claim recovery from zero errors alone.

## 7. Complete configuration JSON and PNM admission

These extensions do not become prerequisites for a typed synthetic reference experiment. Source-format work can be researched earlier; integration requires its explicit dependencies.

- [ ] USJSON-COVERAGE-01: Complete the applicable pinned MULPI/PHY field-level coverage audit.<br>
  Requirements: [REQ-CFG-04](../requirements.md#req-cfg-04), [REQ-SYS-05](../requirements.md#req-sys-05). Architecture: [design/owner](../architecture.md#cmts-configuration-us-configuration-json).<br>
  Depends on: none.<br>
  Acceptance: Every applicable/conditional/reserved/inapplicable row has source/endpoint/encoding/JSON/Rust/fixture mapping; the current area inventory is not completion.
- [ ] USJSON-FORMAT/PRESETS-01: Finalize the versioned generic schema, examples and guide.<br>
  Requirements: [REQ-CFG-03](../requirements.md#req-cfg-03), [REQ-CFG-06](../requirements.md#req-cfg-06), [REQ-API-06](../requirements.md#req-api-06). Architecture: [design/owner](../architecture.md#cmts-configuration-us-configuration-json).<br>
  Depends on: USJSON-COVERAGE-01.<br>
  Acceptance: Examples cover 25/50 kHz, mixed/zero loading and honestly unsupported optional modes; versions/defaults/nulls/unknown fields are independently exercised.
- [ ] USJSON-CORE/PROJECTION/PARITY-01: Implement bounded configuration JSON admission and accepted CMTS/TX/RX views.<br>
  Requirements: [REQ-CFG-01](../requirements.md#req-cfg-01), [REQ-CFG-02](../requirements.md#req-cfg-02), [REQ-CFG-03](../requirements.md#req-cfg-03), [REQ-CFG-05](../requirements.md#req-cfg-05), [REQ-API-06](../requirements.md#req-api-06). Architecture: [design/owner](../architecture.md#cmts-configuration-us-configuration-json).<br>
  Depends on: USJSON-FORMAT/PRESETS-01, US-CONFIG-01.<br>
  Acceptance: Round trips, all-field conditional validation, inventory, atomic replacement and source-preserving projections pass in shared Rust; native Python parity closes under API-PARITY/DOCS-01.
- [ ] US-CONFIG-FORMAT-01: Verify any claimed upstream configuration/profile capture format before adding its importer.<br>
  Requirements: [REQ-PNM-01](../requirements.md#req-pnm-01), [REQ-CFG-05](../requirements.md#req-cfg-05). Architecture: [design/owner](../architecture.md#us-configuration).<br>
  Depends on: none.<br>
  Acceptance: Pinned format evidence and lawful valid/invalid/boundary fixtures identify actual upstream semantics; synthetic JSON is not evidence of a PNM binary decoder.
- [ ] RXMER-FORMAT-01: Verify upstream RxMER format/reference/units/nulls.<br>
  Requirements: [REQ-PNM-01](../requirements.md#req-pnm-01). Architecture: [design/owner](../architecture.md#rxmer-input).<br>
  Depends on: none.<br>
  Acceptance: Pinned upstream format/type/units evidence and lawful independent fixtures precede binary/decoded capture support.
- [ ] PREEQ-FORMAT-01: Verify upstream corrective bank/update formats and base/probe semantics.<br>
  Requirements: [REQ-PNM-01](../requirements.md#req-pnm-01), [REQ-PNM-03](../requirements.md#req-pnm-03). Architecture: [design/owner](../architecture.md#us-pre-eq-input).<br>
  Depends on: none.<br>
  Acceptance: Pinned format/scale/control evidence and lawful fixtures establish bank/update identity, reset and adjustment interpretation.
- [ ] RXMER-INPUT-01: Implement original-preserving typed RxMER admission, association and single/multiple power playback.<br>
  Requirements: [REQ-PNM-01](../requirements.md#req-pnm-01), [REQ-PNM-02](../requirements.md#req-pnm-02). Architecture: [design/owner](../architecture.md#rxmer-input).<br>
  Depends on: DEV-LOOP-01, RXMER-FORMAT-01.<br>
  Acceptance: Independent power/weight/null/time-boundary cases preserve original bytes/hash/grid/time and explicit synthetic schedule; additional captures never silently multiply trials.
- [ ] PREEQ-INPUT-01: Implement fixed banks, multiple snapshots and explicitly based bounded updates.<br>
  Requirements: [REQ-PNM-01](../requirements.md#req-pnm-01), [REQ-PNM-03](../requirements.md#req-pnm-03), [REQ-TX-06](../requirements.md#req-tx-06). Architecture: [design/owner](../architecture.md#us-pre-eq-input).<br>
  Depends on: DEV-LOOP-01, PREEQ-FORMAT-01.<br>
  Acceptance: Independent complex/base/reset/symbol-boundary cases validate immutable schedules; stale/missing/ambiguous probes or banks reject without changing accepted state.

## 8. Supported channel impairment extensions

Keep unsupported composition rejected. Captured-H reconstruction, fractional timing and broad time-varying composition remain deferred.

- [ ] DEV-CH-03: Implement bounded causal synthetic FIR response and exact terminal drain.<br>
  Requirements: [REQ-CH-03](../requirements.md#req-ch-03). Architecture: [design/owner](../architecture.md#ch-03-channel-response).<br>
  Depends on: DEV-LOOP-01.<br>
  Acceptance: Independent literal convolution/impulse/gain/delay/phase/deep-null cases establish T+L-1 length, original origin, history continuity and resumable drain.
- [ ] DEV-CH-04: Implement declared sample AWGN and restricted RxMER residual synthesis.<br>
  Requirements: [REQ-CH-04](../requirements.md#req-ch-04). Architecture: [design/owner](../architecture.md#ch-04-residual-error).<br>
  Depends on: DEV-LOOP-01, RXMER-INPUT-01.<br>
  Acceptance: Independent reference/pilot power and pinned noise draw-order/statistical cases pass; every unsupported C/H/timing combination rejects before consuming input.
- [ ] DEV-CH-05: Implement integer delay, phase/CFO and emitted-clock continuity.<br>
  Requirements: [REQ-CH-05](../requirements.md#req-ch-05). Architecture: [design/owner](../architecture.md#ch-05-timing-and-phase).<br>
  Depends on: DEV-LOOP-01.<br>
  Acceptance: Independent tone/impulse/rotation cases establish signs/origin, T+D drain and phase/chunk/pause continuity; zero settings select bitwise bypass.
- [ ] DEV-COMPOSE-01: Validate the entire joint RxMER/channel/Pre-EQ update schedule before execution.<br>
  Requirements: [REQ-PNM-04](../requirements.md#req-pnm-04), [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design/owner](../architecture.md#channel-simulator-unity-stub-first).<br>
  Depends on: DEV-CH-03, DEV-CH-04, DEV-CH-05, PREEQ-INPUT-01.<br>
  Acceptance: Later incompatible bank events reject the candidate; C, H, targets and noise truth remain separate; explicit stage order/drain/coverage cases pass.
- [ ] WAVE-CH-02: Accept the supported impairment/measurement-driven experiment scope.<br>
  Requirements: [REQ-CH-03](../requirements.md#req-ch-03), [REQ-CH-04](../requirements.md#req-ch-04), [REQ-CH-05](../requirements.md#req-ch-05), [REQ-PNM-04](../requirements.md#req-pnm-04). Architecture: [design/owner](../architecture.md#channel-simulator-unity-stub-first).<br>
  Depends on: DEV-COMPOSE-01.<br>
  Acceptance: All extension-specific and joint-model checks pass with preserved originals/partial outcomes; unsupported combinations remain explicitly unavailable.

## 9. High-level Rust and native Python delivery

Shared Rust API foundation can be developed after typed core admission, but full waveform execution depends on the accepted experiment. Python consumes working Rust operations.

- [ ] API-RUST/INPUT-01: Implement the typed idle Rust session/configuration/input/inventory/preview surface.<br>
  Requirements: [REQ-API-01](../requirements.md#req-api-01), [REQ-API-03](../requirements.md#req-api-03), [REQ-SYS-03](../requirements.md#req-sys-03). Architecture: [design/owner](../architecture.md#paired-rust-and-python-interface-stubs).<br>
  Depends on: US-CONFIG-01.<br>
  Acceptance: Direct Rust valid/invalid/atomic-state/lifetime tests pass while existing FEC calls and schema-1 reports stay compatible; no unverified importer is advertised.
- [ ] API-RUN-01: Expose accepted bounded execution, owned reports, progress/cancellation and QAM/SA access.<br>
  Requirements: [REQ-API-01](../requirements.md#req-api-01), [REQ-API-03](../requirements.md#req-api-03), [REQ-LIFE-01](../requirements.md#req-life-01), [REQ-LIFE-02](../requirements.md#req-life-02), [REQ-LIFE-03](../requirements.md#req-life-03). Architecture: [design/owner](../architecture.md#api-lifecycle-errors-and-result-contracts).<br>
  Depends on: API-RUST/INPUT-01, DEV-LOOP-01.<br>
  Acceptance: Frozen snapshots, limits, Busy, cancellation/partial results and report query/lifetimes pass; pause remains unavailable until its full control contract passes.
- [ ] API-PY/STUB-01: Implement native Python conversion/dispatch and runtime-matching type declarations.<br>
  Requirements: [REQ-API-02](../requirements.md#req-api-02), [REQ-API-03](../requirements.md#req-api-03), [REQ-API-04](../requirements.md#req-api-04), [REQ-API-05](../requirements.md#req-api-05). Architecture: [design/owner](../architecture.md#api-modules-and-planned-stub-paths).<br>
  Depends on: API-RUN-01.<br>
  Acceptance: Actual native import checks structured errors/None/integer-buffer conversion, interpreter release, Busy/session restoration and matching .pyi/py.typed exports; core builds remain independent.
- [ ] API-PARITY/DOCS-01: Validate independent Rust/native-Python parity and deliver runnable paired examples/guides.<br>
  Requirements: [REQ-API-03](../requirements.md#req-api-03), [REQ-API-04](../requirements.md#req-api-04), [REQ-API-05](../requirements.md#req-api-05), [REQ-API-06](../requirements.md#req-api-06). Architecture: [design/owner](../architecture.md#api-delivery-and-validation-gates).<br>
  Depends on: API-PY/STUB-01.<br>
  Acceptance: Actual deterministic runs compare settings/seeds/provenance/status/FEC/partial coverage within declared numerical tolerances; cancellation/concurrency/lifetime and supported schema cases pass, not mocks.
- [ ] API-01: Close all supported high-level Rust and Python API delivery gates.<br>
  Requirements: [REQ-API-01](../requirements.md#req-api-01), [REQ-API-02](../requirements.md#req-api-02), [REQ-API-03](../requirements.md#req-api-03), [REQ-API-04](../requirements.md#req-api-04), [REQ-API-05](../requirements.md#req-api-05), [REQ-API-06](../requirements.md#req-api-06). Architecture: [design/owner](../architecture.md#high-level-rust-and-python-apis).<br>
  Depends on: API-PARITY/DOCS-01.<br>
  Acceptance: Required API feature gates and documented supported configurations pass; delivered input modes include their shared Rust/Python semantics. Deferred modes are explicitly scoped, not silently dropped.

## 10. Foundation delivery and deferred design gates

These items remain pending. GUI and broader PHY modes need a dedicated design/authorization gate; listed design work is not an implementation claim.

- [ ] DEV-LICENSE-01: Complete copied-material/dependency attribution and package-scope review.<br>
  Requirements: [REQ-NFR-02](../requirements.md#req-nfr-02). Architecture: [design/owner](../architecture.md#ownership-results-and-acceptance).<br>
  Depends on: none.<br>
  Acceptance: Retain actual notices/licenses/modifications; no private evidence/captures/generated outputs or GPL presentation code enter the independent Apache scientific distribution.
- [ ] SETUP-04: Validate actual fresh-machine setup on each declared target.<br>
  Requirements: [REQ-NFR-03](../requirements.md#req-nfr-03). Architecture: [design/owner](../architecture.md#checkpoint-and-target-overview).<br>
  Depends on: none.<br>
  Acceptance: Real provisioning/lifecycle evidence is recorded separately from existing mocked/read-only checks; no automatic system install is authorized by this checklist.
- [ ] DEV-UI-PLAN-01: Define the presentation implementation plan and readiness/editor acceptance before GUI work.<br>
  Requirements: [REQ-OBS-03](../requirements.md#req-obs-03), [REQ-OBS-04](../requirements.md#req-obs-04). Architecture: [design/owner](../architecture.md#planned-upstream-signal-path-and-workbenches).<br>
  Depends on: DEV-LOOP-01, INSTRUMENTS-01.<br>
  Acceptance: Dedicated plan maps block/stage routes, actual tap selection, draft/apply/cancel, text readiness and truthful complete/partial results to concrete UI owners/tests; GUI implementation remains pending that plan and authorization.
- [ ] RX-EXT-01: Design wider received-signal acquisition, tracking, calibrated confidence and finite-file framing.<br>
  Requirements: [REQ-RX-01](../requirements.md#req-rx-01), [REQ-RX-04](../requirements.md#req-rx-04), [REQ-RX-06](../requirements.md#req-rx-06), [REQ-SYS-04](../requirements.md#req-sys-04). Architecture: [design/owner](../architecture.md#cmts-us-rx-block-architecture).<br>
  Depends on: DEV-LOOP-01.<br>
  Acceptance: Define source applicability, algorithms, bounds and independent acceptance before claiming any extension; configured-timing/frame-policy support stays explicitly bounded.
- [ ] CH-EXT-02: Design captured-H reconstruction, fractional clock/phase noise and broader RxMER/C/H composition.<br>
  Requirements: [REQ-CH-03](../requirements.md#req-ch-03), [REQ-CH-04](../requirements.md#req-ch-04), [REQ-CH-05](../requirements.md#req-ch-05), [REQ-PNM-04](../requirements.md#req-pnm-04). Architecture: [design/owner](../architecture.md#channel-simulator-unity-stub-first).<br>
  Depends on: WAVE-CH-02.<br>
  Acceptance: Resolve evidence/model/reference/combination decisions and independent test oracles before execution support; unknown bins and inverse-C truth are not invented.
- [ ] ARCH-RANGING-01: Design initial/fine-ranging preambles, probing and received-signal acquisition.<br>
  Requirements: [REQ-SYS-04](../requirements.md#req-sys-04), [REQ-CFG-04](../requirements.md#req-cfg-04). Architecture: [design/owner](../architecture.md#deferred-burst-modes-and-preambles).<br>
  Depends on: DEV-LOOP-01.<br>
  Acceptance: Pinned PHY/MULPI applicability, distinct waveforms/controls and bounded RX acceptance are defined; modes remain unsupported until separately implemented and validated.
- [ ] FOUNDATION-03: Complete independent workspace delivery, required CI/tooling/user guides and reviewed distribution scope.<br>
  Requirements: [REQ-SYS-03](../requirements.md#req-sys-03), [REQ-NFR-02](../requirements.md#req-nfr-02), [REQ-NFR-03](../requirements.md#req-nfr-03), [REQ-NFR-04](../requirements.md#req-nfr-04). Architecture: [design/owner](../architecture.md#checkpoint-and-target-overview).<br>
  Depends on: DEV-LICENSE-01.<br>
  Acceptance: Declared foundation gates have actual evidence; existing local workspace/tooling is partial completion, not hosted/native/publication proof. Setup provisioning remains SETUP-04.
- [ ] DEV-HANDOFF-01: Reconcile requirements, architecture, checklist, user guides and actual evidence for the accepted delivery scope.<br>
  Requirements: [REQ-NFR-04](../requirements.md#req-nfr-04), [REQ-SYS-05](../requirements.md#req-sys-05). Architecture: [design/owner](../architecture.md#api-delivery-and-validation-gates).<br>
  Depends on: DEV-LOOP-01, API-01, FOUNDATION-03.<br>
  Acceptance: Record actual commands/outcomes/limits, keep unsupported/platform/source gaps visible, and never treat this checklist as authorization to commit/push/install. Measurement/UI extensions close only with their own gates.

## Requirement coverage

Every baseline requirement maps to active delivery work below. Coverage is not
completion; deferred UI/wider-mode work remains subject to its explicit gates.

| Requirement | Delivery task IDs |
| --- | --- |
| [REQ-SYS-01](../requirements.md#req-sys-01) | DEV-LOOP-01 |
| [REQ-SYS-02](../requirements.md#req-sys-02) | PHY-01, DEV-CH-06, DEV-RX-01, DEV-RX-02, DEV-RX-03, DEV-RX-04, DEV-RX-05, DEV-RX-06, DEV-RX-07, DEV-RX-08, DEV-RX-09, WAVE-RX-01, DEV-LOOP-01 |
| [REQ-SYS-03](../requirements.md#req-sys-03) | DEV-CORE-01, API-RUST/INPUT-01, FOUNDATION-03 |
| [REQ-SYS-04](../requirements.md#req-sys-04) | US-CONFIG-01, DEV-LOOP-01, RX-EXT-01, ARCH-RANGING-01 |
| [REQ-SYS-05](../requirements.md#req-sys-05) | LDPC-01, LDPC-02, USJSON-COVERAGE-01, DEV-HANDOFF-01 |
| [REQ-CFG-01](../requirements.md#req-cfg-01) | US-CONFIG-01, USJSON-CORE/PROJECTION/PARITY-01 |
| [REQ-CFG-02](../requirements.md#req-cfg-02) | US-CONFIG-01, USJSON-CORE/PROJECTION/PARITY-01 |
| [REQ-CFG-03](../requirements.md#req-cfg-03) | USJSON-FORMAT/PRESETS-01, USJSON-CORE/PROJECTION/PARITY-01 |
| [REQ-CFG-04](../requirements.md#req-cfg-04) | USJSON-COVERAGE-01, ARCH-RANGING-01 |
| [REQ-CFG-05](../requirements.md#req-cfg-05) | US-CONFIG-01, PHY-01, USJSON-CORE/PROJECTION/PARITY-01, US-CONFIG-FORMAT-01 |
| [REQ-CFG-06](../requirements.md#req-cfg-06) | USJSON-FORMAT/PRESETS-01 |
| [REQ-PRBS-01](../requirements.md#req-prbs-01) | SOURCE-01 |
| [REQ-PRBS-02](../requirements.md#req-prbs-02) | SOURCE-01 |
| [REQ-PRBS-03](../requirements.md#req-prbs-03) | SOURCE-01, DEV-RESULTS-01 |
| [REQ-PRBS-04](../requirements.md#req-prbs-04) | SOURCE-01, DEV-RESULTS-01 |
| [REQ-TX-01](../requirements.md#req-tx-01) | PHY-01, WAVE-TX-01 |
| [REQ-TX-02](../requirements.md#req-tx-02) | LDPC-01, LDPC-02, DEV-TX-02, WAVE-TX-01 |
| [REQ-TX-03](../requirements.md#req-tx-03) | DEV-TX-03, WAVE-TX-01 |
| [REQ-TX-04](../requirements.md#req-tx-04) | DEV-TX-04, WAVE-TX-01 |
| [REQ-TX-05](../requirements.md#req-tx-05) | DEV-TX-05, WAVE-TX-01 |
| [REQ-TX-06](../requirements.md#req-tx-06) | DEV-TX-06, WAVE-TX-01, PREEQ-INPUT-01 |
| [REQ-TX-07](../requirements.md#req-tx-07) | DEV-TX-07, WAVE-TX-01 |
| [REQ-TX-08](../requirements.md#req-tx-08) | DEV-TX-08, WAVE-TX-01 |
| [REQ-CH-01](../requirements.md#req-ch-01) | DEV-CH-01, WAVE-CH-01, DEV-COMPOSE-01 |
| [REQ-CH-02](../requirements.md#req-ch-02) | DEV-CH-02, WAVE-CH-01 |
| [REQ-CH-03](../requirements.md#req-ch-03) | DEV-CH-03, WAVE-CH-02, CH-EXT-02 |
| [REQ-CH-04](../requirements.md#req-ch-04) | DEV-CH-04, WAVE-CH-02, CH-EXT-02 |
| [REQ-CH-05](../requirements.md#req-ch-05) | DEV-CH-05, WAVE-CH-02, CH-EXT-02 |
| [REQ-CH-06](../requirements.md#req-ch-06) | DEV-CH-06, WAVE-CH-01, INSTRUMENTS-01 |
| [REQ-RX-01](../requirements.md#req-rx-01) | DEV-RX-01, WAVE-RX-01, RX-EXT-01 |
| [REQ-RX-02](../requirements.md#req-rx-02) | DEV-RX-02, WAVE-RX-01 |
| [REQ-RX-03](../requirements.md#req-rx-03) | DEV-RX-03, WAVE-RX-01 |
| [REQ-RX-04](../requirements.md#req-rx-04) | DEV-RX-04, WAVE-RX-01, RX-EXT-01 |
| [REQ-RX-05](../requirements.md#req-rx-05) | DEV-RX-05, WAVE-RX-01 |
| [REQ-RX-06](../requirements.md#req-rx-06) | DEV-RX-06, WAVE-RX-01, RX-EXT-01 |
| [REQ-RX-07](../requirements.md#req-rx-07) | DEV-RX-07, WAVE-RX-01 |
| [REQ-RX-08](../requirements.md#req-rx-08) | LDPC-01, LDPC-02, DEV-RX-08, WAVE-RX-01 |
| [REQ-RX-09](../requirements.md#req-rx-09) | DEV-RX-09, WAVE-RX-01 |
| [REQ-PNM-01](../requirements.md#req-pnm-01) | US-CONFIG-FORMAT-01, RXMER-FORMAT-01, PREEQ-FORMAT-01, RXMER-INPUT-01, PREEQ-INPUT-01 |
| [REQ-PNM-02](../requirements.md#req-pnm-02) | RXMER-INPUT-01 |
| [REQ-PNM-03](../requirements.md#req-pnm-03) | PREEQ-FORMAT-01, PREEQ-INPUT-01 |
| [REQ-PNM-04](../requirements.md#req-pnm-04) | DEV-COMPOSE-01, WAVE-CH-02, CH-EXT-02 |
| [REQ-OBS-01](../requirements.md#req-obs-01) | INSTRUMENTS-01 |
| [REQ-OBS-02](../requirements.md#req-obs-02) | DEV-RESULTS-01 |
| [REQ-OBS-03](../requirements.md#req-obs-03) | DEV-UI-PLAN-01 |
| [REQ-OBS-04](../requirements.md#req-obs-04) | DEV-UI-PLAN-01 |
| [REQ-API-01](../requirements.md#req-api-01) | API-RUST/INPUT-01, API-RUN-01, API-01 |
| [REQ-API-02](../requirements.md#req-api-02) | API-PY/STUB-01, API-01 |
| [REQ-API-03](../requirements.md#req-api-03) | API-RUST/INPUT-01, API-RUN-01, API-PY/STUB-01, API-PARITY/DOCS-01, API-01 |
| [REQ-API-04](../requirements.md#req-api-04) | API-PY/STUB-01, API-PARITY/DOCS-01, API-01 |
| [REQ-API-05](../requirements.md#req-api-05) | API-PY/STUB-01, API-PARITY/DOCS-01, API-01 |
| [REQ-API-06](../requirements.md#req-api-06) | DEV-RESULTS-01, USJSON-FORMAT/PRESETS-01, USJSON-CORE/PROJECTION/PARITY-01, API-PARITY/DOCS-01, API-01 |
| [REQ-LIFE-01](../requirements.md#req-life-01) | DEV-CORE-01, DEV-RUN-01, DEV-LOOP-01, API-RUN-01 |
| [REQ-LIFE-02](../requirements.md#req-life-02) | DEV-RUN-01, DEV-LOOP-01, API-RUN-01 |
| [REQ-LIFE-03](../requirements.md#req-life-03) | DEV-RUN-01, API-RUN-01 |
| [REQ-NFR-01](../requirements.md#req-nfr-01) | DEV-CORE-01, DEV-RUN-01 |
| [REQ-NFR-02](../requirements.md#req-nfr-02) | DEV-LICENSE-01, FOUNDATION-03 |
| [REQ-NFR-03](../requirements.md#req-nfr-03) | SETUP-04, FOUNDATION-03 |
| [REQ-NFR-04](../requirements.md#req-nfr-04) | FOUNDATION-03, DEV-HANDOFF-01 |

## Completed design and tooling records

Prior IDs, text and checked states are preserved here. These records establish
design/setup work only; supporting requirement links do not claim functional
acceptance. Prior feature records contain their original evidence and limits.

- [x] REQ-BASELINE-01: Consolidate the current architecture into a project-wide
  [requirements baseline](../requirements.md) with stable behavior/acceptance IDs,
  scope, owner/delivery traceability and explicit evidence gaps; documentation only.<br>
  Supports: [REQ-SYS-05](../requirements.md#req-sys-05). Architecture: [design record](../architecture.md#checkpoint-and-target-overview).
- [x] FOUNDATION-01: Inspect PDE and record selective adoption decisions.<br>
  Supports: [REQ-SYS-05](../requirements.md#req-sys-05). Architecture: [design record](../architecture.md#checkpoint-and-target-overview).
- [x] FOUNDATION-02: Inspect MERLIN and document reusable/upstream-specific owners.<br>
  Supports: [REQ-SYS-05](../requirements.md#req-sys-05). Architecture: [design record](../architecture.md#checkpoint-and-target-overview).
- [x] ARCH-01: Define PRBS → CM-US-TX → unity Channel Simulator → CMTS-US-RX,
  ordered processing stages and shared QAM/SA observation contracts. This is
  documentation only; see [design](features/upstream-signal-path/design.md).<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-PRBS-01: Define the self-contained PRBS-TX/PRBS-RX block, sequence,
  interfaces, lifecycle, readiness and independent comparison contracts;
  see [PRBS design](features/prbs-source/design.md). Implementation stays planned.<br>
  Supports: [REQ-PRBS-01](../requirements.md#req-prbs-01). Architecture: [design record](../architecture.md#prbs-block-architecture).
- [x] ARCH-TX-00: Define the CM-US-TX block, eight internal stages and typed
  observation boundaries; see [transmitter design](features/cm-us-tx/design.md).<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-TX-NAV: Link all TX overview/output labels to local stage sections,
  retain pending placeholder status and adopt the generic rule in local/PDE
  development-workflow skills and architecture templates.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-PATH-01: Backfill each signal-path block/stage with planned code/test
  filenames, explicit create/reuse/extend status and shared ownership; adopt the
  rule in local/PDE skills and templates. See [layout design](features/code-layout/design.md).<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-TX-01: Expand grant framing/FEC selection, source/fill/shortening/pad
  accounting, bounded admission and stage acceptance. Documentation only.<br>
  Supports: [REQ-TX-01](../requirements.md#req-tx-01). Architecture: [design record](../architecture.md#tx-01-grant-framing-and-fec-selection).
- [x] ARCH-TX-02: Define LDPC encoding/shortening, exact transmitted bit order,
  grant assembly, codec ownership, inspection and source-validation boundaries;
  see [TX-02](../architecture.md#tx-02-ldpc-encoding-and-shortening). Architecture only.<br>
  Supports: [REQ-TX-02](../requirements.md#req-tx-02). Architecture: [design record](../architecture.md#tx-02-ldpc-encoding-and-shortening).
- [x] ARCH-TX-03: Define the 23-bit grant randomizer, register/first-bit convention,
  bit coverage, state validation and independent RX soft inverse;
  see [TX-03](../architecture.md#tx-03-grant-seeded-phy-randomization). Architecture only.<br>
  Supports: [REQ-TX-03](../requirements.md#req-tx-03). Architecture: [design record](../architecture.md#tx-03-grant-seeded-phy-randomization).
- [x] ARCH-TX-04: Define MSB-first cell words, exact upstream constellation/role
  loading, reference scaling, bounded mapping, QAM inspection and code/test paths;
  see [TX-04](../architecture.md#tx-04-cell-word-construction-and-qam-mapping). Architecture only.<br>
  Supports: [REQ-TX-04](../requirements.md#req-tx-04). Architecture: [design record](../architecture.md#tx-04-cell-word-construction-and-qam-mapping).
- [x] ARCH-TX-05: Define shared pilot/resource roles, block partitioning, joint
  address generation, physical-bin pilots/boosting, bounded grid assembly and
  code/test paths; see [TX-05](../architecture.md#tx-05-pilots-ofdma-framing-and-interleaving).
  Architecture only; exact masks/vectors and executable acceptance remain planned.<br>
  Supports: [REQ-TX-05](../requirements.md#req-tx-05). Architecture: [design record](../architecture.md#tx-05-pilots-ofdma-framing-and-interleaving).
- [x] ARCH-TX-06: Define coefficient/reference planes, defaults/exclusions,
  normalization, update/reset boundaries, bounded application and code/test paths;
  see [TX-06](../architecture.md#tx-06-cm-pre-eq). Architecture only; no adaptive loop.<br>
  Supports: [REQ-TX-06](../requirements.md#req-tx-06). Architecture: [design record](../architecture.md#tx-06-cm-pre-eq).
- [x] ARCH-TX-07: Define upstream IFFT geometry, centered bin order/unitary scaling,
  useful-sample timing, shared transform ownership, bounds and code/test paths;
  see [TX-07](../architecture.md#tx-07-ifft). Architecture only; no waveform execution.<br>
  Supports: [REQ-TX-07](../requirements.md#req-tx-07). Architecture: [design record](../architecture.md#tx-07-ifft).
- [x] ARCH-TX-08: Define upstream CP/RP, extension/taper/overlap, prefix/useful
  origins, tail/guards, bounded chunk emission and planned code/test paths;
  see [TX-08](../architecture.md#tx-08-sample-assembly). Architecture only.<br>
  Supports: [REQ-TX-08](../requirements.md#req-tx-08). Architecture: [design record](../architecture.md#tx-08-sample-assembly).
- [x] ARCH-CH-00: Stage the Channel Simulator with six linked sections, support
  states and planned files; keep a compact block/configuration/PNM contents list.
  See [channel design](features/channel-simulator/design.md).<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-CH-01/02/06: Define sample admission, exact unity transport, output
  observations and bounded lifecycle. Architecture only; no channel execution.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-RXMER-01: Add the separate upstream RxMER input, original provenance,
  exact association, power selection/playback and model/metric boundaries;
  see [RxMER input](../architecture.md#rxmer-input). Implementation remains planned.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-US-CONFIG-01: Define US Configuration input, retained profile inventory,
  selection, shared TX/RX admission and code/test paths; architecture only.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-PNM-02: Define single-shot/multi-input RxMER and US-Pre-EQ,
  bounded bank/update replay, explicit bases/events and joint-model compatibility;
  see [input design](features/upstream-inputs/design.md). Implementation planned.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-USJSON-01: Record generic OFDMA JSON as the CMTS configuration
  subsection of CMTS-US-RX; define shared TX/RX projections, support states,
  version/coverage plan, planned paths and flows.
  See [JSON design](features/us-configuration-json/design.md). Architecture only.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-CH-03: Define causal complex FIR, original tap/path reference,
  bounded history/work, exact tail and independent acceptance; architecture only.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-CH-04: Define sample AWGN and restricted unity-C/H RxMER synthesis,
  reference/pilot power, seeded draw order and independent acceptance; architecture only.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-CH-05: Define integer delay and constant phase/CFO, emitted-clock
  state, length/drain rules and independent acceptance; architecture only.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-RX-00: Define CMTS-US-RX block inputs/results, nine-stage processing
  chart, lifecycle and inspection overview; see [receiver design](features/cmts-us-rx/design.md).<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-RX-NAV/PATH: Link all RX overview/output labels to stage sections,
  with backlinks, planned code/test paths and explicit existing codec reuse.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] ARCH-RX-01: Expand burst framing/timing and bounded indexed-sample admission.<br>
  Supports: [REQ-RX-01](../requirements.md#req-rx-01). Architecture: [design record](../architecture.md#rx-01-burst-framing-and-timing).
- [x] ARCH-RX-02: Expand useful-window selection, CP/overlap and validity.<br>
  Supports: [REQ-RX-02](../requirements.md#req-rx-02). Architecture: [design record](../architecture.md#rx-02-useful-symbol-extraction).
- [x] ARCH-RX-03: Expand forward transform admission, metadata and independent vectors.<br>
  Supports: [REQ-RX-03](../requirements.md#req-rx-03). Architecture: [design record](../architecture.md#rx-03-fft).
- [x] ARCH-RX-04: Expand pilot estimate/correction, coverage, reliability and nulls.<br>
  Supports: [REQ-RX-04](../requirements.md#req-rx-04). Architecture: [design record](../architecture.md#rx-04-channel-estimation-and-equalization).
- [x] ARCH-RX-05: Expand exact resource extraction and inverse joint visits.<br>
  Supports: [REQ-RX-05](../requirements.md#req-rx-05). Architecture: [design record](../architecture.md#rx-05-resource-extraction-and-inverse-interleaving).
- [x] ARCH-RX-06: Expand MSB-first LLR metrics, labels/scales and confidence policy.<br>
  Supports: [REQ-RX-06](../requirements.md#req-rx-06). Architecture: [design record](../architecture.md#rx-06-soft-qam-demapping).
- [x] ARCH-RX-07: Expand soft grant mask reversal, word ordering and pad separation.<br>
  Supports: [REQ-RX-07](../requirements.md#req-rx-07). Architecture: [design record](../architecture.md#rx-07-phy-soft-derandomization).
- [x] ARCH-RX-08: Expand shortening/codec integration and separate decode outcomes.<br>
  Supports: [REQ-RX-08](../requirements.md#req-rx-08). Architecture: [design record](../architecture.md#rx-08-shortening-restoration-and-ldpc-decoding).
- [x] ARCH-RX-09: Expand receiver-known deframing and partial information results.<br>
  Supports: [REQ-RX-09](../requirements.md#req-rx-09). Architecture: [design record](../architecture.md#rx-09-information-deframing).
- [x] ARCH-RANGING-00: Reserve explicit future ranging/preamble and probing modes;
  see [placeholder](../architecture.md#deferred-burst-modes-and-preambles).<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).
- [x] SETUP-01..03: Adopt generic installer guidance and implement/test explicit
  development setup. Nineteen setup tests and Ubuntu 22.04 read-only modes pass;
  see [design/checklist](features/development-setup/design.md).<br>
  Supports: [REQ-NFR-03](../requirements.md#req-nfr-03). Architecture: [design record](../architecture.md#checkpoint-and-target-overview).
- [x] ARCH-API-01: Review the reference high-level Rust/native Python structure;
  define a separate [API architecture](../architecture.md#high-level-rust-and-python-apis),
  paired design stubs, planned code/test/type-stub paths and local skill rules.<br>
  Supports: [REQ-CH-01](../requirements.md#req-ch-01). Architecture: [design record](../architecture.md#channel-simulator-unity-stub-first).

At every completion/commit-msg review, reconcile this checklist, requirements,
architecture, feature records and actual validation evidence. See the
[checklist traceability feature record](features/software-development-checklist/design.md).
