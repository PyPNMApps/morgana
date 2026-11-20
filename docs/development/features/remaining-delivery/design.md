# Remaining delivery gates

The 2026-11-20 request authorizes completing all fourteen remaining checklist
gates in dependency order, including measured admission and the listed extension
designs. Git/publication and host provisioning remain separate operations.
Disposable isolated provisioning environments may be used for setup acceptance.

## Architecture and reuse

| Path | Disposition / contract |
| --- | --- |
| `crates/morgana/src/inputs/pre_eq.rs` | Create immutable CM-OSSI bank/update decoder; exact originals, scale and identities. |
| `crates/morgana/src/inputs/ucd_projection.rs` | Create multipart reconstruction and source-field projection; reuse `ucd` validation. |
| `crates/morgana/src/inputs/measured.rs` | Create explicit bounded association/plan; reuse Rust power and coefficient playback, never a second DSP engine. |
| `crates/morgana/src/api/session.rs` | Extend atomic configure/run to retain measured source provenance. |
| `bindings/python/src/capture.rs` | Extend conversion-only native API and matching `.pyi`; no Python decoding. |
| `crates/morgana/tests/` and `bindings/python/tests/` | Extend independent format, association, actual execution and cross-consumer tests. |
| `examples/measurements/` | Add invented source-derived fixtures before production parsing. |
| `.github/workflows/ci.yml` | Create bounded required hosted entrypoint reusing local gates; a file is not hosted execution evidence. |
| `tools/packaging/` | Create reviewed scientific-only source distribution; exclude private engineering guidance with unresolved redistribution terms. |
| `docs/development/features/extension-designs/` | Create UI, RX, channel and ranging design acceptance, without pretending these waveforms/UI execute. |

Existing synthetic and configuration owners remain authoritative. The new
measured plan carries immutable raw captures and explicit external associations,
then projects through those owners. Loading and failed admission never run or
replace accepted state. Reports carry source bytes/hash/metadata separately from
derived model values. Full-plan preflight includes every later event.

## Source and test decisions

CM-OSSI I27 Tables77/78 pp189–192 define a 34-byte major1 header, I/Q signed
16-bit pairs: applied bank s2.13; last update s1.14. The adapter explicitly uses
most-significant octet first, matching the existing pinned PNM adapter profile;
vendor minor bytes remain raw. A last-update file lacks the Set/Adjust control,
probe/base identity and application status. An explicit caller record supplies
these, never capture order. PHY I20 §7.4.17 pp106–108 owns reset/normalization
and corresponding-probe multiplication. Non-success external status rejects.

MULPI I25 Tables28/29 and Fig33 own UCD semantic projection. An entire bounded
multipart set must agree on sender/destination and the four fixed fields; each
sequence appears once. Unsupported channel/burst fields reject projection but
remain available through lossless structural inspection. External CM assignment,
bandwidth and simulation grant/epoch remain explicit, separate from UCD time.

RxMER CCAP-OSSI I18 Table410/§7.3.2.5 retains source epoch/ifIndex/CM/grid.
Admission requires an explicit CCAP/interface-to-UCID mapping and an explicit
0/1 Boolean adapter profile, rejects other raw flags, and preserves that profile
and its evidence in the plan. No source claim extends to arbitrary vendor files.
Capture time and synthetic symbol offsets are separate coordinates. Missing
required bins reject; partial grids remain inspectable rather than extrapolated.

## Requirements and acceptance

REQ-PNM-01..04, REQ-CFG-05 and REQ-API-01..06 apply unchanged. Importers MUST
preserve raw source bytes; association SHALL be exact; unsupported composition
SHALL reject before execution. Independent literal offsets/scales, all signed
boundary encodings, truncations, wrong identities/grid/time, explicit bases,
multi-input power policies, native parity and actual capture-driven closed loops
are required. Design-only extension gates MUST specify algorithms, source
applicability, bounds, proposed files and independent acceptance before closure.

Validation results and unmet external gates belong in `validation.md`, rather
than being inferred from task counts. SETUP-04 needs real target provisioning;
fresh containers prove userspace setup, not a complete machine/OS lifecycle.
