# Saved data and language bindings

[Skill](../SKILL.md)

A saved document shared by desktop and headless APIs is an input contract. Test
an actual UI-produced fixture through every promised consumer, including generated
recipes and embedded representations rather than only already-decoded samples.
Shared decoding/materialization/validation owns reconstruction; adapters must not
silently drop settings, change defaults or require manual conversion.

Loading should remain idle unless execution-on-load is explicitly part of the
product contract. Preserve selected inputs, seeds, missing values, provenance and
resource limits. Presentation-only fields may be ignored under a documented policy.
Test bounded deterministic execution after load, meaningful outcome parity and
partial/cancellation behavior. A successful UI reopen is not headless compatibility.

Keep unsupported versions explicit or supply versioned migration. A manual workaround
is an open compatibility gap. Update all promised language examples and use native
idioms: structured exceptions/None in Python, typed errors/options in Rust.

Document result ownership and buffer lifetime; don't claim zero-copy without
layout/lifetime evidence. Keep optional binding runtimes out of core-only builds.
Manage interpreter locks and callback delivery in the adapter. Library APIs must
not exit the process or require parsing printed messages. Test error categories,
result reuse and core-only independence, as well as success parity.

Use the [compatibility matrix](../../../templates/project/compatibility-matrix.md).
