# Requirements through implementation

## Inputs and first decision

Read the target's instructions, current revision/status, existing architecture and
active requirement records. Classify the task as new codebase or existing behavior.
A new feature in an existing application uses the existing-code path. If the user
requested only a plan, stop after the design/checklist; documents do not authorize code.

## Procedure

1. Write observable requirements with stable IDs, acceptance criteria, constraints
   and non-goals. Separate unknowns from accepted behavior. Avoid implementation
   choices disguised as requirements (for example, a class name).
2. For existing code trace entrypoints, owners and tests, then write the behavioral
   delta. For new code identify the minimal public operation and data model needed
   to demonstrate the first requirement.
3. Design responsibility/data/lifecycle/error boundaries. Record alternatives only
   where they explain the decision. Name the existing extension point or justify a
   new owner. Include a requirement-to-owner-to-test mapping.
4. Create dependency-ordered checklist items small enough to verify independently.
   Put prerequisites ahead of dependent UI or adapters. Mark blocked/partial items
   honestly; a combined item stays unchecked until all acceptance checks pass.
5. Implement a vertical slice, validate it, then continue. Update the design if the
   actual contract changes; do not leave an abandoned plan described as implemented.
6. At handoff reconcile requirements, architecture, checklist, user guidance and
   software facts. Report actual commands/results and any unsupported environment.

## Worked example

R1: cancelling an import leaves the previous accepted document usable.
Architecture: importer creates a candidate; document owner replaces accepted state
only after full validation. Cancellation invalidates the candidate generation.
Checklist: add candidate owner → cancellation checks → controller integration →
late-result regression → user help. Acceptance: cancel before parse, during parse
and immediately before completion; accepted document identity/content remain equal.

## Deliverables and failure cases

Use the local [requirements](../../../templates/project/requirements.md),
[architecture](../../../templates/project/architecture.md) and
[checklist](../../../templates/project/checklist.md) templates. A small task can
combine these sections in one file. Missing acceptance criteria or an unknown
ownership boundary is a design gap to resolve, not permission for broad refactoring.


[Skill](../SKILL.md)
