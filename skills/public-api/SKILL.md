---
name: public-api
description: Design MORGANA public Rust models and operations with shared validation, bounded execution and matching future native Python semantics.
---

# Shared scientific API

Use [api-contracts](../api-contracts/SKILL.md),
[coding-style](../coding-style/SKILL.md) and
[scientific-testing](../scientific-testing/SKILL.md). Read the current
[architecture](../../docs/architecture.md) and
[API proposal](../../docs/development/features/foundation/design.md#foundation-03-workspace-and-public-api).

The current public facade lives in `crates/morgana`; standalone FEC belongs in
`crates/ldpc`. Rust owns algorithms, validation and result schemas. CLI and future
Python/UI adapters translate inputs/errors and present returned results.

- Use typed configurations, explicit units/defaults/nulls and structured errors.
  Prefer borrowed slices and owned immutable snapshots; document lifetimes,
  mutability/threading and bounds. No caller-input panics, process exits or
  console-driven library results. Do not promise unproved zero-copy behavior.
- Keep core inputs independent of paths, Python and Qt. File parsing is an
  adapter around the same typed validation. Do not hardcode capture profile lists
  in examples promising complete inventory; future inventory discovery is Rust.
- Shared Python capabilities land in public Rust first. Future PyO3/maturin
  bindings are separate/optional, release the interpreter lock for long Rust work
  and map Result/Option into structured exceptions/None. No Python DSP or sidecars.
  Rust/Python requests and examples cover both unless the user limits language;
  label proposed Python methods as unimplemented rather than runnable examples.
- Keep configuration/load idle until an explicit run. Document cancellation,
  progress, partial results and application limits before exposing jobs.
  Convergence, parity, known zeros and original-bit comparison remain separate.
- Version exported schemas and reject unsupported versions/fields explicitly.
  JSON is an adapter to typed results, not the only scientific interface.
  No saved-workbench format exists in this checkpoint.

If a saved experiment/workbench is introduced, every supported setting, embedded
capture and generated recipe must load/run through Rust and implemented Python
consumers with equal semantics. Preserve grids, nulls, seeds, provenance, limits,
defaults and accepted values. Support explicit migration or structured rejection;
failed loading preserves prior accepted state. Test producer fixtures through
both consumers with a bounded deterministic run; manual conversion is not parity.

Acceptance covers valid/invalid boundaries, units, owned results surviving later
calls, Rust-only independence and actual wrapper parity when a wrapper exists.
Current FEC API support does not imply full OFDMA experiment support or a stable C ABI.
