# Validation entrypoint contract

[Tool map](README.md)

Implement one target-owned entrypoint with named phases: identity/version, tooling,
style/static analysis, unit/integration, feature/API modes, UI/native, security and
package/lifecycle where applicable. A project may expose focused phases for local
iteration; release/push selects the required set explicitly.

Each phase declares prerequisites, command argument array, working directory,
time/resource bounds, output/report location and exit behavior. Missing required
tooling fails with a useful message. A skipped optional phase is reported as skipped,
not counted as passed. Do not put install/push/publication into validation.

Example command contract (not an existing CLI):

```text
validate --scope local
validate --scope release --target windows-x64
```

Implementation owns how those scopes map to actual tools; do not execute these
example names until implemented. Build once where reusable and preserve artifacts.
Return nonzero on any required failure. Keep exact test discovery and known serial
cases. Report dependency-audit/CodeQL results separately from unit test totals.

The implemented local owner is [validate.sh](../../scripts/validate.sh).
