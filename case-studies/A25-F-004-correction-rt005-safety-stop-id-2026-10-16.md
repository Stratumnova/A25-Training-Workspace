# A25-F-004 — Correction to RT-005 safety-stop case-study ID

**FROM:** GPT — A25 Project Lead
**FOR:** Zed, Claude, A25 builders
**DATE:** 16 October 2026
**RE:** Additive correction for duplicate A25-F-002 identifier and direct retry authorization
**BASIS:** Claude's 15:40 MDT review supplied by Zed; GitHub read-back of both relevant records; Zed's exact message in this conversation

## Correction

The newly created `case-studies/A25-F-002-safety-stop-rt005-index-2026-10-16.md` was incorrectly assigned `A25-F-002`. That identifier already belongs to `legacy/pockettest/a25-training/case-studies/A25-F-002-proposed-gpt-fork-sandbox.md`, whose front matter explicitly says `id: A25-F-002` (verified by GitHub read-back). The safety-stop incident's **correct canonical identifier is A25-F-004**. The original incorrectly titled committed record remains unchanged as historical evidence. This correction supersedes its identifier only, not its incident details.

Claude reports that `A25-F-003` was reserved for its Block 1 rollback; that reservation is **Claude-attested**, not independently verified as an archived record here.

## Human authorization — direct quotation

Zed wrote in the GPT conversation, immediately after reviewing the proposed RT-005 index:

> Now try to put it up on GitHub with my permission and see if it blocked again

This is direct authorization for the single index retry; the previous case study had only paraphrased it. The index write succeeded at commit `3da739ec4cf2fd6c6df91a99c80797ed3654b6d4`, and GitHub read-back succeeded. The first safety block's cause remains unknown.

## Evidence and follow-up

- Misnumbered, preserved original: `case-studies/A25-F-002-safety-stop-rt005-index-2026-10-16.md` at commit `14a7ecc67cc70e44cb4be7c70bc3a7bec1ca1d27`.
- Prior owner of ID F-002: `legacy/pockettest/a25-training/case-studies/A25-F-002-proposed-gpt-fork-sandbox.md`.
- This file is the canonical correction/alias record for incident **A25-F-004**.
- The Watchdog W5 design should detect the duplicated F-002 identifier in the historical tree and recognize this explicit correction; no Watchdog run or detection is claimed here.
- Before assigning future case-study IDs, inspect legacy records and reservations, not only the top-level `case-studies/` directory.

**Status:** Corrected by additive record; original remains immutable. Claude's independent review of this correction remains pending.
