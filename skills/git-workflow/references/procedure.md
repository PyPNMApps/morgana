# Review and prepare a local save

[Skill](../SKILL.md) · [Implemented helper](../../../tools/git/git-save.sh)

1. Inspect status, unstaged/staged diffs and every untracked file. An initial
   repository has no HEAD; review its entire non-ignored candidate. Preserve
   existing staged content and identify overlapping/concurrent edits explicitly.
2. Review architecture, checklist and feature design against the whole candidate.
   Update material status/ownership gaps; leave partial items unchecked. Source
   validation findings remain visible even when unit tests pass.
3. Read the actual helper and run the project validation. Document exact results,
   omissions and known limitations. Do not invoke an absent helper or invent flags.
4. Prepare one command from the actual target root using --commit-msg and one
   quoted multiline argument. Feature:, BugFix: or Documentation: begins the
   subject; follow with - details and - Tests:. Every line is at most 60 characters.
5. Report the command as prepared, never executed. Save includes all non-ignored
   current changes plus staged content, and never pushes, tags or bumps versions.

The helper stages the candidate before running validation. Failed validation
leaves that candidate staged for review; it does not discard files or reset the
index. It checks whitespace, nonempty content, HEAD/index stability and changes
created during validation. Tests exercise it only in disposable repositories.

Example message:

```text
Feature: Preserve initial toolkit checkpoint
- Record existing code and unfinished validation
- Add portable local guidance and save tooling
- Tests: Local workspace and tooling checks pass
```

A dirty index, missing Git identity, failed gate, changed candidate or concurrent
HEAD movement is a concrete failure to resolve. Do not bypass the gate or convert
a test failure into success. No push helper exists yet; a future implementation
needs known remote/ancestry, clean state and separately authorized publication.
