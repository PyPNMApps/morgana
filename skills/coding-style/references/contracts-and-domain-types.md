# Contracts and domain types

[Skill](../SKILL.md)

Use public documentation to specify behavior: purpose, arguments/units, ownership,
returns/missing values, errors, side effects and concurrency. Include only applicable
sections; do not invent panic-free/thread-safe guarantees or generate accessors
just to document them. Translate conventions into the target language's idiom.

Name types for meaning rather than width. Aliases improve vocabulary but may not
prevent identity mixing; use validated wrappers/newtypes when that distinction is
required. Do not change wire widths, overflow behavior or accepted values just to
introduce names. Centralize constants only when semantics match; equal numeric
values are not sufficient. Keep format-specific sentinels with their format.

Name Rust lifetimes for the data they borrow when it clarifies relationships.
Keep constants/types, constructors and public/private operations in a coherent
order without changing initialization behavior. Explain regular expressions with
an example, whole-input/submatch behavior and important exclusions; distinguish
extraction from validation.

Apply conventions incrementally to touched code. Preserve upstream/generated
sources and licenses. A private repository does not authorize relabeling copied
code, inventing copyright owners or discarding notices. Exact banner syntax and implementation-language choices remain project policy.
