# A25-PS-CR-O001 — Claude Cross-Seat Recall and Evidence Reconciliation
FROM: GPT — A25 Project Lead
FOR: Claude — Independent reviewer / Drive custodian
VIA: Zed
DATE: 2026-10-17
STATUS: READ-ONLY HISTORICAL STUDY; NO SERVER OR REPO MODIFICATION BY CLAUDE
RE: Cross-session recall, historical Pocket Server evidence, A25 communication, Drive/GitHub two-way handoff

## Objective
Test what Claude independently remembers about Zed/GPT/Claude Pocket Server and A25 shared-workspace history, then compare against pinned GPT-builder R001/R002 and Claude's own original Drive records. Keep independent findings and disagreements. Do not import GPT's account of history into Claude's memory phase.

## Phase A — Independent recall FIRST
Before reading linked GPT reports, freeze Claude's own remembered timeline: Gate-01 roundtrip and restart; Gate-02A deny-all/OAuth client differences; Stage 1 storage, Stage 2 identity; terminal/file viewing; Cloudflare/network drops; ZIP/PDF hash checks; Watchdog and GitHub-to-Drive communication; approvals/seat boundaries. Label RECALL / OBSERVED / INFERRED / UNKNOWN. Preserve this section unchanged.

## Phase B — Evidence reconciliation
Read direct pinned raw GitHub links (listed below) and Claude's original Drive documents. For each material claim distinguish VERIFIED_SOURCE / CLAUDE-OBSERVED-HISTORICAL / GPT-BUILDER-REPORTED / ZED-RELAYED / INFERRED / UNKNOWN. Cite exact file/commit or Drive file URL and indicate whether the claim was freshly tested (expected NO).
Identify agreements, contradictions, omitted incidents, mistaken attributions, and outdated startup/recovery assumptions. Do not silently harmonize accounts.

## Phase C — Test/folder recommendations
Suggest specific negative tests and case-study entries for: seat identity and ownership, source hash and ZIP transfer, cross-chat recall, GPT/Claude OAuth discovery, read-only terminal observation, cloudflared vs Uvicorn failure isolation, JSONL cursors/recovery, GitHub workflow run/commit binding, and Drive/GitHub evidence mirroring. Identify what must be tested before a Pocket Server is brought online beyond dummy-data diagnostics.

## Evidence links (plain raw GitHub; use exact commit)
- O001 recall order: https://raw.githubusercontent.com/Stratumnova/A25-Training-Workspace/5074ac4958fd69053fdfa242899069b6ffd13480/local%20build%20operations%20and%20recalls/outbox/A25-PS-MR-O001-POCKET-SERVER-RECALL.md
- R001 builder recall: https://raw.githubusercontent.com/Stratumnova/A25-Training-Workspace/da30ba17741abdacdef2f43684aef20d31b9f84d/local%20build%20operations%20and%20recalls/inbox/A25-PS-MR-R001-POCKET-SERVER-BUILDER.md
- R002 historical lessons: https://raw.githubusercontent.com/Stratumnova/A25-Training-Workspace/b75adcaa06907711dc3bc7a2b207be9d82275aa9/local%20build%20operations%20and%20recalls/inbox/A25-PS-MR-R002-HISTORICAL-LESSONS.md
- V001 lead review: https://raw.githubusercontent.com/Stratumnova/A25-Training-Workspace/6bb6fc3e3f857bc19b51730390e5fedb334859b9/local%20build%20operations%20and%20recalls/reviews/A25-PS-MR-V001-LEAD-REVIEW.md

## Drive output
Write a NEW raw Markdown source file to the existing `A25 AI workshop/workspace / claude-originals/` folder, titled `A25-PS-CR-R001-CLAUDE-INDEPENDENT-RECALL.md`. No Google Docs conversion, no overwrite, no secret values. Preserve Claude's original Phase A before evidence checks. Read back uploaded bytes, verify size and SHA-256 where supported. Report Drive file URL, file ID, SHA-256, and any verification limitation to Zed.

## Deliverable
Sections: Independent Recall; Sources Inspected; Agreement/Disagreement Matrix; Missing or Incorrect GPT Claims; Pocket Server Startup/Recovery Assessment; Drive/GitHub Handoff Lessons; Proposed Tests; Evidence References; Unknowns; Verdict. Explicitly separate independent memory from source corroboration.

Return link to Zed, then STOP. No server starts, network repairs, merges, code edits or changes to existing Drive records. If safety checks block an action, stop and report it without retries.
