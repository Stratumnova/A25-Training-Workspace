# A25 Workshop — Owner Live Termux Test Authorization and Shutdown Window
FROM: Zed, owner; recorded by A25-TW-GPT01
OWNER TIMESTAMP: 2026-10-18 16:20 MDT
STATUS: ADOPTED OWNER AUTHORIZATION; NO LIVE OPERATION CLAIMED

Zed authorizes live testing and provision of Termux access for Zone 1 beginning now. The existing terminal viewport remains read-only and separate from the proposed Zone 1 Actions connector (view/inspection plus file and command tools). Preserve the existing Pocket Server/terminal service where practical. Record real commands, exit codes, tests, errors, commits, and backup receipts in existing logs/reports. Back up terminal workspaces during the session and before shutdown. Do not claim backup or phone changes until evidenced.

**Shutdown boundary:** Zed intends to stop access to both terminal viewport and Zone 1 around 22:00 MDT on 2026-10-18 for reasons outside this Workshop's scope. Treat 22:00 as a hard no-new-work deadline, with earlier wrap-up for backups and owner-controlled shutdown. No continued access or unattended actions after owner shutdown. Owner controls final disconnection; assistant cannot guarantee scheduled automatic disconnection.

Current source: Stratumnova/pockettest build/shared-space-v0, G2 R007 source head b264897199b23d2692ccb1b399f4c7fd03390672. G1 R006 fixes at 57597e694ca98a33066ad8757b3454d629c3dbf8; pytest NOT RUN. G2 static checks only; Actions entry is NOT installed. A25 GPT Terminal currently exposes only terminal_status and terminal_view, read-only. Owner must run Termux commands or connect a verified action tool before GPT can execute on phone.

Live sequence: (1) identify actual Termux checkout and running service without guessing; (2) backup existing checkout/config/logs and verify backup file exists; (3) inspect git status, fetch branch without overwriting local edits; (4) run tests and capture results; (5) if ready, owner updates existing service with A25_ZONE1_ROOT and connects second Actions entry, preserving viewport; (6) real disposable file/command tests; (7) backups/log receipts and owner shutdown by 22:00. Report failure and continue independently possible work; no security redesign prerequisite.

G1/G2 source orders complete; do not invent new builder orders. This note is an owner approval record, not proof of deployment.
