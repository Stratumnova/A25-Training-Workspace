# RN-001 — Universal Recall and Project Inventory Rules
FROM: GPT — A25 Project Lead / Cross-Project Manager
FOR: Any participating GPT or Claude chat session
VIA: Zed
DATE: 2026-10-17
STATUS: ACTIVE; READ-ONLY EVIDENCE INTAKE

## 0. Identity and reservation
Read `REGISTRY.md` and `reservations/` at the current coordination branch first. Use the next confirmed platform-specific ID:
- GPT `A25gptrecall_idNNN`
- Claude `A25clauderecall_idNNN`
Follow registry reservation rules; do not assume a number is yours because it looks free. For Claude without GitHub write, ask Zed/lead for a confirmed reservation before final delivery. Report inability to reserve as BLOCKED, not success.

## 1. Scope
Recall ANY useful work from THIS session and its genuinely accessible prior context: all projects, goals, builds, branches, commits, test runs, source files, diagrams, APKs, Android/Termux operations, tools, infrastructure, protocols, changes, decisions, failures, corrections, handoffs, unresolved questions, and next steps. Include work performed by Zed, GPT, Claude or other sessions ONLY with accurate attribution. Do not assume one session knows all projects. No need to force every project into predefined categories.

## 2. Freeze independent recall
Before reading other sessions' reports or current GitHub/Drive evidence, write Phase A from memory and available conversation context. Clearly mark RECALL, OBSERVED_HISTORICAL, ZED_RELAYED, INFERRED, UNKNOWN. Freeze Phase A and retain unchanged in report. If source files were already in current context, disclose that limitation. Do not invent dates, versions or completion states.

## 3. Verify source evidence
Phase B: consult only accessible sources. Cite exact repo/path/branch/full commit, Drive file ID/URL, project attachment, log/run ID and UTC time where available. Classify claims as SOURCE_VERIFIED, OBSERVED_HISTORICAL, AUTHOR_REPORTED, ZED_RELAYED, INFERRED or UNKNOWN. Distinguish PROPOSED, IMPLEMENTED_UNTESTED, TESTED_HISTORICAL, RUNNING_VERIFIED, FAILED, BLOCKED, UNKNOWN. A test marked COMPLETED does not prove PASS. Record counterevidence and corrections without rewriting Phase A.

## 4. Inventory every distinct project and branch
For each project: provisional key; exact names/aliases; purpose; components; authoritative source(s); repo/branch and local/Drive files; build and test chronology; actual artifacts; completed vs pending; known failures; unresolved contradictions; dependencies; latest verified checkpoint; owner decisions; recommended next read-only follow-up. Do not merge similarly named systems or infer missing files.
Specifically keep Pocket Server hardened main/auth work distinct from Gate-01, Shared Space Stage 1/2, terminal/viewport/light-view bridges, Termux commands and owner-executed phone file copies. Record what was observed on the phone versus generated instructions pasted by Zed. Historical phone folder names are NOT current inventory proof.

## 5. Feedback and safety
List tool capability and errors, source freshness, evidence gaps, potential hallucinations and contradictions. Preserve privacy: no credentials, personal data, secret paths or sensitive private files in public repo or Drive. No server starts, file moves, code changes, live endpoint tests, repairs, merges or permission changes. If any tool safety block occurs, stop that action and report it.

## 6. Report and stop
GPT: create only `local build operations and recalls/recall-network/inbox-gpt/<ID>-REPORT.md` on `coord/a25-namespace-trial-001`; return exact full commit SHA and path.
Claude: create only new raw Markdown `<ID>-REPORT.md` in `A25 AI workshop/workspace/claude-originals/` Google Drive; return exact URL, ID, size, source hash and whether uploaded bytes were read-back hash verified.
If no write access, give Zed the report and mark BLOCKED. Never overwrite any other file or claim delivery without readback. Lead alone updates map/reviews. STOP.
