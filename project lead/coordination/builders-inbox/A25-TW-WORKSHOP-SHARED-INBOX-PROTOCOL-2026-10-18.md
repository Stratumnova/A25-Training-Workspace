# A25 Terminal Workshop — Shared Inbox and Short-Trigger Protocol
FROM: A25-TW-GPT01 — Workshop Lead
TO: Zed; A25-TW-BG-GPT01; A25-TW-BG-GPT02; future A25-TW-BC-CLAUDE01
DATE: 2026-10-18
STATUS: OWNER-REQUESTED COMMUNICATION CONVENIENCE — EXISTING A25 WORKFLOW RETAINED
BASIS: Approved Zone 1 Workshop Plan 001, Archives Review 022, Zed's 13:43 approval.

## Single check-in point
Both active GPT builders write their **progress, questions, blockers and handoff notes** as separate, uniquely named Markdown files under:
`project lead/coordination/builders-inbox/`

Formal order-completion reports remain separate, uniquely named Markdown files under:
`project lead/coordination/reports/`

Workshop Lead publishes new numbered orders under:
`project lead/coordination/orders/`

All use the existing `Stratumnova/A25-Training-Workspace` repository and `coord/a25-namespace-trial-001` branch. Do not overwrite another builder's files, silently revise evidence, create new branch/repo/folder, or treat GitHub author metadata as authenticated AI identity.

## Builder filing convention
- G1 interim: `A25-TW-BG-GPT01-YYYY-MM-DD-<topic>.md`
- G2 interim: `A25-TW-BG-GPT02-YYYY-MM-DD-<topic>.md`
- Claude C1 when activated: `A25-TW-BC-CLAUDE01-YYYY-MM-DD-<topic>.md`
- Formal reports: use exact destination named in pinned order; each includes source refs, verified observations, unresolved issues, and full commit SHA returned after publishing.
- If progress is unchanged, no redundant new file is needed. If a correction is needed, publish a distinct addendum.
- If GitHub write fails, return the exact failure to Zed for relay; do not claim the report was posted.

## Owner's short-trigger handoff
After relaying instructions to either or both builders, Zed can return to Workshop Lead chat and write:
- `done` — lead checks the existing inbox and reports, reads any newly published items, evaluates them, and reports next actions.
- `next` — lead checks records, resolves ready work and publishes the next warranted scoped order, then gives Zed the relay message/link.
- `status` — lead checks and briefly summarizes both builder states, blockers and owner decisions needed.
These words are **chat instructions to the Workshop Lead**, not automatic triggers or claims that an AI posted a file. If no new GitHub evidence exists, report that fact; do not guess progress. If multiple orders are active, use order IDs and file names to distinguish them.

## Preserve current process
This protocol is a shorthand for existing GitHub reads and handoffs, **not** a new messaging service, workflow replacement or autonomous cross-chat connection. Zed still relays pinned orders to separate chats; the lead checks GitHub on request. Existing Archives evidence classification applies. Claude C1 remains on standby until specifically activated. Drive boundaries remain unchanged.

## Initial orders
- `A25-TW-O001-BG-GPT01-POCKET-SERVER-SOURCE-ROUTE.md` (G1)
- `A25-TW-O002-BG-GPT02-GPT-CONNECTOR-CAPABILITY.md` (G2)
- `A25-TW-O003-BC-CLAUDE01-CLAUDE-READINESS-AND-CONNECTOR.md` (queued, NOT delivered/activated)
