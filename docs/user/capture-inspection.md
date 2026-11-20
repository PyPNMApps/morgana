# Offline UCD inspection

MORGANA can inspect one unfragmented DOCSIS3.1 OFDMA UCD message (Type51,
version5) through Rust and native Python. This reads the management envelope and
raw channel/burst TLVs. It does not configure or run a simulation.

The input slice **starts at the destination MAC address and ends at the end of
management payload**. Exclude the common DOCSIS MAC header, CRC, PCAP record
headers and transport containers. The caller must know this boundary; the loader
does not guess an envelope. CRC integrity is not checked at this boundary.
Fragmented UCDs return `UnsupportedCapability` with field`ucd.multipart` and
offset19. They require future explicit reassembly rather than partial admission.

Rust owns parsing, bounds, exact originals and SHA-256. Unknown/duplicate raw TLVs
remain ordered and available. Structural admission does not validate every source
field, establish measured-CM identity/time or supply bandwidth, grants or endpoint
settings. Even an empty structural inventory can be inspected; it is not a valid
complete channel. Existing generic JSON configuration remains the runnable input.

## Rust

```rust
use morgana::api::UcdCapture;

fn inspect(bytes: &[u8]) -> Result<(), Box<dyn std::error::Error>> {
    let capture = UcdCapture::from_mac_management(bytes)?;
    println!("{}", capture.to_json()?);
    assert_eq!(capture.header().message_type, 51);
    assert_eq!(capture.original_bytes(), bytes);
    Ok(())
}
```

`header()`, `channel_parameters()` and `bursts()` borrow immutable raw views;
clones share original byte storage. `original_sha256()` hashes the exact original.
Run the authored-fixture consumer with:

```bash
scripts/cargo-local.sh run --locked -p morgana --example inspect_ucd
```

## Native Python

With the optional native module already built/importable:

```python
from pathlib import Path
import json
from morgana import UcdCapture, ApiError

source = bytes.fromhex(
    Path("examples/measurements/ucd/scheduled-50khz.hex").read_text()
)
capture = UcdCapture.from_mac_management(source)
inspection = json.loads(capture.to_json())
assert inspection["header"]["message_type"] == 51
assert capture.original_bytes() == source
print(capture.original_sha256(), inspection["bursts"])
```

Python performs bytes conversion and presentation; the same Rust loader owns
all interpretation. Owned exported text/bytes survive the capture object's life.
`ApiError.code`, `.field` and `.offset` preserve Rust failure information.
Capture offsets are zero-based in the exact input envelope. Non-capture API errors
have `.offset=None`; existing categories remain unchanged.

The input budget is65549 bytes and1024 total outer/nested TLVs. Both limits
reject before additional unbounded allocation. Inspection JSON is tagged
`morgana.ucd-inspection`, schema1, `structural-inspection-only`, capped at1MiB;
it contains raw header/TLV values, offsets and original hash/size. Exact original
bytes are returned separately. It is not `morgana.us-configuration` or a saved
workbench and cannot be loaded as either.

See the [source/fixture audit](../development/features/capture-formats/design.md)
and [fixture record](../../examples/measurements/ucd/README.md). Separate
[RxMER file decoding](rxmer-captures.md) is available for bounded inspection.
The separate [measured experiment plan](measured-experiments.md) implements
Pre-EQ decoding, measured association/playback, captured-UCD projection and bounded
multipart assembly. Transport unwrapping/MAC CRC remain unsupported.
After crate testing, follow the
[cleanup commands](../development/build.md) once dependent checks finish.
