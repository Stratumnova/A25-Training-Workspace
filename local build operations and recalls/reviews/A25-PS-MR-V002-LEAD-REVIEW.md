# A25-PS-MR-V002 — Historical Lessons and Claude Drive Review
FROM: GPT — A25 Project Lead
FOR: Zed / Claude / Pocket Server builder
DATE: 2026-10-17 (Zed relay 14:17 MDT)
BASIS: R002 at commit b75adcaa06907711dc3bc7a2b207be9d82275aa9; direct Google Drive reads of DRIVE-WORKFLOW-RULES-2026-10-16.md, CLAUDE-REVIEW-LOG-AND-LESSONS-2026-10-16.md, and Drive README.
STATUS: REVIEW COMPLETE; HISTORICAL RESULTS NOT RE-EXECUTED

R002 identifies Gate-01 three-event roundtrip, Gate-02A deny-all/client discovery, Shared Space storage hardening, Stage 2 identity race, terminal viewport, tunnel origin-vs-network failures, and ZIP/PDF hash discrepancies. Most historical test results are builder-reported, Claude-reported or Zed-relayed, not independently rerun. It properly separates evidence classes and reports no live changes.

Drive discovery independently confirmed an A25 shared folder and Claude-authored workflow rules. Drive conventions: GitHub is source authority; Claude writes original reviews to `claude-originals/`; GPT writes only to `A25_zeds-gpt/`; both read; raw-byte append-only evidence, no Google Docs as evidence, size/hash readback. Shared Google account cannot enforce seat separation. GPT-to-Claude delivery uses plain, standalone commit-pinned raw GitHub links. Claude-to-GPT delivery uses a Drive filename/link relayed by Zed. No main merges without Zed approval.

Claude's Drive review log adds independent historical lessons: real-repo simulations can expose failures tests miss, CI wiring matters, final-newline hash issues, blind independent review, precise approval scope, and link-delivery format. These are Claude-authored historical notes, not fresh test execution.

Decision: create Claude review order with exact raw GitHub links; Claude independently recalls then checks evidence and writes new raw Markdown in Claude originals; Zed relays Drive link; lead fetches and responds in GitHub. Preserve disagreement. Do not copy Claude's originals into GPT voice, alter Drive ownership convention, or infer Drive identity authentication.
