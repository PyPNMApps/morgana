# Development installer

MORGANA's setup prepares Ubuntu 22.04/24.04 amd64 development prerequisites.
Python 3.10+ must already be available on PATH; these Ubuntu releases supply it.
Run from a source checkout as your normal user:

```bash
./install.sh --development --check
./install.sh --development --dry-run
./install.sh --development
```

Only the final command applies changes. It installs missing `ca-certificates`,
`git`, `build-essential` and `python3` packages using normal apt confirmation;
sudo is limited to apt. It prepares the exact Rust channel in rust-toolchain.toml
with rustfmt/Clippy under ignored `local/cargo` and `local/rustup`, then fetches
Cargo.lock dependencies for `x86_64-unknown-linux-gnu` with `--locked`.
It does not compile or test. Run `scripts/validate.sh` separately after setup.

The root shell file only dispatches. Focused Python development modules under
`scripts/bootstrap/` own host admission, package operations and local Rust setup.
Python performs no simulation calculations and is not a scientific runtime.
No Qt, GUI, Python bindings, services, shell startup changes or application install
is included. Existing toolchains/configuration and Cargo build outputs are kept.
Re-running setup skips satisfied apt/Rust steps and repeats the locked source fetch.

Check/plan do not write files, download, elevate, refresh indexes or create caches.
They execute installed pinned Rust binaries directly, suppressing rustup automatic
installation/update and Cargo networking. Source-cache completeness is reported
as uninspected; a ready check is not a pristine offline-build promise.

| Status | Meaning |
| --- | --- |
| 0 | Ready, valid dry-run plan or completed setup |
| 1 | Check found missing packages or pinned Rust/components |
| 2 | Invalid arguments, unsupported host or failed setup |

No arguments and inspection flags without `--development` display usage and
return 2. Unsupported hosts are rejected before transactions. The installer owns
default local roots; unset conflicting CARGO_HOME/RUSTUP_HOME for setup. It rejects
tool paths redirected outside this repository rather than writing through them.
The regular Cargo wrapper may still use intentional caller overrides outside setup.

First provisioning requires internet/configured Ubuntu repositories. A missing
local manager uses rustup-init 1.28.2 with a tracked SHA-256, size/deadline limits
and verification before execution. Toolchain manifests and Cargo.lock remain
unchanged. Temporary bootstrap files are removed without deleting retained caches.
The [official rustup installation documentation](https://rust-lang.github.io/rustup/installation/index.html)
describes local tool roots, and the
[Cargo fetch reference](https://doc.rust-lang.org/cargo/commands/cargo-fetch.html)
documents locked/target-aware source acquisition. These contracts were reviewed
2026-11-19; the bootstrap pin is not a latest-version claim.

Mocked transaction tests and this configured Ubuntu 22.04 host's read-only modes
are the validation scope. Fresh-machine provisioning and Ubuntu 24.04 runtime
remain unverified. See [design](features/development-setup/design.md).

Fresh target setup has passed on isolated Ubuntu22.04 and24.04 amd64 virtual
machines. See the [provisioning evidence](features/remaining-delivery/validation.md#fresh-target-setup)
for signed-image hashes, normal-user apply, repeat/readiness checks and limits.
This verifies development setup, not Windows/macOS, desktop installation or hosted CI.
