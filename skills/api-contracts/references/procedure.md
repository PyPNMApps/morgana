# Define and verify a shared API

## Contract inventory

List each public operation's inputs, ownership, units, defaults, invalid cases,
resource limits, cancellation and outputs. Enumerate promised consumers (library,
CLI, GUI, language bindings). Keep shared validation in one owner and adapters thin.
Use stable error categories with details rather than matching human error strings.

For a Rust library with a native Python wrapper, define both language signatures
and planned implementation/type-stub/test paths together. Keep proposed declarations
distinct from implemented exports. Bind working Rust operations; Python performs
checked conversions and exception mapping. Verify type stubs against the actual
extension and run shared fixtures through both consumers before claiming parity.

Example: load_document(bytes, limits) returns an idle validated session; run(session,
options) starts explicit work. An adapter cannot replace missing inputs with guessed
values. If a recipe needs reconstruction, that operation belongs in the shared core.

## Persistence migration

Record schema version separately from application version. Specify accepted older
versions, unknown-field policy and explicit unsupported-version errors. Keep a
producer fixture for each important representation, including generated/embedded
inputs. Test that all promised consumers resolve the same settings and perform a
bounded equivalent run. Keep UI-only state distinct from execution settings.

## Bindings and failure checks

Prove output lifetime after input buffers are released or retained as documented.
Test caller reuse, structured errors, optional arguments, cancellation and callbacks.
Keep interpreter/UI dependencies optional so core-only builds remain independent.
Do not promise ABI stability or zero-copy just because a wrapper compiles.

Use [compatibility-matrix.md](../../../templates/project/compatibility-matrix.md).
A row records producer fixture → schema → consumer → resolved settings/outcome →
actual command. Manual conversion is a gap, not a passed row. Update examples in
all supported languages when the shared operation changes.


[Skill](../SKILL.md)
