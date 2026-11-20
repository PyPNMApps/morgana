# OFDMA configuration JSON coverage plan

[Feature design](design.md) ·
[Canonical CMTS configuration](../../../architecture.md#cmts-configuration-us-configuration-json)

Status: **source-area inventory only; field-level coverage audit pending**.
Listing an area below does not establish complete option/enum/default coverage.
USJSON-COVERAGE-01 stays unchecked until every applicable field is mapped and
reviewed against the pinned original specification and independent fixtures.

## Pinned scope

MULPI: `CM-SP-MULPIv3.1-I25-230419`; PHY: `CM-SP-PHYv3.1-I20-230419`.
The scope is OFDMA channel/burst-profile configuration and associated per-CM
assignment/probe controls. Inventory all applicable options in these areas,
including common fields whose applicability includes OFDMA. Full MAC/security/
service-flow management and TDMA/S-CDMA-only attributes are outside this model;
record inapplicability explicitly instead of importing their defaults.

| Source area / initial anchors | Fields to audit into the generic model | State |
| --- | --- | --- |
| MULPI §6.4.3, UCD fixed fields and Table 28, pp103–113 | Type-51 identity/change/channel association, all OFDMA-applicable common fields and conditional presence. | Pending full field audit. |
| Table 28 channel TLVs 3, 16, 18, 19 | Applicable preamble superstring, ranging requirement, ranging hold-off and channel-class controls. | Pending exact types/defaults/conditional rules. |
| Table 28 channel TLVs 23–25 | DOCSIS 3.1 burst descriptors, change bitmask, OFDMA timestamp/minislot snapshot. | Pending field/bit/width mapping. |
| Table 28 channel TLVs 26–33 | CP, RP, spacing, index-zero frequency, excluded/unused bands, frame symbols and 23-bit randomization seed. | Pending complete enum/range/mask fixtures. |
| Table 29 and §6.4.3.4, pp114–121 | Applicable burst preamble length/value offset, Nir/Nfr, OFDMA data profile and broadcast initial-ranging power control; audit every other row for applicability. | Pending conditional per-IUC mapping. |
| §6.4.3.3–4.1 and Table 31, pp120–121 | Exact carrier-to-minislot mapping, profile group ordering/counts and illustrative encoding reconciliation. | Pending complete coverage/expansion rules. |
| §6.4.4, Table 32 and relevant Version-5 MAP fields, pp121–128 | Applicable IUC/interval selection, allocation offsets, channel/UCD association and reserved/conditional cases. | Pending explicit field/option inventory. |
| §6.4.4, Figures 40/41 and Table 33, pp126–128 | P-MAP header and P-IE SID, MER/PW/EQ/St controls, probe frame/symbol, start carrier, skipping and power-dependent interpretation. | Pending all enum/interaction/boundary fixtures. |
| §10.5.1–10.5.1.3, pp454–456 | IUC-13 role, pre/post-registration assignment context and profile-testing/probe measurement configuration; separate configuration representation from MAC test-burst execution. | Pending normative-to-model mapping. |
| Annex C §C.1.5.1.11–12, p658 | Assigned OUDP IUC list and testing SID; count/value/identity and update-context rules. | Pending exact shared types/fixtures. |
| PHY §7.4.3–7, §7.4.9–11, §7.4.15–17, §8.2.3 | Dependent waveform/loading/pilot/frame/ranging/probe/Pre-EQ rules referenced by MULPI fields. | Existing stage contracts are inputs; complete cross-field audit pending. |
| Every remaining UCD/burst-table row and reserved value in the pinned areas | Explicitly classify applicable, conditional, inapplicable or unresolved, with a source reason; do not assume omission from this starter inventory means out of scope. | Pending exhaustive reconciliation. |

The I25 inventory ends at channel TLV 33; do not import fields from a later
edition just because its table/search result looks similar. Distinguish channel
TLV 21 from nested burst TLV 21 by full source path. Known pilot pattern index,
data modulation index, IUC, generic preset ID and optional vendor template ID
are different domains. Pattern 0 belongs only to a zero-valued minislot; an
ordinary data modulation index of 1 is reserved in this pin. Exact validity
belongs in the source-reviewed domain matrix, not a loose shared numeric enum.

## Required final row contents

Each atomic field/conditional option must identify:

1. Document/revision, section, physical PDF page, table/TLV path and endpoint.
2. Normative force and required/optional/conditional applicability.
3. Source encoding, width, units, allowed values/ranges and reserved values.
4. Proposed JSON pointer/type and omitted/default/explicit-zero/null behavior.
5. Shared Rust owner, cross-field dependencies and support states for inspection,
   domain validation and execution.
6. Independent valid, invalid, boundary and conditional fixture paths, with
   expected typed errors where applicable.
7. Review status and any source/layout/format ambiguity still unresolved.

Completion requires every applicable row to have a typed mapping and fixture,
every inapplicable row to have an explicit reason, and no unresolved source
entries hidden behind generic extension fields. Schema structure checks alone
cannot establish PHY validity or executable support. Keep optional/deferred
settings representable without silently executing or discarding them.
