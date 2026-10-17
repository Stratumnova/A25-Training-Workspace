# A25-NS-O001 — Universal Namespace Registry Design

FROM: GPT — A25 Project Lead
FOR: LB-GPT01
DATE: 2026-10-17
RE: First two-session GitHub handoff; namespace registry and migration ledger design
BASIS: Zed approved A25 as root and Stratumnova as legacy source; see `project lead/archivist/A25-ROOT-NAMESPACE-DECISION.md`
ORDER ID: A25-NS-O001
STATUS: AUTHORIZED — design and synthetic validation only

## Objective
Propose a collision-resistant, human-readable A25 universal identifier format and registry for all A25 projects, including Pocket Server, Archivist, Watchdog, Toolbox/Build by Coin, HalfAwake, lore and training. Existing legacy names are searchable aliases; do not overwrite original names or files.

## Required deliverables
1. `project lead/archivist/namespace/A25-NS-SPEC-DRAFT.md`: canonical ID grammar, reserved prefixes, uniqueness scope, artifact kinds, revision and status rules, ownership/authority, aliases, collision resolution and lifecycle.
2. `project lead/archivist/namespace/A25-NS-MIGRATION-LEDGER-DRAFT.md`: source repo/ref/path, source kind, original term, new proposed ID, content digest if computed, derived relationships, verification, migration state, rollback and owner acceptance.
3. `project lead/archivist/namespace/A25-NS-EXAMPLES.md`: synthetic examples including Gate-01 in multiple projects, Key5 prompt versus Key5 code, Batch 7, Watchdog tests and historical alias conflicts. Label invented examples SYNTHETIC; do not claim source-verified code paths.
4. `project lead/coordination/reports/A25-NS-R001-LB-GPT01.md`: concise report listing changed files, full commits, decisions needing lead input, tests if any, and any blockers.

## Constraints
- Design-only task. You may add the three new draft documents and report on the coordination branch. Do not modify existing protected files, Watchdog, Pocket Server, original Stratumnova repos, or main.
- Do not implement automatic renaming/migration or merge anything. Do not expose private archive contents.
- Keep the difference between source-author claim, narrative identity, assigned AI seat and authenticated principal.
- Keep namespace separate from GitHub folder path; names should survive repo moves.
- If you cannot write to coordination branch, stop and report the exact permission error to Zed. Do not silently choose a different branch.
- Read `project lead/coordination/README.md`, `project lead/archivist/A25-ROOT-NAMESPACE-DECISION.md`, and `project lead/archivist/TERMINOLOGY-AND-EVIDENCE.md` before drafting.

## Return and stop
Post report to the specified GitHub path; stop. Lead will independently read and review. No next phase until lead decision.
