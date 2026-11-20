# Channel Simulator stages and RxMER input

Status: all six channel stages and RxMER input have architecture for their
declared initial modes; scientific implementation and capture adapters remain planned.
Scope is architecture documentation extending the existing signal-path design.
Scientific implementation retains the existing approval boundary. All behavior
is described locally.

## Requirements

| ID | Requirement | Owner / acceptance |
| --- | --- | --- |
| CH-ARCH-01 | Show ordered channel stages, compact block/configuration/PNM contents links and planned code/test paths. | Canonical architecture; contents links resolve, six unique stage anchors and independently linked PNM inputs. |
| CH-UNITY-01 | Deliver exact TX samples and metadata with no impairments or random draws. | Unity owner; bit-identical finite I/Q, indices, burst/tail/guard validity and chunk invariance. |
| CH-STATE-01 | Bound buffers/work, admit atomically and retain completed output on pause/cancel/error. | Pipeline; backpressure, cursor/state retention, stale identity, gap and overflow cases. |
| CH-OBS-01 | Expose channel input/output to the shared SA without affecting transport. | Passive observations; matching unity sample ranges, retention limits and no invented gaps. |
| RXMER-IN-01 | Stage original RxMER inputs independently of starting/applying a channel model. | Rust observation/import owners; unchanged bytes, hashes, arrays, nulls, times and atomic Apply. |
| RXMER-IN-02 | Associate upstream probe RxMER with the exact CM/user, channel, physical grid and accepted run. | Admission; missing active readings, wrong direction/reference, mismatched identity/grid and time-tolerance rejection. |
| RXMER-IN-03 | Offer single, equal-capture power average, hold and power interpolation. | Pure Rust residual/playback owners; original epochs unchanged, explicit symbol schedule, no frequency resampling. |
| RXMER-IN-04 | Separate measured probe RxMER, model targets and simulated receiver/source outcomes. | Channel/metrics boundary; no target/H/C truth supplied to normal RX and no double-counted residual floor. |
| CH-EXT-01 | Define response, RxMER residual and timing/phase scopes with explicit support states. | Mode dispatcher; first implemented milestone unity only, unimplemented/unsupported selections reject instead of bypassing. |
| CH-RESPONSE-01 | Define bounded causal complex FIR with exact input clock, history and terminal drain. | Shared response owner; independent convolution/impulse/tone, deep-null, chunk and tail cases. |
| CH-RESIDUAL-01 | Separate sample-power AWGN from normalized RxMER-conditioned symbol noise. | Residual adapter/shared noise; explicit power reference, I/Q variance, compatible modes and pilot-boost expectations. |
| CH-RNG-01 | Freeze noise-only RNG/dependency/seed and canonical draw order. | Noise owner; retry, observer, schedule, pause and chunk invariance without sharing source state. |
| CH-TIMING-01 | Define bounded integer delay and positive complex phase/frequency rotation on emitted sample time. | Timing owner; exact counts, sign/origin, phase continuity, delay drain and unsupported fractional-clock rejection. |
| CH-COMPOSE-01 | Compose stage supports/drains transactionally and preserve normal RX independence. | Pipeline; compatibility matrix, bounded work quanta, explicit partial delivery and no truth-based receiver correction. |

## Canonical architecture and reuse review

