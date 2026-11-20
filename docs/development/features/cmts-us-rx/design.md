# CMTS-US-RX block and stage design

Status: receiver block and all nine stage contracts are defined for the declared
initial scope. Scientific implementation, independent source/algorithm acceptance
and future policies remain planned. Scope is architecture documentation only.

## Requirements

| ID | Requirement | Owner / acceptance |
| --- | --- | --- |
| RX-ARCH-01 | Use CMTS-US-RX and show the nine ordered receiver stages. | Canonical block architecture, one processing chart and matching local stage index. |
| RX-NAV-01 | Link every overview/output label to its corresponding section and back to the index. | Nine unique stage targets, 18 linked overview/output rows, index backlinks and the compact block contents. |
| RX-PATH-01 | Name implementation/shared numerical/test files per stage with create/reuse disposition. | Existing codec reuse is verified; proposed PHY files remain absent and algorithms have one owner. |
| RX-INPUT-01 | Recover from received samples and a receiver-specific accepted configuration. | No injected H/C, RxMER target, channel seed, original bits or PRBS truth in normal recovery. |
| RX-STATE-01 | Bound work/state and preserve completed outcomes on pause/cancel/failure. | Receiver composition; per-stage contexts, partial status, no silent gap filling or restart on inspection. |
| RX-DOMAIN-01 | Separate samples, physical/equalized cells, soft bits and decoded information. | Stage boundaries and passive SA/QAM/LLR/FEC inspection; source association/comparison outside RX. |
| RX-SCOPE-01 | Keep scheduled-data/configured-timing scope and stage design status explicit. | No blind acquisition, ranging/probe processing, downstream BCH/PLC/NCP or implementation claim. |
| RX-COVERAGE-01 | Preserve missing positions without changing symbol/cell/bit order. | Explicit gap/window/cell outcomes, zero LLR erasures with reasons, no source-based repair or dropped failures. |
| RX-POLICY-01 | Define actual receiver algorithms and confidence assumptions. | FrameFlatLs / FramePilotLinear, zero-forcing validity and finite ReferenceVariance MaxLog; no hidden measured-noise or fast-tracking capability. |
| RX-CODEC-01 | Reuse existing restoration/decoding and expose real work boundaries. | T-element codec inputs; no double restoration, distinct flags, 1..100 iterations and pause/cancel between codewords. |

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
| Planned `crates/phy/src/signal_processing/channel_estimation.rs`, `crates/phy/src/signal_processing/equalization.rs` | Frame-based pilot LS/interpolation and zero-forcing validity; algorithms and bounds defined in RX-04. |
| Planned `crates/phy/src/signal_processing/demapping.rs` | MSB-first MaxLog using shared labels/scales, explicit reference variance and finite saturation as defined in RX-06. |
| Existing `crates/ldpc/src/codec.rs` | Standalone codec reuse; keep LDPC-01/02 source/milestone gaps visible and no BCH dependency. |

