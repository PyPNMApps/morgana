# CM-US-TX block and stage design

Status: transmitter overview and TX-01 through TX-08 architecture defined;
scientific implementation and integration remain planned.
Scope is documentation in this repository, with no links to another source
checkout and no scientific, UI, CLI or binding implementation changes.

## Requirements and ownership

| ID | Requirement | Owner / acceptance |
| --- | --- | --- |
| TX-ARCH-01 | Use CM-US-TX consistently and describe its eight internal stages. | Canonical architecture, README and development records; one ordered TX path. |
| TX-NAV-01 | Link every TX overview/output label to its canonical local section. | Eight unique stage targets; future sections explicitly remain placeholders. |
| TX-PATH-01 | Name code/test files in every TX stage section. | Planned adapters, shared numerical owners and existing codec reuse agree with the directory overview. |
| TX-ARCH-02 | Distinguish bit, complex-cell/frequency-grid and time-sample boundaries. | Rust stage contracts; meaningful bit/QAM/SA instrumentation with bounded passive observations. |
| TX-PLAN-01 | Derive coded capacity from accepted grant resources/loading, then choose the exact upstream codeword sequence. | Shared resource owner and Rust grant planner; independent capacity/threshold/order/borrowing cases. |
| TX-PLAN-02 | Separate meaningful bytes, information-fill ones, shortening zeros, parity and zero grant padding. | Framing/codec boundary; conservation, byte-residue and source-consumption checks. |
| TX-PLAN-03 | Plan without source mutation and admit bounded work transactionally. | Orchestration; rejected inputs preserve accepted state and source, no unbounded grant history. |
| TX-PLAN-04 | Let RX derive the same layout from accepted configuration without transmitter truth. | Shared pure planner called independently by endpoints; no original bits/seed/source ledger in RX recovery. |
| TX-PLAN-05 | Keep validation/results shared by Rust and future Python/UI consumers. | Public facade and thin adapters; typed errors/owned results and versioned export changes. |
| TX-FEC-01 | Preserve TX-01's codeword identity and encode retained information with systematic parity. | Existing Rust codec; source-verified upstream matrices, independent parity oracle and exact bit ordering. |
| TX-FEC-02 | Append shortening zeros before encoding and omit only those coordinates afterward. | Codec shortening owner; all families, full/shortened boundaries and unchanged information-fill ones. |
| TX-FEC-03 | Assemble ordered encoded words and final grant pad with bounded, explicit partial status. | Transmitter adapter; checked offsets/totals, chunk invariance, stale-input and failure/cancellation coverage. |
| TX-RAND-01 | Use the Figure 7 23-bit seed/tap/first-bit convention and reset once per grant. | Rust PHY randomizer; independent literal vectors and repeated-grant/first-step checks. |
| TX-RAND-02 | Process exactly transmitted grant bits, including parity/pad, without extra clocks for shortening or pilots. | Grant stream adapter; role/length/offset conservation and arbitrary-chunk continuity. |
| TX-RAND-03 | Preserve state on invalid input and completed output on bounded cancellation. | Independent job-owned contexts; stale/duplicate/overrun, budget, observer and pause/resume cases. |
| TX-RAND-04 | Regenerate the mask independently at RX and reverse randomization on soft bits before LDPC. | Shared Rust mask algorithm with separate RX state; sign/magnitude/position and future adapter parity checks. |
| TX-QAM-01 | Build MSB-first cell words in the shared resource-visit order with exact per-role loading. | Rust mapping adapter; mixed-loading, partial-word and coded-bit conservation cases. |
| TX-QAM-02 | Use exact Annex A labels and Table 54 scaling for upstream BPSK/QPSK through 4096-QAM. | Shared Rust tables/lookup; independent literal vectors, cardinality and uniform-label energy checks, including 8-QAM and 32-QAM. |
| TX-QAM-03 | Distinguish data, complementary data, known pilots and inactive resources. | Accepted profile/resource validation; complementary loading max(data bits minus four, one), no payload clocks for known pilots or zero minislots. |
| TX-QAM-04 | Preserve bounded state/results on invalid input, backpressure and cancellation. | TX adapter; chunk invariance, stale/duplicate/overrun cases, partial status and passive QAM observations. |
| TX-GRID-01 | Derive one accepted role/loading/physical-address plan shared by capacity, mapping and inverse recovery. | Resource owner; contiguous minislots, edge transitions, exclusions, zero resources and exact bit/cell conservation. |
| TX-GRID-02 | Partition each frame's eligible grant minislots into normative blocks and use the specified joint bit-reverse address sequence. | Rust partition/permutation owners; independent 24-minislot boundary, power-of-two and bijection checks. |
| TX-GRID-03 | Generate exact known pilot signs and apply required role/pattern power scaling once. | Independent PRBS12 and pilot owners; fixed-seed physical-bin vectors, all-bin clocks and boosting/exception cases. |
| TX-GRID-04 | Assemble complete physical symbol grids with bounded state, valid partial results and matching receiver expectations. | TX framer and RX adapters; frame/block merging, failure/cancel/observer cases and known-amplitude inverse checks. |
| TX-PREEQ-01 | Apply one complex corrective coefficient per physical carrier after pilot-role scaling and before IFFT. | Shared Rust numerical owner and TX adapter; independent phase/gain vectors and exact grid/role conservation. |
| TX-PREEQ-02 | Normalize newly calculated banks over used and unused non-excluded carriers, preserving excluded zeros. | Coefficient admission; independent full-domain energy/phase cases, empty/zero/nonfinite rejection and atomic state. |
| TX-PREEQ-03 | Distinguish defaults/reset, replacement and multiplicative adjustment with explicit geometry/base identities. | Configuration owner; stale-base, range, reset-trigger and future last-probe association cases; no MAC parsing or live adaptation claim. |
| TX-PREEQ-04 | Keep corrective C separate from injected H, source truth and receiver estimation. | Pipeline/API observations; received-pilot effective-response checks and bounded partial/observer behavior. |
| TX-IFFT-01 | Admit complete upstream physical grids at 2K/50 kHz or 4K/25 kHz and 102.4 Msamples/s. | Shared accepted geometry and TX adapter; exact length, clock, identity and inactive-bin checks. |
| TX-IFFT-02 | Use the positive centered exponent and unitary scaling with ascending physical bins. | Shared safe Rust transform; independent complex-sum/tone/impulse and energy checks, not round trips alone. |
| TX-IFFT-03 | Emit one owned useful complex symbol with local timing before CP/window/overlap assembly. | Sample types and adapter; exact N/order/rate/validity, no invented global continuity or power calibration. |
| TX-IFFT-04 | Bound plans/scratch/output and share conventions with RX and passive instruments. | Rust numerical owner; atomic failure, completed-symbol retention, concurrency and future adapter parity cases. |
| TX-ASSEMBLY-01 | Admit exact upstream CP/RP sample choices with RP strictly below CP for scheduled data. | Shared configuration; independent Tables 9/10 cases, incompatible/stale geometry and unsupported-mode rejection. |
| TX-ASSEMBLY-02 | Apply exact cyclic extension, half-sample raised-cosine taper and overlap-add at N+CP cadence. | Focused Rust numerical owners; independent indexing/coefficient/adjacent-symbol cases including zero RP. |
| TX-ASSEMBLY-03 | Preserve absolute prefix/useful origins, isolated burst edges, final tail and explicit guard intervals. | Burst plan and assembly; checked lengths/ranges, no tail truncation or invented schedule padding, independent RX extraction. |
| TX-ASSEMBLY-04 | Emit identical samples across output chunks with bounded state and honest partial completion. | TX adapter/job; backpressure, transactional failure, drain/pause/cancel/reset and passive observation acceptance. |

