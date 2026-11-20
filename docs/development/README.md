# Development

- [Architecture](../architecture.md)
- [Accepted backend delivery decisions](../architecture.md#accepted-backend-delivery-decisions)
  and [milestone/validation record](features/backend-delivery/design.md)
- [Backend stage implementation and independent cases](features/backend-stages/design.md)
- [Upstream capture format/fixture verification](features/capture-formats/design.md)
  and [UCD inspection acceptance](features/capture-formats/validation.md)
- [CCAP RxMER format and decoder evidence](features/rxmer-capture/design.md)
  and [actual validation](features/rxmer-capture/validation.md)
- [Requirements baseline](../requirements.md) and
  [consolidation/validation record](features/requirements/design.md)
- [Planned code layout](../architecture.md#planned-code-layout) and
  [per-section layout design/checklist](features/code-layout/design.md)
- [Upstream signal path and QAM/SA architecture](../architecture.md#planned-upstream-signal-path-and-workbenches)
  and [ARCH-01 design](features/upstream-signal-path/design.md)
- [US Configuration](../architecture.md#us-configuration),
  [PNM RxMER](../architecture.md#rxmer-input) and
  [PNM US-Pre-EQ](../architecture.md#us-pre-eq-input), with
  [input design/checklist](features/upstream-inputs/design.md)
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
- [CMTS-US-RX block architecture](../architecture.md#cmts-us-rx-block-architecture),
  [CMTS configuration / US Configuration JSON](../architecture.md#cmts-configuration-us-configuration-json),
  [RX stage sequence](../architecture.md#receiver-stage-sequence)
  and [receiver design/checklist](features/cmts-us-rx/design.md)
- [Generic OFDMA JSON design/checklist](features/us-configuration-json/design.md)
  and [MULPI coverage plan](features/us-configuration-json/coverage.md)
- [High-level Rust and Python API architecture](../architecture.md#high-level-rust-and-python-apis),
  [paired interface stubs](../architecture.md#paired-rust-and-python-interface-stubs)
  and [API design/checklist](features/public-api/design.md)
- [Official software development checklist](checklist.md),
  [requirement coverage](checklist.md#requirement-coverage) and
  [traceability design/validation](features/software-development-checklist/design.md)
- [Foundation design and reuse/specification assessments](features/foundation/design.md)
- [All-family LDPC source audit](features/ldpc-source-audit/design.md)
  and [codec acceptance evidence](features/ldpc-source-audit/validation.md)
- [Checkpoint validation](features/foundation/validation.md)
- [Foundation adoption and local overrides](foundation-adoption.md)
- [Build guide](build.md)
- [Development setup](setup.md) and [setup design/checklist](features/development-setup/design.md)
- [Git save](../git.md)
- [Skill catalog](../../skills/README.md)
- [Software facts](../sw-facts/README.md)

Private evidence, downloaded specifications and generated outputs belong under
ignored `docs/development/local/`. Plans and concise validation summaries are tracked.


[Backend scientific/native validation](features/backend-stages/validation.md) and
[maintained user guides](../user/README.md) record actual supported stages,
configuration, examples, controls, limits and the remaining capture/platform scope.
