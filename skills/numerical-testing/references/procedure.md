# Independent numerical and parser checks

## Select an oracle

List the behavior under test and expected-value origin: hand-worked arithmetic,
independently transcribed reference, another implementation or empirical observation.
Do not compute expectations with the production helper being tested. A round trip
is useful but cannot reveal a shared encoder/decoder mistake.

Example for a signed fixed-point value with four fractional bits: raw 0 maps to 0,
1 to 0.0625, -1 to -0.0625, 24 to 1.5. Test raw extrema separately for the selected
wire width. These are synthetic arithmetic examples, not protocol-specific sentinels.
Test byte ordering, scaling selection and unavailable markers through the parser
owner as well as the numeric helper. Missing is not zero.

## Parameter and failure matrix

Cover legal boundaries, just-outside inputs, truncation, declared-length mismatch,
trailing bytes, unsupported types, overflow and allocation/runtime limits. For
iterative algorithms assert status, iterations and truth separately. Preserve
failed cases as evidence instead of filtering them out of plots/statistics.

Choose exact equality for exactly representable values; otherwise state absolute/
relative tolerance and why it is adequate. Seeds reproduce stochastic input, not
wall-clock duration. Cancellation keeps completed work under the declared contract.
Turning diagnostics on/off must not alter random draws or algorithm decisions.

Use [validation-matrix.md](../../../templates/project/validation-matrix.md) and
map each fixture/assertion to a discovered test target. After test splitting,
compare combinations and expectations, not just increased case counts.


[Skill](../SKILL.md)
