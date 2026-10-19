# A25 Workshop — Plugin Tool Discovery Recovery Note
Date: 2026-10-18
Author: A25-TW-GPT01
Applies to: Gate-02 and future A25 connector/plugin builds

## Owner-observed recovery procedure (ADOPTED as troubleshooting guidance)
When a plugin tool was added to a running MCP service but the existing ChatGPT conversation still listed an older tool inventory, browser-side tool refresh alone did not resolve the stale tool list in that conversation. A new ChatGPT conversation did expose the new tool. Later the owner closed the ChatGPT application, revoked and restored plugin permissions in **app profile settings** (not the browser), and the original conversation then discovered all three tools. The owner emphasizes that **PC and phone settings/options are separate**; do not assume a browser-side permission or refresh operation is equivalent to mobile app profile permission reauthorization.

## Verified tool result after app permissions restored
In the original conversation, A25-TW-GPT01 independently discovered three tools: terminal_status, terminal_view, terminal_send. Called terminal_status: workspace_exists true, directories src/tests/logs/reports/backups/config true, identity gpt-workshop. Called terminal_send(session='a25-test',command='echo A25_THREE_TOOLS_VERIFIED'): response ok true. Called terminal_view(session='a25-test'): returncode 0 and screen displayed the command and output A25_THREE_TOOLS_VERIFIED. No files modified in this test.
terminal_status still returns mode='read-only', a stale metadata label; actual terminal_send functionality was verified by output.

## Reusable diagnostic sequence for future plugins
1. Confirm service actually runs the updated source and starts cleanly.
2. Check tool discovery in the current ChatGPT conversation; distinguish tool missing from connection failing.
3. Test fresh conversation tool discovery to isolate stale conversation definitions.
4. If tools remain stale, use the **relevant platform's app profile settings** to remove and restore plugin permission, then reopen/recheck. On phone use phone app settings; on PC use the corresponding PC controls. Do not assume identical menu paths or automatic cross-device propagation.
5. Re-discover tools and independently run a harmless end-to-end test; distinguish advertised tool, accepted invocation, and verified effect.
6. Do not claim reauthorization always fixes discovery. It worked in this observed case; future behavior may vary by platform/version.
7. Permission changes are owner-controlled; never claim GPT can revoke/grant its own app permissions.

## Classification
VERIFIED: all three tools available in current conversation; send/read echo marker successful; stale mode label.
OWNER-REPORTED: closed app, revoked then restored app-profile permission; browser refresh alone previously insufficient.
INFERENCE: stale client/session tool inventory was refreshed by app permission cycle; exact internal cause UNKNOWN.
ADOPTED: retain this diagnostic in future A25 connector runbooks; preserve PC vs phone distinction.
