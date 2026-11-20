# Authored UCD structural fixtures

[Capture source audit](../../../docs/development/features/capture-formats/design.md) ·
[Usage](../../../docs/user/capture-inspection.md)

Copyright2026 MORGANA contributors. SPDX-License-Identifier: Apache-2.0.
These tiny hand-authored protocol vectors are independent test inputs, not modem
captures, external interoperability evidence or reproduced specification pages.
They contain invented locally administered MAC addresses and no customer data.
Hex whitespace is formatting; hashes below cover decoded octets.

| File | Octets | SHA-256 | Expected structure |
| --- | --- | --- | --- |
| [minimal.hex](minimal.hex) | 24 | `ccc6c4df3a909210e86062fe8bb273a6be35ab530d1c6e87b30edca0f9d9a269` | Empty structural inventory; message length10, UCID7/change254/minislot0/DSID9. Not a conforming complete channel. |
| [scheduled-50khz.hex](scheduled-50khz.hex) | 92 | `7e47467fae5d8aaabbaa52f7d2dda028a3865fa5b9bf603548a38c00393c3e74` | Message length78, ten channel TLVs and two Type23 wrappers with IUC5/13. No simulation association is supplied. |

Source: MULPI I25 §6.2.1.2 and §6.4.1–3, Figures30/32/34, Tables26–29.
Both spans begin at DA, exclude the common MAC header and end before CRC.
DA=`020000000001`, SA=`020000000002`, LLC=`000003`, version5/type51/multipart0.

The second fixture has the following absolute offsets and exact raw values:

| Offset | Type | Value / meaning from source |
| --- | --- | --- |
| 24 | 24 | `0000`, raw change bitmask. |
| 28 | 25 | `01234567890abcdef0`, exact nine-octet timestamp snapshot. |
| 39 | 26 | `04`, CP192 samples. |
| 42 | 27 | `03`, rolloff64 samples. |
| 45 | 28 | `02`, spacing50kHz. |
| 48 | 29 | `00c35000`, subcarrier-zero frequency12.8MHz. |
| 54 | 30 | `0000007f021007ff`, exclusion ranges0..127 and528..2047. |
| 64 | 31 | `00c0020f`, unused192..527. |
| 70 | 32 | `06`, six physical symbols/frame. |
| 73 | 33 | `7fffff`, raw23-bit randomization seed. |
| 78 | 23 | IUC5, nested type21 at81, value`4107` (loading4/pattern1, eight minislots). |
| 85 | 23 | IUC13, nested type21 at88, value`2107` (loading2/pattern1, eight minislots). |

The lengths and hashes were frozen before the parser. No production encoder or
serializer generates expected fixtures. Malformed/boundary cases are explicit
byte mutations in `crates/morgana/tests/ucd_capture.rs`; they cover every prefix,
length/LLC/type/version/fragment errors, nested structure, unknown/duplicate values
and exact byte/record budgets. Inspection preserves raw semantics; full source
conformance and captured-configuration projection remain a separate task.
