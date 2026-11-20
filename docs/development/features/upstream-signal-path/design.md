# Upstream signal path and shared instruments

Status: architecture defined; processing/instrument implementation remains planned.
Task: ARCH-01. This request authorizes documentation, not scientific or Qt code.

## Requirements

- Show PRBS → CM-US-TX → Channel Simulator → CMTS-US-RX → independent PRBS check.
- Name ordered TX/RX stages and their state/data boundaries.
- Keep the first channel a genuine unity pass-through; reserve impairment extension points.
- Add a separate optional upstream RxMER input for later channel residual models,
  preserving original observations and distinct input/derived/receiver results.
- Add US Configuration as a shared channel/profile/grant input to TX/RX.
- Group RxMER and US-Pre-EQ under PNM Files; define single-shot/multi-input
  selection and multiple explicit Pre-EQ updates into TX-06.
- Specify the same shared QAM Analyzer and Spectrum Analyzer interaction model
  as the reference workbench, with upstream metadata and clear reference planes.
- Preserve upstream normative processing and distinguish planned support from the
  existing standalone FEC checkpoint.

## Architecture and source decisions

The canonical design is the new
[staged signal path section](../../../architecture.md#planned-upstream-signal-path-and-workbenches).
Use its stage/tap tables rather than maintaining a competing processing diagram.
The [planned directory overview](../../../architecture.md#planned-code-layout)
and section-level file tables now locate configuration/source, all TX/RX stages,
unity channel, instruments, orchestration and future facade/adapter tests.
Existing files are identified as reuse/extension; proposed files remain absent.
Own PRBS generation, configuration, TX/channel/RX, instruments and orchestration
in Rust; adapters present snapshots. A future neutral shared numerical crate is
a candidate, not an approved migration of another repository.

The [Channel Simulator design](../channel-simulator/design.md) now expands that
boundary into six linked stages and a separate
[RxMER input](../../../architecture.md#rxmer-input). All six channel contracts
are defined for their declared initial modes; implementation remains planned.
RxMER input uses the reference selection/power-playback workflow
with upstream CMTS/user/probe semantics, not downstream DPD/file assumptions.
The first waveform milestone still requires exact unity without measurements.
The [input extension](../upstream-inputs/design.md) defines US Configuration,
single-shot/multi-input PNM selection and multiple Pre-EQ updates separately
from RxMER power playback. Configuration supplies legitimate common settings;
Pre-EQ feeds TX-06, and neither C nor model targets become normal RX truth.

The [CMTS-US-RX design](../cmts-us-rx/design.md) defines the receiver block,
chart, nine linked stage sections, output inspections and per-stage file paths.
RX-01..09 now have complete contracts for configured burst timing, exact useful
windows/FFT, frame-based received-pilot estimation, inverse visits, finite-confidence
MaxLog metrics, soft mask reversal, existing-codec adaptation and information
deframing. Receiver implementation and source-matrix acceptance remain pending.
Fast within-frame response tracking and calibrated received-noise confidence
remain explicit future policies; no hidden C/update/H truth repairs recovery.

Read-only reference inspection: MERLIN architecture, source/PRBS implementation,
waveform spectrum estimator and QAM/SA instrument adapters at revision
`096d5a476194d4f2e016863d723b225257bb6037`. Reuse its workbench organization,
bounded matched observations and normalized PSD conventions. Its downstream
4K/8K geometry, 204.8 MHz clock, PLC/NCP and coding chain are not upstream rules.

Controlling upstream evidence is CM-SP-PHYv3.1-I20-230419 §7.4.1, Figure 5,
PDF p50; §7.4.1.5–7, p51; §7.4.3–7, pp52–65; §7.4.9–10, pp65–69;
§7.4.16–17, pp101–107. Figure 5 and the accompanying p50 text were visually
checked in the original locally supplied PDF. Detailed table values/formulas
remain implementation-time PDF checks; the documented sample rate/FFT sizes
come from §7.4.9's explicit text. PHY4.0 I07 §7.2.4 and §7.3.4 delegation was
checked in the pinned extraction, not its original PDF.

## Acceptance and validation

- [x] Document the complete path and independently owned source comparison.
- [x] Define unity channel, future impairment interfaces and reference planes.
- [x] Define QAM/SA selectors, passive bounded taps and Rust calculation ownership.
- [x] Reconcile architecture/checklist/design links and planned/implemented status.
- [x] Backfill block/stage code and validation paths without completing future
  stage contracts or creating source placeholders.
- [ ] Implement and validate these processing/instrument contracts after approval.

Documentation validation checks local links, stage/diagram consistency and Git
whitespace. No Rust/Qt changes or builds are needed for this architecture update.
`python3 tools/validation/check.py` passed 20 skill/resource checks and 237 local
documentation links; `git diff --check` passed. Source/diagram review confirmed
the post-FEC randomizer position, upstream-only resource roles, unity channel
reference planes and separation of receiver recovery from source comparison.
