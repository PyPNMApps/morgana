# MORGANA upstream DOCSIS simulation toolkit

Work in this repository. Source repositories used for inspection remain read-only
unless the user explicitly authorizes a scoped update to their canonical guidance.
MORGANA owns Rust upstream OFDMA science for one CM and a simulated CMTS receiver;
it does not implement a full MAC, scheduler, service group or downstream waveform.

## Current authorization and status

The current scientific implementation is an unfinished checkpoint. Further
simulation implementation requires explicit approval of the plan. Saving this
checkpoint and adopting skills/instructions are authorized. A request for
`commit-msg` means prepare the local save-helper command, not execute it.
After each completed section, include the reviewed `commit-msg`
command in the handoff automatically; the user does not need to ask again.
Development-installer implementation and its generic foundation guidance update
are authorized; executing system installation is a separate action.
Do not commit, push, tag, publish or install system packages without an explicit
request to execute that operation. Tests may use disposable Git repositories.

Read [architecture](docs/architecture.md), [requirements](docs/requirements.md),
[checklist](docs/development/checklist.md),
[feature design](docs/development/features/foundation/design.md) and
[software facts](docs/sw-facts/README.md) before implementation. Follow
Architecture → Requirements → Developer checklist → Implementation → Validation.
When asked for a plan, stop after planning. When asked for `next`, choose the next
unfinished prerequisite in the checklist only when implementation is authorized.
The official checklist SHALL link every active task to exact requirement and
architecture targets, list dependency IDs and define acceptance. Preserve stable
IDs/status and complete requirement coverage; completed design is not runtime
acceptance. Follow the development-workflow traceability procedure.

## Skills and source evidence

Canonical skills live under [skills](skills/README.md); `.agents/skills/` and
`.claude/skills/` contain relative discovery links. Apply development-workflow,
reuse-first-changes, coding-style, build-validation and third-party-reuse where
applicable. Use generic-guidance for skill changes; preserve complete local
procedures, examples, failure cases and link dependencies. See the
[foundation adoption record](docs/development/foundation-adoption.md).
Apply [modular-bootstrap](skills/modular-bootstrap/SKILL.md) for `install.sh`
and development-setup changes. The root dispatcher stays thin; package/toolchain
implementation lives in focused modules under `scripts/bootstrap/`.

Apply docsis-signal-processing, scientific-testing and the relevant pinned
docsis-phy-3-1-i20 / docsis-phy-4-0-i07 skills for PHY/FEC changes. Apply public-api
and api-contracts for public or persisted models. Keep specification revisions,
sections, PDF pages, normative endpoint and unsupported modes explicit. Private
PDFs/extractions/page images belong under ignored `docs/development/local/`.
Consult [local evidence setup](docs/reference/specifications.md); do not ship
copyrighted specification corpora or infer missing tables from matching sizes.

The high-level Rust API and optional native Python wrapper have their own
[architecture section](docs/architecture.md#high-level-rust-and-python-apis).
Define paired Rust/Python contracts and planned stub paths for new shared
capabilities. Implement the Rust operation first; Python only converts and
dispatches. Preserve the existing FEC facade. Architecture stubs are proposals,
not callable APIs or permission to implement scientific work.

## Scientific ownership and limits

All FEC, DSP, channel models and orchestration remain Rust, including algorithm
dependencies. Project crates forbid unsafe code. No native DSP/codec FFI or Python
calculations. Keep the codec independent of waveform, QAM, channel and BCH stages.
Upstream ordinary data has no downstream BCH outer code or assumed puncturing.
Do not equate a recognized modulation/code with an implemented PHY chain.

Keep simulator truth outside normal receiver inputs. Estimate effective C×H
from received pilots. Preserve convergence, syndrome, shortened-zero consistency
and independent source comparison as separate outcomes. Preserve failed decisions
and actual iterations. Bound files, allocations, runtime and iterations; retain
completed trials on cancellation when job orchestration is introduced.
Preserve original capture bytes, hashes, grids, nulls, timestamps and provenance.
Measured Pre-Eq is a corrective response, not exact RF truth or receiver noise.

MORGANA-owned scientific code/tooling is Apache-2.0. Preserve actual copied notices
and modification records. Do not import GPL presentation code into the core.
No source checkout dependency, vendored capture decoder, SNMP/TFTP/device control,
network-analysis service, GUI or Python sidecar is implied by this foundation.

## Development and handoff

Use focused modules and meaningful domain types. Every public callable needs
multiline documentation covering arguments, results, errors and relevant ownership.
Use multiline branches; the formatter is necessary but is not the whole style rule.
Plans/validation live under `docs/development/features/<feature>/`, indexed from
`docs/development/README.md`; maintained guides live under `docs/user/`.
Each architecture block/stage section names planned implementation/test file
paths and distinguishes new files from existing reuse or extensions. Keep the
directory overview and earlier sections aligned; proposed files remain design
only until implementation is authorized.
Review architecture/checklist at completion and every commit-msg request. Keep
partial or source-unverified work unchecked. Do not edit solely to log a review.

Run `scripts/validate.sh`; use `scripts/cargo-local.sh` for individual Cargo calls.
The gate checks local guidance/navigation, setup/Git tooling, formatting, workspace
tests and Clippy. Preserve Cargo/toolchain caches. Do not install prerequisites
incidentally; see [build guide](docs/development/build.md). Hosted/platform runs,
external interoperability and publication require separate actual evidence.

## Git

Read git-workflow and [local Git guide](docs/git.md). Inspect staged, unstaged and
every untracked file before preparing a message; preserve the user's index during
review. Use `tools/git/git-save.sh --commit-msg` with one multiline message:
`Feature:`, `BugFix:` or `Documentation:`, `- detail` lines and `- Tests:`, each at
most 60 characters. Start command blocks with `cd /home/dev01/Projects/morgana &&`.
Save includes all non-ignored changes and existing staged content, runs the gate
and commits locally. Never imply push, release or a version bump. VERSION is the
canonical source version; release/bump/push automation is still planned.
