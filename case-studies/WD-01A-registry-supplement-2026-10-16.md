# WD-01A registry supplement — baseline identifier families

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude, and builders
**DATE:** 16 October 2026; exact write time unknown
**RE:** Additive supplement to initial case-study ID registry
**BASIS:** Claude's independent inventory of the 64-file c498e84 baseline, relayed to GPT; initial registry at `case-studies/ID_REGISTRY.md`

## Scope

This supplement preserves the original F-series registry and records the additional ID families observed by Claude in the pinned baseline. It is a *baseline inventory supplement*, not certification that newer commits or the entire current repository have been exhaustively scanned.

| Identifier | Baseline classification |
| --- | --- |
| A25-ARCH-001 | Assigned frontmatter |
| A25-CORR-README-001 | Assigned frontmatter |
| A25-DEC-001 | Assigned frontmatter |
| A25-DEC-001-RESOLUTION | Distinct assigned resolution identifier |
| A25-DEC-002 | Assigned frontmatter |
| A25-F-001 | Assigned; see initial registry |
| A25-F-001-CORR-001 | Distinct correction identifier |
| A25-F-002 | Historical collision; see initial registry and F-004 correction |
| A25-F-003 | Reserved, not confirmed archived |
| A25-F-004 | Filename-derived corrective identifier |
| A25-REV-001 | Assigned frontmatter |
| A25-SC-20261016-1237-CLAUDE | Assigned frontmatter |
| A25-VAL-001 | Assigned frontmatter |
| A25-MIG-001 | Filename-derived |
| WD-000 | Filename-derived work order |
| RT-001 through RT-005 | Filename-derived Roundtable sessions |

`A25-F-UNASSIGNED` and `A25-H-UNASSIGNED` are **template placeholders**, not assigned IDs and not collisions. A resolution or correction suffix must remain distinct from its base identifier.

## Approved B4 extraction direction

For numbered identifiers, extract a recognized canonical `A25-<FAMILY>-<NNN>` prefix from a filename or frontmatter, retaining explicit structured suffixes such as `-CORR-001` and `-RESOLUTION`. Do not treat descriptive filename tails as distinct identities. Detect disagreement between frontmatter and filename rather than silently picking a winner. Template placeholders are excluded. WD-02 implementation must test the legacy F-002 collision and the distinct DEC-001-RESOLUTION and F-001-CORR-001 cases.

## Review state

Claude's independent inventory supports the baseline entries above. Automated current-tree validation and full WD-01A certification are pending.
