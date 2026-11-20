# Official implementation checklist

Current authorization: preserve this checkpoint, adopt local guidance/tooling and
implement development setup; further scientific implementation awaits plan approval.
See [architecture](../architecture.md) and [foundation design](features/foundation/design.md).

- [x] FOUNDATION-01: Inspect PDE and record selective adoption decisions.
- [x] FOUNDATION-02: Inspect MERLIN and document reusable/upstream-specific owners.
- [x] SETUP-01..03: Adopt generic installer guidance and implement/test explicit
  development setup. Nineteen setup tests and Ubuntu 22.04 read-only modes pass;
  see [design/checklist](features/development-setup/design.md).
- [ ] SETUP-04: Validate actual fresh-machine provisioning on declared targets.
- [ ] FOUNDATION-03: Complete independent workspace foundation. Rust workspace,
  lock, local skills/instructions, notices and save tooling exist; hosted CI,
  release preparation, public API/user guides and full distribution review remain.
- [ ] LDPC-01: Verify all upstream matrix entries/order against pinned PHY tables.
  Long/medium/short implementations exist. Known pending issue: the long base
  matrix's fifth row, zero-based column 20, is currently -1; PDF p57 shows 12.
  Preserve this finding until scientific work is explicitly resumed; source
  correction and an independent regression are not part of the save-only task.
- [ ] LDPC-02: Complete validated standalone upstream LDPC milestone. Existing
  23 unit tests pass, including Gaussian-reference comparison, controlled/AWGN
  LLRs, nonconvergence and shortening. They share source table constants, so they
  do not resolve LDPC-01. External vectors are unavailable; no external claim.
- [ ] PHY-01: Validate grant/codeword selection and virtual CMTS configuration.
- [ ] WAVE-TX-01: Implement one specification-verified upstream data burst.
- [ ] WAVE-RX-01: Independently recover its original payload from received samples.
- [ ] WAVE-CH-01: Add controlled impairments and provenance-preserving Pre-Eq inputs.
- [ ] API-01: Complete experiment reports and matching native Python wrapper.

At each completion/commit-msg review, reconcile this checklist, architecture,
feature records and actual validation evidence. No item implies authorization to
publish, edit source repositories or run system installation.
