# Capture-driven experiments

Use `Simulation.configure_measured_json` in both Rust and native Python. It
validates schema1 `morgana.measured-experiment`, all sources/associations and
every later event before replacing accepted settings. Loading is idle. Rejected
input preserves accepted state. The original measured-plan JSON, every original
capture and its SHA-256 survive complete or cancelled runs in report field
`measurement_provenance_json` (an additive optional schema1 report field).
Existing synthetic/FEC entrypoints and schemas remain available.

```rust
use morgana::api::{ExperimentOptions, Simulation};
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let mut session = Simulation::new(ExperimentOptions::default())?;
session.configure_measured_json(include_bytes!("../../examples/measurements/measured/capture-driven.json"))?;
let preview = session.preview()?; // idle, no source/RNG consumption
let report = session.run()?;
assert!(report.reference_recovered);
# Ok(()) }
```

```python
from pathlib import Path
import morgana

session = morgana.Simulation()
session.configure_measured_json(
    Path("examples/measurements/measured/capture-driven.json").read_bytes()
)
preview = session.preview()
report = session.run()
assert report.reference_recovered
```

The [runnable fixture](../../examples/measurements/measured/README.md) uses
authored source-derived bytes, not modem recordings. Rust also exposes typed
`MeasuredExperiment::from_json/prepare/provenance_json` and capture/header types;
Python uses native conversions and the same Rust owners, with no DSP calculations
or subprocess sidecar. `PreEqCapture.from_pnm`, `RxmerCapture.from_pnm` and
`UcdCapture.from_mac_management` remain idle inspection operations.

## Source and association contract

`configuration` is the complete existing generic document: selected preset,
explicit CM assignment, bandwidth, grant timing/frames/minislots, source seed,
receiver policy and job budgets. `ucd_fragments` optionally supplies a complete
ordered Type51/version5 multipart set; admitted source channel/burst fields
replace the selected preset's channel through the shared source validator.
Fragment IDs/sequence/count/sender/fixed fields must agree. Unknown/duplicate or
inapplicable source fields reject projection; inspection still retains them.
Fragments may divide only at complete TLV boundaries in this supported profile.

For RxMER, the external association records exact CCAP-ID bytes, ifIndex-to-selected-UCID
mapping, RPD/port, downstream management MAC, inclusive source epoch interval and
`adapter_evidence`. CCAP/interface/RPD fields may be null when no RxMER sources
are selected; independent Pre-EQ admission does not invent those identities. Match CM, RF-zero, spacing and exact physical-bin extent to
the selected channel. The adapter evidence must identify why the exporter/file
uses the declared MS-octet-first PNM profile and RxMER Boolean0/1 convention.
The pinned object model provides0/1 semantics; it does not independently settle
every vendor's file-octet encoding. Do not supply an unsupported profile or invent
evidence from filenames. Raw vendor minor bytes and padding remain preserved.
Unknown RxMER flag values, inconsistent flags, empty required coverage and invalid
averaging counts reject model admission while remaining inspectable.

`rxmer` stores source IDs and raw bytes. `rxmer_policy` selects exactly single,
average, hold or interpolate (none only with no sources). Hold/interpolate require
strictly increasing explicit physical-symbol offsets beginning at0; source epochs
must be nondecreasing but never become activation offsets automatically. Average
combines normalized error powers with equal weights; interpolation is linear in
power. Missing required bins reject; unneeded nulls remain null. Source count does
not affect `simulation.grants`.

`pre_eq_initial` is an applied major1 s2.13 file covering all non-excluded bins,
or absent for explicit unity/zero-excluded reset. `pre_eq_initial_id` is nonzero.
The model retains measured raw coefficients separately and applies the existing
whole-bank normalization; normalized model coefficients are not a claim of exact
quantized CM transmitter state. Event sources are complete snapshots or s1.14
last-update files. Snapshot never multiplies its predecessor. Initialize replaces
addressed probe-base values; Adjust multiplies them. Updates require explicit
operation, base bank, corresponding probe, source time and success(2) application
status. Probes record their actual effective bank and earlier physical-symbol/
source-time coordinates. Wrong, missing, stale or future lineage rejects before
source consumption; complete banks activate only at symbol boundaries. Multiple
updates may refer to an older bank only when it was actually used by their
explicit corresponding probe. Zero-valued excluded entries stay in original
captures and are omitted only from the derived update address list; nonzero
excluded coefficients reject model admission.

## Models, ownership and limits

RxMER is an equalized upstream probe-relative target. Synthesis still uses the
supported unity-C/unity-H residual model; any nonunity initial or later C, FIR,
separate AWGN or timing/phase model rejects combined RxMER preparation. Applied
Pre-EQ with a separate admitted FIR/noise experiment is supported without RxMER.
No inverse-C plant response, calibrated RF-noise attribution or automatic
adaptation is inferred. Normal RX gets received samples and legitimate
configuration, never measured targets, injected H or original source bits.

Plans are at most16MiB, with16 UCD fragments,256 RxMER sources,255 events,
256 probes and4096-bin arrays, plus existing cumulative work/sample limits.
Provenance export is independently bounded and checked before configuration
acceptance. Results own all data; capture handles and sessions may be dropped.
Use existing progress/pause/resume/cancel controls; completed science and source
provenance survive cancellation. Python long operations release the interpreter
and concurrent mutable session access reports Busy.

The report's `source_configuration_json/original` describe the supplied generic
context; the frozen `configuration` contains actual projected scientific input.
Full captured UCD/metadata/control context is in measured provenance. These views
are deliberately distinct, rather than rewriting original source documents.
