# Generic US Configuration examples

These are explicit synthetic examples, not recommended universal modem profiles.
The format/schema is `morgana.us-configuration` / 1; see the
[schema](../../schemas/us-configuration-v1.schema.json),
[field audit](../../docs/development/features/us-configuration-json/coverage.md)
and [user guide](../../docs/user/upstream-experiments.md).

| File | Meaning | Execution |
| --- | --- | --- |
| [us-50khz.json](us-50khz.json) | 2K, 20 MHz encompassed band, eight selected minislots, ordinary 16-QAM, separate robust IUC13 entry. Template 224 is optional provenance. | Scheduled PRBS data. |
| [us-25khz.json](us-25khz.json) | 4K, 20 MHz, mixed 16/64-QAM and two zero-valued minislots with pilot pattern 0. | Scheduled PRBS data. |
| [us-synthetic-playback.json](us-synthetic-playback.json) | Separate original synthetic RxMER targets/nulls, interpolation, explicit probe-based unity-bank adjustment and observation guards. | Scheduled-data residual model, verified through Rust/native JSON consumers. |
| [us-controls-inspection.json](us-controls-inspection.json) | Conditional ranging attributes/power, timestamp/class/change bits, assignment/testing SID, CAT0 MAP including expansion words and CAT1 probe controls. | Inspection/round trip only; selected probe execution rejects explicitly. |

From the repository root:

```bash
scripts/cargo-local.sh run --locked -p morgana-cli -- upstream examples/configuration/us-50khz.json
scripts/cargo-local.sh run --locked -p morgana-cli -- upstream examples/configuration/us-25khz.json
```

Normative source fields are in `presets[].channel` and assignment/control records;
engineering run choices are in `simulation`. Generic preset IDs, vendor template
numbers, IUCs, pilot indices and bit-loading indices are distinct domains. Loading
multiple presets does not create trials; one explicit selection is projected.
No actual UCD/MAP wire encoder or binary PNM decoder is implied by these files.
