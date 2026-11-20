# US Configuration and PNM Files

Current execution status: bounded synthetic stage science, generic source JSON
and native APIs are recorded in the [backend validation](../backend-stages/validation.md).
The [capture-format milestone](../capture-formats/design.md) adds bounded raw
Type51 UCD inspection; captured-channel projection and PNM formats retain
separate delivery gates.
The [upstream RxMER decoder](../rxmer-capture/design.md) now preserves bounded
major2 binary observations; measured association/playback remains pending.
The design history below is retained; capture/import, broader PHY and presentation
items do not gain runtime acceptance from completed design checkboxes.

Status: architecture defined; scientific runtime, editors and input-format
adapters remain planned. This task changes documentation only.

## Requirements and ownership

| Requirement | Canonical design / planned acceptance |
| --- | --- |
| INPUT-NAV-01 | Compact contents links PRBS, CM-US-TX, CH-SIM and CMTS-US-RX; US Configuration is separate, with RxMER/US-Pre-EQ grouped under PNM Files. Stage indexes remain inside their blocks. |
| US-CONFIG-ARCH-01 | [US Configuration](../../../architecture.md#us-configuration) owns channel/profile/grant settings shared by TX/RX, profile inventory/selection, atomic edits and common readiness. Test malformed/duplicate profiles, incompatible geometry and retained-original preservation. |
| RXMER-MULTI-01 | [RxMER](../../../architecture.md#rxmer-input) covers single-shot and multi-input selection, equal-capture power average and hold/interpolate replay. Test selection, boundaries, provenance and unchanged trial counts. |
| PREEQ-MULTI-01 | [US-Pre-EQ](../../../architecture.md#us-pre-eq-input) covers a fixed single bank, multiple snapshots and multiple initialization/adjustment updates, with explicit bases/probes and bounded immutable schedules. Test independent complex arithmetic, dependency errors and event boundaries. |
| INPUT-COMPOSE-01 | US Configuration feeds both endpoints; Pre-EQ feeds [TX-06](../../../architecture.md#tx-06-cm-pre-eq); RxMER feeds future CH-04. Preflight the entire bank/update plan against initial unity-C/H RxMER restrictions. No hidden C/H/target-noise inputs to normal RX. |
| INPUT-PATH-01 | Each canonical section lists concrete planned Rust importer, domain, configuration, replay and test paths with create/extend status. Keep matching future Python semantics on the same Rust operations. |

## Reuse and evidence

Read-only reference review at MERLIN revision
`096d5a476194d4f2e016863d723b225257bb6037` covered the modulation-profile
input/editor, retained profile inventory, atomic selection, RxMER Single Shot/
Average/Replay and bounded measurement epochs. Adapt the interaction/ownership
patterns. No source code or assets were copied; no other checkout is linked or
needed to understand these contracts. Downstream DPD types, H semantics and
profile fields do not establish upstream input-format compatibility.

The normative coefficient boundary remains PHY I20 §7.4.17, PDF pp106–108,
as recorded in TX-06. Rechecked the local extraction, including the p108
continuation before the downstream heading: adjustment bases correspond to the
last probe; normalization applies over used and unused non-excluded carriers.
The [publisher's PHY I20](https://account.cablelabs.com/server/alfresco/4eb470eb-aca3-4e64-af88-773b8c594fbd)
was checked for revision identity. Existing TX-06 evidence records original-page
visual inspection; no new visual verification is claimed by this update.
RxMER's upstream endpoint/reference remains §9.4.8, p196, as recorded in its
canonical section. Profile/waveform/grant rules remain in the existing TX stage
contracts. Input inventories, synthetic symbol offsets, failure atomicity and
resource budgets are engineering policies, not new PHY timing requirements.

Upstream configuration/profile, RxMER and Pre-EQ binary formats need pinned
OSSI/MULPI/format evidence and lawful fixtures before support. No downstream
decoder type or wire interpretation is assumed. Scheduled synthetic replay
does not implement CMTS coefficient estimation, live probing or MAC control.

## Generic JSON configuration extension

The [US Configuration JSON feature](../us-configuration-json/design.md) expands
this input into a generic versioned-document delivery plan owned by the CMTS
configuration subsection of CMTS-US-RX. Shared Rust configuration remains
independent of receiver algorithms and provides separate accepted TX/RX views.
The [MULPI source-area inventory](../us-configuration-json/coverage.md) starts the
coverage audit; complete field mappings, schema, generic examples and parser
remain pending. A synthetic configuration JSON is separate from the still-
unverified PNM binary/decoded capture formats. RxMER/US-Pre-EQ stay independent
inputs, never serialized as hidden RX configuration truth.

## Checklist

- [x] Simplify navigation and use US Configuration / PNM Files labels.
- [x] Define shared configuration and retained profile selection/paths.
- [x] Make single-shot and multi-input selection explicit for both PNM inputs.
- [x] Define complete-bank versus update kinds, explicit probe bases, bounded
  replay, lifecycle and whole-plan compatibility.
- [x] Align TX-06, CH-SIM, README and development/checklist records.
- [ ] Verify upstream configuration/profile, RxMER and Pre-EQ input formats.
- [ ] Implement and validate typed configuration/PNM operations after approval
  and the reference waveform prerequisites; import/UI/Python adapters follow.
- [ ] Design broader measured RxMER/nonunity-C composition and fast within-frame
  response tracking. RX-04 now defines frame-based estimation only.

## Validation

`bash scripts/validate.sh` passed on the local Ubuntu development checkout
in 2.561 seconds: 20 skill/resource checks, 330 local links, 5 Git-helper tests,
19 setup tests, 23 Rust tests, doctests, formatting and Clippy. An additional
documentation audit resolved 154 fragment links across the changed input/stage
docs, checked the exact seven top-level destinations and all 23 TX/CH/RX stage
targets, and confirmed proposed PHY/source paths remain absent.
`git diff --check` passed.

Only documentation changed; the helper was inspected and its save command is
prepared, not executed. Existing codec/tooling tests do not validate any new
waveform, configuration importer, update replay or capture format. LDPC source
transcription acceptance and all new scientific/runtime milestones stay pending.
