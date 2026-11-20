# Upstream experiments

MORGANA runs a continuous PRBS15 source through all eight CM-US-TX stages,
an explicitly selected channel, all nine CMTS-US-RX stages and independent source
comparison. Scientific code, validation and orchestration are Rust. The native
Python module dispatches to the same Rust API and contains no scientific math.

## Supported scope

Scheduled data uses 2K/50 kHz or 4K/25 kHz geometry at 102.4 Msamples/s,
source-checked upstream LDPC, QAM through 4096 including non-square orders,
all 14 scheduled-data pilot patterns, centered unitary transforms and exact
CP/rolloff/overlap. The PRBS15 payload and PHY randomizer are separate clocks.

The receiver uses configured burst timing and either frame-flat least squares
or bounded pilot-frequency interpolation, followed by valid zero forcing and
finite MaxLog reference-variance metrics. It receives samples and legitimate
configuration. Original bits, injected H/C/noise and RxMER targets stay outside RX.
A changing response inside one frame can cause genuine failures; there is no
blind acquisition, fast tracking or hidden supplied-channel correction.

Channel modes include exact unity, causal synthetic FIR, sample AWGN, integer
delay, constant phase/CFO, and restricted synthetic RxMER residual synthesis.
RxMER is a target error-power model, not a replay of a field RF event. That mode
requires identity H, unity C in **every** Pre-EQ event, zero sample AWGN and
disabled delay/phase. Incompatible composition rejects before source consumption.
RxMER power does not multiply by pilot boost. The independent noise stream uses
32 seed bytes, ChaCha8 and the exact dependency pins recorded in each report.

Typed synthetic RxMER supports single, power average, hold and power interpolation.
Synthetic Pre-EQ supports a fixed bank, snapshots and explicit initialization/
adjustment events based on the bank used for the named probe. Events activate at
physical-symbol boundaries without resetting PRBS, mask, pilot, overlap or RNG.
Replay offsets restart in each explicit repeated isolated grant. Capture epochs
are not synthetic offsets. These synthetic objects do not decode binary PNM files.

Ranging/probe/testing controls are representable in the generic source document
for inspection. Their waveform/MAC execution is unsupported. Measured-file simulation,
full captured-UCD/MAP projection, measured-grid association and live device control
are not delivered. Separate [offline UCD inspection](capture-inspection.md)
preserves raw unfragmented header/TLV data without configuring a simulation.
[Upstream RxMER inspection](rxmer-captures.md) decodes the bounded CCAP file
without enabling measured playback or changing its raw metadata.
A recognized setting or inspected format is not waveform execution support.

## Run a configuration

From the repository root, with the existing development prerequisites:

```bash
scripts/cargo-local.sh run --locked -p morgana-cli -- upstream examples/configuration/us-50khz.json
scripts/cargo-local.sh run --locked -p morgana-cli -- upstream examples/configuration/us-25khz.json
```

The CLI reads a regular file up to 16 MiB and writes one owned experiment report
to stdout. A run without full verified recovery returns nonzero **after** writing
its actual report. Redirect output only to a new destination you intend to create.
There is no overwrite-capable export command. The existing `ldpc` CLI is preserved.

The [schema](../../schemas/us-configuration-v1.schema.json) and
[examples](../../examples/configuration/README.md) define format
`morgana.us-configuration`, schema 1. Normative source fields, arbitrary named
presets and simulation settings are separate. A vendor template number such as
224 is provenance only. Loading is idle. Unknown fields/versions reject; optional
controls accept omission/null, while required fields have no guessed defaults.
`original_bytes()`/`original_sha256()` retain exact original input independently
from resolved canonical export, including whitespace; JSON-loaded reports own both
representations and the original hash. The authoritative Rust validator additionally checks conditional/source rules,
carrier coverage, reserved bits, pilot families and execution support.

`simulation.channel`, `guards`, `synthetic_rxmer` and `synthetic_pre_eq` are
optional. Null/omission selects unity channel, zero guards and no synthetic
measurement playback; default C is unity except excluded zeros. There is no
implicit noise floor. A supplied channel model contains every explicit parameter,
including 32 seed bytes. Targets and update records retain their original values
in the independently versioned source document attached to a JSON-loaded report.
This source configuration format is not a desktop saved workbench or FEC report.

## Rust API

```bash
scripts/cargo-local.sh run --locked -p morgana --example upstream_loop
scripts/cargo-local.sh run --locked -p morgana --example upstream_measurements
scripts/cargo-local.sh run --locked -p morgana --example upstream_document
```

