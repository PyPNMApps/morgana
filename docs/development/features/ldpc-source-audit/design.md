# All-family LDPC source audit

Date: 2026-11-20. The user authorized implementation of the accepted backend
plan. This first slice closes LDPC-01 and LDPC-02 before dependent waveform work.
The [official checklist](../../checklist.md) owns status. Requirements:
[REQ-SYS-05](../../../requirements.md#req-sys-05),
[REQ-TX-02](../../../requirements.md#req-tx-02) and
[REQ-RX-08](../../../requirements.md#req-rx-08).
The [TX-02 layout](../../../architecture.md#tx-02-ldpc-encoding-and-shortening)
owns implementation/test paths; waveform integration remains a separate task.

## Evidence and independent expectations

Controlling source: CableLabs CM-SP-PHYv3.1-I20-230419, Table 8 p52,
§7.4.3.2 pp56–57 and §7.4.3.3 p58. Original PDF SHA-256:
`304c26937f5beaf7ffddc88158abacead4ead2bc29e6acaae5226898c9f716bc`.
The PDF and enlarged page images are inspected, then all 490 matrix cells are
transcribed independently under ignored `docs/development/local/ldpc-source-audit/`.
Production constants are compared only after that transcription exists.

Before correcting production, add compact fixtures derived from that independent
input: per-base-row FNV-1a fingerprints, a fingerprint of all lifted edges, and
sparse impulse parity supports. Fingerprints detect accidental transcription
changes; they are regression checks, not cryptographic provenance. Hash shifts
as signed 16-bit little-endian values, including -1. Hash lifted edges in sorted
(check, variable) order as two unsigned 32-bit little-endian coordinates.

The standalone Rust generator uses inverse column displacement for edge
enumeration and polynomial support rotation/XOR for parity, independent of
production's sparse row expansion/peeling and the existing Gaussian oracle.
Its input is a private, source-reviewed transcription, never production constants.
Frozen impulse cases include block boundaries and columns affected by the
recorded discrepancy. Tests are ordinary offline Rust tests; source PDFs,
private transcriptions and a second checkout are unnecessary for test execution.

## Reuse and acceptance

| Owner | Disposition | Contract and gap |
| --- | --- | --- |
| `crates/ldpc/src/definitions.rs` | Edit | Preserve all public identities/dimensions; correct source-verified row values and their column positions. |
| `crates/ldpc/src/codec.rs`, `crates/ldpc/src/sparse_encoder.rs` | Reuse | Existing systematic/shortening and layered decoding ownership; retain notices and public contracts. |
| `crates/ldpc/src/tests/oracle.rs` | Reuse | Gaussian arithmetic is independent of production encoding but uses its transcribed data. Source fixtures close that shared-data gap. |
| `crates/ldpc/src/tests.rs` | Edit | Register focused source acceptance; preserve existing family/error/noise cases. |
| `crates/ldpc/src/tests/source_audit.rs`, `crates/ldpc/src/tests/source_fixtures.rs` | Add | Independent source signatures, exact parity vectors and extended public-codec acceptance. |
| `tools/validation/ldpc_source_reference.rs` | Add | Reproducible, development-only Rust fixture derivation from reviewed source input. |
| `crates/ldpc/Cargo.toml` | Edit | Compile/check the reference generator as an example without a new dependency. |
| `crates/morgana/src/report.rs` | Edit | Verify all-family source-truth and shortened-zero accounting in unchanged schema-1 reports. |

Run new source checks against the checkpoint first and retain the failing result.
Then correct only independently verified discrepancies and require all-family
source checks, full/shortened parity/recovery, bounded failures, finite saturation,
invalid input/state preservation, owned results, actual iterations and separate
known-zero/source-truth outcomes. Run the complete local validation gate.
No dependency, schema, Python wrapper, waveform or external interoperability claim
is introduced. Record results in [validation](validation.md).
