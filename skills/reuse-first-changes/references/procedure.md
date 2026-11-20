# Existing-code change procedure

## Build an evidence-backed change map

Search the target checkout for the visible action, public API, model, serializer,
configuration key and tests. Follow the real call chain rather than stopping at a
matching symbol. Record caller → adapter → owner → dependency and the reverse
error/result path. Check build registration and all promised public consumers.

For each candidate write: exact path/symbol, supported semantics, unmet requirement,
and reuse/extend/candidate/reject disposition. Read cancellation, lifetime, thread,
units, missing-value and persistence contracts before choosing reuse. Candidate
means evidence is missing; do not present it as implemented reuse.

## Choose the smallest coherent change

Extend the owner when the responsibility fits. Extract a helper only when multiple
real callers need the same semantics. Preserve re-exports or migration adapters
when public imports must remain compatible. Do not widen visibility merely to
avoid understanding an ownership boundary. Keep optional new behavior disabled or
explicit where compatibility requires it.

Example: a UI export needs an additional derived field also used by a CLI. Extend
the core result/serializer, update both adapters and fixtures, and test equality.
Do not add the calculation independently to QML and CLI text formatting.

## Regression review

Verify old default behavior, new behavior, invalid input, cancellation and saved
state compatibility. Search for old imports, duplicate implementations, stale
feature registrations and obsolete docs. Missing in-tree callers do not prove an
external interface is unused. Keep unrelated formatting separate.

Deliver the reuse table inside the [architecture template](../../../templates/project/architecture.md)
and resulting requirement/checklist mapping. Record a rejected candidate's reason
so the next maintainer does not repeat the same investigation.


[Skill](../SKILL.md)
