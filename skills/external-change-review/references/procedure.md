# Review work without depending on another chat

[Skill](../SKILL.md) · [Review record](../../../templates/project/external-change-review.md)

## Establish evidence and scope

Read local instructions, architecture, requirements/checklist and software facts.
Record the checkout, branch and HEAD before edits. Inspect all three work states:

```bash
git status --short
git diff --name-status
git diff --cached --name-status
git ls-files --others --exclude-standard
git log -5 --oneline
```

Then inspect actual unstaged and staged diffs, not just their statistics. Read
untracked files explicitly: git diff omits them. Review renames, deletions, file
modes, symlink destinations and binary/large files using appropriate tools. Do not
print secret contents; scope sensitive-file checks to metadata or redacted findings.
Ignored personal data and build caches are not part of an automatic review sweep.

For already committed work, identify an agreed last-reviewed revision. Inspect
`git diff BASE HEAD` and relevant `git log BASE..HEAD`; replace BASE with the
verified revision. A merge base against a target branch can identify a PR boundary,
but is not automatically the last reviewed state. Review constituent commits when
history matters, such as reverted code, release gates or migration sequencing.
If no reliable baseline exists, state the chosen boundary and limitation; review
current affected behavior without claiming complete coverage or inventing authorship.

Keep pre-existing staged changes separate. Do not reset, stash, stage, amend,
checkout over or delete unfamiliar changes. Compare state again before handoff;
if concurrent work alters reviewed paths, refresh the affected review rather than
claiming the old result applies. Ask only when overlapping changes make intended
behavior or safe ownership unclear. Approval of a review is not approval to publish.

## Match the changes to the right rules

Read the applicable skills, not every skill indiscriminately:

| Changed area | Review focus |
| --- | --- |
| Existing behavior | Requirements → Architecture → Checklist; reuse current owners and preserve compatibility |
| Source code | Formatting, public contracts/banners, constants, errors, bounded work and justified complexity |
| APIs or persistence | Shared ownership, schema/migrations, producer/consumer compatibility, cancellation and accepted state |
| UI | Layout, themes, accessibility, native behavior, presentation versus domain ownership |
| Setup or Git/release tools | Modular entrypoints, read-only modes, no-clobber behavior, validation and authorization boundaries |
| Reusable skills/docs | Generic terminology, complete local resources, source-of-truth consistency and linked navigation |
| Third-party material | Copyright/SPDX, permission, license texts, notices and packaging obligations |
| External contracts | Official-source freshness for the relevant version; do not silently upgrade pins |

Archived reference snapshots are historical, not active policy. Do not genericize
archived originals or execute archived tooling merely because they appear in a
large staged diff. State whether archive bytes were verified or only metadata and
scope were inspected. Keep actual reused-material attribution intact.

## Semantic review and focused corrections

Trace callers, data/state ownership and failure paths around each changed behavior.
A grammatically correct diff can still introduce a hidden prerequisite or relax a
backend restriction. Verify terms are defined locally and examples can be used in
a future repository. Do not turn one application's workflow, names, numeric budget
or one-time permission into a universal rule.

Classify findings by concrete impact with file/section and evidence. Separate
bugs or contract gaps from optional preferences. Fix authorized issues in the
smallest coherent change; preserve useful work. For a review-only request, report
findings without editing. Update architecture, facts, guides and checklists where
the correction changes their contract. Never mark an unavailable integration test
complete just because another session said it passed.

## Validation and handoff

Inspect changed executable validation scripts before running them. Choose checks
proportional to the change using the target's actual commands. Documentation work
needs links, metadata and relevant example/resource validation; behavior changes
need meaningful tests for the affected contracts. Distinguish static checks, local
tests, live provider calls, native OS execution and hosted CI. Do not execute an
installer, network inference or release as an incidental review check.

Record reviewed base and working state, applicable rules, findings/fixes, commands
and actual results, remaining gaps and any concurrent changes. Recheck diff and
index preservation. A clean review means no findings within the stated scope and
evidence; it is not a guarantee of universal compliance.

## Scenarios

- Another session adds a demo UI rule with an undefined startup lock: keep the
  useful simulated-output labeling rule, define the restriction conditionally,
  and do not introduce a new global policy.
- A staged release change coexists with unstaged docs: review them separately,
  correct only the authorized scope and leave the index intact.
- A handoff says tests passed but code changed afterward: rerun the relevant
  checks on the actual candidate; retain the earlier report as historical evidence.
- A new untracked helper is referenced by a skill: inspect it and its local
  dependencies, not just the tracked Markdown diff, before accepting portability.
