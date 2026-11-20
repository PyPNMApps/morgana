# Build and validation

Use Rust 1.85.1 with rustfmt/Clippy, a native linker/C build prerequisites required
by Rust's host toolchain, Bash and Python 3.10+ for development-only checks.
Scientific code and tests are Rust; Python is used only for repository tooling.

Use the [development installer](setup.md) to inspect/prepare the Ubuntu baseline:
`./install.sh --development --check` and `./install.sh --development --dry-run`
are read-only. Only `./install.sh --development` applies prerequisite changes.

`scripts/cargo-local.sh` prefers an existing isolated `local/cargo`/`local/rustup`
installation; otherwise it uses Cargo on PATH. No other source checkout is needed.
The wrapper does not install prerequisites or modify shell startup files.

```bash
scripts/cargo-local.sh check --workspace --locked
scripts/cargo-local.sh fmt --all -- --check
scripts/cargo-local.sh test --workspace --locked
scripts/cargo-local.sh clippy --workspace --all-targets --locked -- -D warnings
scripts/validate.sh
```

Retain downloaded dependencies and toolchains. After crate testing, clean this
repository's generated Cargo build outputs once all dependent checks finish.
Use Cargo's profile-specific cleanup to preserve logs, isolated validation tools
and reviewed wheels alongside the build directories:

```bash
scripts/cargo-local.sh clean --profile dev --target-dir target
CARGO_TARGET_DIR=target/python scripts/cargo-local.sh clean --manifest-path bindings/python/Cargo.toml --profile dev
CARGO_TARGET_DIR=target/python scripts/cargo-local.sh clean --manifest-path bindings/python/Cargo.toml --profile release
```

The optional native commands apply when that adapter was tested. Later builds
recompile these outputs. Validation checks the current implementation. The
all-family matrix source audit and
corrections have their own retained evidence; passing does not prove external
DOCSIS interoperability. Linux is the local host;
Windows, macOS, installed behavior and hosted CI remain unverified.


Optional native Python has a separate locked workspace. With an existing Python
interpreter/header toolchain, run `python3 tools/python/check_native.py`; the
[experiment guide](../user/upstream-experiments.md) documents actual APIs, local
wheel checks, controls and limits. Core validation never requires Python bindings.
Actual native formatting/Clippy use the binding manifest explicitly. Local wheel
packaging requires existing maturin1.8.3 and uses `tools/python/build_wheel.py` after
the native checker; it verifies packaged notices and tests the actual artifact.
No package is installed/published, and non-Linux/wider ABI/source-distribution
acceptance remains separate. Preserve the build caches.
