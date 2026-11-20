# Build and validation

Use Rust 1.85.1 with rustfmt/Clippy, a native linker/C build prerequisites required
by Rust's host toolchain, Bash and Python 3.11+ for development-only checks.
Scientific code and tests are Rust; Python is used only for repository tooling.

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

Retain target/toolchain caches. Do not run cargo clean routinely. Validation
checks the current checkpoint; passing does not resolve the documented matrix
transcription finding or prove DOCSIS interoperability. Linux is the local host;
Windows, macOS, installed behavior and hosted CI remain unverified.
