# Planned code layout per architecture section

Current execution status: bounded synthetic stage science, generic source JSON
and native APIs are recorded in the [backend validation](../backend-stages/validation.md).
The design history below is retained; capture/import, broader PHY and presentation
items do not gain runtime acceptance from completed design checkboxes.

## Requirements and design

PATH-01: Each signal-path block/stage section names the repository-relative
directories and files planned for its implementation and validation. Distinguish
new planned files, existing reuse and existing files to extend. A directory name
alone is not enough to identify the algorithm or adapter owner.

PATH-02: Backfill the existing PRBS, configuration, transmitter, channel,
receiver, instrument and orchestration designs. Preserve the current crate
boundaries: facade → proposed PHY → standalone LDPC, with adapters using the
public facade. Shared algorithms have one owner named by both TX and RX.

PATH-03: Add the reusable rule to development-workflow and its procedure/template
in the foundation and adopt it locally with source hashes. Proposed paths are
code-formatted text until files exist; no empty implementation files are created.

The canonical layout and per-section path tables live in
[architecture](../../../architecture.md#planned-code-layout). This record tracks
the documentation change; it does not authorize scientific implementation or
complete the pending TX/RX stage designs.

## Checklist and validation

- [x] Add a directory overview and per-block/stage implementation/test paths.
- [x] Reconcile existing feature records and the official checklist.
- [x] Update the foundation/local skill, procedure, template and adoption record.
- [x] Verify existing versus planned paths, local anchors, metadata and adoption
  hashes; run both repositories' required validation.

`scripts/validate.sh` passed 20 skills, 278 local links, 23 existing Rust tests,
19 setup tests and 5 Git tests, formatting and Clippy. Focused layout review
covered seven block-level sections, eight TX stages and nine RX adapter rows.
Nine existing code/test files and the root Cargo.toml resolved; all 81 proposed
files in the complete inventory remained absent. The receiver table locates
each adapter/test and identifies shared algorithms. No PHY/binding directories,
source modules or Cargo registrations were created. At that layout-backfill
checkpoint TX-04..08 and scientific implementation milestones remained pending;
subsequent stage designs update the canonical architecture/checklist separately.

Focused checks resolved 59 local section links, preserved all 16 TX overview/
output links, and verified the updated PDE source hashes and matching procedure/
template. Both development-workflow skill metadata validators passed. PDE's
link/anchor/portability checker and all 31 existing tests passed. Whitespace
checks passed in both repositories. These results validate documentation and
the existing checkpoint, not execution of the proposed file layout.
