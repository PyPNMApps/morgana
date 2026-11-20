# Foundation adoption

Adopted on 2026-11-19 at the user's explicit request. Source checkouts remained
read-only. This record owns source attribution; generic skill procedures do not
require source checkout paths or lineage maps.

| Source | Inspected revision | Adopted scope |
| --- | --- | --- |
| User's PDE engineering foundation | Base `6f7197d17b0efc7a4be0d44a517d886b2f03009d`, working-tree inputs pinned by file hashes | 14 relevant complete skill folders with references and 15 required planning/review templates |
| MERLIN | `096d5a476194d4f2e016863d723b225257bb6037` | Pinned PHY skill instructions/navigation, locally retained corpora and adapted scientific/API procedures |

The [source manifest](foundation-sources.json) records original file paths and
SHA-256 values. Local changes adapt terminology/navigation to this repository,
replace unavailable helper contracts and preserve original operational detail.
Core sparse encoding attribution is separately retained in NOTICE/source headers.
PDE's Git-workflow entry/procedure had existing uncommitted edits when inspected;
they were adopted as a working-tree snapshot and then deliberately adapted here.
Other uncommitted PDE work is outside this adoption. No uncommitted author is
inferred, and the base revision alone is not claimed to reproduce those inputs.

The PDE subset covers development/reuse, coding, builds, Git, generic guidance,
third-party reuse, API contracts, numerical testing, fixture hygiene, freshness,
external review and knowledge maintenance. Required resources are carried locally;
unrelated desktop/install/bootstrap/credential and archived-project material was
excluded. Git policy is deliberately adapted: no-file-list saves include all
non-ignored current changes, as requested, rather than only an existing index.
No external checkout is needed for build, validation or local save.

MERLIN's upstream-relevant PHY3.1 I20 / PHY4.0 I07 instructions are retained with
local evidence paths. Scientific-testing, public-api and signal-processing skills
are adapted to upstream ownership, current support and future Python parity.
Downstream PLC/NCP processing, Qt and release tooling were not imported.
Full specification corpora are copied only under ignored local evidence; tracked
skills retain metadata/topic maps/indexes, not bulk specification text.

Canonical skills are under `skills/`. Both `.agents/skills/` and `.claude/skills/`
contain relative links to each canonical folder. Validate frontmatter, local links,
resource closure, private-evidence exclusion and tool behavior with
`scripts/validate.sh`. A clean clone may lack optional private corpora; skills
explain their exact paths and the missing-evidence stopping boundary.

Local overrides: this is a paused scientific checkpoint; further implementation
needs plan approval. Current APIs are FEC-only; no GUI, Python adapter, workbench,
CI/release or installed-platform claim is implied. Keep source findings unchecked.
Other checkouts are read-only; updates are reviewed diffs, never automatic sync.

PDE has no root redistribution license. This user-authorized local adoption does
not silently assign Apache-2.0 to its instructional text. Public redistribution
terms remain unresolved before publication. The scientific/tooling root LICENSE
applies to project-owned code; preserve component notices and inspect actual
source/binary packages before asserting complete distribution compliance.
