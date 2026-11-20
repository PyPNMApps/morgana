# Select and measure validation

## Establish the gate

Inventory languages, independent packages/locks, feature modes, generated code,
UI adapters and platform deliverables. Define one project-owned validation command
using the [validation contract](../../../templates/tools/validation.md). Local
push and hosted workflows call that owner; avoid copied command lists drifting apart.

Classify the change: docs/links, isolated behavior, shared API/serialization,
UI/native integration, packaging or dependency/toolchain. Pick checks covering
those risks; broaden for shared consumers. Do not run every simulation merely for
a label edit, and do not use a label test to claim schema compatibility.

## Parallelism and failure handling

List independently schedulable cases and shared resources. Assign unique temporary
paths/ports or serialize cases that actually share them. Bound concurrency by CPU
and peak memory. Keep mandatory examples, feature-mode checks and doctests outside
or inside the pool explicitly. Each failure remains visible; do not replace a
flaky failure with automatic success after retries.

Record exact command/revision/toolchain, elapsed wall time, cold/warm build state,
case totals, omissions and failure artifacts. Counts alone do not prove coverage;
map old assertions when reorganizing. Cache identity includes OS, architecture,
toolchain, SDK, lock/dependency and build-profile inputs.

## Completion criteria

A check passes only on its stated environment. Installed lifecycle, interactive
native behavior and hosted jobs need their own evidence. Use
[validation-matrix.md](../../../templates/project/validation-matrix.md). Retain
build caches; cleanup must use a guarded project-owned mechanism and exclude
tracked sources, toolchains and downloads. Missing prerequisites are reported,
not silently converted into skipped passing tests.


[Skill](../SKILL.md)
