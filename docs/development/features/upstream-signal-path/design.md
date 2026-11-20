# Upstream signal path and shared instruments

Status: architecture defined; processing/instrument implementation remains planned.
Task: ARCH-01. This request authorizes documentation, not scientific or Qt code.

## Requirements

- Show PRBS → CM-US-TX → Channel Simulator → CMTS-RX → independent PRBS check.
- Name ordered TX/RX stages and their state/data boundaries.
- Keep the first channel a genuine unity pass-through; reserve impairment extension points.
- Specify the same shared QAM Analyzer and Spectrum Analyzer interaction model
  as the reference workbench, with upstream metadata and clear reference planes.
- Preserve upstream normative processing and distinguish planned support from the
  existing standalone FEC checkpoint.

## Architecture and source decisions

The canonical design is the new
[staged signal path section](../../../architecture.md#planned-upstream-signal-path-and-workbenches).
Use its stage/tap tables rather than maintaining a competing processing diagram.
Own PRBS generation, configuration, TX/channel/RX, instruments and orchestration
in Rust; adapters present snapshots. A future neutral shared numerical crate is
a candidate, not an approved migration of another repository.

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
- [ ] Implement and validate these processing/instrument contracts after approval.

Documentation validation checks local links, stage/diagram consistency and Git
whitespace. No Rust/Qt changes or builds are needed for this architecture update.
`python3 tools/validation/check.py` passed 20 skill/resource checks and 237 local
documentation links; `git diff --check` passed. Source/diagram review confirmed
the post-FEC randomizer position, upstream-only resource roles, unity channel
reference planes and separation of receiver recovery from source comparison.
