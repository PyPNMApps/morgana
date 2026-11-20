# Curate and package a fixture collection

## Inventory and transformation

Start from approved source access and a non-overwriting output destination. Record
format/version, identifiers, original hashes, license/provenance and relationships.
Decode each source identity from structured data rather than guessing from filenames.
Build a stable synthetic mapping: source A is alias A across all times/channels;
source B is alias B. Preserve relationships required for comparisons.

Transform only known fields using the format owner, then decode both versions and
compare all non-sensitive semantics. Update dependent names/checksums deliberately.
Unknown layouts, malformed archives, links/path traversal and expansion limits
fail before producing an apparently valid output. Screenshots and prior Git history
need separate review; changing a fixture does not change their contents.

## Inventory schema example

A manifest entry contains relative_path, format_version, byte_size, sha256,
source_record, sanitized_identity_group and package_role. Keep private originals/
identities outside the distributable manifest. Require an exact approved set:
missing files and extra files both fail. Read-only hygiene must not rewrite data.

## Deterministic bundle

Use stable member order and declared archive timestamps/modes where applicable;
retain actual payload bytes. Generate into a new staging location, hash the result,
repeat and compare bytes. Failure leaves no complete release payload. Test installed
resource discovery, corrupt/missing samples and native package ownership.

Use [fixture-review.md](../../../templates/project/fixture-review.md) and the
[packaging tool contract](../../../templates/tools/packaging.md). A format-specific
sanitizer is not provided by the foundation; implement/test one for the selected format rather
than invoking an unavailable source-project script or generic binary replacement.


[Skill](../SKILL.md)
