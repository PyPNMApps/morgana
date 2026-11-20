# Scientific distribution inventory

The scientific source archive and native Linux CPython3.10 wheel are the reviewed
local artifact scopes. Root repository or reusable engineering-guidance publication
is a separate scope; no publication or hosted pass is inferred from these files.

| Component | Origin / rights / local disposition |
| --- | --- |
| Project scientific source, facade, CLI, native conversions and authored fixtures | MORGANA contributors, Apache-2.0; root LICENSE/NOTICE and file banners retained. |
| Locally adapted sparse codec, PRBS, transforms, QAM/reference resources and notice tooling | Exact reference revisions, original holders and local modifications are retained in NOTICE and per-file headers. No source-checkout dependency. |
| QAM resources | `crates/phy/resources/qam-table/{LICENSE,NOTICE,provenance.json}` records original source, modification and hashes; these files ship in both artifact scopes. |
| Pinned Rust/native dependencies | Actual full source notices copied for79 host-reachable wheel dependencies; manifest records versions, repositories, selected license expressions and hashes. Registry sources are not vendored into the source archive. |
| Engineering skills/templates | Private adopted instructional material has unresolved redistribution terms. Excluded from both scientific artifacts; it is not relicensed by root LICENSE. |
| Specification corpora and source captures | Private/local-only, excluded. Tracked input fixtures contain invented identities/source-derived values and are not modem recordings. |
| GUI/GPL presentation code, external project checkouts, toolchains and build outputs | Excluded from the scientific artifacts. The wheel contains its own required native extension, not intermediate Cargo outputs. |

License selection uses exact reviewed alternatives: Apache-2.0 where offered,
MIT/0BSD for the applicable packages, and retained Unicode-3.0 or LLVM-exception
obligations where conjunctively required. Unknown expressions fail review rather
than being reduced to a permissive substring. `tools/python/notices.py` and
`tools/python/build_wheel.py` own collection and actual archive verification.
The one shared-notice archive gap is accepted only with exact same repository,
version/commit/license evidence already enforced by the collector. Full texts
and applicable source copyright/author notices remain packaged; an inventory
or a selected SPDX expression does not replace them.

`tools/packaging/source_bundle.py` owns the explicit source allowlist, path/
symlink bounds, no-overwrite export and exact hash inventory. Its generated
SOURCE-README documents independent build/use without engineering guidance.
The source archive includes the independent LDPC oracle required by its manifest;
standalone extraction/build/run acceptance caught and resolved that initial gap.

See [actual package/setup evidence](../development/features/remaining-delivery/validation.md).
These records describe inspected contents and acceptance, not general legal
approval for other artifacts, targets or root-repository redistribution.
