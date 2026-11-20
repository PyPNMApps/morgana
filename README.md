# MORGANA

Planned DOCSIS 3.1/4.0 upstream OFDMA simulation toolkit for one cable modem and
a simulated CMTS receiver. Scientific processing stays in Rust.

**Current state: unfinished foundation and standalone LDPC checkpoint.** The
long, medium and short codec implementations, shortening, Rust facade, JSON reports
and single-word CLI exist. The current 23 unit tests pass; matrix-source review
is incomplete and has a known pending transcription correction. This is not yet
a validated upstream PHY release. Further simulation implementation is paused
until plan approval. No OFDMA waveform, GUI or Python binding is implemented.

- [Architecture and ownership](docs/architecture.md)
- [Development index and official checklist](docs/development/README.md)
- [PDE adoption and skill sources](docs/development/foundation-adoption.md)
- [Agent instructions](AGENTS.md) and [skill catalog](skills/README.md)
- [Build and validation](docs/development/build.md)
- [Local Git save workflow](docs/git.md)
- [Specification setup and evidence limits](docs/reference/specifications.md)
- [Notices and redistribution gaps](NOTICE)

With Rust 1.85.1 and prerequisites available:

```bash
scripts/cargo-local.sh run --locked -p morgana-cli -- ldpc short 420 42
scripts/cargo-local.sh run --locked -p morgana --example ldpc_loop
scripts/validate.sh
```

The CLI writes one deterministic reference trial to stdout. JSON identifies this
as standalone LDPC and leaves waveform RxMER null. Source version is 0.1.0;
packages are not published. MORGANA-owned scientific code/tooling is Apache-2.0;
see [LICENSE](LICENSE), [NOTICE](NOTICE) and the adoption record for component scope.
