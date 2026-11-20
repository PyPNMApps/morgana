# Upstream capture format verification and UCD inspection

[Architecture and paths](../../../architecture.md#upstream-configuration-capture-inspection) ·
[Official checklist](../../checklist.md#7-complete-configuration-json-and-pnm-admission)

Current acceptance: source format and shared inspection pass their local Rust/
native gates; [validation](validation.md) records actual scope and remaining work.

This milestone covers US-CONFIG-FORMAT-01 and US-CONFIG-INSPECT-01. It is
source-derived structural inspection, not full captured-channel projection,
external interoperability, PNM decoding or waveform acceptance.

## Source and envelope decision

Pinned authority: CableLabs CM-SP-MULPIv3.1-I25-230419, SHA-256
`fe9daf3d2bcee2a84b34cfcfed1094841efb04baa6136d1fe44d776a9a8afc1a`.
The [publisher's pinned document](https://account.cablelabs.com/server/alfresco/79935977-877b-4027-8f6f-7d739945e1d1)
was located by revision identity. The privately supplied PDF and extraction are inspection inputs only. Original
PDF pp100/107 were rendered and inspected before implementation. The earlier
source-field audit retains Table28/29 page inspections; pp101/103/105/114 are
checked here for multipart/version/burst rules. PHY does not define this wire
format; downstream DPD or a CM provisioning configuration file is not its source.

| Source | Verified rule / independent expectation |
| --- | --- |
| §6.2.1.2, p83 | Multi-octet MAC numeric values are most-significant octet first. |
| §6.4.1, Figure30 p100 | Six-octet DA, six-octet SA, two-octet message length, LLC00/00/03, version/type/multipart. Message length counts DSAP through payload. |
| §6.4.1 p101 | Version5 multipart: upper nibble is last fragment index, lower nibble sequence; zero is unfragmented. Fixed UCD fields repeat in each fragment. |
| Table26 p103; Table27 p105 | OFDMA UCD message type51, version5; only Type23 burst descriptors. |
| §6.4.3, Figure32 p107 | Four fixed octets UCID/change-count/minislot-size/DSID followed by one-octet type, one-octet length, exact value. All channel parameters precede burst descriptors. |
| Figure34 p114 | Burst length includes one-octet IUC and all nested TLV bytes; IUC occupies low four bits, high four bits zero. |
| Tables28/29 pp110–117 | Raw example channel and burst encodings; typed interpretation remains a separate execution validator. |

The adapter takes exactly the bytes from DA through the end of payload. Common
DOCSIS MAC framing/HCS, CRC, PCAP records, MPEG/transport encapsulation and PNM
headers are outside this envelope. A CRC-bearing frame must be unwrapped by a
future separately validated adapter; trailing bytes reject. Neither addresses nor
unprovided capture time are used to guess the originating CM. Header DA/SA describe
management delivery, not a unique measured-CM association.

This initial implementation explicitly rejects multipart messages with a known
unsupported error after validating sequence bounds. It never treats one fragment
as a complete descriptor. Unsupported type/version remain separate from malformed
length/LLC/TLV structure. Source p103 retains an older RSVD description; the
version5-specific multipart rules and Figure30 p100 govern this version.

## Reuse and implementation decisions

Reuse shared ApiError categories, bounded JSON, sha2 and the existing native bytes
conversion pattern. Extend ApiError with capture field/byte offset and an explicit
category; preserve existing callers and error codes. New immutable UcdCapture
keeps exact bytes in Arc storage, raw header fields, ordered channel TLVs and
ordered IUC/attribute records. No copied parser, new dependency, Python parsing,
source-tree dependency or unsafe code is needed. Full UsChannel projection remains
US-CONFIG-INPUT-01; no assumed bandwidth/grant/timestamp/assignment fills its gaps.

The maximum byte span is65549 (14+65535), with1024 total outer/nested TLVs.
Checking limits precedes owned copies. Inspection JSON is independently tagged
`morgana.ucd-inspection`, schema1, structural-only, and bounded to1MiB. Raw originals
are returned separately; canonical JSON never replaces bytes/hash. Python releases
interpreter access for shared Rust parsing/export and returns owned snapshots.

## Independent cases recorded before implementation

1. Frozen authored minimal structural envelope:24 octets, message length10;
   IDs7/9, change254, zero minislot field. Absence of TLVs does not claim channel
   conformance. This distinguishes structural acceptance from runnable settings.
2. Frozen authored 92-octet scheduled50kHz example: message length78; ten channel
   TLVs, two Type23 bursts, IUC5/13, raw profile bytes4107/2107. Snapshot raw bytes
   `01234567890abcdef0` and exclusion/unused bands retain byte order exactly.
3. Every truncated prefix rejects without a panic; appended bytes and byte-swapped
   message lengths reject. Unfragmented type/version, LLC and multipart sequence
   mutations have independently listed offsets/categories.
4. Zero-length unknown values and duplicate known/unknown TLVs retain original
   order/raw bytes; they do not silently become a source-valid configuration.
5. Incomplete outer/inner headers, length overrun, empty burst, high IUC bits,
   legacy bursts and channel parameters after a burst reject at exact offsets.
6. Maximum byte span, one byte over budget, exactly1024 TLVs and1025 TLVs exercise
   resource policy. Nested attributes count toward the same budget.
7. Original input mutation/drop cannot change the accepted snapshot; a failed
   parse cannot change any existing session/report. Exact SHA-256 is checked
   against frozen fixture hashes independent of the production parser.
8. Actual native import/export/signatures, original lifetime, errors and offsets
   match an independently executed Rust consumer on both frozen fixtures.

Fixtures are small MORGANA-authored protocol vectors, not captured customer data
or copied specification pages. Their checked hashes and origin are retained in
[the fixture record](../../../../examples/measurements/ucd/README.md).
RxMER/Pre-EQ research remains separate and does not close its format gates here.
