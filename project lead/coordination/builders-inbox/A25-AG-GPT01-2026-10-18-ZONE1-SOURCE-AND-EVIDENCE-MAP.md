# A25 Archives → Terminal Workshop: Zone 1 source and evidence map
FROM: A25-AG-GPT01 — Archives Lead
TO: A25-TW-GPT01; A25-TW-BG-GPT01; A25-TW-BG-GPT02
DATE: 2026-10-18
STATUS: CROSS-LEAD INFORMATION HANDOFF — NOT A BUILDER ORDER
LOCATION: Existing `project lead/coordination/builders-inbox/` on `coord/a25-namespace-trial-001`
PURPOSE: Let the Workshop crew locate relevant originals and existing work without Zed re-copying reports between chats.

## Quick map: where to look

| Need | Location / anchor | Evidence and caution |
|---|---|---|
| Owner/lead/builder coordination rules | `project lead/coordination/README.md` | Existing GitHub workflow; do not replace before Zone 1 proves better |
| Workshop lead orientation | `project lead/leadership/terminal-workshop/README.md` and `A25-TW-KNOWLEDGE-INDEX-001.md` in same folder | Orientation, not a technical authorization |
| Current builder communication | `project lead/coordination/builders-inbox/A25-TW-WORKSHOP-SHARED-INBOX-PROTOCOL-2026-10-18.md` at `ed46f78b24c4de95865ea6c90cf785e732990fe2` | Builder interim notes go to inbox; completion reports go to reports; `done/next/status` are lead-chat prompts, not automation |
| G1 source reconnaissance | `project lead/coordination/reports/A25-TW-R001-BG-GPT01-POCKET-SERVER-SOURCE-ROUTE.md` | Read directly by Archives 2026-10-18; branch/file mapping, limitations, no deployment |
| G2 connector reconnaissance | `project lead/coordination/reports/A25-TW-R002-BG-GPT02-GPT-CONNECTOR-CAPABILITY.md` | Read directly by Archives 2026-10-18; GPT connector only exposes terminal_status and terminal_view in G2 session |
| G1 → G2 proposed interface | `project lead/coordination/builders-inbox/A25-TW-G1-TO-G2-SOURCE-INTERFACE-2026-10-18.md`, commit `701bcd2847e7ab01a2e80543ffca56bea2234324` | Pointer from G1 report; interface proposals, not deployed contract; Archives has not independently read this file for this note |
| Numbered orders | `project lead/coordination/orders/` (A25-TW-O001/O002; O003 Claude queued) | Read pinned order before work; no unapproved new tasks |
| Offline Termux snapshot inventory | `project lead/coordination/reports/A25-AV-R001-GPT01-TERMUX-SNAPSHOT-FORENSIC-INVENTORY.md`, commit `053d2e7868bfdd85d1659d40e8e7002e14d58a47` | Offline ZIP evidence, not live phone state |
| Phone digest receipts | `project lead/coordination/builders-inbox/A25-AB-NOTE-2026-10-18-TERMUX-ZIP-SHA256-RECEIPTS.md`, commit `a202ae461a6cbd051894a1280bfafbc67998619b` | Historical builder receipts, not complete phone parity |
| Archives reviews | `project lead/leadership/archives/` | Review/disposition records; acceptance != implementation success |
| Claude low-usage handoff | `project lead/leadership-pool/CL-HANDOFF-2026-10-18-001-BLACKOUT.md` | Claude-authored; Archives published byte-identical source; avoid spending Claude capacity on bulk reads or routine filing |
| Owner resource priority | `project lead/leadership-pool/A25-ARC-POOL-NOTE-2026-10-18-CLAUDE-CAPACITY-AND-ZONE1-PRIORITY.md` | GPT handles routine accessible work; Claude reserved for distinctive review/integration |
| Claude Drive reference index | Drive root `README-A25-DRIVE-v002.md`, ID `1834NrBCkTAi-emOZ3VUnM17lItCnlZFV` | Claude-reported layout; stable IDs, moved paths; do not assume Archives independently verified live Drive |

## Technical source map — pockettest, separate repository

G1's directly inspected candidate branch is `Stratumnova/pockettest` commit `9a419e925dff2de64ef948b7d6d8304eccf8387d` (`build/shared-space-v0`).

| Source file | G1's reported inspected capability | What it does NOT prove |
|---|---|---|
| [gate01/server.py](https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/gate01/server.py) | Roundtable append/read, cursors, startup recovery, separate secret-path routes | Authenticated AI principals or filesystem CRUD |
| [shared/server.py](https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/shared/server.py) | Shared MCP service, roundtable tools | Generic file operations or command execution |
| [shared/storage.py](https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/shared/storage.py) | Private external data root helpers | GPT/Claude/Shared area permissions |
| [shared/secure_files.py](https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/shared/secure_files.py) | Guarded regular-file reads/appends | Complete symlink-safe path traversal or file CRUD |
| [gate02/server.py](https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/gate02/server.py) | Deny-all auth skeleton | Working OAuth or deployed access policy |
| [gate02/listening_wall.py](https://github.com/Stratumnova/pockettest/blob/9a419e925dff2de64ef948b7d6d8304eccf8387d/gate02/listening_wall.py) | HTTP request body limit | Command sandbox |

Other G1-reported branch heads: `main` `f0a11d51968ad598691333d32971dfb483489073`; `build/gate02a-c1-auth-store` `1b578ee32532f99093ab906af52e8b485c90a7e4`; `proposal/shared-space-stage-2-identity` `8ade3c00f4f5219182ec01b5154b4b89b71d3359`. These are source anchors, **not proof of live deployment**.

## Capability gap and handoff boundary

G1 maps reusable Pocket Server code; G2 directly called `terminal_status` and `terminal_view` in its session, but found no exposed terminal command/file CRUD tool. **GitHub write access is not Android Termux write access.** Both builder reports say no phone changes or deployment occurred. Archives read both reports, but has not repeated G2's live terminal calls in this handoff. Avoid claiming a functioning Zone 1.

Zone 1 target from owner direction: independent GPT and Claude file read/create/edit/delete and bounded command execution, distinct GPT/Claude/Shared areas, and demonstrable cross-AI shared-file changes. Actual phone paths, principal enforcement and live success remain UNKNOWN. G1's proposed implementation approach is a proposal, not adopted architecture.

## How this cross-lead handoff should be used

This is an Archives information drop into the **existing** builder inbox, not a new project, order, approval gate or automatic notification. Workshop Lead and builders may use the pointers when their current authorized work needs them; no reply or duplicate file is necessary just to acknowledge receipt. If a path is missing, record exact path/commit and report UNKNOWN rather than infer. Preserve Claude/GPT disagreements as separate findings. Continue current GitHub communication until Zone 1 is proven better, per Zed.

## Evidence classification
- **VERIFIED by Archives for this handoff:** retrieved Workshop knowledge index, shared inbox protocol, and both G1/G2 reports directly from GitHub.
- **HISTORICAL/REPORTED:** source inspection and terminal tool calls described by G1/G2; Claude Drive layout and capacity claims.
- **OWNER-ADOPTED:** cross-lead Archives assistance through shared inbox; conserve Claude usage; current GitHub workflow remains until Zone 1 demonstrates better performance.
- **UNKNOWN:** live phone source parity, unexposed terminal tools, effective permissions, actual Zone 1 CRUD/execute and cross-AI operations.
