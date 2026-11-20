# Consistent engineering rules

[Skill](../SKILL.md) · [Language examples](language-examples.md) ·
[Review template](../../../templates/project/coding-review.md)

## Apply the existing architecture

For existing code, inspect instructions, formatter/linter settings, ownership,
public consumers and tests before editing. Extend the responsible module and
reuse its types, error model and validation. Keep compatibility through existing
interfaces or deliberate migrations. For new code, record those decisions before
implementation. Neither case permits an unrelated rewrite or automatic formatting
of the whole repository. Review full changed functions, not only added lines.

## Formatting and comments

Use the checked-in formatter as the mechanical authority; record the version and
check command. For a new project select indentation, line width, import ordering,
newline policy and formatter once in configuration. Do not invent a universal
line width across languages. Use consistent whitespace, a final newline, no
trailing whitespace and no mixed indentation. Separate logical steps with blank
lines; do not align columns manually where the formatter will undo them.

Use multiline if/else bodies, including guard returns and error branches. Use
braces in brace-based languages. Do not hide side effects in ternaries or Boolean
short-circuit chains. Keep match/switch alternatives explicit and preserve unknown
cases. Prefer guard clauses when they reduce nesting without changing cleanup.

Put one blank line before standalone explanatory comments; keep each comment
block intact. If formatting removes that separation, move the comment above its
owning statement. Comments explain intent, invariants and non-obvious decisions,
not a paraphrase of the code. Document regex intent, synthetic input/output,
capture groups, anchoring, flags and exclusions. Explain extraction versus validation.
Keep TODOs actionable with the owning issue/checklist ID; remove stale claims.

## Naming and magic values

Use descriptive domain names, explicit units and bounds: `timeout_ms`,
`payload_length_bytes`, `end_exclusive`, `records_by_id`. Name types by meaning,
not just width. Use unit wrappers/newtypes where mixing values is a correctness
risk; aliases alone may not enforce identity. Avoid Boolean parameter puzzles;
use named options or enums when call sites otherwise hide intent.

Name protocol signatures, offsets, sentinels, conversion factors, tolerances,
retry budgets, resource limits and repeated configuration defaults. Define each
constant with its unit, meaning and evidence or rationale. Distinguish protocol
requirements, application safety policy, defaults and user settings. Validate
configurable values at the boundary. Do not make every constant user-configurable.

Ordinary zero origins, increments and obvious mathematical identities need no
artificial names. Equal values do not imply shared semantics: an unavailable-byte
sentinel and an unsigned maximum can both be 255 and need separate owners.
Keep format constants beside the format; share conversions only when semantics
match. Never create a catch-all constants module merely to remove literals.
Use checked arithmetic for input-controlled lengths/offsets and explicit conversion
or rounding rules. Floating-point comparisons need a domain-derived tolerance,
not an unexplained epsilon copied from another calculation.

## Classes, members and responsibility

Document every public class/type/interface with purpose, invariants, lifecycle,
ownership, mutability and concurrency rules where relevant. Prefer cohesive classes
and composition; introduce inheritance only for a real substitutable contract.
Keep fields private by default; expose public data when the API deliberately
represents a value/DTO and document its constraints. Do not generate accessors
solely to add banners. Do not expose mutable internal collections accidentally.

Place constants/types before implementation, constructors/factories before public
operations, then private helpers, retaining related operations together. Keep
interface/trait implementations cohesive. Never reorder initialized fields or
statements when order affects behavior. Constructors establish valid state or
fail explicitly; document cleanup/disposal, callback ownership and cancellation.
Do not invoke overridable behavior on incompletely constructed objects.

## Required public documentation banners

Every explicitly declared public/exported constructor, method, function, accessor,
override and trait/interface implementation needs a multiline documentation banner.
Public fields/properties need documented meaning, units, valid range and mutability
where relevant. A repeated name or bare inherited-doc reference is insufficient.
Summarize the contract locally and link shared details without duplicating essays.

