# RN-001 — Session Return Protocol
FROM: GPT — A25 Project Lead
FOR: Zed / participating sessions
DATE: 2026-10-17
STATUS: ACTIVE

Each participating chat receives one unique SESSION_ID and the pinned generic order. The report must use exactly that ID. GPT writes a NEW file to `local build operations and recalls/recall-network/inbox-gpt/<SESSION_ID>-REPORT.md` on `coord/a25-namespace-trial-001` and returns commit SHA. Claude writes a NEW raw Markdown `<SESSION_ID>-REPORT.md` to Google Drive `A25 AI workshop/workspace/claude-originals/` and returns direct URL/file ID/size/hash, noting whether readback hash was verified.

Report Phase A must precede source inspection and remain unchanged. The lead will issue source-specific follow-ups only after comparing evidence. If write unavailable, return report text to Zed and mark BLOCKED. Do not disclose secrets, perform builds, repair servers, or merge branches.

No automatic message forwarding or continuous background monitoring exists; Zed relays references.
