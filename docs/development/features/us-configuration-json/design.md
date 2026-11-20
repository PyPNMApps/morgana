# Generic OFDMA JSON and CMTS configuration

Current execution status: bounded synthetic stage science, generic source JSON
and native APIs are recorded in the [backend validation](../backend-stages/validation.md).
The design history below is retained; capture/import, broader PHY and presentation
items do not gain runtime acceptance from completed design checkboxes.

Status: architecture/delivery plan recorded; coverage audit, schema, JSON
examples, Rust implementation and adapter/runtime validation remain planned.
This feature belongs to US Configuration, documented as a CMTS control
subsection of CMTS-US-RX; it does not add a receiver processing stage.

## Requirements

| ID | Requirement | Owner / planned acceptance |
| --- | --- | --- |
| USJSON-ARCH-01 | Locate the generic JSON plan under CMTS-US-RX while retaining the public US Configuration input and shared TX/RX configuration ownership. | [Canonical CMTS subsection](../../../architecture.md#cmts-configuration-us-configuration-json); configuration-flow and receiver-flow links; unchanged RX-01..09 sequence. |
| USJSON-COVERAGE-01 | Map every applicable OFDMA option in the pinned MULPI configuration scope, including required, optional and conditional fields. | [Coverage plan](coverage.md); source-to-JSON-to-Rust-to-fixture matrix, complete only after every applicable field is resolved. |
| USJSON-FORMAT-01 | Define a generic versioned configuration document with named preset inventory/selection and explicit units/default/null/extension policy. | Planned `schemas/us-configuration-v1.schema.json`; format/version, cross-field, malformed and bounded fixtures. |
| USJSON-PRESETS-01 | Supply generic 25/50 kHz and mixed/zero-loading/optional-mode examples with honest support states. | Planned `examples/cli/us-configuration/`; values labeled engineering examples, vendor IDs only optional metadata. |
| USJSON-CORE-01 | Decode and validate through shared Rust configuration owners and publish one immutable CMTS plan atomically. | Planned `crates/morgana/src/inputs/us_configuration.rs` and `crates/phy/src/configuration/cmts.rs`; preserved originals, pure preview and unchanged accepted state on failure. |
| USJSON-PROJECTION-01 | Give TX and normal RX distinct legitimate configuration views. | Planned `crates/phy/tests/cmts_configuration.rs`; matching geometry/grant/pilot/PHY seed without injected H/C, PNM targets, PRBS truth or whole-job settings in RX. |
| USJSON-PARITY-01 | Keep domain validity, representation validity and execution support distinct across Rust and future Python/UI consumers. | Planned `crates/morgana/tests/us_configuration_json.rs`; same errors/availability and explicit unsupported-mode rejection. |

## Canonical ownership and flow

Use the [architecture subsection](../../../architecture.md#cmts-configuration-us-configuration-json)
for the data groups, concrete planned files, source boundaries, budgets and
flowchart. The [US Configuration overview](../../../architecture.md#us-configuration)
remains the public input entrypoint. Avoid a second configuration model inside
receiver code or duplicate admission logic in JSON/Python/UI adapters.

| Existing/planned owner | Reuse or extension decision |
| --- | --- |
| Planned shared `configuration/profile.rs`, `waveform.rs`, `burst.rs`, `grant.rs`, `receiver.rs` | Reuse their existing architecture and one Rust validator per domain; extend models only after the source matrix resolves applicable fields. |
| Planned `configuration/cmts.rs` | New focused composition/selection/projection owner; no receiver algorithm or MAC scheduler. |
| Planned `configuration/probing.rs` | Typed future probe controls and support checks; do not place probe execution in configuration admission. |
| Planned `crates/morgana/src/inputs/us_configuration.rs` | Extend the already planned input responsibility with bounded JSON decoding and original-source ownership. |
| Existing `crates/morgana/src/lib.rs` | Future public facade extension preserving FEC-only APIs/reports. |
| Existing FEC report schema 1 | Separate contract; the proposed `morgana.us-configuration` marker/version does not reinterpret existing reports as configuration documents. |

The planned sequence is document → bounded decode/shared Rust validation →
candidate preset/compatibility preview → atomic CMTS plan → separate TX/RX
projections. PNM inputs remain separate. Acceptance rechecks their association;
it does not load an impairment, generate a Pre-EQ update or start simulation.
Saved-workbench integration, if later introduced, preserves this versioned
document's meanings and shared Rust/Python compatibility rules.

## Evidence and scope

Pin `CM-SP-MULPIv3.1-I25-230419` and `CM-SP-PHYv3.1-I20-230419`.
Relevant source excerpts were inspected read-only; prior research visually
checked original PHY Figures 39–42 and MULPI pp116–117/121/454–455. The
[publisher's MULPI I25](https://account.cablelabs.com/server/alfresco/79935977-877b-4027-8f6f-7d739945e1d1)
confirms the OFDMA data-profile encoding boundary. The complete field/enum/
conditional audit and further original-page review remain USJSON-COVERAGE-01.
The PHY skill is not used as authority for MULPI fields.

The generic JSON is MORGANA's configuration representation. It does not claim
to be a CableLabs JSON standard, vendor CLI import, captured upstream PNM
format, raw UCD/MAP encoder or operational CMTS. DOCSIS 4.0/newer MULPI fields
need a separately pinned extension audit. Preserve private evidence locally;
public docs contain concise mappings/derived examples, not source corpora.

## Dependency-ordered checklist

- [x] USJSON-ARCH-01: Record the CMTS subsection, generic groups, file ownership,
  lifecycle, support boundaries, schema policy and updated shared flows.
- [ ] USJSON-COVERAGE-01: Complete field-level MULPI/PHY mappings, conditional
  rules, all enum/boundary values, exclusions and independent fixture inventory.
- [ ] USJSON-FORMAT-01: Finalize schema version 1, exact fields and error paths.
- [ ] USJSON-PRESETS-01: Create/review generic example JSON and usage index.
- [ ] USJSON-CORE-01: Implement approved typed Rust admission and bounded parser.
- [ ] USJSON-PROJECTION-01: Integrate immutable CMTS selection and TX/RX views.
- [ ] USJSON-PARITY-01: Validate round trips/version handling, conditional errors,
  provenance, bounds, atomic failure and future Python/UI parity.
- [ ] USJSON-DOCS-01: Deliver the maintained user guide with actual support.

## Validation

`bash scripts/validate.sh` passed on the local Ubuntu checkout in 3.387 seconds:
20 skill/resource checks, 361 local links, 23 existing Rust tests, 19 setup tests,
5 Git-helper tests, doctests, formatting and Clippy. Focused checks resolved
175 fragment links across the ten changed/new Markdown files; preserved the
compact contents, all nine RX stages, 18 overview/output links and nine backlinks;
and verified the three shared diagrams now route JSON through the CMTS plan
to separate accepted TX/RX settings. The dedicated configuration-flow diagram
and linked owners also resolve.

All 21 planned artifact paths named by the new subsection remain absent; the
one existing facade extension target exists. Source/schema/runtime milestones
remain unchecked. `git diff --check` passed. No schema/example JSON, new Rust
module, Python binding or configuration runtime was delivered or executed.
The local save command is prepared only; no staging, commit or push occurred.
