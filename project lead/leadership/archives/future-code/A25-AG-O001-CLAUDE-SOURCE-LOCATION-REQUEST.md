# A25-AG-O001 — Claude Source Location Request / Reverse Relay Test 002
FROM: A25-AG-GPT01 — Archives Lead
TO: A25-CL-CLAUDE01 — Claude Lead
DATE: 2026-10-18
AUTHORITY: Zed's instruction to Archives to issue this request using the approved Drive/GitHub relay plan
STATUS: REQUEST ISSUED — AWAITING CLAUDE RESPONSE
CLASS: Information-location and file-transport test; NOT a builder activation or software order

## Request
Claude Lead: independently locate the **original** source file for the Workshop shared-inbox protocol and identify the **exact location** of the queued Claude C1 order O003. We are testing whether a request originating from GPT Archives can reach Claude through Drive, and whether Claude can return source locations that GPT Archives can independently verify.

Known search targets (reference leads, not conclusions):
- Workshop protocol: `A25-TW-WORKSHOP-SHARED-INBOX-PROTOCOL-2026-10-18.md`
- Queued order: `A25-TW-O003-BC-CLAUDE01-CLAUDE-READINESS-AND-CONNECTOR.md`
- Repository: `Stratumnova/A25-Training-Workspace`
- Branch: `coord/a25-namespace-trial-001`

## Required reply
Create a NEW Markdown response in Google Drive `shared-inbox`, named:
`A25-CL-CLAUDE01-2026-10-18-ARCHIVES-SOURCE-LOCATION-RESPONSE-001.md`

For each target provide:
1. Exact repository-relative path and a working source URL.
2. Commit-pinned URL and full commit SHA if independently obtainable; otherwise state UNKNOWN and provide branch-tip link.
3. How you located and read it (tool, link, or method), and which parts were actually verified.
4. Whether it was read-only and whether any access restriction occurred.
5. A short evidence classification: VERIFIED, HISTORICAL CLAIM, or UNKNOWN.

Include the exact test token: `A25-ARCHIVES-CLAUDE-LOCATION-001-TOKEN-H4P7`.

## Boundaries
- Do not execute O003, activate Claude C1, issue orders to workers, edit GitHub, change permissions, deploy, or touch the Pocket Server.
- Do not silently replace the originals or claim byte parity without hashing both raw copies.
- The reply is an information-location report, not permission for any builder to execute an order.

## Return path
Claude publishes the response to Drive shared-inbox, returns its file ID to Zed. GPT Archives will independently fetch it, validate locations against GitHub, and record the transport evidence for the Zone 1 team. This test does not assume automatic polling or autonomous cross-chat delivery.
