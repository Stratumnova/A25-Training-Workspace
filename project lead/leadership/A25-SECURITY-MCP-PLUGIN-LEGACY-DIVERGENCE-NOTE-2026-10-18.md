# A25 Security — Legacy MCP / Plugin Divergence Notice
Date: 2026-10-18
FROM: A25 Workshop Mapping
TO: A25 Project Lead and Security Team
STATUS: OWNER-REPORTED + VERIFIED LOCAL EVIDENCE; REGISTRATION UNKNOWN

## Owner statement (owner-reported, not independently verified)
Zed confirms having created several plugins/connectors for **both Claude and ChatGPT** during early Pocket Server and viewport development. Do not infer there was only one plugin per platform, or that the current bridge replaces the earlier integrations.

## Verified local evidence
- Gate-01 README documents separate Claude and GPT MCP endpoints, with route-derived identity.
- Gate-01 and Gate-02 virtual environments each have mcp and uvicorn executables.
- Gate-02 baseline source has OAuth provider interfaces and DenyAllProvider.
- Workshop src/bridge.py imports BridgeTokenVerifier from src/auth.py; src/chatgpt_readonly.py has separate transport-security imports and no such import in inspected declarations.
- A live process was observed running src.chatgpt_readonly.
- Two cloudflared processes reference the a25-gpt-bridge named tunnel and same config.
- Oct 8 recovery index references historical pocket-server-gate02 tunnel, not a verified current remote registration.

## Security mapping question
Build a **per-platform, per-plugin historical inventory**: name/ID, creation period, intended endpoint, platform (Claude vs GPT), tool surface, identity/auth method, current registration/enabled status, and local process/tunnel relationship. Do not collapse MCP server instances, platform-side plugins, Cloudflare tunnels, and local Python packages into one category.

## Open unknowns
Number and IDs of early plugins, active vs stale registrations, permissions, authentication enforcement, endpoints still registered, whether old secret-path identities remain configured, relationship to 'viewport'. No active exploit, compromise or vulnerability is established merely by source differences.

## Scope / handling
Workshop remains **mapping-only**. No uninstall, edits, resets, reconfiguration, active endpoint tests, credential reads or cleanup. Security/Lead own interpretation and remediation. Treat historical documents as reference; preserve disagreements and provenance.
