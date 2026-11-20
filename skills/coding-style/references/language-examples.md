# Language mappings and banner examples

[Shared rules](procedure.md)

These are documentation patterns, not complete source files. Replace bracketed
header placeholders only after verifying project ownership and component licensing.

## File banners

C/C++, Java, Rust, JavaScript/TypeScript and CSS use valid block comments:

```text
/*
 * Copyright [creation year or preserved range] [verified holder]
 * SPDX-License-Identifier: [approved identifier or expression]
 */
```

Python/shell use comments, preserving an existing executable shebang first:

```text
#!/usr/bin/env python3
#
# Copyright [creation year or preserved range] [verified holder]
# SPDX-License-Identifier: [approved identifier or expression]
#
```

For shell use its actual interpreter; do not copy the Python shebang. QML supports
comment banners. Preserve language-required directives and source encodings.

## Java / object-oriented public members

```java
/**
 * Owns unique record identifiers for one editing session.
 *
 * <p>Identifiers are non-null and immutable once added. Instances are confined
 * to their owning thread; callers must not share them concurrently.
 */
public final class RecordIndex {
    private final java.util.Set<String> identifiers = new java.util.HashSet<>();

    /**
     * Creates an empty session index without external resources.
     */
    public RecordIndex() {
    }

    /**
     * Adds an identifier without replacing an existing identifier.
     *
     * @param identifier non-null, nonblank identifier; whitespace is preserved
     * @return true if newly added; false if already present
     * @throws IllegalArgumentException if identifier is null or blank
     *
     * Expected set insertion is amortized O(1); validating and hashing a new
     * string also costs O(k) for k characters. Storage grows with unique IDs.
     */
    public boolean add(String identifier) {
        if (identifier == null || identifier.isBlank()) {
            throw new IllegalArgumentException("identifier must be nonblank");
        }
        return identifiers.add(identifier);
    }
}
```

Use the project's Java formatter and Javadoc checks. Methods/fields use lower
camel case and types upper camel case; constants use its established convention.
Do not introduce inheritance solely for code sharing.

## Rust

```rust
/// Finds a target in an ascending, sorted slice of record identifiers.
///
/// # Arguments
/// * `sorted_ids` - Caller-owned IDs, sorted in ascending order.
/// * `target` - Identifier to locate.
///
/// # Returns
/// An index of a matching ID, or `None` if absent. For duplicate IDs, the
/// selected matching index is unspecified. No input is mutated or retained.
///
/// # Complexity
/// O(log n) comparisons and O(1) auxiliary memory for n IDs. The caller owns
/// sorting cost; an unsorted slice may yield an incorrect result.
pub fn find_id(sorted_ids: &[u64], target: u64) -> Option<usize> {
    sorted_ids.binary_search(&target).ok()
}
```

Use rustfmt/Clippy, snake_case functions/fields, UpperCamelCase types and
SCREAMING_SNAKE_CASE constants. Use Result for recoverable failures and Option for
absence. Name explicit lifetimes by their relationship when useful, such as
`'input`; use inferred lifetimes where no name is needed. Do not invent `# Errors`
or `# Panics` sections for operations without those caller-visible behaviors.

## Python

```python
class PayloadPolicy:
    """Validate byte counts against an application allocation policy.

    Instances retain only an integer limit and perform no I/O. The limit is
    application policy, not a claim about a file format's permitted size.
    """

    def __init__(self, maximum_bytes: int) -> None:
        """Create a policy with a positive maximum.

        Args:
            maximum_bytes: Largest allowed byte count.
        Raises:
            ValueError: If the maximum is not positive.
        """
        if maximum_bytes <= 0:
            raise ValueError("maximum_bytes must be positive")
        self._maximum_bytes = maximum_bytes

    def accepts(self, length_bytes: int) -> bool:
        """Check whether a byte count fits without allocating a payload.

        Args:
            length_bytes: Candidate count; negative counts are rejected.
        Returns:
            True for counts from zero through the configured maximum.
            False otherwise. Does not mutate the policy.
        """
        return 0 <= length_bytes <= self._maximum_bytes
```

Annotations are not runtime validation of untrusted types; validate external
input in the adapter. Use project-selected formatting/linting, snake_case
functions and UpperCamelCase classes; docstrings live inside definitions.

## C++ / Qt, TypeScript and shell

C++ public classes and members use Doxygen banners with `@param`, `@return` and
`@throws` where applicable. Document QObject parent ownership, signal delivery,
thread affinity and object lifetime; use RAII and the existing naming/clang-format
policy. Qt properties/signals document units, notification and accepted/draft state.
QML owns presentation, not a second domain implementation.

TypeScript exported classes/functions use multiline TSDoc/JSDoc; document Promise
rejection, cancellation and null/undefined explicitly. Prefer typed unknown input
plus validation to `any` or unchecked assertions. Use the selected formatter/linter;
await asynchronous failures at their responsible boundary.

Shell entrypoints and reusable functions use comment banners describing arguments,
stdout/stderr, exit codes, side effects and prerequisites. Use explicit Bash when
Bash syntax is needed, quoted arrays, strict mode and deliberate error handling.
Strict mode alone does not make conditional/pipeline failures safe. Never eval
configuration. Python/tooling adapters should stay independent of presentation.
