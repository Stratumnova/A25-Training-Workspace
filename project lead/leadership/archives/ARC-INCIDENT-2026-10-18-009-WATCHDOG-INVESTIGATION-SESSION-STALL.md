# ARC Incident 009 — Watchdog investigation session interruption and recovery routing

**Date:** 2026-10-18
**Author:** A25 Archives Lead (GPT), acting on Zed's request
**Status:** RECORDED for leadership review; proposed procedures NOT ADOPTED
**Scope:** Read-only investigation continuity; no Watchdog code, PR merge, CI or phone changes

## Trigger and evidence
- **REFERENCE (owner-provided screenshot):** Another GPT session began the six-question read-only Watchdog approval/merge investigation, searched GitHub materials, and displayed a preliminary conclusion that PR #3 is builder-intake documentation rather than the implementation PR. Zed reports the session froze. Screenshot is in the owner-to-Archives conversation; no GitHub source for the screenshot is asserted.
- **VERIFIED (GitHub inspection on 2026-10-18):** The newest 25 commits returned for `coord/a25-namespace-trial-001` end at `71e58a4bc69f137bf3a329711fb0a852214c260d` (AB-05 Watchdog evidence), with no subsequent six-question investigation report in that checked range. The newest 15 `main` commits end at `34b0d235a2bc78c975c57c1d16ecd74028832f5d`, likewise without an identifiable new investigation report in that range. This is a **bounded commit-history check**, not proof that no file exists anywhere on GitHub or outside these branches.
- **VERIFIED (PR #3 metadata/diff from separate direct GitHub inspection):** https://github.com/Stratumnova/A25-Training-Workspace/pull/3 adds two `roundtable/builders-inbox/` Markdown files and no Watchdog code or workflow file. The PR is open and unmerged.
- **UNKNOWN:** Whether the GPT session failed technically, was interrupted by the client, or had an unpublished final response; exact time and mechanism; whether it wrote elsewhere. No inference of approval, deployment or CI causation is justified from the screenshot.

## Leadership problem
Long read-only investigations can be lost at the chat/tool boundary before the result is durable. Owner may see research activity but no deliverable, creating repeated investigation work and ambiguous responsibility. A visible preliminary finding must not be promoted to an adopted decision or a complete report.

## Proposed Roundtable assistance — NOT ADOPTED
1. Roundtable Lead maintains a task receipt with owner authorization, precise six questions, evidence links, assigned investigator, read-only scope and expected report path.
2. When a seat stalls, mark its work **INTERRUPTED / OUTPUT NOT VERIFIED**, rather than failed implementation or completed research. Roundtable may reassign the evidence-reconstruction task to an independent seat; do not assume the interrupted seat's unpublished findings.
3. Keep an explicit owner decision gate: no merge, workflow rerun, branch modification or permissions change without Zed's approval.

## Proposed Archives assistance — NOT ADOPTED
1. Preserve the owner's screenshot and preliminary statements as REFERENCE, without inventing missing final findings.
2. Maintain a compact source-access ledger, checked branch/SHA, exact original links, verified facts, unresolved claims and work still needed. Separate archival acceptance from technical approval.
3. At an interruption, publish a small durable **recovery checkpoint** (not a fabricated final report) if authorized: completed original-source checks, open questions, and resume instructions. For sensitive tool safety blocks, present exact payload and await owner approval before retry.
4. Compare later GPT and Claude reports independently. Preserve conflicting claims until original evidence resolves them; escalate unresolved conflicts to GPT Lead.

## Immediate disposition
- PR #3 remains untouched.
- Six-question approval-to-implementation-to-CI causation investigation remains **OPEN / UNKNOWN**.
- Next justified action: Project Lead assigns a fresh read-only investigator using the existing WD-000, BI-001, PR #3, WD-05 and AB-05 source index, and requires a durable report with exact citations. Archives reviews its source ledger; Claude provides independent review if requested.
- This document is an incident/continuity note only. Zed and authorized project leadership must decide whether to adopt the proposed recovery procedure.

## Direct GitHub sources
- PR #3: https://github.com/Stratumnova/A25-Training-Workspace/pull/3
- AB-05: https://github.com/Stratumnova/A25-Training-Workspace/blob/71e58a4bc69f137bf3a329711fb0a852214c260d/project%20lead/coordination/reports/A25-AB-R005-GPT01-WATCHDOG-SAFETY-CI-EVIDENCE.md
- Coordination branch: https://github.com/Stratumnova/A25-Training-Workspace/tree/coord/a25-namespace-trial-001
