# Implement a modular development installer

[Skill](../SKILL.md) · [Adoption contract](../../../templates/tools/development-setup.md)

## Requirements and ownership

Identify the target OS/version/architecture, required interpreter, canonical
language/SDK versions, package sources, local tool roots and source locks. Keep
required build/test prerequisites separate from optional GUI/editor/server,
packaging, bindings and authentication tools. A minimal CLI does not require a
companion desktop application's SDKs. Inspect an existing installer before reuse;
record actual copied-source attribution outside generic instructions.

Choose the public interface before implementation. A project may use an explicit
`--development` action or named `--profile` selections; neither is universal.
No arguments should explain usage or offer deliberate interactive selection,
never start an unattended package transaction. Parse all options and validate
all selected profiles, host mappings, pins and destination ownership before any
change. An unknown option after a valid selection must leave the host untouched.

Keep root `install.sh` thin and location-independent. Suggested owners are:
argument dispatch, host detection, declarative profiles, shared package runner,
local toolchain readiness/installation and locked source preparation. Select
shell/Python/another development language according to existing prerequisites;
do not make an unavailable interpreter a hidden prerequisite of its own installer.
Modules must not install, download or elevate when imported/sourced.

## Modes and statuses

- Help explains intent, supported targets, modes, write locations and exit codes.
- Check reports missing packages, exact pinned tools and required components,
  returning a documented nonzero missing status. Unsupported/invalid input is
  distinguishable from missing prerequisites.
- Dry-run prints the resolved missing-package/tool/source plan and returns success
  for a valid plan. It does not perform the planned work.
- Install explains changes, performs only missing transactions, then verifies the
  resulting requirements. Failure propagates; later success does not mask it.

Both inspection modes are strictly read-only: no package-index refresh, privilege
request, downloads, directory/cache creation, bytecode, logs or configuration
writes. Do not assume a tool's version or offline command is passive: wrappers
can lazily download a missing toolchain or acquire/write caches. Select an
already-installed tool explicitly, disable automatic install/update/network behavior
and test an empty tool-root case. Do not use a mutating dependency fetch as a
readiness probe. State whether source-cache completeness is inspected or deferred.

## Apply a complete validated plan

Deduplicate package requirements before querying/installing them. Inspect package
manager state, not just executable presence: a runtime binary does not establish
that headers/linker components exist. Resolve package candidates against the
chosen repositories, retain the package manager's confirmation policy and scope
privileges to the system package step. Do not add repositories or bypass package
manager ownership implicitly. Skip the transaction entirely when nothing is missing.

Keep toolchain destinations explicit and independent from another checkout.
Reject symlink/path redirection outside owned roots before writes; do not overwrite
an existing external SDK or user configuration. Document how caller environment
overrides interact with installer and build wrappers. Run local tool/source steps
as the desktop/developer user rather than root when that is their ownership policy.

Derive exact tool versions/components from a tracked manifest. Prefer a pinned
bootstrap artifact with a reviewed digest; validate hashes and safe archive members
before execution/extraction. Bound transfer time/size and subprocess duration.
Keep temporary downloads under an owned ignored location and clean only the
operation's temporary directory. Do not remove toolchains, user inputs or build
outputs as routine recovery. Use atomic promotion where partial downloads could
otherwise look ready. Existing complete toolchains are reused, not silently upgraded.

Fetch dependency sources through the package manager using the committed lock
and required target set. Do not regenerate lockfiles, vendor another project,
compile or test as an undocumented setup side effect. Authentication, services,
remote access and private-key creation need separate explicit actions. Preserve
existing keys and shell startup files.

## Regression scenarios

Use temporary fixture roots, fake package/tool/download commands and complete
before/after filesystem snapshots. A test flag that disables real elevation must
not become a production bypass. Test callable functions and the public dispatcher.

| Scenario | Expected behavior |
| --- | --- |
| Help/no action/unknown option/conflicting modes | Clear usage/status; no writes or package calls |
| Missing host mapping or invalid profile/pin | Reject before any transaction |
| Empty local tool root under check/dry-run | Missing status/plan; no lazy download or directory creation |
| Tool exists but wrong version/component is absent | Report unready, never substitute a different tool |
| Repeated requirements/setup | One missing-package transaction; complete tools reused |
| Redirected local root | Reject before any writes to the destination |
| Package/download/checksum/source-fetch failure | Nonzero; no execution of unverified artifact; preserve inputs |
| Already-ready host | No package/index/tool install; documented source-fetch policy |
| Partial prior setup | Recheck and resume missing pieces without wiping caches |

Record exact commands, host/tool pins, test cases, elapsed time and omissions.
Mocked lifecycle tests prove control flow within that harness. Read-only execution
on a configured machine proves inspection only. Claim a new platform provisioned
only after actual authorized clean-machine installation and build verification.

## Adoption

Copy the full skill/reference/template closure, adapt links to local owners and
create relative discovery links. Document local interface/platform/package/tool
choices in the consuming repository. Keep version-specific official sources and
required notices; generic procedures must work without a previous project's files.
Use the [adoption contract](../../../templates/tools/development-setup.md) to review
completeness, and preserve consumer overrides during explicit updates.
