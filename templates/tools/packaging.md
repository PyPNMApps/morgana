# Application packaging tool contract

[Tool map](README.md) · [Planned delivery](../../docs/development/checklist.md)

Suggested responsibilities, not files that already implement a packager:

```text
packaging/
  identity       canonical version, product/package IDs, naming
  inventory      approved staged files, sizes, hashes, notices
  runtime        target-specific runtime/resource discovery
  linux          DEB staging/build metadata
  windows        MSI authoring/build metadata
  macos          app bundle, signing boundary, DMG layout
  verify         exact expected package set and content checks
  lifecycle      disposable native install/upgrade/remove checks
  collect        same-run artifacts -> release allowlist
```

Inputs: immutable source revision, canonical version, target, compiled payload,
approved resource manifest, explicit new output directory, toolchain identity.
Outputs: packages, checksums and machine-readable inventory with version/target,
source commit, size/hash and relevant validation/signing state. Internal reports
are separate from release assets.

Example inventory shape:

```json
{
  "schema_version": 1,
  "version": "1.2.3",
  "source_commit": "replace-with-exact-commit",
  "target": "windows-x64",
  "files": [
    {"name": "example-desktop_1.2.3_windows_x64.msi",
     "role": "installer", "bytes": 1234, "sha256": "replace-with-measured-digest"}
  ]
}
```

This is illustrative data, not valid release evidence. Reject mismatched/incomplete
records, unknown roles, extra files, unsafe paths and output reuse that would overwrite
user data. Sign/staple before final hashes. Never mark native lifecycle passed from
packaging alone. Unit-test all identity/manifest guards with synthetic outputs;
run installers only on authorized disposable native systems.
