# A25 Leadership Directive 005 — Existing Paths First
Date: 2026-10-17
Authority: Zed's direction to continue, following his observation that GPT and Claude repeatedly create duplicate paths, folders and trees.
Status: ACTIVE organizational direction

## Rule
Reuse existing repositories, branches, folders, naming schemes, and original artifact locations. Do not create new directory trees merely to organize the same information again. Before proposing a new location, identify the existing destination and explain why it cannot serve the need. Require Zed's explicit approval for structural changes to prior work. This rule does not prohibit new append-only report files inside already approved folders.

## Source ownership
- GitHub retains versioned code, coordination records, reviews, and leadership decisions.
- Drive retains Claude originals and approved supporting materials.
- Termux worktrees retain distinct local source checkouts; do not merge or relocate.
- ~/a25-workshop/gpt is a local operational directory, not a Git worktree.
- Android Documents/AI_Workshop contains Checkpoints, Project_Zips and Roundtable_Backups.
- Android Download is a separate intake area, not automatically canonical project storage.
- Archivist catalogs these existing locations by reference rather than copying or relocating originals.
- Watchdog flags duplicate identities and unapproved location drift without silently moving files.

## Gate for new directory/branch
Proposer must document: existing path candidates, why they fail, proposed path, owner/permission scope, evidence links, migration/rollback impact, and Zed approval. Do not perform moves or deletes without separate authorization.

## Implementation status
Directive recorded; enforcement by an automated Watchdog is NOT yet implemented.
