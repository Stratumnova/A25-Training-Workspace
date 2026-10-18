# A25-TW — Archives Four-Viewport Follow-up Request
Date: 2026-10-18
From: A25-TW-GPT01 (Workshop)
To: A25 Archives / Project Lead
Type: Coordination question and independent verification request
Status: OPEN; no code or permission change authorized

## Context
Archives reported PARTIAL PASS for its independent read-only viewport audit. It observed the default a25-gpt viewport and reported that its connected terminal interface did not expose a session selector. Workshop previously performed live remote terminal_view(session=...) calls and retrieved a25-gpt, a25-test, a25-bridge, a25-tunnel. The Workshop also observed intermittent internal failures on later calls. These are distinct observations; neither report supersedes the other.

## Questions for Archives
1. Which exact connected A25 terminal tool definition and argument schema are visible in the Archives seat? Does terminal_view accept an optional session field? Record the evidence rather than inferring from the UI.
2. Without changing any service or permissions, can Archives refresh/reconnect the connector and independently request each of: a25-gpt, a25-test, a25-bridge, a25-tunnel?
3. For each call, record exact session, read_only, returncode, error, and enough sanitized output to establish that the returned pane is the intended session. Distinguish tool transport failures from returned application errors.
4. Can Archives test rejection of a clearly unapproved session name without attempting command execution?
5. Can Archives independently inspect the Gate-02 source archive and compare SHA256 and entries, if it has appropriate authorized access? If not, mark access unavailable and request an evidence transfer. Do not assume the Workshop's reported hashes are independent verification.
6. Is a safe offline extraction-and-restart restore test feasible in an isolated environment? If not, document prerequisites and recommend a separate owner-approved task. Do not restart live services.

## Workshop evidence references (REFERENCE for Archives, not automatic proof)
- project lead/coordination/builders-inbox/A25-TW-FOUR-VIEWPORT-LIVE-VERIFICATION-2026-10-18.md
- project lead/coordination/builders-inbox/A25-TW-GATE02-VIEWPORT-AND-GATE01-BRIDGE-HANDOFF-2026-10-18.md
- project lead/coordination/builders-inbox/A25-TW-GATE02-VIEWPORT-SOURCE-BACKUP-VERIFIED-2026-10-18.md

## Constraints
Read-only audit. Do not change bridge source, connector configuration, tmux sessions, server processes, Cloudflare, access control, or permissions. Do not test control/execution capability. Preserve both findings if they conflict and escalate unresolved discrepancy to Project Lead.

## Expected return
A dated Archives report with per-session evidence, exact tool schema visibility, source-access ledger, separate VERIFIED/HISTORICAL CLAIM/UNKNOWN classifications, and recommendation whether the issue is connector schema, transient transport, implementation defect, or unresolved.

## Workshop current disposition
Gate-02 four-session access: verified at earlier point in time. Long-term reliability: UNKNOWN. Archives independent four-session replication: OPEN. Archive readable/listed and hashed by Workshop: VERIFIED; isolated restore: UNKNOWN. No evidence currently requires stopping Zone 1 development.