The canonical [CM-US-TX block](../../../architecture.md#cm-us-tx-block-architecture)
owns the overview and
[TX-01 section](../../../architecture.md#tx-01-grant-framing-and-fec-selection)
owns grant planning. The [TX-02 section](../../../architecture.md#tx-02-ldpc-encoding-and-shortening)
owns encoding, shortening and ordered grant assembly. The existing codec stays independent of
source, grant resources, modulation and waveform processing. All eight stage
sections now have detailed contracts; no scientific modules are created by
architecture completion.
The [TX-03 section](../../../architecture.md#tx-03-grant-seeded-phy-randomization)
owns grant-seeded bit randomization and the paired RX soft inverse. Its primitive
belongs in the proposed Rust PHY bit-processing owner, independently of the codec.
Each stage section now includes a repository-relative path table with explicit
planned creation versus existing reuse. The [directory overview](../../../architecture.md#planned-code-layout)
defines module roots. TX-01 maps to shared resource/grant planning and
`crates/phy/src/transmitter/framing.rs`; TX-02 adds
`crates/phy/src/transmitter/ldpc.rs` around the existing codec; TX-03 uses
`crates/phy/src/bit_processing/randomizer.rs` with separate transmitter/receiver
adapters. All eight stages have proposed file locations. Test filenames are
recorded beside each owner in the canonical
section rather than creating empty modules or duplicate algorithms.
The [TX-04 section](../../../architecture.md#tx-04-cell-word-construction-and-qam-mapping)
defines exact label/role/scaling contracts and stateful word assembly. It adds
planned `crates/phy/src/configuration/modulation.rs`,
`crates/phy/src/signal_processing/qam_tables.rs` and
`crates/phy/tests/tx_mapping.rs` alongside the existing planned lookup/adapter
paths. Shared `resources/permutation.rs` supplies the visit sequence; its detailed
implementation follows the shared ARCH-TX-05 contract. These eight stage designs do
not establish a running grant-integrated transmitter.
The [TX-05 section](../../../architecture.md#tx-05-pilots-ofdma-framing-and-interleaving)
owns shared resource roles, block partitioning, joint visits, pilot expectations
and physical grid assembly. New planned leaves are
`crates/phy/src/resources/pilot_patterns.rs`,
`crates/phy/src/resources/pilots.rs`,
`crates/phy/src/resources/interleaving_blocks.rs` and
`crates/phy/src/bit_processing/pilot_sequence.rs`; focused tests are
`crates/phy/tests/upstream_interleaving.rs` and
`crates/phy/tests/upstream_pilots.rs`, alongside the existing planned framer/grid
tests. RX reuses the pure plan/expectations with its own processing state. This
design does not implement masks, sequence vectors, address generation or adapters.
The [TX-06 section](../../../architecture.md#tx-06-cm-pre-eq) owns the accepted
corrective bank and its application after role scaling. It adds planned
`crates/phy/src/configuration/pre_eq.rs`,
`crates/phy/src/signal_processing/pre_eq.rs` and
`crates/phy/tests/tx_pre_eq.rs` beside the already planned transmitter adapter,
grid/types and primitive acceptance tests. Normalization is bank admission,
not a per-symbol/active-mask adjustment. Defaults are unity on used/unused
non-excluded carriers and zero on excluded carriers. Single-shot freezes one
bank; planned [US-Pre-EQ input](../../../architecture.md#us-pre-eq-input) also
defines multiple-bank/update replay with an immutable schedule and explicit
probe bases. TX-06 applies each selected complete bank at its declared symbol
boundary. Live probe-driven updates and format support remain deferred; all
import/replay implementation is pending. See the
[input design](../upstream-inputs/design.md) for acceptance and evidence gaps.
The [TX-07 section](../../../architecture.md#tx-07-ifft) defines full upstream
geometry, the centered unitary transform and useful-symbol sample metadata.
The planned shared `crates/phy/src/signal_processing/transform.rs` owns safe Rust
radix-2 arithmetic and paired synthesis/analysis conventions. It reuses the
reviewed numerical organization with upstream parameters; no new FFT dependency
or copied implementation is introduced. Planned `transmitter/ifft.rs` and
`receiver/fft.rs` admit their own inputs, while `types/samples.rs` and
`configuration/profile.rs` remain shared owners. `crates/phy/tests/tx_ifft.rs`
adds stage checks beside `crates/phy/tests/transforms.rs`. No useful symbols
are silently concatenated into a final time stream; TX-08 owns assembly.
The [TX-08 section](../../../architecture.md#tx-08-sample-assembly) defines
upstream CP/RP admission, cyclic copies, the half-sample transmit taper,
overlap-add, indexed useful/prefix references, burst tail and optional simulation
silence. New planned shared owners are
`crates/phy/src/configuration/waveform.rs`,
`crates/phy/src/signal_processing/cyclic_extension.rs`,
`crates/phy/src/signal_processing/transmit_window.rs` and
`crates/phy/src/signal_processing/overlap_add.rs`; their responsibilities are
separate from `crates/phy/src/transmitter/assembly.rs` admission/output cursors.
The geometry owner is also named in the configuration and TX-07 sections so
profile validation and waveform adapters do not invent competing definitions.
`crates/phy/tests/transmit_window.rs` adds independent primitive checks beside
`crates/phy/tests/burst_assembly.rs`. All ten TX-08 code/test paths are planned
creations. No empty files, new Cargo member or Python calculations are added.

## Reference and source boundaries

Read-only reference review uses the staged-workbench/owned-boundary organization
from MERLIN revision `096d5a476194d4f2e016863d723b225257bb6037`. All behavior needed
for this block is written locally. No source code, downstream BCH/NCP/PLC chain,
fixed downstream geometry or presentation assets are imported.

Controlling upstream evidence is CM-SP-PHYv3.1-I20-230419 §7.4.1.1–3, PDF p50;
§7.4.3–7.4.3.1.1, pp52–56; §7.4.3.3, p58; §8.2.1–3, p172. Original PDF
pp53–55 were rendered and inspected for selection constants, the fixed 420-bit
borrowing step, minimum-grant guidance and information-fill requirements.
Remaining cited prose was reviewed in the pinned extraction. Appendix IV's
reverse calculation is informative and is not the controlling forward selector.
Real UCD/MAP/MAC framing requires separate MULPI evidence. FDD/FDX extensions are
not claimed by this initial scheduled-data contract.

TX-02 adds original-PDF review of §7.4.3.2–3, pp56–58: systematic information/
parity order, matrix dimensions/right-shift orientation, the known long-code
source discrepancy and append/encode/omit shortening. This review does not
complete the all-cell matrix audit. Existing local definitions, sparse encoder,
codec operations and shortening tests were inspected; no reference-project
implementation or new numerical code is introduced.

TX-03 adds original-PDF review of §7.4.4, Figure 7, p58. The seed LSB/MSB labels,
delays 18/23, feedback direction, reset boundary and pre-clock first mask were
checked visually. The numeric register expression and first-step cases in the
canonical section are local engineering transcriptions, not externally supplied
vectors. Original PDF p50, Figure 6 was also rendered and visually checked
for scrambled FEC codewords and scrambled minislot padding; the pinned extraction
provides the associated §7.4.1.2–3 ordering/coverage prose. Real UCD seed-field constraints remain separate
MULPI evidence; raw 23-bit primitive behavior is not a wire-conformance claim.
Read-only reference inspection confirmed state/error handling and soft-inverse
patterns. Its downstream cell-based arithmetic/reset is unsuitable for this
upstream bit stream; no implementation is copied or linked.

TX-04 uses §7.4.5.1, p61 (shared address/loading inputs, extracted prose),
§7.4.6–7.4.7.2, pp64–65, Figure 13, §7.4.16, p102, and Annex A/A.1,
pp197–198, Figures 99–103, plus A.2, p206, Table 54. Original PDF
pp64–65/102/197–198/206 were rendered and visually inspected for roles,
MSB-first words, endpoint capability distinctions, low-order labels and scale
factors. Higher-order full-label audits remain implementation acceptance.
The [publisher's I20 edition](https://account.cablelabs.com/server/alfresco/4eb470eb-aca3-4e64-af88-773b8c594fbd)
identifies the same pinned document; local PDF review controls the design.
Read-only reference review covered checked lookup, immutable embedding,
provenance and independent-label/energy tests. Its downstream table set omits
8-QAM/32-QAM and includes 8192-QAM/16384-QAM, so it cannot be adopted wholesale
as the upstream capability set. No reference tables, source or third-party assets
are copied; future actual reuse requires its own attribution/compatibility review.

TX-05 uses §7.4.5–7.4.5.1, pp58–64, Figures 8–12; §7.4.15.3.3, p99,
Figure 35; §7.4.16–7.4.16.3, pp101–105, Figures 38–42; §7.4.16.6,
p106; and §8.2.1–8.2.3.11, pp172–175, Table 51/Figure 85. Original PDF
pp59–60/62–63/99/102–106/173/175 were rendered and visually reviewed for
partition/counter control flow, pilot taps/patterns, boosting and geometry/serial
order. Remaining cited prose was read in the pinned extraction. Appendix III
was read as informative context, not controlling normative behavior or imported C.
Full per-cell mask and independent address/sequence-vector audits remain scientific
acceptance prerequisites. Read-only reference inspection confirmed its downstream
bit interleaver and 13-bit pilot sequence cannot provide upstream algorithms;
only immutable physical-index/validation patterns inform this local design.

TX-06 uses §7.4.1.5–6, p51 (placement, extracted prose), and §7.4.17,
pp106–108. Original pp107–108 were rendered and visually reviewed for
defaults/exclusions, complex adjustment, signed update components, normalization,
reset triggers and probe/control boundaries. The p108 continuation is upstream
§7.4.17 text despite being carried in the extraction indexed under 7.5; review
stopped at the actual downstream heading. The calibrated CMTS performance
procedure is not acceptance for this bank/replay architecture. Wire field decoding
and normative command/probe scheduling require separate MULPI/probing evidence;
explicit synthetic symbol offsets are an engineering replay policy. Read-only reference
review supplied complex-response and receiver-estimation ownership patterns only;
its downstream H interpretation/inverse floor are not a CM transmit-bank contract.

TX-07 uses §7.3.2, Table 7, p48; §7.4.1.6, p51 (extracted placement prose);
and §7.4.9, pp65–66, Figure 15. Original PDF pp48, 65 and 66 were rendered
and visually inspected for 2K/4K geometry, 102.4 Msamples/s, positive centered
exponent, unitary scaling and lowest-to-highest physical bin order. The
[publisher's pinned PHY I20](https://account.cablelabs.com/server/alfresco/4eb470eb-aca3-4e64-af88-773b8c594fbd)
was also checked for revision/section identity. Read-only reference inspection
covered the safe Rust radix-2 plan, forward/inverse wrappers and sample-rate
ownership. Fixed downstream 4K/8K geometry is unsuitable here. Mathematical
equivalence of the centering methods and useful-window timing/retention policies
are local engineering contracts, not additional CM RF requirements. Source
inspection does not execute the planned kernel, stage or receiver.

TX-08 uses §7.4.1.7, p51 (extracted placement prose), §7.4.10–7.4.10.2.1,
pp67–70, Tables 9/10 and Figures 17/18, plus §7.4.11–7.4.11.1, pp70–71,
Figure 19. Original pp67–71 were rendered and visually reviewed for every CP/RP
count, scheduled-data RP<CP, exact extension, half-sample window equation,
overlap/cadence and prefix/useful timing references. R=0 is an upstream table
choice; the reference project's downstream evaluation-only qualification is
rejected. The publisher's I20 revision/section identity was also checked.
Read-only reference review covered pure prefix insertion, immutable window
coefficients, retained-tail/drain/reset and fixed downstream geometry. Numerical
organization is an adaptation candidate; no implementation or source checkout
link is copied. Isolated-burst support, optional simulation guards, transactional
draining and cancellation policies are local contracts. They do not establish
real MAC scheduling, RF spectral compliance, receiver acquisition or echo immunity.

## Dependency-ordered checklist

- [x] ARCH-TX-NAV: Link all eight TX overview/output labels to unique local
  sections with overview backlinks; all eight now have detailed architecture.
- [x] ARCH-TX-PATH: Name planned implementation/test files in every TX section
  and distinguish existing codec reuse from new PHY adapters.
- [x] ARCH-TX-00: Standardize CM-US-TX and document the ordered internal stages.
- [x] ARCH-TX-01: Define grant capacity, selection, framing/bit roles, admission,
  inspection and independent acceptance checks.
- [x] ARCH-RANGING-00: Reserve [future burst modes and preambles](../../../architecture.md#deferred-burst-modes-and-preambles)
  with explicit unsupported-mode dispatch and matching RX requirements.
- [x] ARCH-TX-02: Define upstream LDPC encoding/shortening, transmitted ordering,
  reuse boundaries, bounded assembly, inspection and independent validation.
- [x] ARCH-TX-03: Define grant-seeded PHY randomization, precise register/first-bit
  behavior, bit coverage, bounded state, inspection and independent soft inverse.
- [x] ARCH-TX-04: Define cell-word construction, exact label/scale/role contracts,
  shared visit-order dependency, bounded mapping and independent acceptance.
- [x] ARCH-TX-05: Define resource roles/geometry, exact block/counter conventions,
  independent pilots/gains, grid assembly, shared ownership and acceptance checks.
- [x] ARCH-TX-06: Define Pre-Eq bank normalization, multiplication, defaults,
  update/reset identities, truth boundaries, streaming and independent acceptance.
- [x] ARCH-TX-07: Define IFFT geometry, centered/unitary conventions, useful-sample
  timing, bounded shared ownership, planned file paths and independent acceptance.
- [x] ARCH-TX-08: Define CP/RP admission, exact extension/taper/overlap,
  burst timing/edges/tail/guards, bounded output cursors and independent acceptance.
- [ ] PHY-01: Implement and validate the shared grant planner after scientific
  plan approval; verify exact boundaries, borrowing and bit-role conservation.
- [ ] WAVE-TX-01: Integrate all accepted stages into one verified upstream burst
  after codec/source/resource prerequisites are complete.
- [ ] ARCH-RANGING-01: Expand mode-specific ranging/preamble and probing TX/RX
  architecture after the scheduled-data unity closed loop; implementation follows
  separate acceptance criteria and authorization.

The PRBS block supplies only meaningful source bits; information byte residue,
coding fill, omitted shortening and grant padding do not consume that source.
Grant planning does not fix the documented LDPC matrix transcription finding.
Keep architecture completion separate from scientific implementation acceptance.

## Validation scope

Checks cover local links/anchors, stage-order/label consistency, self-contained
design records and whitespace. Source inspection substantiates the plan;
no transmitter execution, Python parity or native UI behavior is claimed.

`python3 tools/validation/check.py` passed 20 skills and 260 local links.
Focused checks confirmed the CM-US-TX label, local section anchors, all eight
overview stages and the absence of external/workstation links in the new block
and feature design. `git diff --check` passed. `scripts/validate.sh` passed
23 existing Rust, 19 setup and 5 Git tests, formatting and Clippy. Those results
validate the existing checkpoint; the planned transmitter stages are unimplemented.

The subsequent preamble-placeholder update is documentation only. Its acceptance
is explicit scheduled-data versus ranging/probing ownership, no unsupported-mode
fallback and accurate pending status; it introduces no acquisition implementation.

For TX-02, `python3 tools/validation/check.py` passed 20 skills and 265 local
links. Focused checks resolved its section anchors, confirmed the self-contained
contract and kept LDPC-01/02 implementation/source acceptance unchecked.
`git diff --check` and `scripts/validate.sh` passed, including the existing
23 Rust, 19 setup and 5 Git tests, formatting and Clippy. This is checkpoint
regression evidence; grant-integrated TX-02 and future adapter parity remain
unimplemented, and the known matrix-source discrepancy remains unresolved.

For TX-03 and navigation, `scripts/validate.sh` passed 20 skills, 269 local
links, 23 existing Rust tests, 19 setup tests and 5 Git tests, formatting and
Clippy. Focused checks resolved 46 local section targets in changed Markdown,
including all 16 TX overview/output labels to eight unique stage sections.
TX-04..08 remain five explicitly pending placeholders. The new TX sections have
no external-checkout links. The development-workflow skill metadata check and
PDE adoption hashes passed; the shared procedure/template match their scoped
source inputs. This is documentation/checkpoint validation, not executed PHY
randomizer, transmitter or receiver acceptance.

For TX-04, `scripts/validate.sh` passed 20 skills, 281 local links, the existing
23 Rust tests, 19 setup tests and 5 Git tests, formatting and Clippy. Focused
documentation checks resolved 49 section links in changed files, retained all
16 TX overview/output links and confirmed that TX-04's eight planned code/test
paths remain absent. TX-05..08 remain placeholders; LDPC-01/02, grant integration
and waveform implementation acceptance remain unchecked. `git diff --check`
passed. PDF visual review supports the documented low-order anchors/scaling and
role/bit-order contracts; it does not complete the higher-order full-label audit
or execute the proposed mapper, streaming adapter, Python bindings or QAM UI.

For TX-05, `scripts/validate.sh` passed 20 skills, 284 local links, the existing
23 Rust tests, 19 setup tests and 5 Git tests, formatting and Clippy. Focused
documentation checks resolved 52 section links, retained all 16 TX overview/output
links and confirmed that the stage's 12 planned code/test paths remain absent.
TX-06..08 remain placeholders and LDPC-01/02, grant integration and waveform
implementation milestones remain unchecked. `git diff --check` passed. The source
figure review substantiates the architecture; mask/address/sequence execution,
pilot-boost runtime behavior, Python parity and native instruments remain
unimplemented and are not established by the existing checkpoint tests.

For TX-06, `scripts/validate.sh` passed 20 skills, 287 local links, the existing
23 Rust tests, 19 setup tests and 5 Git tests, formatting and Clippy. Focused
documentation checks resolved 56 section links, retained all 16 TX overview/output
links and confirmed that the seven planned code/test paths remain absent.
TX-07/08 remain placeholders, and LDPC-01/02, grant integration and waveform
implementation acceptance remain unchecked. `git diff --check` passed. Original
PDF review includes the upstream continuation on p108; no coefficient normalizer,
complex-grid stage, live update/probe controller, capture adapter or Python/UI
behavior was implemented or validated by executing this documentation change.

For TX-07, `scripts/validate.sh` passed 20 skills, 290 local links, the existing
23 Rust tests, 19 setup tests and 5 Git tests, formatting and Clippy. Focused
documentation checks resolved 61 section links, retained all 16 TX overview/output
links and confirmed that the seven planned code/test paths remain absent.
TX-08 remains a placeholder; LDPC-01/02, grant integration and waveform
implementation acceptance remain unchecked. `git diff --check` passed. Original
PDF review substantiates geometry and transform conventions; no IFFT kernel,
sample adapter, receiver transform, Python binding or SA execution was added.
These results validate the existing checkpoint and documentation, not the
planned numerical vectors or useful-symbol processing.

For TX-08, `scripts/validate.sh` passed 20 skills, 293 local links, the existing
23 Rust tests, 19 setup tests and 5 Git tests, formatting and Clippy. Focused
documentation checks resolved 66 section links, retained all 16 TX overview/output
labels and confirmed that the ten TX-08 code/test paths remain absent. All eight
stage designs are checked; LDPC-01/02, grant integration and waveform execution
remain unchecked. `git diff --check` passed. Shared geometry is named in both
the earlier configuration/TX-07 sections and TX-08. Original PDF pp67–71 were
reviewed; no extension/window/overlap implementation, sample emission, RX
extraction or Python/SA runtime was executed. Results cover the local checkpoint
and documentation, not the planned waveform acceptance cases. Gate elapsed time
was not measured separately; hosted/platform and external evidence remain absent.
