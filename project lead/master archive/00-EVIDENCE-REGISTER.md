# A25 Master Lead Archive — Pass A Evidence Register

FROM: GPT — A25 Project Lead
FOR: Zed, Claude, delegated builders and replacement lead
DATE: 2026-10-16 (user's current archive instruction)
RE: Preserve sources for sections 03, 04 and 05 before LBO-002
BASIS: GitHub Actions API, repository files, Zed's screenshots and statements, pending ChatGPT account export

## Scope and provenance
This is an initial **source register**, not a complete export of this conversation. No claim of full conversation coverage is made. Keep source originals unmodified. The user's ChatGPT account export has been requested and the email screenshot says preparation may take a few days; no exported archive has been supplied or verified. A share link is not a guaranteed durable original. Do not upload private account export or private screenshots into this public repository.

### Source groups
- GH-ACTIONS-20-54: GitHub Actions API on branch `build/wd-02-watchdog-v0`, observed run conclusions and commit identifiers; see section 03 for full sequence.
- GH-LOG-37: run #37, https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39003453631 ; historical report in `training/ACTIONS-REPORTS-AND-LESSONS-2026-10-16.md`.
- GH-LOG-47: run #47, https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39005925303 ; job log directly checked: 23 tests PASS, 0 FAIL / 4 WARN, push-base supplied.
- GH-BASELINE: original manifest Git blob `e317b1c42668126141baecd797cad84b4a1d57fe`, broken blob `bf3f3d85413deb94c1b36eee3ea4aabd414cddee`; these are Git SHA-1 blob IDs, not SHA-256.
- GH-EXCEPTIONS: `exceptions/WD-30-handoff-exception.sidecar.md`, `exceptions/WD-35-baseline-restoration.sidecar.md`, `manifests/W3_EXEMPT.txt`, `manifests/W4_RESTORATIONS.txt`, `manifests/ADDITIONS.sha256`.
- GH-BLACKOUT: `training/CLAUDE-BLACKOUT-CHECKPOINT-001-2026-10-16.md` and `training/CLAUDE-BLACKOUT-LOG-001-WD35-REPAIR.md`.
- GH-CS004: `training/CS-004-CONTEXT-COMPACTION-AND-SESSION-CONTINUITY.md`, `training/CS-004-INCIDENT-01-CLAUDE-USAGE-LIMIT-2026-10-16.md`.
- DRIVE-CLAUDE: Claude-authored Drive review `claude-originals/WD-35-claude-review-baseline-recovery.md`, training rules and review log. Existence/content were reported in previous lead checkpoint; re-fetch and verify hashes in Pass B.
- CHAT-ZED: human approvals at 22:43, pass-through exception rule at 22:52, blackout instruction at 23:16, archive-first instruction in this conversation. The exact original conversation export remains pending; quotations in earlier durable sidecars are provenance records, not substitutes for full export.
- CHAT-UI: screenshots of Claude compaction and usage limit as described in CS-004. The public GitHub record contains a description, not original screenshots.

## Evidence status rules
VERIFIED = checked against the named primary source; HUMAN-ATTESTED = reported by Zed; SECONDARY = prior report not freshly verified; PROPOSED = future plan; UNKNOWN = unresolved. Do not transform a screenshot into a completed audit, a green draft CI run into production approval, or a human relay into an independent Claude vote.

## Pass A intake when full export arrives
1. Store raw export locally or in an access-controlled location chosen by Zed. Preserve filename, export timestamp, SHA-256 and file size.
2. Identify this conversation by stable export ID, not just its title. Record message count, roles, original timestamps and attachment references. Avoid publishing private text.
3. Create a line/event index mapping conversation messages to GitHub commits, Actions runs, Drive reviews and decisions. Keep exact quotes separate from editorial summaries.
4. Mark gaps and unavailable attachments. Never invent missing messages.
5. Produce a redacted public index only after Zed reviews disclosure. Any private original stays outside the public A25 repository.

## Pending
Full account export not received; independent Drive re-verification outstanding; Claude ZIP audit interrupted; complete pre-#20 Actions evidence not indexed; individual #31–#45 logs not all re-audited. Sections 03–05 are therefore first-pass evidence-based working records, not a complete historical certification.
