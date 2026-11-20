---
name: numerical-testing
description: Design independent parser and numerical validation, including scientific models and bounded parallel test execution.
---

# Numerical Testing

## Independent expectations

Build expected values independently of production helpers and shared constants.
A reversible encoder/decoder pair can share the same error. Distinguish a local
round trip, independently transcribed specification checks and external vectors.
Meet the project's actual acceptance scope; do not invent interoperability as a
prerequisite, or claim it from a closed-loop result.

For fixed-point or binary data, cover zero, signed boundaries, one representable
step, fractional values, byte order and component ordering. Keep format-specific
missing markers in their parser owner; identical bits can be valid data in another
format. Exercise both the helper and the public parser/serializer path.

For numerical models, explain tolerances, preserve deterministic seeds and test
truth independently from convergence/status. A solver can converge to a wrong
answer; zero observed failures does not establish zero failure probability.
Do not compare elapsed time for deterministic equality. Keep measured, derived,
simulated and interpreted values distinct.

## Coverage ownership

Organize tests by concrete parser/algorithm responsibility, with common plumbing
separate from domain assertions. Cover truncation, declared lengths, trailing
bytes, unsupported versions, overflow, missing samples and allocation/work limits.
Label synthetic fixtures and preserve source provenance. When splitting suites,
map every old assertion/parameter combination to its new target and verify test
discovery; test counts alone do not establish equivalent coverage.

Keep observation/instrumentation passive: enabling a plot or diagnostic must not
consume extra randomness, change processing decisions or discard failed samples.
Test cancellation and partial results at defined boundaries.

Use the [validation matrix](../../templates/project/validation-matrix.md).
For parallel scheduling use [build validation](../build-validation/SKILL.md).

[Catalog](../README.md)

## Standalone procedure

Read the [operational guide](references/procedure.md) for inputs, implementation
steps, examples, failure cases and acceptance checks. Required resources are in
the foundation; no other repository is required or referenced by the procedure.

## Changeable guidance

When this task relies on external APIs, tooling, platform support or other changing
contracts, apply [knowledge-freshness](../knowledge-freshness/SKILL.md) and update
affected local guidance from verified official evidence as part of the task.
