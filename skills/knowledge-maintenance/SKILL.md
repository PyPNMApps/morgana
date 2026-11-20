---
name: knowledge-maintenance
description: Promote project lessons into reusable skills and keep GitHub documentation discoverable.
---

# Knowledge Maintenance

Capture the concrete problem, evidence, resolution, limitations and reusable principle. Keep project facts local; promote generalized guidance only after checking scope and confidentiality. Write self-contained generic guidance without repository lineage maps. Preserve required notices for actual third-party reuse; never import sensitive payloads or unauthorized code.

When work in a consuming project changes reusable skill guidance, reconcile it
with the canonical skill owner in the same task if that checkout is available and
its modification is within the authorized scope. Consumer work alone does not
authorize edits to a separate checkout. Keep the the foundation
wording generic and independently usable; leave project-specific behavior and
evidence in the consumer. Do not create a consumer-local synchronization skill or
automatically overwrite other consumers. If the canonical checkout cannot be updated, prepare a generic learning update
locally and report the pending reconciliation explicitly.

Update the existing skill when possible. Separate proposed, locally validated and platform-validated guidance. Adopt foundation updates explicitly in downstream projects and record the source revision; never overwrite local customizations automatically.

Keep README task-oriented with relative links and heading anchors. Maintain folder indexes and searchable synonyms (software facts/sw-facts, Qt/QML, setup/bootstrap). Repair incoming links after moves and distinguish archive from maintained guidance. Use the [lesson template](../../templates/project/lesson.md).

[Skill catalog](../README.md)

## Standalone procedure

Read the [operational guide](references/procedure.md) for inputs, implementation
steps, examples, failure cases and acceptance checks. Required resources are in
the foundation; no other repository is required or referenced by the procedure.

## Changeable guidance

When this task relies on external APIs, tooling, platform support or other changing
contracts, apply [knowledge-freshness](../knowledge-freshness/SKILL.md) and update
affected local guidance from verified official evidence as part of the task.

Apply [generic-guidance](../generic-guidance/SKILL.md) to reusable skills for future repositories; keep required notices for actual reused material under [third-party-reuse](../third-party-reuse/SKILL.md).
