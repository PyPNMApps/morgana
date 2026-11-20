# High-level Rust API and native Python wrapper

Current execution status: bounded synthetic stage science, generic source JSON
and native APIs are recorded in the [backend validation](../backend-stages/validation.md).
The design history below is retained; capture/import, broader PHY and presentation
items do not gain runtime acceptance from completed design checkboxes.

Status: architecture and paired interface stubs defined; implementation remains
planned. Current callable support is the FEC-only Rust facade. This task creates
no Rust modules, Cargo members, native extension or installed Python type stubs.

The [accepted backend order](../../../architecture.md#accepted-backend-delivery-decisions)
develops the Rust session alongside typed configuration, integrates its run API
before unity-loop acceptance and adds native Python afterward. An early FEC-only
Python wrapper is outside that milestone order. Bounded cancellation/partial
results come first; pause/resume has a separate later acceptance task.

## Requirements and acceptance

| ID | Requirement | Planned acceptance |
| --- | --- | --- |
| ARCH-API-01 | Give the high-level APIs a separate architecture section with paired contracts and concrete file placement. | [Canonical API section](../../../architecture.md#high-level-rust-and-python-apis), linked indexes and explicit support status. |
| API-RUST-01 | Expose typed idle configuration, input admission, discovery, preview and execution in Rust before binding shared capabilities. | Planned `crates/morgana/src/api/` and Rust integration tests; preserve existing facade/re-exports and FEC reports. |
| API-INPUT-01 | Cover US Configuration plus single/multiple RxMER and Pre-EQ banks/updates through shared Rust validation. | Original bytes, stable scoped IDs, explicit association, nulls and atomic failure; no guessed capture formats. |
| API-RUN-01 | Freeze accepted settings and execute with bounded controls, progress and owned partial results. | Runtime/memory limits, Busy behavior, completed trials retained on cancellation and safe lifecycle boundaries. |
| API-PY-01 | Expose the same supported capabilities through an optional native Python adapter. | Separate PyO3 crate; Rust-only builds have no binding dependency; checked conversions and structured errors. |
| API-STUB-01 | Maintain Python type declarations matching actual native exports when implemented. | Planned `bindings/python/python/morgana/__init__.pyi` and `py.typed`; import/signature checks against the built extension. |
| API-PARITY-01 | Verify matching settings, domain failures, provenance and scientific outcomes across both languages. | Independently executed deterministic native calls, declared numerical tolerances, lifetime/Busy/cancellation tests. |
| API-DOCS-01 | Publish paired examples and language-specific guides for implemented behavior. | Rust example executes; Python example imports real extension and runs the same bounded case. |

## Read-only reference review and reuse decisions

Reviewed MERLIN checkout revision `096d5a4` on 2026-11-20. Source inspection is
evidence of structure and existing tests; its native adapter was not built or
executed during this task. No source, manifests or dependency versions were
copied, and no dependency on that checkout is introduced. The upstream-specific
API design is original MORGANA documentation; no downstream OCD/DPD/PLC/BCH model
is imported. Reference names below record provenance without cross-repository
links; all operational guidance is self-contained locally.

| Inspected reference path / symbol | Observed contract | MORGANA decision |
| --- | --- | --- |
| `crates/ofdm/src/api/mod.rs` | Focused public configuration/controller/error/input/report/session/unit exports. | Adopt the separation concept under the existing `crates/morgana` owner, retaining FEC entrypoints. |
| `crates/ofdm/src/api/simulation.rs`, `Simulation` | Idle session wrapping existing controller; configuration/load operations delegate without implicit execution. | Define a typed upstream session, not a copy of downstream profile/OCD operations. |
| `crates/ofdm/src/api/controller.rs`, `prepare`, `run_with_control` | Shared preparation, measurement selection and explicit controlled execution. | Use shared PHY/input planners and one Rust simulation owner; preserve single/multi input policies. |
| `crates/ofdm/src/api/error.rs`, `ApiError` / `ErrorCode` | Structured domain diagnostics; callers do not parse human text. | Define upstream error details and mapping without changing existing LDPC error imports. |
| `crates/ofdm/src/api/inputs.rs`, `NamedCapture` / provenance | Bounded owned originals, source hashes/timestamps and Rust-discovered inventories. | Retain upstream originals and scoped IDs; defer unverified formats rather than reuse downstream decoders. |
| `bindings/python/Cargo.toml`, `pyproject.toml` | Separate native PyO3/maturin adapter and independent workspace; direct public Rust dependency. | Plan an optional independent binding build; choose compatible versions/platforms at implementation. |
| `bindings/python/src/lib.rs`, `error` | Native registration and stable code/message exception properties. | Thin conversions with native error categories, proposed import `morgana` / extension `morgana._native`. |
| `bindings/python/src/controller.rs`, `PyMerlin` / `execute` | Serialized controller ownership, Busy rejection, interpreter detachment and cooperative signal/cancellation handling. | Define the same responsibilities, with lifecycle delegated to Rust; no Python orchestration of scientific stages. |
| `bindings/python/src/workbench.rs` | Shared Rust load/execute semantics for saved inputs. | Carry the compatibility rule for any later saved experiment; do not claim such a format now. |
| `bindings/python/tests/test_parity.py` | Native Python calls compared against recorded independently executed Rust jobs, including selection/provenance/outcomes. | Plan independent native parity fixtures; do not call mocks or source inspection runtime validation. |

The current MORGANA `crates/morgana/src/lib.rs` and `report.rs` are extension/
reuse targets. Their existing `Morgana::new(settings)` and `run_ldpc(bits)` remain
valid. The older foundation sketch `Morgana::configure(...).run()` is superseded
by the separate proposed `morgana::api::Simulation` surface. Existing reports
remain schema 1; new configuration/experiment documents get separate versions.

## Contracts, paths and failure boundaries

The canonical architecture owns the
[module/path inventory](../../../architecture.md#api-modules-and-planned-stub-paths),
[paired signature stubs](../../../architecture.md#paired-rust-and-python-interface-stubs),
[lifecycle/errors/results](../../../architecture.md#api-lifecycle-errors-and-result-contracts)
and [delivery gates](../../../architecture.md#api-delivery-and-validation-gates).
The stubs are documentation declarations; no no-op APIs pretend to run a waveform.

Keep session configuration, options and admitted observations distinct. Preview
resolves inventory and association without execution. Explicit runs freeze a
snapshot. Failed loads/selections preserve accepted state, and in-progress changes
return Busy. Results outlive session disposal; missing values remain missing.
The independent comparison may access source truth; normal RX never does.

Do not duplicate parsing, capacity arithmetic, interpolation, Pre-EQ combination,
QAM/SA or FEC in Python. Core-only validation remains independent of Python/Qt.
Python bindings detach for long Rust work and provide shared cancellation without
holding the session lock. Pause/resume stays reserved until its complete safe-state
and elapsed-time semantics are defined. Type stubs must match exported runtime
behavior once implemented; their existence alone does not establish support.

## Dependency-ordered checklist

- [x] ARCH-API-01: Review the reference read-only, record reuse decisions, create
  the separate architecture, paired interface stubs and local skill requirements.
- [ ] API-RUST-01: Implement approved typed session/error/configuration foundation;
  preserve FEC facade compatibility and a Python-independent build.
- [ ] API-INPUT-01: Integrate approved configuration inventory and source-verified
  PNM formats, typed synthetic inputs, single/multi policies and atomic validation.
- [ ] API-RUN-01: Integrate source-verified TX/channel/RX prerequisites, complete
  reports, bounded controls, observations and cancellation/progress semantics.
- [ ] API-PY-01: Build the optional native adapter with structured conversion and
  interpreter/Busy/signal handling; document actual supported environments.
- [ ] API-STUB-01: Deliver and verify actual `.pyi`/`py.typed` exports.
- [ ] API-PARITY-01: Run independent Rust/native-Python fixtures including malformed
  inputs, bounds, partial/cancelled outcomes, result lifetimes and lock release.
- [ ] API-DOCS-01: Deliver runnable paired examples and maintained guides.

Scientific source validation and waveform prerequisites remain tracked in the
[official checklist](../../checklist.md), including LDPC-01. This architecture
work does not resolve those prerequisites or authorize scientific implementation.

## Validation

`bash scripts/validate.sh` passed in the local checkout: 20 skills, 380 local
links, 23 existing Rust unit tests, 19 setup tests, 5 Git-helper tests, doctests,
formatting and Clippy. Reported test durations were 0.607 seconds for Git tooling,
0.837 seconds for setup and 0.55 seconds for the 21 LDPC cases; the two facade
cases reported 0.00 seconds. These validate existing checkpoint behavior, not
the proposed APIs or the unresolved LDPC source transcription.

The skill-creator validator passed for both updated skills. A focused navigation
check resolved 179 fragment links across all 11 changed/new Markdown files,
retained eight TX and nine RX stages, and confirmed the planned API, binding and
PHY source directories remain absent. `git diff --check` passed.

No native Python runtime or new API behavior was executed. Native import,
signature/type-stub agreement, interpreter concurrency, cancellation, scientific
parity, packaging and hosted/platform checks remain pending. No staging, commit,
push, dependency installation or modification of reference repositories occurred.
