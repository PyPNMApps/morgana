# Paired Rust and Python API design

[Skill](../SKILL.md) · [Architecture](../../../docs/architecture.md#high-level-rust-and-python-apis)

## Inventory and placement

Inspect the current Rust facade, downstream callers, binding manifests, exports,
error conversion and parity tests before adding an API. Record which operations
exist and which are proposals. Keep one table mapping each Rust operation to its
Python signature, shared validation owner, result/error type and acceptance case.
Name implementation files, declaration files and tests with create/reuse/extend
status. JSON serialization alone is not a high-level typed API.

Use an idle session plus explicit configuration, input admission, preview and
execution operations when the product requires a staged experiment. Preserve
existing low-level APIs and imports. Configuration failure must retain accepted
state; discover available IDs through Rust rather than fixed Python lists.
Distinguish document inventory, measurement playback and batch execution.

## Planning stubs and implementation

During architecture work, write proposed Rust declarations and Python signatures
in clearly labeled documentation fences. Neither is executable or a stable API
promise. Do not use `todo!()`, success-returning no-ops or importable packages as
evidence of scientific support. Any requested source scaffold needs a separate
explicit support/readiness contract and implementation authorization.

Once authorized, implement and test the Rust operation first. Keep bindings in
a separate optional native crate; avoid binding/runtime dependencies in the core.
Define the Python extension/package names and version/build policy before adding
manifests. Pin dependencies from verified compatible evidence at implementation,
rather than copying another project's version choices without checking them.
Maintain native `.pyi` signatures and `py.typed` with real exported classes,
defaults, return types and exception behavior. Type stubs do not replace the
extension or demonstrate it can load.

## Conversion and lifecycle

Rust owns domain validation, units, association, transformations and execution.
Python handles syntax, checked integer/buffer conversion and structured exception
mapping. Native argument-type failures may use Python exceptions; domain error
codes must match Rust without parsing messages. Optional values use `None`.
Keep results owned after input release, subsequent calls and session disposal;
document copies and lifetimes instead of assuming zero-copy behavior.

Release the interpreter lock during long native work. Serialize mutable session
access, report Busy deterministically, restore state on errors and keep shared
cancellation accessible from another thread. Buffer bounded Rust progress for
polling; never invoke Python callbacks from a simulation worker holding core
locks. Specify safe pause/cancel boundaries, partial results and elapsed-time
policy before exposing those controls. Unsupported controls remain unavailable.

Example mapping: Rust `preview(&self) -> ApiResult<Preview>` maps to Python
`preview(self) -> Preview`; a missing input raises `ApiError` with a stable
`MissingSetting` code. Neither operation starts work or changes accepted state.

## Failure cases and acceptance

Reject negative/overflowing counts, nonfinite values, incompatible grids, invalid
IDs, exceeded limits and unsupported execution modes through the shared domain
contract. Do not silently drop settings, select a guessed capture or execute on
load. Preserve missing values, original bytes/hashes and source identities.

Acceptance needs a Rust-only build independent of Python/UI, native import and
signature checks, valid/invalid conversion cases, output-lifetime checks and
paired deterministic runs against independently executed Rust results. Compare
errors, selected inputs, seeds, provenance, status and completed/partial science;
declare tolerances for floats. Cancellation and lock release need actual native
tests. Mock Python calculations, matching JSON text or parsed Rust source alone
do not establish runtime parity. Keep pending evidence visibly unchecked.
