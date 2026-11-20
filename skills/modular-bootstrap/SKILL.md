---
name: modular-bootstrap
description: Design or implement modular development install.sh entrypoints with explicit setup intent, read-only check/dry-run modes and project-local pinned toolchains; excludes application package installation.
---

# Modular development setup

Use the [procedure](references/procedure.md) and
[adoption contract](../../templates/tools/development-setup.md). Read the target's
requirements, setup owners and package/tool pins before adding another installer.
This skill describes development provisioning, not application installation.

Keep root `install.sh` a dispatcher. Separate argument/profile selection, supported
host detection, package transactions and language-toolchain/source preparation.
Validate the whole plan before mutation. Profile declarations have no side effects.

Require explicit install intent: a documented development flag/profile or explicit
interactive selection. `--check` and `--dry-run` must never elevate, refresh package
indexes, download, create caches/logs/configuration or trigger lazy tool installation.
Readiness probes use the selected version/components and suppress automatic updates.

Install only missing prerequisites. Keep language tools/caches project-local when
that is the chosen policy; preserve existing user toolchains/configuration and build
artifacts. Use reviewed sources/pins and verify downloaded artifacts before running
or extracting them. Keep source fetch, compilation/tests and application installation
as separate operations. Do not hide services, keys or shell-profile edits in setup.

Apply [coding-style](../coding-style/SKILL.md),
[third-party-reuse](../third-party-reuse/SKILL.md) and
[knowledge-freshness](../knowledge-freshness/SKILL.md) where applicable.
Adapt the complete local dependency closure; no other source checkout is required.
Mocked package/download tests and real fresh-machine provisioning are separate
kinds of evidence. [Skill catalog](../README.md).
