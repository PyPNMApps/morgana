---
name: build-validation
description: Choose reproducible builds and meaningful validation for code, documentation and packaging changes.
---

# Build Validation

Read repository build entrypoints and pinned tool/dependency versions before running commands. Preserve caches and stable build directories. Start with checks covering changed behavior; broaden for shared contracts and integration. Test outcomes and failures, not copied implementation details.

Keep unit, integration, UI, installed lifecycle and hosted CI evidence separate. Documentation/link checks do not prove runtime behavior. Bound concurrent tests and resources, retain serialized timing cases and necessary doctests. Record exact commands, environment, results, omissions and blockers. Packaging validation must inspect bundled versions/files and exercise installation only in an authorized environment.

[Skill catalog](../README.md)

## Detailed lessons

For applicable changes, read [parallelism and cache evidence](references/parallelism-and-cache-evidence.md).

## Standalone procedure

Read the [operational guide](references/procedure.md) for inputs, implementation
steps, examples, failure cases and acceptance checks. Required resources are in
the foundation; no other repository is required or referenced by the procedure.

## Changeable guidance

When this task relies on external APIs, tooling, platform support or other changing
contracts, apply [knowledge-freshness](../knowledge-freshness/SKILL.md) and update
affected local guidance from verified official evidence as part of the task.
