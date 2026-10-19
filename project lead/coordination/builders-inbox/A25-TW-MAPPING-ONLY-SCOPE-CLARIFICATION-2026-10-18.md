# A25 Workshop — Mapping-Only Scope Clarification
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, A25 Project Lead, Security, Claude, Archives, builders
STATUS: ADOPTED owner directive

Owner explicitly clarifies: A25 Workshop maps what exists and what can or cannot currently be seen. It does NOT build, fix, install, reconfigure, clean up, move, delete, restart, or actively probe systems. Other teams handle implementation and remediation.

Map each finding by provenance (Android native / Termux provided / A25 or Pocket Server custom-built / historical artifact / unknown), runtime status (verified active / verified inactive within defined scope / unknown), observability (visible / restricted / blocked), and evidence quality (VERIFIED / HISTORICAL CLAIM / ADOPTED / UNKNOWN). Do not equate source presence with running deployment or a tool's availability with authorization.

Use only bounded, non-invasive read-only views and commands. Do not open credentials or personal/private application data. Never send commands into service-running tmux panes. On a blocked step, stop that step and report the exact blocker to owner for review; do not install substitutes or route around restrictions. Preserve the original state. Do not recommend fixes as Workshop actions.

Earlier request to use alternative /proc/net/tcp inspection remains UNAPPROVED and should not be attempted unless the owner explicitly authorizes it. Existing worktree/tunnel inventory is a map, not a cleanup list.
