# Preserve licensing through import, modification and release

[Skill](../SKILL.md) · [Notices template](../../../templates/project/third-party-notices.md)

## Identify actual reuse

Inventory copied source, adapted snippets, vendored libraries, generated output
containing licensed material, fonts, icons, images, fixtures and packaged runtime
components. A language translation or renamed API may still be an adaptation;
do not assume rewriting syntax eliminates obligations. Separately record pure
engineering ideas expressed in new prose; those do not need a lesson lineage map.

For each reused item record its exact origin/release or revision, affected local
paths, copyright holders, license expression and evidence of permission. These
records belong to the future project's third-party inventory, not its generic
skill catalog. Private visibility and access to a repository do not grant reuse
rights. If permission or ownership is unclear, do not import the item until the
responsible owner resolves it; continue independent work when possible.

## Before importing

Read the actual applicable license, per-file exceptions and upstream NOTICE data
for the selected version. Determine what is copied versus linked, modified versus
unchanged, and which source/binary/server distributions are planned. Record license
compatibility and any required source, relinking, attribution, modification or
other delivery obligations. Do not treat all permissive or copyleft licenses as
interchangeable. Escalate unresolved compatibility decisions to the responsible
project owner rather than inventing an interpretation.

## Files and notices

Preserve original copyright, SPDX identifiers and applicable license comments.
Add a separate modification record for local changes where required, with verified
holder and dates; do not replace upstream ownership with the application's name.
Use the project's multiline source-banner syntax without damaging required text.
For non-commentable assets use supported sidecars or file-level metadata rather
than corrupting the file. A root project license does not automatically relicense
third-party files.

Maintain a project-level THIRD_PARTY_NOTICES.md (or established equivalent) from
the linked template. Include component identity, exact origin, local scope, license,
modifications, locations of full license text and required attribution. Preserve
upstream NOTICE entries where the license requires them, with their wording intact;
do not replace those entries with a link. Keep license texts in the project's
LICENSES/ or established package location. Avoid duplicating license texts manually
in multiple drifting inventories.

A NOTICE file and a license file serve different purposes. For example, Apache-2.0
section 4 requires license delivery, retention of applicable source notices,
change notices for modified files, and specified handling of an included upstream
NOTICE. A single credits line does not cover all of these obligations. Verify the
actual component terms before deciding what its packages must carry.
[Apache license text](https://www.apache.org/licenses/LICENSE-2.0), reviewed 2026-11-19.

For projects adopting REUSE, use its file-level copyright/license metadata and
LICENSES/ conventions; non-commentable files can use adjacent .license files.
An SPDX identifier communicates a license; it does not supply the license text or
prove permission/compatibility. [REUSE specification 3.3](https://reuse.software/spec-3.3/),
reviewed 2026-11-19. Do not claim REUSE conformance without its applicable checks.

## Packaging, updates and verification

Map each distributed component to the artifact that ships it and the notices,
license texts and any additional required materials delivered with that artifact.
Inspect unpacked DEB/MSI/app archives, wheels or other final packages; repository
presence alone does not prove distribution. An About → Licenses screen can expose
notices, but is not automatically sufficient for every license obligation.
CLI/source-only packages need accessible license material too.

On upgrades compare licenses and NOTICE changes alongside code and lockfiles.
Do not silently drop attribution after moving code, translating it or bundling it
into a generated artifact. Remove obsolete inventory entries only when the covered
material is actually absent; retain relevant notices for remaining adaptations.
Review both direct and bundled transitive components. License scanners and SBOMs
help discovery but do not replace examination of actual files and distribution.

Acceptance: each reused file/asset can be traced to permission and accurate notices;
modifications are recorded; each shipped artifact contains its required material;
missing permissions or unresolved distribution duties remain explicit blockers to
that reuse/release. Record actual validation, not a blanket compliance guarantee.
