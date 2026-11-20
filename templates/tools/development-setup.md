# Development setup adoption contract

This is a design/review template, not an executable installer.
[Procedure](../../skills/modular-bootstrap/references/procedure.md).

## Inputs and public interface

- Explicit setup action/profile and no-argument behavior:
- Required interpreter/bootstrap prerequisite and installation instructions:
- Supported OS/version/CPU mappings and actual verification status:
- Check, dry-run, invalid/missing/failed exit statuses:
- Canonical tool version/component manifest and dependency lockfiles:
- Minimal package list; optional capabilities kept separate:
- Local tool/cache/output roots and override/path-redirection policy:

A possible consumer interface is `./install.sh --development --check` or
`./install.sh --check --profile rust`. These are alternative designs; document
and test the selected interface rather than assuming both exist.

## Module and lifecycle map

| Stage | Owner | Read-only probe | Apply action | Failure preservation |
| --- | --- | --- | --- | --- |
| Arguments/profiles | Target dispatcher | Complete validation | None | Reject before mutation |
| Host/package state | Target platform/package modules | Package metadata | Missing-package transaction only | Preserve configuration |
| Local language tools | Target toolchain module | Installed exact version/components, no auto-install | Verified pinned bootstrap/tool install | Preserve ready tools/caches |
| Dependency sources | Target package manager adapter | Optional explicit inventory | Locked target-aware fetch | Do not alter locks |
| Postcheck | Same admission owners | Requirements after apply | None | Report incomplete state |

## Acceptance evidence

Record fixture tests for no-action/invalid/unsupported paths, complete read-only
filesystem invariance, missing versions/components, redirected destinations,
no-op/repeated installs and command/download/checksum failures. Fake commands
must not reach real package managers or network. Keep fresh-machine provisioning
and build evidence separate; do not infer them from check/dry-run or mocks.

## External contracts and notices

Record reviewed official tool/package sources, date, selected versions, checksums,
network/size/work bounds and local ownership. Preserve attribution for any copied
implementation. Keep source/tool downloads ignored, with no dependency on another
checkout. Setup never implies compilation, application installation or publication.
