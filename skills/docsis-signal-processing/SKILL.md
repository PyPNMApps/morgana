---
name: docsis-signal-processing
description: Implement or review upstream DOCSIS FEC and OFDMA signal processing against pinned PHY evidence using Rust algorithms and explicit support states.
---

# Upstream scientific ownership

Read [architecture](../../docs/architecture.md), the
[official checklist](../../docs/development/checklist.md) and the applicable
versioned PHY skill. Follow [scientific-testing](../scientific-testing/SKILL.md)
and [public-api](../public-api/SKILL.md). Follow the current authorization in
AGENTS.md and the accepted checklist order. Completed isolated-codec acceptance
does not complete waveform integration or authorize Git/publication operations.

1. Identify the exact upstream endpoint, code/profile, FDD/FDX applicability,
   revision, section and PDF table. Verify matrices and layout-sensitive values
   against the supplied PDF; missing evidence is a gap, not permission to guess.
2. Locate the existing Rust owner and design the smallest directly testable stage.
   Keep all FEC, modulation, channel, estimation and orchestration algorithms in
   Rust, including dependencies. Core crates forbid unsafe code; no native DSP
   FFI, Python calculations or presentation-owned numerical operations.
3. Preserve systematic information/parity order, right-shifted QC blocks,
   shortening positions, LLR signs/scaling and bounded iterations. Normal upstream
   data does not inherit a downstream BCH stage or ranging puncturing. Matching
   N/K does not make upstream/downstream matrices interchangeable.
4. For future waveforms verify the exact upstream randomization, joint
   interleaving, cell loading, pilot/preamble, IFFT/prefix/window and resource
   order before connecting stages. IUC alone does not prescribe a QAM order.
5. Keep injected H and Pre-Eq C outside receiver inputs. Receiver pilot estimates
   observe effective C×H. Ideal supplied-truth correction must be an explicit
   reference mode. Estimate error/source comparison occur in independent observers.
6. Preserve original capture bytes/grids/nulls/hashes/timestamps. Measured Pre-Eq
   is a corrective transmitter response. Inferred inverse-channel models need
   regularization, gain/delay assumptions and no claim about CMTS receive noise.

Example: test one encoded mother word through finite positive-for-zero LLRs,
then compare actual decoded information against the original. Report convergence,
syndrome, known-zero consistency and bit errors separately. A converged wrong
codeword is a valid failure of source recovery. Avoid double-counting distortion
and noise at different reference planes.

Acceptance requires source-table checks and bounded repeatable closed-loop
evidence for the declared stage. Recognized orders, analytical screening, measured
observations and actual decoder support remain distinct; unsupported cases return
typed errors rather than fallback behavior. No generic coding experiment proves
a DOCSIS receiver or external interoperability.
