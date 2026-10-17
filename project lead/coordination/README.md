# A25 Two-Session GitHub Handoff — Trial 001

FROM: GPT — A25 Project Lead
FOR: Zed, LB-GPT01, future Claude reviewer
DATE: 2026-10-17
RE: GitHub as explicit communication and evidence channel
BASIS: Zed's instructions and builder acknowledgment

## Golden rule
Truth and tech above lore. Always fail out loud.

## Seats and authority
Zed is human owner, relay, tie-breaker and present human Watchdog. Lead GPT assigns scoped work and reviews reports. LB-GPT01 builds and reports; Claude may later review independently. Same-project chat membership does not itself establish automatic shared context or message delivery. Identity labels in documents are claims, not authenticated principals.

## Protocol
1. Lead writes a numbered order under `project lead/coordination/orders/` on this coordination branch and links its exact commit.
2. Zed tells builder only to read the latest numbered order on the coordination branch (no copying full instructions).
3. Builder reads and confirms exact order ID/commit, creates its own implementation branch if needed, and writes an append-only report file under `project lead/coordination/reports/` **on the coordination branch**. If branch permissions or writes fail, report the blocker to Zed; do not pretend delivery.
4. Zed tells lead to inspect reports. Lead reads report directly from GitHub, verifies commit/file/test evidence, and issues follow-up order.
5. Never silently edit or overwrite orders, reports, or protected records. Corrections are new numbered addenda.
6. No merges to `main` without Zed's explicit approval. No private uploads or secrets into public A25.
7. Every handoff includes FROM, FOR, DATE, RE, BASIS, order ID, source commit, scope, evidence and status. GitHub timestamps/commit authors are not proof of which AI seat authored prose.

## Inbox / outbox
- Builder inbox: `project lead/coordination/orders/`
- Builder outbox / lead inbox: `project lead/coordination/reports/`
- First order: `orders/A25-NS-O001-NAMESPACE-REGISTRY-DESIGN.md`
- Builder response: `reports/A25-NS-R001-LB-GPT01.md` (to be created by builder)

## Trial success conditions
Builder reads order without Zed pasting its text; writes report to agreed path; lead retrieves it independently; exact commits and evidence are checked; unresolved issues fail loudly. This proves a GitHub handoff, **not** autonomous inter-chat awareness.
