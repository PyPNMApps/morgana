# Feature requirements

Status: proposed template; replace the example for the adopting project.

## Purpose and scope

Describe the requested outcome, supported milestone and explicit exclusions.

## Requirement language

SHALL and MUST express mandatory obligations. SHALL NOT and MUST NOT express
mandatory prohibitions. Advisory proposals require an explicit mandatory,
excluded or deferred decision before baseline acceptance. Unresolved decisions
MUST be resolved before dependent implementation begins.

## Requirements

### R1

Cancelling an import SHALL preserve the previously accepted document.

Acceptance: cancellation before/during/after parsing and a late completion leave
accepted identity/content unchanged; valid completion adopts a fully validated
candidate atomically. Delivery: [TASK-01 and TASK-02](checklist.md#ordered-work).
Design: [STAGE-01](architecture.md#stage-01-transform).

## Constraints and open decisions

Record compatibility, units, platform/resource bounds, decision owner and the
dependent work held pending. Assign stable IDs and exact link targets to every
additional requirement; do not use an advisory term as a substitute for a decision.
