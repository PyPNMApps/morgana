---
name: coding-style
description: Apply shared code organization principles with language-specific conventions when implementing changes.
---

# Coding Style

Follow the target project's established formatter, naming, license and documentation conventions. Keep entrypoints focused on wiring and split modules by responsibility, not arbitrary file length. Prefer descriptive names, explicit units, typed errors and documented public contracts. Preserve copied copyrights and license obligations; private visibility does not cancel them.

Python: annotate public and changed interfaces, keep CLI/API adapters thin, isolate environments and use project-owned test/lint configuration. Rust: use domain types and explicit errors, keep reusable libraries independent of UI, and preserve lockfiles for reproducible application builds. Java: separate models/services from presentation and derive version metadata from the build owner. Shell: use Bash explicitly, strict mode, quoted arrays, prerequisite checks and meaningful error exits. Never use eval for configuration.

Extend existing formatting rather than reformatting unrelated code. Configuration starters are in [templates](../../templates/README.md); they are starting policies, not proof of supported tool versions.

[Skill catalog](../README.md)

## Detailed lessons

For applicable changes, read [contracts and domain types](references/contracts-and-domain-types.md).

## Standalone procedure

Read the [operational guide](references/procedure.md) for inputs, implementation
steps, examples, failure cases and acceptance checks. Required resources are in
the foundation; no other repository is required or referenced by the procedure.

## Shared requirements

Apply the [detailed rules](references/procedure.md) for formatting, magic values,
class invariants, public member banners, errors, resources, complexity and SPDX.
Use [language examples](references/language-examples.md) to express the same
contracts idiomatically. All explicitly declared public members need meaningful
multiline documentation; new owned source/test files need verified copyright/SPDX
banners. Review with the [coding record](../../templates/project/coding-review.md).
An O(log n) target applies only where the operation permits it; account for full
input/output, preprocessing and memory costs rather than promising it universally.

## Changeable guidance

When this task relies on external APIs, tooling, platform support or other changing
contracts, apply [knowledge-freshness](../knowledge-freshness/SKILL.md) and update
affected local guidance from verified official evidence as part of the task.

For actual copied/adapted material apply [third-party-reuse](../third-party-reuse/SKILL.md); file banners do not replace distribution notices or license text.
