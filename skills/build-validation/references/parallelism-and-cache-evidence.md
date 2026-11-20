# Parallel tests and cache evidence

[Skill](../SKILL.md)

Split independent parameter cases into discoverable tests while preserving every
assertion, seed and combination. Isolate temporary files and process-global state.
Serialize genuinely shared resources or timing-sensitive scenarios. Keep examples,
doctests, alternate feature modes and UI checks in their required phases.

Bound worker count by actual CPU/memory needs. Measure full wall time, environment,
worker count, skipped/failed cases and cold/warm build state. A historical user
estimate is not a controlled baseline. Parallel execution is not result caching;
passing a reviewed subset is not full coverage. Preserve omitted-case manifests
and test-mode identity across retries; do not hide failures with automatic retries.

Preserve stable build profiles and artifacts. For reusable dependency caches,
fingerprint platform/architecture/toolchain/SDK/dependency inputs and exclude
workspace outputs that would disguise stale application builds. Verify restore
integrity and bound archive extraction. A cache uploaded on one run is not evidence
of a successful restore on the next compatible run. Never skip tests to warm caches.

When bootstrapping test tools, pin artifacts/hashes, check archive members and
cache verified downloads locally. No global installation is implied. Investigate
disk usage before cleanup; use an existing guarded owner, restrict cleanup to
verified generated targets and retain toolchains/downloads. Do not delete tracked
or redirected paths merely to make a build pass.
