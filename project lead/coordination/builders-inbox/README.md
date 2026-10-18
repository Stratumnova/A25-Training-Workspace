# Archives Builder Inbox — A25 coordination

STATUS: ACTIVE INTAKE LOCATION — NOT AN APPROVAL OR TECHNICAL CERTIFICATION
OWNER: A25-AG-GPT01 Archives Lead
BRANCH: `coord/a25-namespace-trial-001`

## Purpose
A durable GitHub drop-off point for A25-AB-GPT01 builder notes, source-access ledgers, interim observations, verification receipts and blockers intended for Archives Lead review. This is **not** the separate historical `roundtable/builders-inbox/` introduced by unmerged PR #3; that PR remains Lost & Found and must not be merged or repurposed by this setup.

## Builder posting rules
- Create one new uniquely named Markdown file per handoff, prefixed `A25-AB-NOTE-` with date and subject; never overwrite earlier notes. Formal ordered reports still go to `project lead/coordination/reports/`.
- Include: seat/author, date/time and timezone (if known), related order/report, evidence source, exact commit/file IDs or read-only command and output digest, observed results, uncertainty, blockers and next recommended check.
- Classify each finding as REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED or UNKNOWN. A note's existence is not Archives acceptance; Lead reviews separately.
- For terminal/phone claims, distinguish a **builder-reported live terminal observation** from Archives-independent verification. Provide terminal tool/session and exact read-only commands/outputs or safe redacted receipts where available. Do not assert whole-device parity from a few matching files.
- Do not publish credentials, private keys, secret route paths, tokens, personally identifying paths, or raw sensitive payloads. Redact and state that redaction occurred.
- No modifications to phone, Drive, CI, server, source code, branches, PRs or permissions are authorized by this inbox. Do not use it as a task queue granting independent action.
- Stop and ask Zed if a write is safety-blocked; do not bypass a safety stop.

## First expected handoff
Record Zed's 2026-10-18 builder-reported read-only terminal-to-ZIP SHA-256 comparisons of six file mappings (including both `roundtable.jsonl` and `roundtable.backup.jsonl` against one Gate-01 backup). Include the original read-only terminal command and output if available, exact SHA-256 per file, observed path and timestamp, and state that **full 1:1 Termux parity remains UNKNOWN**. Do not invent missing receipts.
