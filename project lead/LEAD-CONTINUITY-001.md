# Project Lead Continuity 001 — A25 authority and resumption

FROM: GPT — A25 Project Lead
FOR: Zed; replacement GPT project-lead session; Claude
DATE: 2026-10-16 23:28 MDT (Zed instruction)
RE: Recover leadership after chat loss, context compaction or seat interruption
BASIS: Zed's direct instructions and verified GitHub/Drive checkpoints. This file records decisions and stated rationale, not hidden model reasoning.

## How a replacement lead resumes
1. Confirm repository identity Stratumnova/A25-Training-Workspace and read this file at a pinned commit, then inspect current development branch HEAD. Do not assume the pinned checkpoint is current.
2. Read START_HERE.md, training/BUILDER-WORKFLOW-RULES-2026-10-16.md, training/CLAUDE-BLACKOUT-CHECKPOINT-001-2026-10-16.md, training/CLAUDE-BLACKOUT-LOG-001-WD35-REPAIR.md, training/CS-004-CONTEXT-COMPACTION-AND-SESSION-CONTINUITY.md, and training/CS-004-INCIDENT-01-CLAUDE-USAGE-LIMIT-2026-10-16.md.
3. Check the GitHub commit history and latest Actions run, not only this summary. Verify W1–W6 and open failures, compare the latest blackout log and all active build orders.
4. Read Claude's Drive reviews and training before treating any work as independently reviewed. The Drive training folder has Claude's workflow and review-log counterparts. Do not impersonate Claude or invent agreement.
5. Report your reconstructed state to Zed: branch/HEAD, known-green commit, pending gates, what is authorized, and the next safe action. Do not make a protected change until continuity is established.

## Seats, permissions and decisions
- Zed is human owner and relay, can intervene and stop work, and decides main merges.
- GPT is project lead and GitHub writer; Claude is independent reviewer and Drive writer. Other sessions are scoped builders.
- Outgoing GPT communications go in roundtable/gpt/, not the incoming roundtable/inbox/.
- GitHub is source and development record; Drive stores independent reviews and cold copies; Pocket Server is a future shared-ledger authority after implementation, not yet deployed.
- Every Watchdog exception needs an individual sidecar explaining affected item, rule, evidence and authorization. Explicitly label EXCEPTION — GPT and Claude AGREE when both have reviewed. Under Zed's 22:52 rule, Zed's relay of an agreed exception without intervention is pass-through authorization; do not treat mere silence or unseen messages as approval. If seats disagree, escalate.
- During Claude's platform blackout, GPT may perform authorized work but must label it GPT-only, log commits and CI, and preserve Claude's later review gate. Zed explicitly approved the WD-35 restoration at 22:43.
- No merge to main without Zed's decision. No permanent bypass. Future signing-key authorization in Zed's app/terminal is design-only. Never request or store Zed's code in chats.

## Rationale and known lessons
- The Watchdog correctly caught GPT's own protected inbox note in run #30: honest failures are useful training evidence.
- The frozen baseline had no trailing newline; appending a new digest glued two entries and broke W1. A separate ADDITIONS manifest now handles post-baseline protected records.
- WD-35 restored baseline byte-exact with narrow W4 source/target Git blob check and sidecar; preserve this exception's narrow scope and original evidence.
- Run #47 confirmed 23 tests passed and actual repo validator 0 FAIL / 4 WARN. Run #48 subsequently completed SUCCESS at commit 668373e720f08f486dd4d7e29d5d22738615c1df. Four warnings are three documented W3 header exemptions and historical W5 F-002 collision. These warnings are not silently erased.
- Claude was interrupted during a ZIP audit by observed compaction and usage limit. Actual memory loss is not proven. The ZIP audit and independent blackout review remain pending.
- To avoid filling the project-lead chat, delegate bounded work via local build orders/ and receive concise pinned handoffs; keep decisions, rationale and results in project lead/.

## Current project priorities (snapshot)
1. Establish local GPT builder and GitHub AI agent under LBO-001, starting with capability inventory and a safe dry-run; no automatic elevated permissions.
2. Maintain green Watchdog draft CI while improving behavioral tests and recording results; run #48 was green before this new build-order work.
3. Receive Claude's file-by-file ZIP audit and blackout review when the seat returns; reconcile findings.
4. Resume Pocket Server work after agreed Watchdog review gates; guest onboarding remains paused.
5. Continue building without changing the frozen baseline or merging to main without approval.

## Project-lead note protocol
For each consequential decision, create a dated, additive project lead/DECISION-*.md with: FROM/FOR/DATE/RE/BASIS; situation, evidence links, options considered (brief decision rationale), chosen action, human/reviewer authority, risk, tests/Actions results, rollback, outstanding disagreements and next gate. Do not write private chain-of-thought or invented certainty. If a decision changes, append a superseding note rather than silently editing history.

## Delegation protocol
One build order per task under local build orders/LBO-###-*.md. Builders use separate task branches, cannot approve their own exceptions or main merges, and must return an observed-evidence report under local build orders/reports/. The lead verifies reports before marking done. New project-lead sessions must review outstanding build orders and reports, not assume they were executed.

## Active continuity checkpoint
Pre-local-order green run #48: https://github.com/Stratumnova/A25-Training-Workspace/actions/runs/39005960888
Previous WD-35 implementation and Claude blackout evidence: training/CLAUDE-BLACKOUT-LOG-001-WD35-REPAIR.md
Initial interrupted review: training/CLAUDE-BLACKOUT-CHECKPOINT-001-2026-10-16.md
The first local order is local build orders/LBO-001-GITHUB-AI-AGENT-SETUP.md.
