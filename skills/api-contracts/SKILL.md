---
name: api-contracts
description: Design shared APIs and persisted data contracts across CLI, UI and language adapters.
---

# Api Contracts

Give shared behavior one implementation and validation owner. Adapters translate syntax and errors without reimplementing calculations. Document units, defaults, missing values, bounds, cancellation and unsupported states.

For persisted data, define schema/version policy, backward-read expectations, migrations and unknown-field behavior before changing writers. Preserve original input/provenance where required. Test round trips, older fixtures, malformed/bounded inputs and defaults. Python interfaces should expose Python exceptions and None conventions rather than Rust Result/Option syntax. Keep save-file settings separate from global credentials and installation preferences.

[Skill catalog](../README.md)

## Detailed lessons

For applicable changes, read [saved data and bindings](references/saved-data-and-bindings.md).

## Standalone procedure

Read the [operational guide](references/procedure.md) for inputs, implementation
steps, examples, failure cases and acceptance checks. Required resources are in
the foundation; no other repository is required or referenced by the procedure.

## Changeable guidance

When this task relies on external APIs, tooling, platform support or other changing
contracts, apply [knowledge-freshness](../knowledge-freshness/SKILL.md) and update
affected local guidance from verified official evidence as part of the task.