See [Channel Simulator](../../../architecture.md#channel-simulator-unity-stub-first),
[stage sequence](../../../architecture.md#channel-stage-sequence) and
[RxMER input](../../../architecture.md#rxmer-input). Their path tables own code
placement; no new modules, Cargo dependencies, API/schema or UI are created now.
Requirements and implementation acceptance are separate from design completion.
The [stage index](../../../architecture.md#channel-stage-sequence) now links
complete contracts for admission, identity, FIR response, residuals, timing/phase
and output. The compatibility table specifies selected initial models; fractional
timing, phase-noise, captured-H reconstruction and arbitrary model combinations
remain explicit extensions rather than implied support.

Read-only reference review used MERLIN revision
`096d5a476194d4f2e016863d723b225257bb6037`. Reviewed patterns include original
measurement ownership, staged Apply, exact compatibility checks, immutable
measurement playback, linear residual-power combination and independent SA taps.
The source checkout remains unchanged and is not a documentation dependency.

| Reviewed contract / local owner | Decision and gap |
| --- | --- |
| Original observation/provenance → planned `crates/phy/src/measurements/rxmer.rs` | Adapt the ownership pattern; upstream CMTS/user and probe reference replace downstream capture/profile association. |
| Single/average/hold/interpolate → planned `crates/phy/src/channel/measurement_playback.rs` | Adapt pure power queries and separate synthetic schedule; retain original times and complete grids. |
| Residual conversion → planned `crates/phy/src/signal_processing/residual_power.rs` | One Rust numerical owner, shared by preview/planning; model combination is distinct from PHY conformance statistics. |
| Existing downstream importer → planned `crates/morgana/src/inputs/rxmer.rs` | Candidate organization only. Do not assume downstream binary type, DPD/PLC identity or sample scale is an upstream file format. |
| Measured symbol-diagonal synthesis → planned CH-04 | Adapt independent bounded noise synthesis using shared upstream IFFT/window/overlap. Initial RxMER mode requires unity C/H and disabled timing; arbitrary composition remains deferred. |
| Causal filter/history → planned CH-03 | Reuse the reviewed ownership pattern; choose direct bounded upstream convolution and original synthetic taps, without downstream fixed FFT geometry or inferred captured FIR. |
| Existing local ChaCha8/StandardNormal dependencies → planned noise owner | Reuse pinned Rust dependencies with a separate channel stream and explicit seed/draw contract; existing codec/source use does not validate the new noise path. |
| Supplied-H reference receiver path | Rejected for the normal upstream receiver; received pilots estimate effective C×H independently. |
| Qt capture viewer / application controls | Interaction reference only; no GPL presentation source or UI module is imported into the Apache core. |

The controlling upstream meaning comes from CM-SP-PHYv3.1-I20-230419 §9.4.8,
PDF p196: CMTS per-user probe RxMER uses equalized known BPSK error. The original
page was rendered and visually reviewed, including its separate performance-test
statistics context. The [publisher's pinned PHY I20](https://account.cablelabs.com/server/alfresco/4eb470eb-aca3-4e64-af88-773b8c594fbd)
was checked for revision/section identity. That section does not prescribe a
Gaussian data-burst impairment generator or upstream binary-file layout.
Capture format support needs pinned CCAP-OSSI/format evidence and fixtures.
The downstream PNM RxMER/FEC guide is not upstream decoder/threshold authority.
Current follow-up read-only review covered causal filter/drain, sample AWGN and
measurement-driven synthesis ownership at the same revision. FIR, Gaussian and
oscillator equations are engineering models, not new CableLabs requirements.
The current local dependency pins are rand 0.9.5, rand_chacha 0.9.0 and
rand_distr 0.5.1; no dependency or scientific source changes are made here.

## Dependency-ordered checklist

- [x] ARCH-CH-00: Define six linked channel stages, support states and file paths;
  keep compact contents for the four main blocks, US Configuration and PNM Files.
- [x] ARCH-CH-01: Define bounded input admission and identity/timeline validation.
- [x] ARCH-CH-02: Define exact unity transport without RNG or numerical rewriting.
- [x] ARCH-CH-06: Define output commit, observations and partial lifecycle.
- [x] ARCH-RXMER-01: Define upstream input/provenance, association, selection,
  power playback, readiness and model/receiver boundaries.
- [x] ARCH-CH-03: Define bounded causal FIR, response reference, zero history,
  exact drain, transactional work and independent acceptance.
- [x] ARCH-CH-04: Define sample AWGN versus unity-C/H RxMER synthesis, reference
  power/pilot treatment, pinned RNG/draw order, history and acceptance.
- [x] ARCH-CH-05: Define integer delay, phase/CFO sign and origin, emitted-clock
  state, drain, bounds and independent acceptance.
- [ ] CH-EXT-02: Detail captured-H reconstruction, fractional delay/sample-clock
  error, stochastic phase noise and broader measured/response composition before
  enabling those modes; they are outside the declared initial stage scope.
- [ ] RXMER-FORMAT-01: Verify an upstream binary/decoded format with pinned
  source/type/unit/scale/null semantics and lawful representative fixtures.
- [ ] WAVE-CH-01: Implement and validate unity transport after scientific approval
  and its sample/TX prerequisites; retain normal RX independence.
- [ ] RXMER-INPUT-01: Implement Rust typed observations/admission/playback first;
  versioned import and matching future Python consumers follow validated contracts.
- [ ] WAVE-CH-02: Implement approved response/residual models after the unity
  closed loop and their detailed architecture/source prerequisites.
- [ ] RXMER-UI-01: Implement the future input editor/viewer after the shared Rust
  operations exist; no scientific computation belongs in presentation.

All six initial channel stage contracts are defined. The CMTS-US-RX block
overview is now defined; its next detailed architecture stage is RX-01.
Implementation still awaits the existing approval and prerequisites. Importing existing probe
measurements does not implement probe generation, ranging or live device capture.

## Validation

Check section/file links, unique stage targets, planned-path absence, source
boundaries, staged/implemented status and whitespace. Run `scripts/validate.sh`
for existing-checkpoint regression evidence. New transport, import, playback,
RNG, waveform and adapter acceptance requires future executable tests; a passing
documentation gate does not establish those capabilities.

On Ubuntu 22.04.5 LTS, `scripts/validate.sh` passed in 2.62 seconds using the
pinned local Rust wrapper: 20 skill checks, 306 local links, 23 existing Rust
tests, 19 setup tests and 5 Git tests, formatting and Clippy. Follow-up checks
after the contents update resolved 98 section links, covered all ten level-2/3
major headings in the contents, retained six unique channel targets and all
16 TX overview/output labels. All proposed channel/input files remain absent;
response/residual/timing designs, capture-format and scientific milestones remain
unchecked. `git diff --check` passed. No new DSP, input adapter, playback engine,
GUI, Python wrapper or actual upstream probe/measurement execution was added.
These results validate documentation and the existing checkpoint only.

The all-stage architecture follow-up ran `scripts/validate.sh` on the same
Ubuntu 22.04.5 LTS checkout in 3.16 seconds: 20 skills, 307 local links,
23 existing Rust tests, 19 setup tests, 5 Git tests, formatting and Clippy passed.
Focused checks resolved 82 section links in the four changed documents, retained
the major-section contents and all six channel/16 TX stage links, and confirmed
30 unique proposed channel/input paths remain absent. All six stage sections
have architecture status; scientific execution, capture formats and the named
model extensions stay unchecked. `git diff --check` passed. No FIR, Gaussian
stream, RxMER synthesis, oscillator/delay, Python adapter or receiver runtime
acceptance was executed; the new equations/bounds/drain rules remain designs.

## Configuration and PNM input extension

The [input design](../upstream-inputs/design.md) adds explicit single-shot/multi-
input modes, US Configuration and US-Pre-EQ bank/update replay. RxMER remains
a residual-power input to CH-SIM; Pre-EQ feeds TX-06. Both inventories can be
retained together. Initial RxMER synthesis preflights every effective C in the
complete replay plan and rejects any nonunity bank before source consumption.
Unity CH-SIM passes the actual TX waveform, including accepted changing C.
The compact architecture contents uses four main block links, a US Configuration
link and PNM Files links for RxMER/US-Pre-EQ; detailed stage indexes stay local.
All new input/runtime/format work remains planned.
