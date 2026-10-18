# LEAD-DIRECTIVE-025 — Leadership Folder Ownership and Handoff Rules
FROM: A25-AG-GPT01 — Archives and Folder Organization Lead
AUTHORITY: Zed delegated leadership folder setup and rules; owner reports Roundtable Lead agreement
DATE: 2026-10-17 21:59 MDT (owner-supplied)
STATUS: ADOPTED organization policy; existing files preserved
BRANCH: coord/a25-namespace-trial-001

## Canonical layout
`project lead/leadership/` remains the historical leadership root. Do not move, rewrite or silently reclassify any existing file. New work is organized in:
- `project lead/leadership/archives/` — Archives, namespace registry, folder organization, Watchdog support and GitHub Agent/Bot lead notes, decisions, training, handoffs.
- `project lead/leadership/roundtable/` — Pocket Server and Roundtable communication lead notes, decisions, training, handoffs.
- `project lead/leadership/security/` — RESERVED for future designated Security Lead; Archives may create the neutral README only; no security implementation authority.
- `project lead/leadership-pool/` — existing cross-leader inbox, with no automatic adoption.
The legacy root files stay authoritative at their original paths. New leader areas link back to originals instead of copying or migrating them.

## Ownership
- Only the assigned leader or Zed may publish or amend that leader's own leadership notes. Other leaders send cross-project material to `leadership-pool/`; receiving lead records adoption separately.
- Builders and reviewers work in existing orders/reports/reviews/testing and source-code paths, not leadership training folders.
- Leader-written training lives in the leader's own area; no Academy folder or promotion without later Zed decision.
- Security lead area is reserved, not an assignment of Security authority to Archives. Watchdog support raises flags; Security team later investigates controls.
- Owner Zed retains final approval of protected changes, ownership disputes, cross-team priority conflicts, migrations and deployment.

## Required file pattern for NEW leader records
Use unique, descriptive append-only Markdown filenames: `<DOMAIN>-<TYPE>-<YYYY-MM-DD>-<NNN>-<SLUG>.md`.
DOMAIN: ARC, RT, SEC (once assigned). TYPE: DECISION, NOTE, TRAINING, HANDOFF, REVIEW, STATUS.
Every record includes: FROM, FOR, DATE (timezone and whether owner-supplied), SCOPE, SOURCE pinned refs, EVIDENCE STATUS, DECISION/QUESTION, NEXT ACTION, OWNER and BLOCKERS.
Never overwrite an existing numbered file or infer latest from filename alone; read the index and original refs.

## Continuity requirements
Each leader maintains an index/README with current owner, scope, current pinned handoff, active orders/reports, unresolved blockers, exact source refs, last verified checkpoint, and next safe action. After substantive decisions or builder reviews, append a new dated note and update the leader's own index if permitted. An index is navigation, not original evidence. Emergency replacement reads its area's README, latest HANDOFF, linked original evidence and pool notices; it does not trust stale completion claims.

## Cross-project exchange
Use new notes in `project lead/leadership-pool/` with FROM/TO/source/evidence status/requested action. No automatic adoption, approval, or edits to another leader's area. The receiving leader writes its own response or disposition. Preserve competing evidence.

## Change boundaries
No existing file migration, branch creation, code changes, workflow dispatch, deployment, credential or permission changes under this directive. Structural changes to these conventions require a new owner/lead-approved addendum, not silent cleanup. This directive does not ratify unfinished technical prototypes.
