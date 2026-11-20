---
name: scientific-testing
description: Validate upstream LDPC and future OFDMA science using pinned normative checks, independent arithmetic and bounded Rust closed loops.
---

# Scientific validation

Use [numerical-testing](../numerical-testing/SKILL.md),
[build-validation](../build-validation/SKILL.md), the pinned PHY skills and the
[current validation record](../../docs/development/features/foundation/validation.md).

1. Identify the claimed behavior and expected-value source. Separate round trips,
   independently transcribed normative arithmetic, independent algorithm oracles
   and externally supplied reference vectors. State shared-data limitations.
2. Test each upstream code independently: matrix dimensions/cells/orientation,
   systematic encoding and syndrome, noiseless exact payload recovery,
   controlled LLR errors, deterministic AWGN-derived LLRs, actual iterations,
   bounded failure decisions and shortening boundaries. No ordinary data puncture
   or downstream BCH is implied. Exercise invalid lengths/bits/nonfinite values.
3. Verify zero-syndrome/convergence independently from original-bit comparison.
   Include a different valid codeword; it can converge and still recover wrong bits.
   Preserve failed decisions and completed trials when cancellation later exists.
4. For future transforms use independent impulse/DC/tone/direct-sum vectors,
   not only inverse round trips. Verify pilot positions, randomizer state, resource
   exclusions, cell labels, interleaving order and LLR scale against exact sources.
5. Receiver tests consume received samples/configuration, never hidden TX payload
   or injected channel. Keep simulator truth only for separate error measurements.
   Observation must not consume randomness or change scientific outcomes.

The minimum executable milestone is an isolated local upstream LDPC closed loop;
later waveform acceptance compares original → TX → channel → RX → recovered bits.
An external dataset is useful evidence when available; never invent external
compatibility from an internal loop or abandon source checks because tests pass.

For example, a Gaussian test derives real BPSK LLR=2y/sigma² with a documented
seed/variance, counts predecode sign errors, then checks recovered payload and
real iterations. Label this a codec test, not an OFDMA RxMER measurement.

Run `scripts/validate.sh`; keep independent cases discoverable and work bounded.
Retain doctests/examples and caches. Record exact command, elapsed time, platform,
case totals, failures, omissions and scientific evidence gaps. The current
Gaussian oracle shares production's transcribed matrix data; it cannot detect
an incorrect source-table cell. Keep that limitation and pending source findings
visible in the architecture/checklist even when the suite passes.
