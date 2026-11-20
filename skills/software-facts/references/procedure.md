# Maintain durable software facts

## Before investigating

Search the facts index by behavior and likely owner. Check the recorded revision
and refresh triggers against the active checkout. Use a fact as a navigation aid,
not an excuse to trust old runtime claims after its owner changed.

## Write a useful fact

Use [software-fact.md](../../../templates/project/software-fact.md). One entry
answers one coherent question: direct answer, paths/symbols, revision/date,
evidence category, limits and refresh trigger. Source-confirmed means the code
was read. Runtime-observed means the command/environment/result are available.
Inferred means the conclusion still needs validation. Proposed belongs in design.

Example question: does Cancel keep the previous document? Answer: the accepted
owner changes only in commit_candidate after schema validation. Evidence: named
owner/cancel/completion symbols and the late-completion regression. Limit: the
native window-close route has not been exercised. Refresh: any candidate lifecycle
or close-handler change. This is more useful than 'Cancel works'.

## Update and retire

When editing an owner, search facts that name it. Correct invalid claims in the
same change, preserve a brief historical distinction when useful, and link a
replacement instead of maintaining competing answers. Keep evidence concise; do
not paste full logs or secret payloads. Relative source paths and symbols are more
stable than line numbers alone.

Index new facts with searchable terms and link from related skill/navigation pages.
A generic lesson is promoted into the foundation's canonical skill only after removing local
policy and documenting acceptance/limits. Project facts remain local; the foundation facts
about its own tooling remain in the foundation. Do not automatically import external changes.


[Skill](../SKILL.md)
