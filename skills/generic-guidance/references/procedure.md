# Write once for future repositories

[Skill](../SKILL.md) · [Learning update](../../../templates/project/learning-update.md)

## Scope and inputs

Identify the reusable task, required inputs, preconditions, decisions, outputs,
failure behavior and acceptance evidence. Preserve technical detail; generic does
not mean a short abstract summary. Distinguish an engineering rule from a particular
product's language, numeric budgets, supported OS list or one-time authorization.

## Procedure

1. Select the existing skill owner. Follow Architecture → Requirements → Developer checklist
   before implementation. New and existing codebases remain separate workflows:
   new projects choose documented defaults; existing projects reuse current owners
   and preserve contracts with the smallest coherent changes.
2. Write the method in original generic prose, including enough local examples to
   use it without asking where it came from. Use fictional neutral component names,
   project-relative paths and explicit configurable decisions with units/rationale.
3. Preserve non-obvious behavior: cancellation, stale callbacks, error boundaries,
   migration requirements, security gates and actual validation limitations.
   Replace a hard-coded product decision with selection criteria, not vagueness.
4. Link working tools or clearly labeled implementation templates in the adopted
   bundle. Carry the dependency closure when copying skills into a future repo.
   Do not refer to unavailable helpers or an author's workstation directories.
5. Remove lineage tables, prior repository names, source commit inventories and
   lesson-to-project mappings. Retain official technical citations for changing
   external contracts and data provenance needed to interpret fixtures/results.
6. If actual source code/assets/text are reused, keep required attribution under
   third-party-reuse. Do not call copied or adapted material original merely because
   its naming changed. Do not move confidential implementation details into a
   generic skill; retain only authorized, independently usable instruction.
7. Validate navigation, skill metadata and portability, then review a realistic
   new-project and existing-project scenario. Report what was actually executed.

## Example and review

Instead of 'use the old application's release script', explain canonical version
ownership, clean-tree checks, validation, annotated tags, immutable publication and
retry behavior, then link the local release helper/template. Preserve those details
when removing the reference. Instead of copying a product's 30-second timeout,
require a bounded deadline with a justified default and cancellation behavior.

Accept the result when another developer can apply it in a new repository using
only its adopted bundle and relevant official documentation. A lesson map is not
needed; actual third-party attribution still accompanies reused material.
