# Development

- [Architecture](../architecture.md)
- [Planned code layout](../architecture.md#planned-code-layout) and
  [per-section layout design/checklist](features/code-layout/design.md)
- [Upstream signal path and QAM/SA architecture](../architecture.md#planned-upstream-signal-path-and-workbenches)
  and [ARCH-01 design](features/upstream-signal-path/design.md)
- [PRBS block architecture](../architecture.md#prbs-block-architecture)
  and [ARCH-PRBS-01 design/checklist](features/prbs-source/design.md)
- [CM-US-TX block architecture](../architecture.md#cm-us-tx-block-architecture),
  [TX-01 grant framing](../architecture.md#tx-01-grant-framing-and-fec-selection),
  [TX-02 LDPC encoding](../architecture.md#tx-02-ldpc-encoding-and-shortening),
  [TX-03 PHY randomization](../architecture.md#tx-03-grant-seeded-phy-randomization),
  [TX-04 cell-word/QAM mapping](../architecture.md#tx-04-cell-word-construction-and-qam-mapping),
  [TX-05 pilots/framing/interleaving](../architecture.md#tx-05-pilots-ofdma-framing-and-interleaving),
  [TX-06 CM Pre-Eq](../architecture.md#tx-06-cm-pre-eq),
  [TX-07 IFFT](../architecture.md#tx-07-ifft),
  [TX-08 sample assembly](../architecture.md#tx-08-sample-assembly)
  and [transmitter design/checklist](features/cm-us-tx/design.md)
- [Channel Simulator architecture](../architecture.md#channel-simulator-unity-stub-first),
  [channel stage sequence](../architecture.md#channel-stage-sequence),
  [RxMER input](../architecture.md#rxmer-input)
  and [channel design/checklist](features/channel-simulator/design.md)
- [Official checklist](checklist.md)
- [Foundation design and reuse/specification assessments](features/foundation/design.md)
- [Checkpoint validation](features/foundation/validation.md)
- [Foundation adoption and local overrides](foundation-adoption.md)
- [Build guide](build.md)
- [Development setup](setup.md) and [setup design/checklist](features/development-setup/design.md)
- [Git save](../git.md)
- [Skill catalog](../../skills/README.md)
- [Software facts](../sw-facts/README.md)

Private evidence, downloaded specifications and generated outputs belong under
ignored `docs/development/local/`. Plans and concise validation summaries are tracked.
