# MORGANA requirements

Status: architecture-derived requirements baseline. Bounded synthetic stages,
source JSON and native APIs are implemented; capture/platform/extension acceptance
remains incomplete. This document consolidates the existing
[architecture](architecture.md), [feature plans](development/README.md) and
[official checklist](development/checklist.md). It does not authorize scientific
implementation or establish specification compliance.

**Contents**

- [Scope and status](#purpose-and-scope)
- [System boundaries](#system-and-scientific-boundaries)
- [US Configuration](#us-configuration-and-cmts-control)
- [PRBS](#prbs-source-and-independent-verification)
- [CM-US-TX](#cm-us-tx-stages)
- [CH-SIM](#ch-sim-stages)
- [CMTS-US-RX](#cmts-us-rx-stages)
- [PNM Files](#pnm-files-and-measurement-driven-inputs)
- [Instruments and results](#instruments-results-and-planned-presentation)
- [Rust and Python APIs](#high-level-rust-api-and-native-python-api)
- [Lifecycle and constraints](#lifecycle-and-nonfunctional-constraints)
- [Milestones and open decisions](#acceptance-milestones-and-open-decisions)

## Purpose and scope

Provide a standalone upstream DOCSIS OFDMA simulation toolkit for one cable
modem and a simulated CMTS upstream receiver. The first waveform milestone is a
bounded local closed loop:

**PRBS → CM-US-TX → CH-SIM in unity mode → CMTS-US-RX → independent source comparison.**

Later delivery adds explicitly supported channel impairments and measurement-driven
analysis using upstream RxMER and US-Pre-EQ inputs. A high-level Rust API owns
shared behavior; a native Python API wraps that Rust surface and is optional
for consumers to build/install. Delivery of the defined Python API remains a
requirement. Planned workbenches present the same inputs, readiness, instruments
and results.

This baseline excludes a full MAC, scheduler, service group, multiple simulated
CMs, downstream waveform, device capture/control, SNMP/TFTP, network-analysis
service and Python sidecars. Raw UCD/MAP generation, blind acquisition, live
ranging/probing/adaptive Pre-EQ, fractional sample-clock recovery and stochastic
phase noise are outside initial support. Recognizing their settings does not
make those modes executable. Desktop implementation, native packaging and
publication are separate delivery work.

## Interpretation, status and traceability

Each **REQ-** identifier is stable. **SHALL** and **MUST** express mandatory
requirements; **SHALL NOT** and **MUST NOT** express mandatory prohibitions.
Advisory requirement wording MUST NOT be used. A proposed recommendation MUST
be resolved into a mandatory requirement or an explicit exclusion/deferred scope
before acceptance into this baseline. Unresolved design choices MUST be decided
before dependent implementation begins; open questions are not optional obligations.

These keywords describe MORGANA product obligations; they do not assert an
identical CableLabs normative force. Source-derived behavior,
engineering policy and application resource budgets retain their distinct labels
in the linked architecture. Exact algorithms, source equations, file placement
and test paths remain there rather than becoming competing definitions here.
Descriptions of optional source fields/capabilities or consumer installation
choices do not weaken any applicable requirement or acceptance criterion.

Every requirement row supplies observable behavior, acceptance evidence and a
linked architecture owner plus official delivery IDs. Architecture stage links
lead to concrete implementation/test paths and dispositions. Feature-local IDs
remain valid refinements; the official checklist remains the completion record.
A design checkbox means documentation completed, never runtime acceptance.
Each requirement ID has a stable direct anchor. The official checklist's
[coverage table](development/checklist.md#requirement-coverage) maps every
requirement to its active implementation/validation tasks; the
[ordered software development phases](development/checklist.md#how-to-use-this-checklist)
define prerequisites and acceptance without weakening these obligations.
Compact delivery notation such as `WAVE-TX/CH/RX-01` refers to the separate
`WAVE-TX-01`, `WAVE-CH-01` and `WAVE-RX-01` checklist entries.

| Area | Current evidence / delivery boundary |
| --- | --- |
| Standalone LDPC, FEC facade and CLI | All-family source audit and standalone codec acceptance pass locally; waveform integration passes its separate stage/closed-loop cases. |
| Development setup and save tooling | Implemented; mock/read-only checks exist; fresh provisioning and hosted/platform evidence remain incomplete. |
| PRBS, TX-01..08, CH-01..06, RX-01..09 | Implemented/local source-stage and bounded synthetic closed-loop acceptance; configured timing/frame-pilot policies. |
| US Configuration JSON and PNM inputs | Applicable source-field audit/schema/parser/projections and synthetic playback implemented. Binary PNM formats/import/association remain pending. |
| High-level Rust session and native Python wrapper | Actual typed/JSON run, controls, native conversion/runtime/type declarations and independent parity pass locally; wider capture/API aggregate remains pending. |
| QAM/SA and desktop workbenches | Bounded actual QAM/SA and independent matched-data MER implemented; GUI/expanded inspectors remain planned. |

Requirements below apply when their capability is delivered. Extension sections
do not expand the first unity-loop milestone. Deferred features require their
own detailed design, source audit and implementation acceptance before exposure.

## System and scientific boundaries

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-sys-01"></a>REQ-SYS-01 | The toolkit SHALL run a bounded one-CM/one-channel upstream reference experiment from source bits through the actual TX, channel and RX, then compare recovered meaningful bits independently. | A completed and drained unity run recovers all generated meaningful bits with full contiguous coverage and zero mismatches; source counts, recovered counts and decoder flags are checked separately. | [Signal path](architecture.md#planned-upstream-signal-path-and-workbenches); SOURCE-01, WAVE-TX/CH/RX-01. |
| <a id="req-sys-02"></a>REQ-SYS-02 | Normal receiver inputs SHALL contain received samples and legitimate accepted receiver configuration. They SHALL NOT contain source truth or injected channel/noise truth. | Receiver admission tests exclude original bits, PRBS seed/ledger, injected H/C, RxMER targets and noise seeds/power; diagnostic truth is consumed only by separate comparisons. | [Ownership/results](architecture.md#ownership-results-and-acceptance); WAVE-RX-01. |
| <a id="req-sys-03"></a>REQ-SYS-03 | Scientific algorithms, validation and orchestration SHALL execute in safe Rust independently of presentation or language runtimes. Adapters MUST NOT duplicate scientific calculations. | Core-only build/tests require neither Python nor Qt; adapters contain no DSP/FEC/association duplicates, native DSP/codec FFI or unsafe simulation code. | [API ownership](architecture.md#api-ownership-and-dependency-flow); FOUNDATION-03, API-RUST/INPUT-01. |
| <a id="req-sys-04"></a>REQ-SYS-04 | The toolkit SHALL distinguish representable settings, domain validity and executable support. | Unsupported optional modes remain inspectable with reasons; execution rejects them before consuming input, random state or source bits; recognized QAM/code identifiers alone never imply a complete coding chain. | [US Configuration](architecture.md#us-configuration); US-CONFIG-01, USJSON-CORE/PROJECTION/PARITY-01. |
| <a id="req-sys-05"></a>REQ-SYS-05 | Scientific claims SHALL identify pinned evidence and the applicable endpoint without confusing internal closed-loop evidence with external interoperability. Each stage SHALL have source-checked expected inputs/outputs recorded before its implementation, independently of production tables/algorithms. | Source/matrix/label checks record revision, section/page and source-review gaps; reports/docs label internal experiments accurately and retain optional-capability distinctions. Build these cases stage by stage; external interoperability fixtures and a complete upfront catalog are not prerequisites. | [Foundation evidence](development/features/foundation/design.md#ldpc-01-normative-evidence-and-engine-feasibility); LDPC-01/02. |

## US Configuration and CMTS control

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-cfg-01"></a>REQ-CFG-01 | US Configuration SHALL retain a discoverable profile/preset inventory and explicitly select a one-CM/one-channel configuration shared by both endpoints. | Rust inventory exposes every retained entry without hardcoded adapter catalogs; invalid selection preserves the prior accepted plan; inventory does not automatically create multi-preset trials. | [US Configuration](architecture.md#us-configuration); US-CONFIG-01. |
| <a id="req-cfg-02"></a>REQ-CFG-02 | Configuration admission SHALL produce an immutable CMTS plan and separate accepted TX/RX views through shared validation. | Both views agree on permitted geometry/grant/pilot/PHY-seed settings while normal RX excludes source, C/update values and channel/noise truth; failure preserves accepted settings and readiness. | [CMTS configuration](architecture.md#cmts-configuration-us-configuration-json); USJSON-CORE/PROJECTION/PARITY-01. |
| <a id="req-cfg-03"></a>REQ-CFG-03 | Generic OFDMA JSON SHALL have an explicit format/schema version, named presets, selection and separated normative configuration versus simulation settings. | Schema/parser fixtures cover required/optional/null/default/unknown-field behavior, unsupported versions, bounded extension metadata and round trips; vendor IDs are optional provenance, never normative preset meanings. | [CMTS JSON contract](architecture.md#cmts-configuration-us-configuration-json); USJSON-FORMAT/PRESETS-01. |
| <a id="req-cfg-04"></a>REQ-CFG-04 | Configuration coverage SHALL account for every applicable field/option in the pinned MULPI OFDMA scope. | The field-level matrix records source path/page, endpoint, force/applicability, encoding/units/enums, JSON pointer, Rust owner, support state and independent fixtures; every inapplicable or unresolved row has an explicit disposition. | [Coverage plan](development/features/us-configuration-json/coverage.md); USJSON-COVERAGE-01. |
| <a id="req-cfg-05"></a>REQ-CFG-05 | Typed and document-based configurations SHALL use equivalent domain rules and bounded admission. The first reference loop SHALL use typed synthetic configuration; JSON and verified capture loaders SHALL follow its acceptance. | Invalid ranges, reserved values, inconsistent pilot/loading/geometry, associations and aggregate budgets reject atomically; valid synthetic configurations do not require an unverified capture decoder. Full applicable MULPI/JSON delivery remains required after the typed reference milestone. | [US Configuration admission](architecture.md#us-configuration); US-CONFIG-01, USJSON-CORE/PROJECTION/PARITY-01. |
| <a id="req-cfg-06"></a>REQ-CFG-06 | Example presets SHALL demonstrate generic configurations without claiming universal recommended modulation. | Reviewed 25/50 kHz, mixed-loading and zero-valued-minislot examples identify source versus engineering choices; ranging/probe examples explicitly state execution support; conditional/optional settings are not silently discarded. | [JSON delivery plan](development/features/us-configuration-json/design.md); USJSON-FORMAT/PRESETS-01. |

## PRBS source and independent verification

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-prbs-01"></a>REQ-PRBS-01 | The source SHALL emit continuous deterministic PRBS15 using the architecture's recurrence, seed range and bit order, independently of PHY scrambling. | Literal initial vectors and the 32767-bit period pass for independently checked seeds; zero/out-of-range seeds reject; grants, words and chunk boundaries do not reseed the source. | [Sequence contract](architecture.md#sequence-and-bit-representation); SOURCE-01. |
| <a id="req-prbs-02"></a>REQ-PRBS-02 | Source consumption SHALL track accepted meaningful payload with checked absolute positions and bounded chunks. | Fill/shortening/parity/pad/pilots consume no source bits; backpressure and rejected work do not advance the generator; chunked generation matches contiguous generation and overflow rejects before mutation. | [Source interfaces](architecture.md#rust-owners-and-stage-interfaces); SOURCE-01. |
| <a id="req-prbs-03"></a>REQ-PRBS-03 | Verification SHALL compare actual recovered meaningful decisions using an independently owned expected stream and validated source association. | Wrong but valid codewords produce source errors even if parity passes; failures do not suppress available decisions; gaps/duplicates/reordering stop contiguous comparison explicitly without phase search or repair. | [Comparison contract](architecture.md#independent-comparison-and-incomplete-recovery); SOURCE-01, WAVE-RX-01. |
| <a id="req-prbs-04"></a>REQ-PRBS-04 | Verification results SHALL distinguish generated, compared and unverified bits, coverage, mismatch counts and completion. | Zero compared bits yield unavailable BER; zero observed errors with partial/truncated/discontinuous coverage cannot claim complete recovery; retained results survive later operations. | [Comparison contract](architecture.md#independent-comparison-and-incomplete-recovery); SOURCE-01, API-RUN-01. |

## CM-US-TX stages

Each row covers the observable contract of one existing stage. Shared resource,
label and transform conventions SHALL be used consistently by TX and RX while
their mutable processing contexts remain independent.

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-tx-01"></a>REQ-TX-01 | Grant framing SHALL derive coded capacity and the upstream codeword sequence from accepted resources/loading while separating meaningful bytes, information-fill ones, shortening zeros, parity and zero grant pad. | Independent threshold/borrowing/boundary cases conserve bits and source consumption; RX derives the same layout from legitimate configuration; rejected plans preserve state. | [TX-01](architecture.md#tx-01-grant-framing-and-fec-selection); PHY-01. |
| <a id="req-tx-02"></a>REQ-TX-02 | Encoding SHALL use the selected source-verified upstream long/medium/short LDPC family with systematic order and exact shortening semantics. All three code families SHALL pass source audit and codec acceptance before dependent waveform implementation. | Independently checked matrix entries/parity and full/shortened words pass; only appended shortening-zero coordinates are omitted; no downstream BCH or assumed puncturing is added. | [TX-02](architecture.md#tx-02-ldpc-encoding-and-shortening); LDPC-01/02, WAVE-TX-01. |
| <a id="req-tx-03"></a>REQ-TX-03 | PHY randomization SHALL use the defined 23-bit grant seed, first-bit/tap convention and per-grant reset over exactly the transmitted bit positions. | Literal mask vectors, chunk continuity and reset tests cover parity and final grant pad; omitted shortening and known pilots add no clocks; invalid/reordered input preserves state. | [TX-03](architecture.md#tx-03-grant-seeded-phy-randomization); WAVE-TX-01. |
| <a id="req-tx-04"></a>REQ-TX-04 | QAM mapping SHALL form MSB-first cell words in accepted visit order using exact upstream labels, normalization and role-dependent loading. | Independent label/energy vectors cover the declared BPSK/QPSK through 4096-QAM scope including non-square orders; inactive resources consume no payload; unknown/unimplemented orders reject. | [TX-04](architecture.md#tx-04-cell-word-construction-and-qam-mapping); WAVE-TX-01. |
| <a id="req-tx-05"></a>REQ-TX-05 | OFDMA framing SHALL apply the accepted pilot pattern, known signs, role/loading plan, block partitioning and joint interleaving/address order. | Independent masks, pilot vectors and permutation/bijection cases cover supported patterns, edge/body layout, exclusions, zero resources and boost exceptions; bit/cell totals are conserved and scaling occurs once. | [TX-05](architecture.md#tx-05-pilots-ofdma-framing-and-interleaving); WAVE-TX-01. |
| <a id="req-tx-06"></a>REQ-TX-06 | Pre-EQ SHALL apply one accepted complex corrective bank after role scaling and before IFFT, preserving the distinction between C and injected H. | Independent normalization/phase/default/reset/replacement/adjustment cases pass; excluded carriers remain zero; stale bases/nonfinite/invalid banks reject; bank transitions occur only at accepted symbol boundaries. | [TX-06](architecture.md#tx-06-cm-pre-eq); WAVE-TX-01, PREEQ-INPUT-01. |
| <a id="req-tx-07"></a>REQ-TX-07 | IFFT SHALL transform complete accepted 2K/50 kHz or 4K/25 kHz physical grids at 102.4 Msamples/s using the defined centered unitary convention. | Independent direct-sum, tone, impulse and energy checks establish sign/bin order/scaling; useful sample count and timing are exact; inactive bins and invalid geometry are checked. | [TX-07](architecture.md#tx-07-ifft); WAVE-TX-01. |
| <a id="req-tx-08"></a>REQ-TX-08 | Sample assembly SHALL apply the specified CP/RP, cyclic extension, taper and overlap while retaining exact useful/prefix origins, burst edges, tails and explicit guards. | Independent numbered-sample/window tests cover zero/nonzero RP and adjacent symbols; complete output is invariant across chunks/backpressure; invalid geometry rejects and cancellation retains honest partial status. | [TX-08](architecture.md#tx-08-sample-assembly); WAVE-TX-01. |

## CH-SIM stages

REQ-CH-01/02/06 define initial unity delivery. Response, residual and timing
effects are later extensions, enabled only in declared compatible combinations.

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-ch-01"></a>REQ-CH-01 | Channel admission SHALL validate finite indexed sample blocks, clock, identities, continuity and budgets before changing state. | Stale/duplicate/overlap/unexplained-gap/nonfinite/overflow inputs reject atomically; empty blocks are no-ops, not finish; unsupported composition rejects before TX consumption. | [CH-01](architecture.md#ch-01-input-admission); WAVE-CH-01, WAVE-CH-02. |
| <a id="req-ch-02"></a>REQ-CH-02 | Initial unity transport SHALL preserve sample bit patterns and metadata exactly without impairments or random draws. | Bitwise tests include signed zero and arbitrary chunking with unchanged indices/rate/burst/tail/guard/validity; empty/disabled impairment settings use the same bypass. | [CH-02](architecture.md#ch-02-unity-transport); WAVE-CH-01. |
| <a id="req-ch-03"></a>REQ-CH-03 | The response extension SHALL apply the declared causal synthetic complex FIR without implicit normalization, circular wrap or per-symbol resets. | Literal complex convolution/impulse/delay cases establish phase, original origin, state continuity and exact terminal drain; zero/deep-null responses remain valid destructive experiments. | [CH-03](architecture.md#ch-03-channel-response); WAVE-CH-02. |
| <a id="req-ch-04"></a>REQ-CH-04 | Residual synthesis SHALL offer explicit Off, sample-AWGN and restricted RxMER-derived modes using separate deterministic noise state and declared reference power. | Independent power/statistical/draw-order tests cover seeds, missing-carrier policy and pilot/role scaling; initial RxMER synthesis rejects nonunity C/H or incompatible timing across the complete schedule. | [CH-04](architecture.md#ch-04-residual-error); WAVE-CH-02. |
| <a id="req-ch-05"></a>REQ-CH-05 | The timing extension SHALL implement only the designed integer delay, constant phase and CFO with emitted-sample-clock continuity. | Independent impulse/tone/rotation cases establish signs/origin, chunk/pause continuity and exact delay drain; zero mode is bitwise bypass; fractional clock and stochastic phase noise remain unavailable. | [CH-05](architecture.md#ch-05-timing-and-phase); WAVE-CH-02, CH-EXT-02. |
| <a id="req-ch-06"></a>REQ-CH-06 | Channel output SHALL retain indexed samples and bounded passive observations while separating diagnostics from legitimate RX inputs. | Observer selection/capacity does not change samples or randomness; output validity/partial/drain metadata is retained; injected H/noise settings never become hidden RX corrections. | [CH-06](architecture.md#ch-06-output-and-observations); WAVE-CH-01, INSTRUMENTS-01. |

## CMTS-US-RX stages

Initial scope is scheduled data with configured burst timing and frame-based
received-pilot correction. Wrong timing, low confidence, destructive channels and
missing coverage may cause genuine decoding failures; the receiver SHALL not
repair them using simulator truth.

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-rx-01"></a>REQ-RX-01 | Burst framing SHALL derive timing from accepted RX configuration and preserve actual indexed blocks and explicit missing intervals. | Literal origin/stride/window cases pass; unexplained gaps/reordering reject; declared gaps retain coverage loss rather than becoming available zero samples; no hidden timing search is performed. | [RX-01](architecture.md#rx-01-burst-framing-and-timing); WAVE-RX-01. |
| <a id="req-rx-02"></a>REQ-RX-02 | Useful-symbol extraction SHALL select exactly the scheduled N-sample windows without silently filling incomplete windows. | Numbered-sample/CP/overlap/truncation cases distinguish available zeros from missing samples and retain the correct symbol identities and unavailable outcomes. | [RX-02](architecture.md#rx-02-useful-symbol-extraction); WAVE-RX-01. |
| <a id="req-rx-03"></a>REQ-RX-03 | FFT SHALL produce raw physical bins using the inverse of the accepted centered unitary TX convention. | Independent complex-sum, signed-tone, impulse and energy cases establish bin/sign/scaling correctness and preserve availability metadata without injecting channel truth. | [RX-03](architecture.md#rx-03-fft); WAVE-RX-01. |
| <a id="req-rx-04"></a>REQ-RX-04 | Channel estimation/equalization SHALL estimate effective C×H from received known pilots using the declared FrameFlatLs or FramePilotLinear policy and explicit zero-forcing validity. | Independent complex-anchor/interpolation/notch cases verify known pilot gain/sign treatment, estimate coverage and unavailable outputs; no hidden supplied-H, fast within-frame tracking or noise-estimation capability is claimed. | [RX-04](architecture.md#rx-04-channel-estimation-and-equalization); WAVE-RX-01, RX-EXT-01. |
| <a id="req-rx-05"></a>REQ-RX-05 | Resource extraction SHALL independently invert the accepted resource/interleaving order and preserve unavailable scheduled cells and their bit positions. | Independent mixed-loading/permutation/boost cases conserve order/counts; missing cells are not compacted and known amplitude is removed once. | [RX-05](architecture.md#rx-05-resource-extraction-and-inverse-interleaving); WAVE-RX-01. |
| <a id="req-rx-06"></a>REQ-RX-06 | Soft demapping SHALL produce MSB-first finite MaxLog natural-log P(0)/P(1) metrics from shared upstream labels/scales and a valid ReferenceVariance. | Independent label/distance/sign tests cover positive-favors-zero convention, configured saturation, ties and zero-confidence erasures; nonpositive/nonfinite variance rejects. | [RX-06](architecture.md#rx-06-soft-qam-demapping); WAVE-RX-01. |
| <a id="req-rx-07"></a>REQ-RX-07 | Soft derandomization SHALL independently regenerate the grant mask and reverse LLR signs before LDPC without changing magnitude or position. | Mask-one metrics reverse sign; erasures stay zero; every transmitted position including pad advances the mask, while omitted shortening/pilots do not; word ordering and grant resets remain exact. | [RX-07](architecture.md#rx-07-phy-soft-derandomization); WAVE-RX-01. |
| <a id="req-rx-08"></a>REQ-RX-08 | LDPC integration SHALL restore shortening exactly once through the existing codec contract and retain real decoder outcomes. | Retained-length inputs, independent shortening cases and 1..100 iteration bounds pass; convergence, syndrome, shortened-zero consistency, failed decisions and actual iterations remain distinct; controls act between indivisible codec calls. | [RX-08](architecture.md#rx-08-shortening-restoration-and-ldpc-decoding); LDPC-01/02, WAVE-RX-01. |
| <a id="req-rx-09"></a>REQ-RX-09 | Information deframing SHALL remove only receiver-known residual fill and retain actual complete/partial/failed meaningful decisions and coverage. | Independent byte/fill/short-word cases preserve positions and continuity; failures are not dropped; source association/comparison happens outside normal RX. | [RX-09](architecture.md#rx-09-information-deframing); WAVE-RX-01. |

## PNM Files and measurement-driven inputs

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-pnm-01"></a>REQ-PNM-01 | Imported observations SHALL preserve original bytes, hashes, timestamps, exact grids, nulls, identities, units and reference/provenance. | Original input remains recoverable after decode/selection/replay; malformed, incompatible and oversized inputs reject without replacing accepted state; upstream formats need pinned evidence and lawful fixtures. | [PNM input design](development/features/upstream-inputs/design.md); RXMER-FORMAT-01, PREEQ-FORMAT-01, US-CONFIG-FORMAT-01. |
| <a id="req-pnm-02"></a>REQ-PNM-02 | RxMER SHALL support explicit single selection, power-domain averaging and bounded scheduled hold/interpolation policies over multiple captures. | Independent conversions/weights/time-boundary/null cases match resolved power and coverage; original capture times stay unchanged; synthetic replay time is separate and importing more files does not create trials implicitly. | [RxMER](architecture.md#rxmer-input); RXMER-INPUT-01. |
| <a id="req-pnm-03"></a>REQ-PNM-03 | US-Pre-EQ SHALL support a single fixed bank, multiple snapshots and multiple explicitly based initialization/adjustment updates. | Independent complex/base/reset tests reject stale, missing or ambiguous dependencies; immutable schedules apply complete accepted banks only at defined symbol boundaries and preserve probe/source associations. | [US-Pre-EQ](architecture.md#us-pre-eq-input); PREEQ-INPUT-01. |
| <a id="req-pnm-04"></a>REQ-PNM-04 | Combined input preflight SHALL validate the entire selected playback/update plan against channel/receiver support before execution. | A later incompatible Pre-EQ event fails preparation even if the initial bank is compatible; RxMER targets, corrective C and injected H remain separate; no unsupported composition is silently enabled. | [Input composition](development/features/upstream-inputs/design.md); PREEQ-INPUT-01, RXMER-INPUT-01, WAVE-CH-02. |

## Instruments, results and planned presentation

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-obs-01"></a>REQ-OBS-01 | Shared Rust QAM and SA instruments SHALL inspect bounded real stage observations at named TX/channel/RX reference planes. | Query results identify run, configuration, tap, grid/sample units and retention coverage; absent history remains unavailable; instrument enable/disable/query does not alter waveform, RNG or decoder behavior. | [Shared QAM/SA](architecture.md#shared-qam-analyzer-and-spectrum-analyzer); INSTRUMENTS-01. |
| <a id="req-obs-02"></a>REQ-OBS-02 | Scientific results SHALL distinguish measured observations, analytical/model inputs, receiver estimates and simulated FEC/source outcomes. | Reports preserve convergence/parity/known-zero/source-error distinctions, failed words, actual iterations, partial coverage and provenance; zero observed error uses an explicit status rather than fabricated finite RxMER or JSON infinity. | [Results](architecture.md#ownership-results-and-acceptance); API-RUN-01, INSTRUMENTS-01. |
| <a id="req-obs-03"></a>REQ-OBS-03 | Future workbenches SHALL present PRBS, CM-US-TX, CH-SIM and CMTS-US-RX in path order with separate US Configuration and PNM Files inputs. | Stage navigation opens the corresponding defined stage; shared QAM/SA actions route to actual selected taps; source-only acceptance never marks the entire experiment ready. | [Workbench organization](architecture.md#planned-upstream-signal-path-and-workbenches); DEV-UI-PLAN-01 after scientific prerequisites, then a separately approved UI implementation checklist. |
| <a id="req-obs-04"></a>REQ-OBS-04 | Editors SHALL distinguish draft and accepted settings, keep loading/apply idle and preserve accepted state on cancel/invalid apply. | Accepted readiness uses text as well as color; preview consumes no active source/random state; displayed results distinguish complete, partial and discontinuous coverage. | [Source lifecycle/presentation](architecture.md#lifecycle-and-prbs-tx--prbs-rx-presentation); SOURCE-01, DEV-UI-PLAN-01, then a separately approved UI implementation checklist. |

## High-level Rust API and native Python API

Exact proposed signatures and implementation/type-stub/test paths are maintained
in the [paired API architecture](architecture.md#high-level-rust-and-python-apis).
Those declarations remain design stubs until implemented and validated.

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-api-01"></a>REQ-API-01 | The high-level Rust API SHALL expose typed idle session, configuration/inventory/selection, input admission, preview and explicit bounded execution while preserving existing FEC entrypoints. This Rust session SHALL be developed alongside the backend and used for reference unity-loop acceptance. | Direct Rust consumers exercise valid/invalid operations without CLI/Qt/Python; existing FEC imports, calls and schema-1 report semantics remain compatible. | [Paired operations](architecture.md#paired-rust-and-python-interface-stubs); API-RUST/INPUT-01. |
| <a id="req-api-02"></a>REQ-API-02 | The optional native Python API SHALL wrap working public Rust operations with equivalent domain validation and results. Native Python implementation SHALL begin after the Rust unity loop passes acceptance. | Real native calls cover configuration, single/multi inputs and execution; no Python DSP/association/decoder implementation or subprocess sidecar is used; Rust-only dependency checks exclude binding runtimes. No early FEC-only Python wrapper is part of the selected delivery order. | [API ownership](architecture.md#api-ownership-and-dependency-flow); API-PY/STUB-01. |
| <a id="req-api-03"></a>REQ-API-03 | Both APIs SHALL return owned results and structured domain errors using native language conventions. | Error categories/details match without parsing messages; Python uses exceptions/None and checked integer/buffer conversions; outputs remain valid after later calls, input release and session disposal; zero-copy claims require lifetime proof. | [API errors/results](architecture.md#api-lifecycle-errors-and-result-contracts); API-PARITY/DOCS-01. |
| <a id="req-api-04"></a>REQ-API-04 | Native Python execution SHALL release the interpreter lock during long Rust work and serialize mutable session access with explicit Busy behavior. | Actual native concurrency tests demonstrate independent cancellation/progress access, deterministic Busy for competing calls and session restoration after normal/error/cancel exits; no Python callback executes inside core locks. | [API lifecycle](architecture.md#api-lifecycle-errors-and-result-contracts); API-PY/STUB-01, API-PARITY/DOCS-01. |
| <a id="req-api-05"></a>REQ-API-05 | Rust and Python contracts, examples and Python type declarations SHALL describe the same implemented capability set. | Independently executed bounded native runs match resolved settings, seeds, provenance, status, FEC outcomes and partial coverage with declared numerical tolerances; actual extension exports match `.pyi`/typing metadata and paired examples run. | [API gates](architecture.md#api-delivery-and-validation-gates); API-PY/STUB-01, API-PARITY/DOCS-01. |
| <a id="req-api-06"></a>REQ-API-06 | Exported/configuration documents SHALL use explicit independent versions and declared compatibility rules. | Unknown versions/typed fields reject or follow an explicit migration; no FEC report is reinterpreted as configuration/workbench; any later shared saved experiment runs through both APIs without dropped settings or manual conversion. | [API compatibility](architecture.md#api-lifecycle-errors-and-result-contracts); USJSON-FORMAT/PRESETS-01, API-01. |

## Lifecycle and nonfunctional constraints

| ID | Required behavior | Acceptance criterion | Architecture owner / delivery |
| --- | --- | --- | --- |
| <a id="req-life-01"></a>REQ-LIFE-01 | Runs SHALL freeze accepted settings with distinct run/configuration identities and deterministic independent source/noise state. | Repeated runs with equal seeds/settings reproduce declared deterministic outputs; observers/chunking do not affect science; stale results or cross-session IDs are rejected. | [API lifecycle](architecture.md#api-lifecycle-errors-and-result-contracts); SOURCE-01, WAVE-TX/CH/RX-01, API-RUN-01. |
| <a id="req-life-02"></a>REQ-LIFE-02 | Cancellation/failure SHALL preserve completed science and identify incomplete or not-started work under bounded safe work quanta. | Stage-boundary and between-word cancellation tests retain actual completed results/counts, pending tails/ranges and partial status; no forced thread termination or invented completion is used. | [Run ownership](architecture.md#ownership-results-and-acceptance); WAVE-TX/CH/RX-01, API-RUN-01. |
| <a id="req-life-03"></a>REQ-LIFE-03 | Pause/resume, when exposed, SHALL preserve all scientific stream state and define paused-time and stop-from-paused semantics. Bounded cancellation and partial-result acceptance SHALL precede pause/resume delivery. | Tests retain PRBS/mask/permutation/Pre-EQ/RNG/history state and pending output across pause; controls remain unavailable in an API until its safe-boundary/lifecycle contract is implemented. First-loop readiness MUST NOT depend on pause/resume; later exposure requires state/time/stop-from-paused tests. | [API control boundary](architecture.md#api-lifecycle-errors-and-result-contracts); API-RUN-01, API-PY/STUB-01. |
| <a id="req-nfr-01"></a>REQ-NFR-01 | Inputs, expanded plans, per-call work, cumulative runtime/memory, output queues and retained observations SHALL be bounded before allocation/execution. | Existing architecture budgets and independently checked overflow/exhaustion cases reject without state mutation; final cumulative job budgets are documented before execution support. | [Configuration limits](architecture.md#us-configuration), [API limits](architecture.md#api-lifecycle-errors-and-result-contracts); US-CONFIG-01, API-RUN-01. |
| <a id="req-nfr-02"></a>REQ-NFR-02 | Reusable code/tooling SHALL preserve Apache-2.0 ownership and all applicable third-party notices, licenses and provenance. Reviewed reference-code adaptations SHALL remain locally owned and MUST NOT introduce a MERLIN crate/checkout/runtime dependency. | Dependency/reuse/package review retains actual copied notices and modifications; GPL presentation code does not enter the independent scientific core; private PDFs/captures/build outputs remain excluded. Each adaptation retains source/revision/notices/modifications and passes independent upstream checks. | [Foundation/reuse](development/features/foundation/design.md#foundation-02-merlin-reuse-assessment); FOUNDATION-03. |
| <a id="req-nfr-03"></a>REQ-NFR-03 | Development setup SHALL require explicit intent and provide read-only check/dry-run behavior on declared targets. | Mode/host/pin/path/bounds/failure tests pass; inspection creates no caches or installs; apply obtains only missing declared prerequisites with pinned local Rust/locked sources; real fresh provisioning is verified separately. | [Setup requirements](development/features/development-setup/design.md#setup-01-requirements); SETUP-01..04. |
| <a id="req-nfr-04"></a>REQ-NFR-04 | Validation and delivery records SHALL state actual evidence and preserve reproducible local tooling. | Required local gate passes with caches retained; hosted/native/package/interoperability claims require actual corresponding runs; prepared save commands do not imply commit/push/release execution. | [Checkpoint](architecture.md#checkpoint-and-target-overview), [Git workflow](git.md); FOUNDATION-03, official completion reviews. |

## Accepted backend staging

The [six accepted delivery decisions](architecture.md#accepted-backend-delivery-decisions)
refine the requirements above: all-family codec audit; standalone local reference
adaptation; cancellation before pause; independent cases before each stage;
typed synthetic configuration before loaders; Rust API integration before native
Python. Decisions establish scope/order, not source/runtime acceptance. Existing
requirement IDs and deferred delivery obligations are retained.

## Acceptance milestones and open decisions

| Milestone | Required evidence / scope | Pending prerequisites |
| --- | --- | --- |
| Source-verified codec | REQ-SYS-05 and LDPC portion of REQ-TX-02/REQ-RX-08; independent matrix/shortening/parity and decoder outcome checks. | LDPC-01/02 complete: [source audit and codec evidence](development/features/ldpc-source-audit/validation.md). Full TX/RX integration remains pending. |
| Reference unity loop | REQ-SYS-01..04, REQ-PRBS-01..04, REQ-TX-01..08, REQ-CH-01/02/06, REQ-RX-01..09 and applicable lifecycle/resource requirements. | Typed configuration/resource planning, source, all waveform stages and independent stage/source acceptance. No measurement import or external implementation is a prerequisite. |
| Instruments and experiment reports | REQ-OBS-01/02 with bounded retained taps and independent source/decoder accounting. | Actual waveform/results and owned observation contracts; presentation implementation is separate. |
| Measurement/impairment extensions | REQ-PNM-01..04 and REQ-CH-03..05 in their declared compatibility scope. | Source-verified capture formats, whole-schedule association, approved numerical implementation and model-specific independent tests. |
| High-level language APIs | REQ-API-01..06 plus applicable lifecycle requirements. | Shared Rust foundation before bindings; real experiment execution before complete waveform API claims; native parity/type-stub checks and documented support. |
| Optional presentation and wider modes | REQ-OBS-03/04, any later exposure of deferred modes. | Dedicated implementation plans and complete readiness/lifecycle/source/acceptance contracts; no automatic GUI or acquisition commitment. |

The following remain explicit decisions or evidence gaps:

- Complete field-level coverage for `CM-SP-MULPIv3.1-I25-230419` with dependent
  `CM-SP-PHYv3.1-I20-230419` rules; the current inventory is not a full audit.
  DOCSIS 4.0/newer MULPI extensions require separate pinned applicability work.
- Upstream configuration/profile, RxMER and Pre-EQ/update capture formats,
  units/scales and lawful independent fixtures before importer support.
- Independent pilot masks, constellation labels, randomizer/interleaver vectors
  and source-table acceptance before claiming implemented normative behavior.
- Concrete aggregate job budgets and complete pause/resume/signal policy before
  exposing corresponding operations; existing per-stage bounds remain binding.
- Broader RxMER with nonunity/time-varying C/H, captured-H reconstruction,
  received-signal acquisition, ranging/probing and calibrated confidence models.
- Python distribution/dependency/platform selection, native packaging and hosted
  validation; design names and another project's releases are not runtime evidence.

## Baseline maintenance

Keep this document focused on behavior and acceptance. Architecture owns design,
file layout and detailed algorithms; the official checklist owns delivery status;
feature records own task-specific validation. New behavior MUST add/update stable
requirements and corresponding owner/test/checklist links. Do not renumber IDs
to match document order or mark a requirement satisfied solely because its
architecture section exists. No source/runtime artifact is created by this
requirements-only baseline.

See the [baseline creation and validation record](development/features/requirements/design.md)
for the document review and checks performed during consolidation.
