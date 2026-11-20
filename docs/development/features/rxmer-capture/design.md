# Upstream RxMER file verification and lossless decoding

[Architecture](../../../architecture.md#rxmer-input) ·
[Official checklist](../../checklist.md#7-complete-configuration-json-and-pnm-admission)

Current acceptance and limitations are recorded in [validation](validation.md).

This milestone covers RXMER-FORMAT-01 and RXMER-INSPECT-01. It decodes a bounded
upstream measurement for inspection; measured association/playback remains
RXMER-INPUT-01. No live test/capture/control or external interoperability is implied.

## Pinned evidence and decisions

Authority: [CCAP-OSSIv3.1 I18-200610](https://account.cablelabs.com/server/alfresco/8a23d1b7-fbd5-4da0-b128-6da766fc9737),
SHA-256 `a74611960b377d8f23e9d9929af6c272c671164eba858a087432e7ce66c0d0aa`.
Original PDF pp396/397/419 were rendered and visually inspected before decoder
implementation; §7.3.5.5 pp418–420 and §F.5 Table455 p608 were reviewed in context.
PHY I20 §9.4.8 p196 controls the measurement reference: CMTS equalized upstream
probe versus ideal BPSK for one CM/user/channel. PHY does not define this file.

| Source | Verified fact / disposition |
| --- | --- |
| §7.3.2.5 p396 | One byte per consecutive subcarrier, including missing/excluded positions; byte0..254 is dB/4, byte255 is unavailable. No gap compaction. |
| §7.3.3.1/Table397 p397 | PNN-prefixed formats contain major/minor bytes; PNM-prefixed older formats do not. Raw common metadata remains authoritative. |
| §7.3.5.5.7/Table410 p419 | Exact type0x504e4e69, major2, fixed ordered header fields. Major2 adds RPD ID/port. |
| §7.3.5.5.7.2 p419 | Minor is vendor-assigned information, default0. Retain any minor byte without guessing extensions or shifting the header. |
| §7.3.5.5.7.3–14 p420 | Epoch seconds, upstream ifIndex, null-terminated CCAP ID, six-byte RPD ID per Table410, CM identity, averages, PreEq flag, frequency origin, first index, spacing and data extent. |

### Explicit interpretation boundaries

The ordered hexadecimal numeric fields are read most-significant-octet first in
this declared adapter profile. The source describes field order, right-justified
hex values and zero padding; it does not add a separate byte-order sentence.
Endian heuristics and alternate/vendor layouts are unsupported, not silently
inferred. The authored literal counter/frequency/index bytes test this profile.

The one-byte PreEq field copies the Boolean attribute. Table455 maps object-model
Boolean0/1; it does not independently specify this file octet's truth convention.
Retain the raw byte and expose optional0/1 rendering only. Other values remain
unknown (`None`/JSON null), never SNMP1/2 guessing or an implicit false/default.
Measured-model admission still requires a source-confirmed flag interpretation.

Keep all256 CCAP-ID bytes including padding. A NUL terminator is required by the
source. UTF-8 text before its first NUL is optional presentation only; invalid
UTF-8 and nonzero padding remain recoverable raw, not replaced. Default RPD bytes,
zero epoch/ifIndex and averages are retained without inventing provenance.

Table409 models NumAverages as UnsignedByte while Table410 allocates two file
octets. The decoder preserves that full raw file field without claiming every
u16 value is a conforming object-model value. The50kHz fixture's0x0123 tests
field width/order; it is a raw-layout vector, not a valid capture-control request.
The25kHz fixture retains the object-model-valid value1. Semantic measured-input
admission remains a separate gate.

## Existing owners and reuse

Reuse ApiError::Capture/CaptureFailure, bounded JSON, SHA-256 and optional native
bytes conversion. Add inputs/rxmer.rs for the actual wire contract; no external
parser/dependency or Python scientific implementation is needed. Typed synthetic
RxMER/playback remains a different owner/reference contract. Decoding never calls
SyntheticRxmer::new or configures a session. Future association must validate CM,
channel/grid/reference/epoch and explicit synthetic timing before replay.

The profile supports spacing25/50kHz, exact physical subgrid within4096/2048,
297 header bytes and at most4096 data bytes. Byte cap4393 precedes copies. Zero
readings can be inspected, with no invented coverage/readiness. Declared data
extent must match EOF exactly. Counts/spacing outside this scope fail with named
category/field/offset errors; no allocation follows an attacker-sized count.
Decoded-observation JSON uses independent format`morgana.rxmer-capture`, schema1,
with exact metadata, raw data, decoded optional dB, interpretation notes and hash.
Original bytes are returned separately; the1MiB JSON cap remains bounded.

## Independent cases fixed before implementation

- Authored 50kHz fixture:305 bytes; epoch0x01234567, ifIndex0x10203040,
  CCAP`ccap.example`, RPD02000000000a/port3, CM020000000001, averages0x0123,
  flag1, origin12.8MHz, first128, eight readings. Raw005f7f80a0fdfeff means
  [0,23.75,31.75,32,40,63.25,63.5,None] dB at physical128..135.
- Authored 25kHz fixture:301 bytes; vendor minor165, epoch0xfedcba98, ifIndex7,
  CCAP`2001:db8::1`, integrated zero RPD/port, CM020000000002, averages1,
  flag0, origin100MHz, first3800, four rawff0028fe values.
- Frozen SHA-256 and offset matrix are published with the fixture record. No
  production encoder/decoder generates expected fixtures.
- Every truncated prefix, appended data, byte-swapped/huge declared lengths,
  wrong type/major, missing NUL, unsupported spacing and overflowing physical
  subgrids fail deterministically at source offsets. Header length is297;
  data count field begins at293. Quarter-dB zero is a real value, not null.
- Exhaust all256 raw data encodings exactly, maximum4393-byte extent, one byte
  beyond budget, both last-bin boundaries and empty data. Missing values retain
  physical slots. No smoothing, extrapolation or power/noise synthesis occurs.
- All256 minor/PreEq bytes remain preserved; only0/1 have optional Boolean
  rendering. Non-UTF-8 ID bytes and nonzero padding survive. Caller mutation,
  original drop, clone/export and failed parsing cannot change an accepted capture.
- Actual native methods/signatures, original/readings/error lifetimes and both
  independent Rust-process outputs match. Existing UCD/simulation APIs remain
  accepted through the full core/native/artifact gates.

Source documents/renders/extractions and generated artifacts stay ignored.
Fixtures are small MORGANA-authored invented vectors, not device/customer data.
