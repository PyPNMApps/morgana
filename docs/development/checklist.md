# Official implementation checklist

Current authorization: preserve this checkpoint, adopt local guidance/tooling and
implement development setup; further scientific implementation awaits plan approval.
See [architecture](../architecture.md) and [foundation design](features/foundation/design.md).

- [x] FOUNDATION-01: Inspect PDE and record selective adoption decisions.
- [x] FOUNDATION-02: Inspect MERLIN and document reusable/upstream-specific owners.
- [x] ARCH-01: Define PRBS → CM-US-TX → unity Channel Simulator → CMTS-US-RX,
  ordered processing stages and shared QAM/SA observation contracts. This is
  documentation only; see [design](features/upstream-signal-path/design.md).
- [x] ARCH-PRBS-01: Define the self-contained PRBS-TX/PRBS-RX block, sequence,
  interfaces, lifecycle, readiness and independent comparison contracts;
  see [PRBS design](features/prbs-source/design.md). Implementation stays planned.
- [x] ARCH-TX-00: Define the CM-US-TX block, eight internal stages and typed
  observation boundaries; see [transmitter design](features/cm-us-tx/design.md).
- [x] ARCH-TX-NAV: Link all TX overview/output labels to local stage sections,
  retain pending placeholder status and adopt the generic rule in local/PDE
  development-workflow skills and architecture templates.
- [x] ARCH-PATH-01: Backfill each signal-path block/stage with planned code/test
  filenames, explicit create/reuse/extend status and shared ownership; adopt the
  rule in local/PDE skills and templates. See [layout design](features/code-layout/design.md).
- [x] ARCH-TX-01: Expand grant framing/FEC selection, source/fill/shortening/pad
  accounting, bounded admission and stage acceptance. Documentation only.
