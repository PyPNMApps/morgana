# CM-US-TX block and stage design

Status: transmitter overview and TX-01 architecture defined; implementation is
planned. Subsequent stages are expanded one at a time in processing order.
Scope is documentation in this repository, with no links to another source
checkout and no scientific, UI, CLI or binding implementation changes.

## Requirements and ownership

| ID | Requirement | Owner / acceptance |
| --- | --- | --- |
| TX-ARCH-01 | Use CM-US-TX consistently and describe its eight internal stages. | Canonical architecture, README and development records; one ordered TX path. |
| TX-ARCH-02 | Distinguish bit, complex-cell/frequency-grid and time-sample boundaries. | Rust stage contracts; meaningful bit/QAM/SA instrumentation with bounded passive observations. |
| TX-PLAN-01 | Derive coded capacity from accepted grant resources/loading, then choose the exact upstream codeword sequence. | Shared resource owner and Rust grant planner; independent capacity/threshold/order/borrowing cases. |
| TX-PLAN-02 | Separate meaningful bytes, information-fill ones, shortening zeros, parity and zero grant padding. | Framing/codec boundary; conservation, byte-residue and source-consumption checks. |
| TX-PLAN-03 | Plan without source mutation and admit bounded work transactionally. | Orchestration; rejected inputs preserve accepted state and source, no unbounded grant history. |
| TX-PLAN-04 | Let RX derive the same layout from accepted configuration without transmitter truth. | Shared pure planner called independently by endpoints; no original bits/seed/source ledger in RX recovery. |
| TX-PLAN-05 | Keep validation/results shared by Rust and future Python/UI consumers. | Public facade and thin adapters; typed errors/owned results and versioned export changes. |

The canonical [CM-US-TX block](../../../architecture.md#cm-us-tx-block-architecture)
owns the overview and
[TX-01 section](../../../architecture.md#tx-01-grant-framing-and-fec-selection)
owns the detailed first-stage contract. The existing codec stays independent of
source, grant resources, modulation and waveform processing. Further stage
sections will define their detailed contracts rather than creating empty modules.

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

## Dependency-ordered checklist

- [x] ARCH-TX-00: Standardize CM-US-TX and document the ordered internal stages.
- [x] ARCH-TX-01: Define grant capacity, selection, framing/bit roles, admission,
  inspection and independent acceptance checks.
- [ ] ARCH-TX-02: Expand upstream LDPC encoding and shortening.
- [ ] ARCH-TX-03: Expand grant-seeded PHY randomization.
- [ ] ARCH-TX-04: Expand cell-word construction and QAM mapping.
- [ ] ARCH-TX-05: Expand pilots, grant resource mapping and joint interleaving.
- [ ] ARCH-TX-06: Expand CM Pre-Eq and its reference plane.
- [ ] ARCH-TX-07: Expand IFFT geometry, bin order and normalization.
- [ ] ARCH-TX-08: Expand CP, roll-off/window/overlap and burst sample assembly.
- [ ] PHY-01: Implement and validate the shared grant planner after scientific
  plan approval; verify exact boundaries, borrowing and bit-role conservation.
- [ ] WAVE-TX-01: Integrate all accepted stages into one verified upstream burst
  after codec/source/resource prerequisites are complete.

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
