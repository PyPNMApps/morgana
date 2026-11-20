# Software development checklist

Read [requirements](requirements.md) and [architecture](architecture.md) first.
Status: planned template; replace example IDs/paths for the adopting project.

## Completion rules

Each task MUST link precise requirements and architecture, identify prerequisites,
owner/test placement and observable acceptance. Partial work MUST remain unchecked.
Design completion MUST NOT imply implementation or runtime acceptance. Resolve
advisory choices before dependent work; preserve stable IDs when splitting tasks.

## Ordered work

- [ ] TASK-01: Establish the bounded candidate owner and validation contract.<br>
  Requirements: [R1](requirements.md#r1). Architecture: [STAGE-01](architecture.md#stage-01-transform).<br>
  Depends on: none. Paths: [planned owner/test files](architecture.md#planned-code-paths).<br>
  Acceptance: valid/invalid/boundary inputs preserve the accepted-state contract;
  record actual test command, result and limitations in the feature record.
- [ ] TASK-02: Integrate behavior and validate cancellation/failure acceptance.<br>
  Requirements: [R1](requirements.md#r1). Architecture: [STAGE-01](architecture.md#stage-01-transform).<br>
  Depends on: TASK-01. Paths: [planned owner/test files](architecture.md#planned-code-paths).<br>
  Acceptance: cancellation and late results preserve prior accepted state, with
  completed evidence recorded before checking this task.
- [ ] TASK-03: Reconcile delivered behavior, compatibility and user guidance.<br>
  Requirements: [R1](requirements.md#r1). Architecture: [requirement mapping](architecture.md#requirement-mapping-and-validation).<br>
  Depends on: TASK-02. Acceptance: requirement, design and runtime evidence agree;
  documented unsupported/deferred cases remain visible.

## Coverage and evidence

| Requirement | Tasks | Architecture owner | Evidence / state |
| --- | --- | --- | --- |
| [R1](requirements.md#r1) | TASK-01, TASK-02, TASK-03 | [STAGE-01](architecture.md#stage-01-transform) | Pending; record actual commands/results in the feature record. |

Replace this example with the full requirement inventory. Validate target anchors,
unique IDs, dependency order/cycles and coverage, including cross-cutting/deferred
requirements. Requirements name delivery IDs; task entries link back to them.