Use `morgana::api::{Simulation, ExperimentConfig, ExperimentOptions}` for typed
configuration, `preview` and `run`. `ConfigurationDocument::from_json` validates
an owned complete inventory; `configure_document` or `configure_json` atomically
accepts its selected source configuration and budgets. `document().inventory()`
discovers all retained preset names. Typed `configure` clears document provenance.
Later `set_options` changes actual accepted budgets without rewriting the original
source document; the report keeps actual options separately.

Rust exclusive mutable borrowing serializes a session. `RunControl` is cloneable
and independent: `progress()`, `pause()`, `resume()` and `cancel()` never require
session access. Pause acknowledgement is `Paused`; the worker retains its stack
and all scientific state. Active execution time excludes acknowledged pause.
Cancel wakes a paused worker. Completed words/decisions survive cancellation;
pending samples and unverified source positions remain explicit. A new run starts
from accepted seeds; a cancelled report is not a serialized resumable checkpoint.

## Native Python

The optional separate PyO3 package does not participate in core-only builds.
It requires an existing Python 3.10+ interpreter/header toolchain and pinned
maturin 1.8.3 for wheel packaging. A local optimized CPython3.10/Linux x86_64 wheel
passes artifact inventory and native tests. No wheel is published or installed by this work.
For local build/import and actual native tests, run:

```bash
python3 tools/python/check_native.py
```

With existing pinned maturin, `python3 tools/python/build_wheel.py` builds a local
Linux-tagged wheel, verifies full host-reachable dependency notices and tests the
actual artifact under ignored `target/`. It requires the native checker references
first. Other platforms and source distributions remain separate acceptance.

The checker builds the locked extension and stages an import tree under ignored
`target/python-runtime/`. To run the paired example against that local build:

```bash
PYTHONPATH=target/python-runtime python3 -B examples/python/upstream.py
```

Python exposes the typed constructors, `ConfigurationDocument`, `Simulation`,
owned reports and native-matching `.pyi`/`py.typed`. `run` releases interpreter
access while the Rust worker executes. Competing session calls return
`ApiError.code == "Busy"`. Negative/overflowing integers, invalid sequence types,
oversized lists and shared domain errors reject without narrowing or silent fixes.
Reports outlive sessions. Independent threads can poll/pause/resume/cancel through
`RunControl`. SIGINT requests cooperative cancellation and returns the partial
report after session ownership is restored; it does not raise away completed science.

## Results and instruments

Check `status`, `reference_recovered`, source coverage and decoder outcomes
separately. `Completed` means processing ended normally; it does not mean correct
recovery. Recovery requires nonempty complete contiguous source coverage, zero
independent bit errors, parity/convergence/shortened-zero validity and valid fill.
Failed decoder decisions and actual iterations are retained. Empty comparison has
`ber: null`; zero errors alone cannot establish recovery.

Each grant reports planned/emitted/received/pending samples, generated/compared/
unverified meaningful bits, completed and unprocessed codewords, missing symbols,
and matched-data MER. The latter compares actual deboosted data/complementary
symbols against independently matched ideal TX symbols outside RX. It is distinct
from target RxMER or a normative probe measurement. Its state is `FiniteDb`,
`ZeroError` or `Unavailable`; JSON does not invent infinity or a finite floor.

`report.qam(tap, loading, maximum)` returns actual retained cell identities/roles.
`report.spectrum(tap, numerology)` analyzes a retained contiguous sample prefix
using a rectangular unitary FFT and normalized power/Hz. Snapshots include the
actual run/grant identity, sample rate, window, FFT length and units. A retained
TX-useful-symbol interval is analyzed independently from assembled burst output. Frequency is centered
complex baseband, not calibrated dBmV. QAM cells do not become SA samples. Disabled,
full or missing history returns an explicit unavailable error; queries never rerun
science, consume noise draws or join gaps. TX/FFT QAM snapshots retain the first
symbol per frame; equalized payload history includes actual visited frame cells.

## Application bounds

Limits include 256 repeated grants, 16,777,216 aggregate received samples,
1,048,576 coded bits per grant, 268,435,456 demapper-work units, 16,777,216 retained
decision elements, 1..100 LDPC iterations, 1..300000 active milliseconds and
1..65536 transport samples per chunk. Passive retention is 0..65536 points divided
among at most nine explicitly selected taps. FIRs have 1..256 taps, integer delay
and each extra observation guard are at most 4096 samples. JSON/export budgets are
16 MiB/configuration and 64 MiB/report. These are engineering limits, not modem
capability requirements. Full prospective counts are checked before Start.

Validation evidence and remaining delivery boundaries are recorded in the
[backend validation record](../development/features/backend-stages/validation.md).
