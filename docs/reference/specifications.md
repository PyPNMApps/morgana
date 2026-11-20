# Pinned local specification evidence

Use the supplied editions, not an unspecified latest DOCSIS revision:

| Skill | Controlling document | Local corpus root |
| --- | --- | --- |
| docsis-phy-3-1-i20 | CM-SP-PHYv3.1-I20-230419 | `docs/development/local/specifications/docsis-phy-3-1-i20/` |
| docsis-phy-4-0-i07 | CM-SP-PHYv4.0-I07-250627 | `docs/development/local/specifications/docsis-phy-4-0-i07/` |

Each tracked skill carries its metadata/topic map/section index. Complete
extractions (`references/phy-full.txt`, `references/sections/` and keyword index)
are local-only; this workspace has copies from the inspected source skill corpus.
A fresh clone must supply lawful local copies at those paths before textual lookup.
Place original PDFs in the corresponding ignored root. No automatic download or
other repository checkout is required by the guidance. If evidence is missing,
report the exact document/table gap and continue only independent planning work.

For layout-sensitive equations/tables, render and inspect the original PDF.
The current local 3.1 PDF was inspected for pp56–57. Its SHA-256 is
`304c26937f5beaf7ffddc88158abacead4ead2bc29e6acaae5226898c9f716bc`.
The 4.0 delegation was checked in pinned extracted text; its PDF was not inspected.
PHY3.1 §7.4.3 controls upstream FEC; PHY4.0 §7.2.4.3 (FDX) and §7.3.4.3 (FDD)
delegate FEC there. This does not establish full FDD/FDX waveform support.

Do not redistribute PDFs, page images, full extracted specifications or keyword
snippets. Topic/section indexes are navigation metadata. Specification text and
artifacts retain CableLabs rights. Public implementation constants/tests require
their own source mapping; internal round trips do not validate a transcription.
See the [completed LDPC audit](../development/features/ldpc-source-audit/validation.md)
for the resolved transcription findings and independent source fixtures. The
[backend validation](../development/features/backend-stages/validation.md) records
additional rendered PHY/MULPI source pages and separate pending capture research.
