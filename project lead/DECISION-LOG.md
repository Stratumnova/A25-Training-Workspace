# A25 Project Lead — Additive Decision Log

FROM: GPT — A25 Project Lead
FOR: Zed, Claude, builders and successor lead
DATE: 2026-10-16
RE: Durable lead decisions and reasons
BASIS: Zed's instructions and A25 GitHub records

Do not replace earlier decisions. Add new entries with date, source, rationale, authority, commit, Actions evidence and independent review status. Correct errors with a new entry.

## D-PL-001 — Separate seats
Decision: Zed is final authority; GPT lead coordinates GitHub; Claude independently reviews and owns Drive originals; local builders implement bounded orders.
Reason: Prevent seat impersonation and self-approval.
Evidence: training/BUILDER-WORKFLOW-RULES-2026-10-16.md

## D-PL-002 — Watchdog exceptions require sidecars
Decision: Keep W1–W6 intact. Narrow, documented exceptions preserve original evidence and authority.
Reason: Do not hide rule violations to make CI green.
Evidence: exceptions/WD-35-baseline-restoration.sidecar.md; Actions run #47.
Review: Claude reviewed the restoration design, not the blackout implementation.

## D-PL-003 — Claude blackout work is labeled GPT-only
Decision: Continue ordinary work under Zed's 23:16 authorization, but keep an auditable commit/run ledger.
Reason: Keep development moving without inventing independent approval.
Evidence: training/CLAUDE-BLACKOUT-CHECKPOINT-001-2026-10-16.md and training/CLAUDE-BLACKOUT-LOG-001-WD35-REPAIR.md.

## D-PL-004 — Delegate GitHub AI setup
Decision: Zed's local GPT builder receives LBO-001. Lead retains coordination and reviews, not all implementation.
Reason: Limit lead-chat context pressure and make work portable.
Evidence: local build orders/LBO-001-GITHUB-AI-BUILDER-SETUP.md.
Status: Agent setup not yet verified.

## D-PL-005 — Lead succession
Decision: Store numbered checkpoints in project lead/. Zed appoints a new GPT lead if this session becomes unavailable.
Reason: Recover decisions and unresolved gates without relying on platform chat memory.
Evidence: project lead/LEAD-CHECKPOINT-001-2026-10-16.md.

## New entry template
ID / date / decision / reason / alternatives / authorization / changed files and commits / Actions / independent review / next action.
