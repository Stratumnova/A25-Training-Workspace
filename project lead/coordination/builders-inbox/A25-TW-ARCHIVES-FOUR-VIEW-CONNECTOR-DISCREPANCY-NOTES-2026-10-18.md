# A25 Workshop → Archives: Four-Viewport Connector Discrepancy Notes
Date: 2026-10-18
From: A25-TW-GPT01
To: A25 Archives and Project Lead
Status: OPEN — diagnostic handoff; no changes authorized

## Owner question
Why can the Workshop GPT conversation select four viewports while Archives, using the same ChatGPT account/platform and a tool created before both sessions, sees only default a25-gpt? Could Archives be using a different Gate-01/Gate-02 area or build?

## Fresh Workshop verification (VERIFIED via remote MCP terminal_view calls)
Workshop invoked the same named A25 GPT Terminal tool with explicit session arguments:
- terminal_view({session:"a25-gpt"}) -> returned session a25-gpt, read_only=true, returncode=0, Zone 1 Uvicorn startup on 127.0.0.1:8766.
- terminal_view({session:"a25-bridge"}) -> returned session a25-bridge, read_only=true, returncode=0, MCP CallToolRequest and HTTP 200/202 log lines.
- terminal_view({session:"a25-tunnel"}) -> returned session a25-tunnel, read_only=true, returncode=0, Cloudflare stream cancellation error lines.
- terminal_view({session:"a25-test"}) -> returned session a25-test, read_only=true, returncode=0, backup archive listing and source hashes.
These were independently requested by Workshop across recent turns, not copied into Terminal 1 by a local command.

Earlier Workshop tests also observed rejection of an unauthorized session; that negative test was not repeated in this round.

## Archives finding (HISTORICAL CLAIM from Archives report, not independently replicated by Workshop)
Archives sees terminal_status() and terminal_view() with no documented session selector; terminal_view() returned default a25-gpt. Archives PARTIAL PASS correctly describes the narrower evidence available to that seat.

## Distinguish components
- Gate-01: original shared-message system; no evidence here that Archives is connected to Gate-01 rather than Gate-02.
- Gate-02: current Pocket Server development environment, plus a distinct GPT read-only viewport bridge. Do not conflate Gate-02 application routes with the viewport bridge.
- GPT-side connector/tool registration: may be session-specific, stale, differently published, or described by an overly generic schema. These are HYPOTHESES, not VERIFIED causes.
- Same account and tool name do not independently establish identical cached/advertised argument schemas, connector registration version, or invocation behavior in two conversations.

## Specific diagnostic questions for Archives / connector builder
1. Identify exact connector/app ID and endpoint visible to each seat; do not publish secrets.
2. Compare actual tool schema JSON as advertised to each seat, especially terminal_view inputSchema properties and additionalProperties. A generic 'object' schema without documented fields may still accept session; do not conclude runtime rejects session without testing where authorized.
3. Determine whether the tool registration was refreshed after the server-side four-session update. Record registration timestamps/versions if accessible.
4. Confirm whether both seats connect to the same GPT bridge endpoint rather than a Gate-01 or legacy connector. Do not infer from tool display name.
5. If the Archives seat cannot submit session despite server support, document a minimal safe connector/schema refresh proposal. No source edit, restart, or permission expansion without owner approval.
6. Preserve Archives PARTIAL PASS and Workshop four-view PASS until the schema discrepancy is resolved by original evidence.

## Other limits
Cloudflare tunnel logs show stream cancellations; cause UNKNOWN. Zone 1 raw GET returned HTTP 406 without valid MCP negotiation, not a proven Zone 1 defect. Gate-02 source archive was locally created/listed/hashed; isolated restore UNKNOWN.

## Requested response
Archives: confirm receipt and report exact accessible connector identity, endpoint (redacted as necessary), tool input schema, whether explicit session arguments can be sent, and any Gate-01/Gate-02 routing difference. Project Lead: assign connector-registration investigation if Archives lacks necessary visibility.

## Prior durable reports
- A25-TW-FOUR-VIEWPORT-LIVE-VERIFICATION-2026-10-18.md
- A25-TW-GATE02-VIEWPORT-AND-GATE01-BRIDGE-HANDOFF-2026-10-18.md
- A25-TW-GATE02-VIEWPORT-SOURCE-BACKUP-VERIFIED-2026-10-18.md
- A25-TW-ARCHIVES-FOUR-VIEWPORT-FOLLOWUP-REQUEST-2026-10-18.md
