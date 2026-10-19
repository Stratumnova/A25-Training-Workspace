# Cleanup Pass 05 — Baseline Protection and Archives Decision Gates

DATE: 2026-10-19
FROM: A25-TW-GPT01
STATUS: GitHub source comparison only; no terminal commands, phone modifications or tests.
OWNER CUTOFF: 2026-10-18 15:00 MDT.

## Source documents read
- project lead/leadership/terminal-workshop/A25-TW-NOTE-2026-10-18-003-TERMINAL-CHECKPOINT-AND-LEAD-RESPONSIBILITY.md
- project lead/leadership/A25-OWNER-ADOPTED-OCT18-WORKING-TERMINAL-BASELINE-2026-10-18.md
- project lead/leadership/terminal-workshop/workshop clean up notes/A25-TW-CLEANUP-PASS04-2026-10-19.md

## Findings
1. The October 18 owner-adopted working terminal checkpoint is the authoritative *target configuration*, not a verified complete backup or an exhaustive dependency map. ADOPTED decision, not independent restore verification.
2. The original checkpoint note explicitly distinguishes working GPT terminal_send/terminal_view from a full Zone 1 installation, unrestricted Android access, and Claude parity at that time. The later October 19 exchange supplies additional evidence of Claude terminal interaction, without proving full Zone 1 deployment.
3. Owner's later 3 PM October 18 cutoff is a stronger provenance priority than the older generic pre-October-18 rule. Neither date nor lack of use in a bounded test proves safe removal.
4. Older materials may be historical reference while their *runtime files* remain essential. Treat documentary supersession and operational dependency as independent questions.
5. Archives has evidence custody and recommendation responsibility; only Zed approves cleanup. The workshop lead can record candidates but not designate items safe to delete without proof.

## Decision gate for each candidate
- IDENTIFY: exact path, origin, modification date, size, and unique identifier/hash where available.
- DATE: pre-cutoff, post-cutoff, or timestamp UNKNOWN; don't infer from date-only headings.
- DEPENDENCY: currently used (verified), possibly used (unknown), not referenced in bounded evidence (not proof of unused).
- RECOVERY: sole known copy, redundant verified copy, or unknown; test restore only with separate approval.
- ARCHIVES: recommend KEEP / ARCHIVE / INVESTIGATE / PROPOSE REMOVE with rationale and original evidence.
- OWNER: record Zed's explicit disposition separately; recommendation alone never authorizes modification.

## Concrete current dispositions
PROTECT: Workshop bridge runtime, MCP connections, a25-test, a25-gpt, active tunnel configuration until verified.
INVESTIGATE: pockettest, pockettest-c1, pockettest-shared, older bridge and viewport snapshots, other tmux sessions and remote plugin registrations.
REFERENCE PRESERVE: original V1 protocol, decisions, and Zone 1 source contract; historical design alone does not mandate running them.
NO SAFE-TO-REMOVE FINDING: no component has been verified as independent of current startup/restore requirements.

## What can be done within present permission
GitHub document comparison, existing viewport reads, classification and reports. No terminal_send, even for read-only shell commands, under current view-only direction. No extraction, process probes, file moves, restarts or deletion.

## Next evidence needed
A separately authorized process/source/startup map and a preservation manifest for backups; until then Archives should receive these as investigation candidates, not removal orders.
