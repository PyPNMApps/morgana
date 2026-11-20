# Feature requirements

Status: proposed template; replace the example for the adopting project.
Derive requirements from the [architecture and software layout](architecture.md);
each requirement MUST link to its relevant architecture section.

## Purpose and scope

Describe the requested outcome, supported milestone and explicit exclusions.

## Requirement language

SHALL and MUST express mandatory obligations. SHALL NOT and MUST NOT express
mandatory prohibitions. Advisory proposals require an explicit mandatory,
excluded or deferred decision before baseline acceptance. Unresolved decisions
MUST be resolved before dependent implementation begins.

## Requirements

### R1

A cancelled or failed transformation SHALL preserve the previously accepted
result. Successful completion SHALL publish the validated result atomically.

Acceptance: failure or cancellation before/during/immediately before publication
leaves accepted identity/content unchanged; a late cancelled generation cannot
replace it. Successful completion atomically adopts the fully validated result. Delivery: [TASK-01 and TASK-02](checklist.md#ordered-work).
Design: [STAGE-01](architecture.md#stage-01-transform).

## Constraints and open decisions

Record compatibility, units, platform/resource bounds, decision owner and the
dependent work held pending. Assign stable IDs and exact link targets to every
additional requirement; do not use an advisory term as a substitute for a decision.