Cover purpose; every parameter/type parameter; preconditions and units; return and
empty/missing semantics; intentional failures; side effects and state changes;
ownership/borrowing; cancellation and threading where applicable. Include complexity
for collection, computational or potentially expensive operations, defining input
sizes. Include examples when correct use is not obvious. Omit inapplicable sections
rather than inventing guarantees. Update banners with signatures and behavior.

Use rustdoc, Javadoc, Doxygen, Python docstrings, JSDoc/TSDoc or shell comment
banners as appropriate. Keep attributes/decorators attached to their declarations;
Python docstrings belong inside the definition. Private helpers need explanations
when behavior is non-obvious, not mandatory copied public boilerplate.

## Errors, resources and boundaries

Represent expected failures explicitly with the project's typed errors or exception
model. Preserve causes and useful scalar context; never turn an error into an
apparently successful empty result. Missing, zero, unsupported and invalid are
separate states. Validate untrusted inputs before allocation or mutation. Use RAII,
context managers or try/finally for resources. Avoid broad exception swallowing,
production unwrap/panic on external input, and unbounded retries.

Log a terminal failure once at its responsible application boundary. Libraries
return errors and do not configure global logging. Keep secrets, payloads and large
arrays out of logs. Keep stdout suitable for intended data output. Do not make
behavior depend on the log level. Bound files, queues, allocations, work and retry
time. Keep blocking work off the UI thread; cancel cooperatively and reject stale
completions. Shared business calculations and serialization have one owner reused
by CLI/UI/API adapters. Presentation formats values rather than reimplementing rules.

## Complexity and performance

Require the best justified algorithm for the workload, not O(log n) for every
operation. Reading n items or producing n outputs has an Omega(n) lower bound.
Comparison sorting is generally O(n log n); scanning once can be optimal.
Binary search requires an appropriate ordered structure. Hash lookup is expected
O(1) with assumptions, not a universal worst-case guarantee.

Define n and other dimensions, worst-case/expected/amortized time as appropriate,
auxiliary memory, output memory and construction costs. Account for copies,
sorting, serialization, database/network calls and hidden work inside library APIs.
A logarithmic lookup after sorting every request is not an O(log n) request.

Example: matching m selected IDs against n records by repeated scans costs O(mn).
Building an index once costs expected O(n) time and O(n) extra memory, then expected
O(m) lookups. A reusable balanced ordered index offers O(log n) lookup with update
costs. A single scan can still be preferable for one query or tiny inputs. Preserve
duplicate/order semantics and define invalidation before adding a cache/index.

For hot paths, compare realistic and adversarial sizes, measure end-to-end latency
and peak memory, and record environment/input sizes. Timing alone does not prove
asymptotic complexity. Avoid brittle wall-clock unit tests; use meaningful bounded
work/scaling checks where appropriate. Record deliberate tradeoffs; do not replace
readable bounded code with complexity that brings no measured benefit.

## Copyright and SPDX file banners

New project-owned source and test files require a multiline copyright/SPDX banner.
For touched existing files lacking one, first establish ownership and the applicable
repository license policy. Reuse the actual holder, creation year and approved SPDX
identifier/expression for that component; never copy an unrelated copyright holder or assign
an unrelated component license to another project. Private visibility is not a license.
Unresolved ownership/license is a recorded decision gap, not permission to invent it.

Preserve original start years and notices. Extend the end year for current changes
when the project's policy requires it; do not mass-edit untouched files at year
rollover. Keep third-party notices and license terms intact. Headers must agree
with package metadata and required LICENSE/NOTICE material. A header is not a
replacement for those files. This is repository policy, not a legal determination.

Use valid comments before imports/module docs; retain executable shebang first
and Python encoding cookie in its required position if present. Do not insert
comments into JSON, binaries, generated artifacts or lockfiles; use applicable
metadata/provenance. Preserve generated/third-party source headers rather than
relabeling them. See the placeholder banner examples before adoption.

## Acceptance

Use the linked review template. Check formatting with the project's actual tools;
review banners against signatures and error paths, constants against evidence,
and algorithms against complete work. Test changed behavior and boundary failures.
Documentation/header-only changes need relevant syntax/format/documentation checks,
not invented runtime tests. Report commands actually run and explicit limitations.
