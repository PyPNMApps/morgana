# Development setup

## SETUP-01: Requirements

Provide a thin root `install.sh` with explicit `--development`, `--check` and
`--dry-run`. Initial package mappings: Ubuntu 22.04/24.04 amd64. Python 3.10+
is a pre-existing dispatcher prerequisite on those targets, not a simulation
runtime. Set up only missing development packages, repository-local Rust from
`rust-toolchain.toml` with rustfmt/Clippy and locked Cargo sources. No application
install, Qt, scientific changes, tests/builds, shell-profile changes or services.
Inspection modes return 0=ready/plan, 1=missing and 2=invalid/unsupported/failure.
No-argument invocation prints usage and exits 2 without changing anything.

## SETUP-02: Architecture and reuse

PDE's existing modular-bootstrap skill is the canonical generic owner; improve it
and adopt the complete skill/procedure plus setup contract into this repository.
MERLIN revision `096d5a476194d4f2e016863d723b225257bb6037` was inspected read-only:
`install.sh`, `scripts/install-development.sh`, `tools/development/tests/test_setup.py`
and `docs/development/setup.md`. Reuse explicit intent/read-only/local toolchain
design patterns, not the desktop package list or implementation source.

Root shell dispatcher invokes a stdlib-only development Python coordinator
without bytecode writes. `scripts/bootstrap/host.py` validates platform,
`packages.py` owns apt queries/transactions, `toolchain.py` owns pin/readiness/
local Rust setup and `main.py` composes the stages. Arrays, bounded subprocesses,
strict path ownership and typed failures replace shell command-string evaluation.
No dependency on other source checkouts. Installer and normal Cargo wrapper use
the same default local Cargo/rustup roots; reject external redirection before apply.

Check/dry-run query dpkg and installed local Rust only, disabling rustup automatic
installation/update and Cargo networking. They create no local roots, caches,
logs or bytecode. Checking prerequisites does not promise all Cargo sources are
already cached. Apply uses sudo for missing apt packages only, retains normal
apt confirmation, validates package candidates and uses a temporary local directory
for checksum-pinned rustup bootstrap. Keep toolchains/caches/build outputs on retry.
Cargo fetch uses --locked and the Linux host target; it never regenerates a lock.

Source contracts reviewed on 2026-11-19: rustup custom CARGO_HOME/RUSTUP_HOME and
--no-modify-path in the official rustup book; Cargo fetch --locked/--target in the
Cargo book; Ubuntu's Jammy/Noble Python and build-essential package pages.
Rustup bootstrap version 1.28.2, Linux x86_64 SHA-256:
`20a06e644b0d9bd2fbdbfd52d42540bdde820ea7df86e92e533c073da0cdd43c`.
This is an installer pin, not the Rust toolchain version or a latest-version claim.
No real provisioning is authorized by this implementation task.

## SETUP-03: Validation and checklist

- [x] Adopt generic skill/template with relative discovery and source hashes.
- [x] Implement dispatcher and focused host/package/toolchain modules.
- [x] Prove help/errors/check/plan never invoke mutation or alter fixture trees.
- [x] Test supported/unsupported hosts, missing packages/components and pins,
  redirected roots, repeated setup, failed commands and bootstrap checksum failure.
- [x] Wire targeted setup tests/syntax into the local validation entrypoint.
- [x] Run actual read-only check/plan and reconcile build/user/architecture docs.
- [x] Real fresh-machine provisioning on each declared target: see the
  [subsequent VM acceptance](../remaining-delivery/validation.md#fresh-target-setup).

Mocked installation tests use temporary roots and fake package/download/tool
commands. They cannot reach sudo/apt/network on the real host. Full Rust science
validation is unchanged and need not be repeated for setup-only edits.

### Validation results

`python3 -B -m unittest discover -s tools/development/tests -p 'test_*.py' -v`
passed 19 cases in 0.849 s. `python3 -B -m unittest discover -s tools/git/tests
-p 'test_*.py' -v` passed all five existing helper cases in 0.714 s.
`python3 tools/validation/check.py` passed 20 skills, relative discovery/resource
closure, 230 documentation links and version identity. `bash -n install.sh
scripts/validate.sh`, skill-creator quick validation and Git whitespace checks
passed. Exact source hashes for adopted installer guidance were verified locally.

`./install.sh --development --check` and `--dry-run` both returned 0 on Ubuntu
22.04.5 amd64 with the existing local Rust 1.85.1 installation and host packages.
No apt transaction or real toolchain installation was run for validation. An
earlier ad hoc rustup version probe unexpectedly began automatic acquisition;
it was stopped. The implemented probes avoid the manager/proxies entirely, and
fixture tests prove they are not invoked even with missing local tools.

No full scientific workspace rerun was needed: simulation sources/manifests/lock
are unchanged by this setup task. Prior FEC source-review gaps remain explicitly
unfinished. No fresh-machine provisioning, Ubuntu 24.04 execution or hosted CI
result is claimed. Installer apply behavior is validated through controlled mocks.

## Subsequent fresh-machine acceptance

The initial results above remain historical. SETUP-04 subsequently ran actual
setup on clean signed Ubuntu22.04/24.04 amd64 cloud-image guests, using normal-user
installation, read-only before/after checks and repeated apply. Both passed.
See [exact environment/procedure/evidence](../remaining-delivery/validation.md#fresh-target-setup).
No host system packages, shell startup files or external project state were changed.
