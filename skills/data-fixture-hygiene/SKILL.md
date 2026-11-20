---
name: data-fixture-hygiene
description: Prepare reusable binary fixtures and deterministic packaged examples while preserving provenance and semantic identity.
---

# Data Fixture Hygiene

## Prepare data explicitly

Use a format-aware transformation rather than byte-pattern replacement. Inventory
identity fields in decoded headers, metadata, filenames and archive members.
Maintain a consistent alias for the same source across channels/times and distinct
aliases for distinct sources; collapsing identities can invalidate comparisons.
Keep original evidence in its authorized location and record the transformation,
source hash, sanitized hash and applicable license separately.

Fail on unknown layouts rather than guessing offsets. Verify that non-sensitive
semantics remain unchanged through the public decoder. Sanitizing data does not
sanitize screenshots, existing logs or Git history; inspect those separately.
Do not copy customer captures into generic skill examples.

## Package deterministically

Keep curated source fixtures expanded with an explicit inventory of relative
paths, sizes and hashes. Packaging runs read-only hygiene first, then creates new
outputs; it must not silently sanitize or rewrite source fixtures during a build.
Normalize archive metadata where the format permits reproducibility and compare
repeated output bytes. Reject extra/unapproved files, traversal paths, links and
unbounded expanded data. Failure must not leave an apparently complete payload.

Share one bundling owner across platform builders. Test resource discovery from
the installed executable location, missing/corrupt files and packaged bytes—not
only the source fixtures. Preserve notices and original attribution. Package
size ceilings and alias schemes are product policies, not universal constants.

Use the [fixture review](../../templates/project/fixture-review.md).

[Catalog](../README.md)

## Standalone procedure

Read the [operational guide](references/procedure.md) for inputs, implementation
steps, examples, failure cases and acceptance checks. Required resources are in
the foundation; no other repository is required or referenced by the procedure.

## Changeable guidance

When this task relies on external APIs, tooling, platform support or other changing
contracts, apply [knowledge-freshness](../knowledge-freshness/SKILL.md) and update
affected local guidance from verified official evidence as part of the task.