The receiver order is a local engineering decomposition of the accepted upstream
path. Controlling upstream evidence remains CM-SP-PHYv3.1-I20-230419 §7.4.1,
§7.4.3–7, §7.4.9–11 and §7.4.16–17. Corresponding TX sections record their
source/figure reviews. The stage contracts add explicit engineering receiver
algorithms, not new source-table transcriptions or normative CMTS algorithms.
Independent source/mask/label vectors and executable acceptance remain pending.
The [publisher's pinned PHY I20](https://account.cablelabs.com/server/alfresco/4eb470eb-aca3-4e64-af88-773b8c594fbd)
was checked for revision/section identity. Real MAC message parsing needs separate
MULPI evidence; existing probe RxMER input does not implement a probe receiver.

## Stage contract completion

| Stage / canonical section | Defined contract / planned independent validation |
| --- | --- |
| [RX-01](../../../architecture.md#rx-01-burst-framing-and-timing) | Configured B/stride/observation interval, indexed blocks/gaps, bounded quantum and finish; literal indices, truncation and retry cases. |
| [RX-02](../../../architecture.md#rx-02-useful-symbol-extraction) | Exact N-sample windows, CP/guard gaps and missing-window outcomes; numbered samples and overlap-edge cases. |
| [RX-03](../../../architecture.md#rx-03-fft) | Centered unitary forward bins with raw availability; independent impulses, signed tones and energy. |
| [RX-04](../../../architecture.md#rx-04-channel-estimation-and-equalization) | Known pilot gain/sign, frame LS/linear estimates, zero-forcing floor and explicit unsupported fast tracking; literal complex/anchor/notch cases. |
| [RX-05](../../../architecture.md#rx-05-resource-extraction-and-inverse-interleaving) | Exact inverse visits, loading/roles, one boost removal and conserved unavailable positions; independent coordinate/bit sequences. |
| [RX-06](../../../architecture.md#rx-06-soft-qam-demapping) | MSB-first MaxLog, reference variance, saturation/erasures and candidate work; independent label subsets and BPSK metrics. |
| [RX-07](../../../architecture.md#rx-07-phy-soft-derandomization) | Grant mask sign reversal, erasure/pad clocks and ordered retained words; independent register/split cases. |
| [RX-08](../../../architecture.md#rx-08-shortening-restoration-and-ldpc-decoding) | Sole codec restoration, actual decisions/flags/iterations and word-boundary cancellation; independent mother layouts and failures. |
| [RX-09](../../../architecture.md#rx-09-information-deframing) | Receiver-known residual fill, logical byte/word coverage, failed decisions and external comparison; all residues and missing/failed words. |

The existing code review verified that `LdpcCodec::decode` already restores
shortened zero priors, clamps to ±50, resets scratch per call and returns real
convergence/parity/known-zero/iteration/decision outcomes. PHY must adapt it,
not duplicate those operations or promise an unavailable iteration checkpoint.
The source-table issue in LDPC-01 is unchanged.

Original PHY I20 pages 58, 65, 69 and 71 were rendered and visually inspected
for Figure 7 seed/taps and shortening, Figure 13 MSB order and centered IDFT,
Figure 18 cyclic/taper support, and Figure 19 prefix/useful references. Scoped
local text review also covered §7.4.3.1/5/16/17, including p55 residual-bit fill
and p56 grant pad. Existing TX evidence retains the complete pilot/mapping/
interleaver audit prerequisites. Estimators, confidence policy, floors, gap
outcomes and budgets are local engineering choices. This is no new external
interoperability evidence or CMTS RF/performance conformance result.

## Dependency-ordered checklist

- [x] ARCH-RX-00: Define the CMTS-US-RX block, chart, nine stage roles, input/
  result boundaries, lifecycle and inspection overview.
- [x] ARCH-RX-NAV: Link all nine overview/output rows to local stage sections,
  with index backlinks and contents/development navigation.
- [x] ARCH-RX-PATH: Add planned code/test paths for every RX section and identify
  actual codec reuse; no empty modules or new Cargo member.
- [x] ARCH-RX-01: Expand configured-timing framing, indexed input admission,
  bounded buffering, discontinuities, completion and independent acceptance.
- [x] ARCH-RX-02: Expand useful-window selection, CP/overlap boundaries and
  sample identity/validity without receiver access to TX samples.
- [x] ARCH-RX-03: Expand centered unitary FFT admission/metadata and independent
  forward vectors, sharing the TX-07 numerical owner.
- [x] ARCH-RX-04: Expand upstream pilot references, effective C×H estimation,
  coverage/reliability, correction and null/failure behavior.
- [x] ARCH-RX-05: Expand resource extraction and exact inverse visits across
  blocks/frames, preserving loading/roles and bit/cell conservation.
- [x] ARCH-RX-06: Expand MSB-first soft metrics, label/scale/noise-confidence
  semantics, hard-decision observations and independent acceptance.
- [x] ARCH-RX-07: Expand grant mask regeneration on LLRs, codeword ordering,
  pad removal and chunk/offset state.
- [x] ARCH-RX-08: Expand shortening restoration, codec admission and separate
  convergence/syndrome/known-zero/decision/iteration outcomes.
- [x] ARCH-RX-09: Expand receiver-known information deframing and partial output,
  preserving independent source association/comparison outside the block.
- [ ] WAVE-RX-01: Implement approved receiver stages after source/TX/unity-channel
  prerequisites and compare actual recovered bits in the separate verifier.

All RX-01..09 architecture contracts are complete for configured timing,
frame-based response estimation and reference-confidence demapping. Stage IDs
remain RX-01..09; the full block name is CMTS-US-RX. Implementation, source
transcription, independent scientific fixtures and the waveform closed loop
remain unchecked. Future blind acquisition, fast within-frame tracking, received-
noise calibration and finite-file/MAC framing need separate mode contracts.

## Validation

Check section fragments, unique targets, stage order, overview/output/backlink
coverage, planned-path absence and actual reused-path existence. Run the local
validation gate for checkpoint regression. These checks do not execute the
proposed receiver, prove source matrices or establish Rust/Python/UI parity.

### Prior block-overview validation

At that earlier overview checkpoint, on the Ubuntu 22.04.5 LTS checkout,
`scripts/validate.sh` passed in 3.20 seconds:
20 skills, 315 local links, 23 existing Rust tests, 19 setup tests, 5 Git tests,
formatting and Clippy. Focused checks resolved 129 section links in the six
changed/new documents, all 18 RX overview/output links to nine unique stage
targets, nine index backlinks and the major-section contents. All 38 unique
proposed receiver/shared paths remain absent; the one reused codec path exists.
TX/channel navigation remains intact. RX-01..09 detailed designs and scientific
milestones remain unchecked. `git diff --check` passed. No receiver processing,
new numerical algorithm, Python binding or native UI was executed by this work.


### RX-01..09 architecture completion validation

On the local Ubuntu checkout, `bash scripts/validate.sh` passed in 2.458 seconds:
20 skill/resource checks, 339 local links, 23 existing Rust tests, 19 setup tests,
5 Git-helper tests, doctests, formatting and Clippy. Focused documentation checks
resolved 127 fragment links across the five changed files, verified all nine
ordered stage contracts, 18 overview/output links and nine index backlinks,
and preserved the seven compact top-level contents destinations. All 39 unique
planned Rust paths in the receiver block remain absent; the one reused codec
exists. No Rust source, dependency or generated API/schema was changed.

Independent bounded arithmetic spot checks passed for complex pilot LS/correction,
BPSK MaxLog sign/scale, retained/shortened mother-coordinate layout, the minimum
700-bit grant's 52 payload bytes plus four information-fill bits, and centered
forward-tone coordinates. These are design sanity checks, not execution or
acceptance of the proposed Rust algorithms. Existing codec tests still share
source-table data and do not resolve LDPC-01/02.

`git diff --check` passed. Architecture milestones ARCH-RX-01..09 are complete;
WAVE-RX-01, source audits, new independent fixtures and all receiver runtime/
adapter acceptance remain pending. No native UI, Python binding, field device,
installed workflow or external interoperability was exercised. The reviewed
local save command is prepared only; no staging, commit or push was executed.
