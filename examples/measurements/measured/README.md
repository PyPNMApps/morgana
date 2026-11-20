# Authored capture-driven experiment

`capture-driven.json` is one complete schema1 measured plan with invented source
identities. It embeds the separately authored Type51 UCD fixture, a400-bin40dB
RxMER file, a400-bin applied unity bank and a one-bin unity last update. All
PNM files use the explicit MS-octet-first profile with exporter evidence declared
in the plan. Hex files are human-readable source fixtures, not production output.

The UCD supplies UCID7/DSID9,12.8MHz RF-zero,50kHz,192-sample CP,64-sample
rolloff,6-symbol frames, exclusions0..127/528..2047, unused192..527, and8 data
minislots. IUC5 is16-QAM/pattern1; IUC13 QPSK/pattern1. Separate JSON supplies
CM assignment,20MHz bandwidth, two frames, PRBS seed and finite run budgets.

PNM applied/RxMER epoch is19088743; update epoch19088744. The update activates
at physical symbol6 and explicitly adjusts bank1 using probe10 from symbol2.
Raw probe/capture time is distinct from synthetic symbol activation. The plan
keeps one grant; importing more files never creates extra trials. The RxMER
Boolean flag is explicit profile0/1, raw value1. Averaging count1 is within the
source object range. All400 applied coefficients are1+j0, covering used and
unused bins; excluded bins outside the captured extent remain normative zero.

Run from the repository root:

```bash
scripts/cargo-local.sh run --locked -p morgana --example upstream_captures
scripts/cargo-local.sh run --locked -p morgana-cli -- measured examples/measurements/measured/capture-driven.json
```

This proves execution of the source-derived adapter profile through the actual
Rust simulator; it is not a captured modem interoperability result. See the
[paired API guide](../../../docs/user/measured-experiments.md).

`capture-driven-25khz.json` and `ucd-25khz.hex` add a96-byte Type51 source
for4096 bins,25kHz/zeroRF-origin, CP192/RP64 and6-symbol frames. Exclusions
are0..255/1056..4095; unused384..1055. Source IUC5 groups are
(4bits,pattern8,4slots), (zero,pattern0,2slots), (6bits,pattern8,2slots);
IUC13 isQPSK/pattern8 for8slots. Applied/RxMER extents cover800 bins starting256.
Other source IDs/control/times match the50kHz example. The corresponding Rust
consumer is `scripts/cargo-local.sh run -p morgana --example upstream_captures -- 25`.
