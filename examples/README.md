# Runnable examples

- [Generic configuration JSON](configuration/README.md): 25/50 kHz scheduled data
  and source-valid inspection controls.
- [Native Python](python/upstream.py): loads the same generic JSON through Rust.
- [Authored UCD capture fixtures](measurements/ucd/README.md): independent
  structural examples for the shared Rust/native Python inspector.
- [Authored upstream RxMER files](measurements/rxmer/README.md): independent
  metadata, quarter-dB, null and grid cases for the shared decoder.
- Rust examples live under `crates/morgana/examples/`: `ldpc_loop`,
  `upstream_loop`, `upstream_measurements`, `upstream_document`, `inspect_ucd`
  and `inspect_rxmer`.

See the [experiment guide](../docs/user/upstream-experiments.md) for commands,
setup, ownership, limits and unsupported modes. Examples do not install or publish.