- [x] ARCH-TX-02: Define LDPC encoding/shortening, exact transmitted bit order,
  grant assembly, codec ownership, inspection and source-validation boundaries;
  see [TX-02](../architecture.md#tx-02-ldpc-encoding-and-shortening). Architecture only.
- [x] ARCH-TX-03: Define the 23-bit grant randomizer, register/first-bit convention,
  bit coverage, state validation and independent RX soft inverse;
  see [TX-03](../architecture.md#tx-03-grant-seeded-phy-randomization). Architecture only.
- [x] ARCH-TX-04: Define MSB-first cell words, exact upstream constellation/role
  loading, reference scaling, bounded mapping, QAM inspection and code/test paths;
  see [TX-04](../architecture.md#tx-04-cell-word-construction-and-qam-mapping). Architecture only.
- [x] ARCH-TX-05: Define shared pilot/resource roles, block partitioning, joint
  address generation, physical-bin pilots/boosting, bounded grid assembly and
  code/test paths; see [TX-05](../architecture.md#tx-05-pilots-ofdma-framing-and-interleaving).
  Architecture only; exact masks/vectors and executable acceptance remain planned.
- [x] ARCH-TX-06: Define coefficient/reference planes, defaults/exclusions,
  normalization, update/reset boundaries, bounded application and code/test paths;
  see [TX-06](../architecture.md#tx-06-cm-pre-eq). Architecture only; no adaptive loop.
- [x] ARCH-TX-07: Define upstream IFFT geometry, centered bin order/unitary scaling,
  useful-sample timing, shared transform ownership, bounds and code/test paths;
  see [TX-07](../architecture.md#tx-07-ifft). Architecture only; no waveform execution.
- [x] ARCH-TX-08: Define upstream CP/RP, extension/taper/overlap, prefix/useful
  origins, tail/guards, bounded chunk emission and planned code/test paths;
  see [TX-08](../architecture.md#tx-08-sample-assembly). Architecture only.
- [x] ARCH-CH-00: Stage the Channel Simulator with six linked sections, support
  states and planned files; keep a compact block/configuration/PNM contents list.
  See [channel design](features/channel-simulator/design.md).
- [x] ARCH-CH-01/02/06: Define sample admission, exact unity transport, output
  observations and bounded lifecycle. Architecture only; no channel execution.
- [x] ARCH-RXMER-01: Add the separate upstream RxMER input, original provenance,
  exact association, power selection/playback and model/metric boundaries;
  see [RxMER input](../architecture.md#rxmer-input). Implementation remains planned.
- [x] ARCH-US-CONFIG-01: Define US Configuration input, retained profile inventory,
  selection, shared TX/RX admission and code/test paths; architecture only.
- [x] ARCH-PNM-02: Define single-shot/multi-input RxMER and US-Pre-EQ,
  bounded bank/update replay, explicit bases/events and joint-model compatibility;
  see [input design](features/upstream-inputs/design.md). Implementation planned.
- [x] ARCH-USJSON-01: Record generic OFDMA JSON as the CMTS configuration
  subsection of CMTS-US-RX; define shared TX/RX projections, support states,
  version/coverage plan, planned paths and flows.
  See [JSON design](features/us-configuration-json/design.md). Architecture only.
- [ ] USJSON-COVERAGE-01: Complete all applicable pinned MULPI OFDMA fields,
  values/conditional rules and independent fixture mappings;
  [source-area inventory](features/us-configuration-json/coverage.md) is not full coverage.
- [ ] USJSON-FORMAT/PRESETS-01: Finalize/create the versioned configuration
  schema, generic JSON presets and usage guide after field-coverage review.
- [ ] USJSON-CORE/PROJECTION/PARITY-01: Implement shared Rust JSON admission and
  CMTS TX/RX views; validate atomicity, bounds, round trips and future bindings.
- [ ] US-CONFIG-01: Implement shared configuration/profile admission and inventory.
- [ ] US-CONFIG-FORMAT-01: Verify upstream configuration/profile capture formats
  against pinned source evidence and fixtures before exposing import support.
- [ ] PREEQ-FORMAT-01: Verify upstream bank/update formats, scales and control
  semantics with pinned OSSI/MULPI evidence and lawful fixtures.
- [ ] PREEQ-INPUT-01: Implement typed banks/updates, provenance-preserving import
  and bounded preflight/replay after the reference waveform prerequisites.
- [x] ARCH-CH-03: Define causal complex FIR, original tap/path reference,
  bounded history/work, exact tail and independent acceptance; architecture only.
- [x] ARCH-CH-04: Define sample AWGN and restricted unity-C/H RxMER synthesis,
  reference/pilot power, seeded draw order and independent acceptance; architecture only.
- [x] ARCH-CH-05: Define integer delay and constant phase/CFO, emitted-clock
  state, length/drain rules and independent acceptance; architecture only.
- [x] ARCH-RX-00: Define CMTS-US-RX block inputs/results, nine-stage processing
  chart, lifecycle and inspection overview; see [receiver design](features/cmts-us-rx/design.md).
- [x] ARCH-RX-NAV/PATH: Link all RX overview/output labels to stage sections,
  with backlinks, planned code/test paths and explicit existing codec reuse.
- [x] ARCH-RX-01: Expand burst framing/timing and bounded indexed-sample admission.
- [x] ARCH-RX-02: Expand useful-window selection, CP/overlap and validity.
- [x] ARCH-RX-03: Expand forward transform admission, metadata and independent vectors.
- [x] ARCH-RX-04: Expand pilot estimate/correction, coverage, reliability and nulls.
- [x] ARCH-RX-05: Expand exact resource extraction and inverse joint visits.
- [x] ARCH-RX-06: Expand MSB-first LLR metrics, labels/scales and confidence policy.
- [x] ARCH-RX-07: Expand soft grant mask reversal, word ordering and pad separation.
- [x] ARCH-RX-08: Expand shortening/codec integration and separate decode outcomes.
- [x] ARCH-RX-09: Expand receiver-known deframing and partial information results.
- [ ] RX-EXT-01: Design received-signal acquisition/clock recovery, fast response
  tracking, calibrated noise confidence and finite-file framing before claiming
  support; initial RX-01..09 architecture is complete only for its declared scope.
- [ ] CH-EXT-02: Detail captured-H reconstruction, fractional timing/clock error,
  stochastic phase noise and broader RxMER/response/Pre-EQ-update composition
  before support.
- [ ] RXMER-FORMAT-01: Verify upstream format/type/units/null handling and lawful
  fixtures before claiming a binary/decoded capture adapter.
- [x] ARCH-RANGING-00: Reserve explicit future ranging/preamble and probing modes;
  see [placeholder](../architecture.md#deferred-burst-modes-and-preambles).
- [x] SETUP-01..03: Adopt generic installer guidance and implement/test explicit
  development setup. Nineteen setup tests and Ubuntu 22.04 read-only modes pass;
  see [design/checklist](features/development-setup/design.md).
- [ ] SETUP-04: Validate actual fresh-machine provisioning on declared targets.
- [ ] FOUNDATION-03: Complete independent workspace foundation. Rust workspace,
  lock, local skills/instructions, notices and save tooling exist; hosted CI,
  release preparation, public API/user guides and full distribution review remain.
- [ ] LDPC-01: Verify all upstream matrix entries/order against pinned PHY tables.
  Long/medium/short implementations exist. Known pending issue: the long base
  matrix's fifth row, zero-based column 20, is currently -1; PDF p57 shows 12.
  Preserve this finding until scientific work is explicitly resumed; source
  correction and an independent regression are not part of the save-only task.
- [ ] LDPC-02: Complete validated standalone upstream LDPC milestone. Existing
  23 unit tests pass, including Gaussian-reference comparison, controlled/AWGN
  LLRs, nonconvergence and shortening. They share source table constants, so they
  do not resolve LDPC-01. External vectors are unavailable; no external claim.
- [ ] PHY-01: Implement and validate grant/codeword selection and US
  Configuration against [TX-01](../architecture.md#tx-01-grant-framing-and-fec-selection),
  including byte-residue ones, zero grant padding and shortened-codeword borrowing.
- [ ] SOURCE-01: Implement the explicit continuous PRBS15 source and independent
  verifier against the [PRBS block contract](../architecture.md#prbs-block-architecture),
  including upstream grant lengths, incomplete-recovery accounting and bounds.
- [ ] WAVE-TX-01: Implement one specification-verified upstream data burst.
- [ ] WAVE-CH-01: Implement the bounded exact unity channel stub and input/output
  sample observations; no impairments in the first full waveform path.
- [ ] WAVE-RX-01: Independently recover its original payload from received samples,
  initially with configured burst timing and received-pilot channel correction.
- [ ] INSTRUMENTS-01: Add shared Rust QAM/SA collectors and matched TX/channel/RX
  taps from the [signal path architecture](../architecture.md#planned-upstream-signal-path-and-workbenches).
- [ ] RXMER-INPUT-01: Implement typed Rust observations/association and shared
  power playback; import and future Python/UI adapters follow validated contracts.
- [ ] WAVE-CH-02: Add approved RxMER residual/response/controlled impairments and
  provenance-preserving measured Pre-Eq inputs after the unity closed loop passes.
- [ ] ARCH-RANGING-01: Detail initial/fine-ranging preambles, distinct probing
  waveforms and matching RX acquisition after the scheduled-data unity loop;
  keep these modes unsupported until implemented and validated.
- [x] ARCH-API-01: Review the reference high-level Rust/native Python structure;
  define a separate [API architecture](../architecture.md#high-level-rust-and-python-apis),
  paired design stubs, planned code/test/type-stub paths and local skill rules.
- [ ] API-RUST/INPUT-01: Implement approved shared Rust session/configuration,
  inventory, validated inputs and preview while preserving the existing FEC API.
- [ ] API-RUN-01: Expose bounded execution, owned reports, progress/cancellation
  and QAM/SA after source-verified waveform prerequisites.
- [ ] API-PY/STUB-01: Implement optional native Python dispatch plus matching
  `.pyi`/`py.typed`; keep core-only builds independent of binding dependencies.
- [ ] API-PARITY/DOCS-01: Validate real native Rust/Python parity, lifecycle,
  errors and ownership; deliver runnable paired examples and maintained guides.
- [ ] API-01: Complete all high-level Rust and native Python delivery gates in
  the [API feature checklist](features/public-api/design.md#dependency-ordered-checklist).

At each completion/commit-msg review, reconcile this checklist, architecture,
feature records and actual validation evidence. No item implies authorization to
publish, edit source repositories or run system installation.
