# Inspect upstream RxMER captures

MORGANA decodes one bounded upstream CCAP RxMER file through shared Rust and
native Python. It preserves original bytes, raw metadata, the exact contiguous
subcarrier grid and missing readings. Loading is idle: it does not configure a
session, select a noise model or associate the capture with a simulation.

The supported profile is file type`0x504e4e69`, major2, with its297-byte header
and exact declared data EOF. Vendor minor bytes are retained without guessing
extensions. The decoder accepts25/50kHz subcarrier spacing and at most4096 data
bytes within their physical4096/2048-bin grids. Total input cap is4393 bytes.
Empty data remains empty; it does not become ready to run. Compressed/container
files, other majors/types, guessed endian layouts and trailing bytes reject.

Each raw byte0..254 becomes an exact quarter-dB reading0..63.5. Byte255 becomes
`None`/JSON null, while remaining available in the raw data. Interior gaps retain
their physical positions: array index j corresponds to first-subcarrier+j.
No interpolation, compacting, averaging or noise-power calculation is performed.

## Rust

```rust
use morgana::api::RxmerCapture;

fn inspect(bytes: &[u8]) -> Result<(), Box<dyn std::error::Error>> {
    let capture = RxmerCapture::from_pnm(bytes)?;
    let header = capture.header();
    println!("CM {:?}, first {}", header.cm_mac, header.first_active_subcarrier);
    println!("{:?}", capture.readings_db());
    assert_eq!(capture.original_bytes(), bytes);
    println!("{}", capture.to_json()?);
    Ok(())
}
```

`header()`, `readings_db()`, `raw_readings()` and `original_bytes()` borrow
immutable views; clones share original byte storage. `original_sha256()` returns
an owned fingerprint. The authored-fixture consumer runs independently with:

```bash
scripts/cargo-local.sh run --locked -p morgana --example inspect_rxmer
```

## Native Python

With the optional native module built and importable:

```python
from pathlib import Path
import json
from morgana import RxmerCapture

source = bytes.fromhex(
    Path("examples/measurements/rxmer/ccap-50khz.hex").read_text()
)
capture = RxmerCapture.from_pnm(source)
print(capture.readings_db())
print(capture.raw_readings(), capture.original_sha256())
observation = json.loads(capture.to_json())
assert capture.original_bytes() == source
print(observation["header"]["cm_mac"])
```

Python performs conversion/presentation only; Rust owns parsing and dB conversion.
Returned bytes/lists/text are owned and survive the capture object's life. Failures
use the same `ApiError.code`, `.field` and absolute zero-based `.offset` as Rust.
See the [native build guide](../development/build.md) for validation and post-test
cleanup commands; core-only builds do not require PyO3/Python.

## Provenance and interpretation limits

The full256-byte CCAP ID, CM/RPD identities, ifIndex, capture epoch, averages,
frequency origin, first index, spacing, minor and raw PreEq flag are retained.
No capture time/identity is derived from a filename. Numeric fields use the
explicit most-significant-octet-first adapter profile of ordered hex fields.
The pinned source does not add a separate byte-order sentence; no alternate
layout is detected heuristically.

The file gives averages two octets, while the object model uses UnsignedByte.
Inspection retains the full raw file field; this does not admit out-of-domain
values into a measured simulation model.

`ccap_id_text()` optionally renders UTF-8 before the first NUL. Invalid UTF-8,
nonzero padding and empty text do not replace the raw source. `pre_eq_enabled()`
optionally renders raw0/1 using the object-model Boolean convention; other values
return None, never a guessed false or SNMP1/2 conversion. The file does not
independently define its flag's wire truth encoding, so measured-model association
still needs source-confirmed interpretation. Unknown metadata is inspectable.

JSON is independently tagged`morgana.rxmer-capture`, schema1,
`decoded-observation-only`, bounded to1MiB. It contains header/raw/decoded data,
original hash/size, reference-plane and encoding-limit declarations. It is not
runnable configuration or a saved workbench. Exact originals remain separate.

The measurement reference is a CMTS equalized upstream probe relative to ideal
BPSK. It is a measured observation, distinct from synthetic target error power,
injected channel truth and receiver noise variance. The separate
[measured experiment plan](measured-experiments.md) now admits the declared
exporter profile with exact associations and explicit single/multiple playback;
this inspection decoder alone does not configure residual synthesis. Pre-EQ bank/
update decoding and controlled playback use the same measured-plan boundary.
See [source/independent cases](../development/features/rxmer-capture/design.md)
and [fixture provenance](../../examples/measurements/rxmer/README.md).
