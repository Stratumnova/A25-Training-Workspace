# A25 Workshop — Source Dependency Map Pass 07
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Security, Archives, Claude
STATUS: VERIFIED read-only source inspection
Scope: source import and declaration lines only, via a25-test. No files or services modified.

## Observed modules and dependencies
- Workshop src/bridge.py: pathlib, FastMCP, AuthSettings, src.auth.BridgeTokenVerifier; terminal_status definition.
- Workshop src/auth.py: hmac, pathlib, MCP AccessToken and TokenVerifier; BridgeTokenVerifier class.
- Workshop src/chatgpt_readonly.py: pathlib, subprocess, FastMCP, TransportSecuritySettings; terminal_status, terminal_view, terminal_send definitions.
- pockettest/gate01/server.py: asyncio, json, os, Starlette, FastMCP, TransportSecuritySettings; ledger parsing, startup recovery, cursor, status, read, append, per-identity MCP creation, secret-path functions.
- pockettest/gate02/server.py: OAuth provider interfaces/settings, FastMCP, TransportSecuritySettings, Pydantic, Starlette, listening_wall.BodyLimitMiddleware; DenyAllProvider and health handler.
- pockettest/gate02/listening_wall.py: asyncio, json, os, urllib, observe function, BodyLimitMiddleware.
- pockettest-shared/shared/server.py: secure_files.secure_read/secure_append/secure_rdwr, storage.resolve_data_root/prepare_data_root, FastMCP, Starlette; ledger parsing/recovery/read/append and per-identity MCP creation.
- pockettest-shared/shared/storage.py: os/pathlib, resolve_data_root and prepare_data_root.
- pockettest-shared/shared/secure_files.py: os/stat/contextmanager, secure_append, secure_read, secure_rdwr.

## Cross-evidence comparison
Earlier process metadata showed live 'python -m src.chatgpt_readonly'. That module's inspected import declarations do not include src.auth.BridgeTokenVerifier, unlike bridge.py. This is a VERIFIED source difference, not a complete authentication assessment.
Gate-01 and Shared Space both contain ledger/cursor/recovery/append declarations; Shared Space additionally uses secure file/storage modules. Existence of source does not verify deployment, successful recovery, or operational security.

## Classification
VERIFIED: source imports/declarations and previously observed live process name.
UNKNOWN: runtime external authentication, current deployed code hash, full data flow, unused historical code, third-party/plugin registration, actual connector principals.
ADOPTED: mapping only; no building, remediation, installation, changes, or service commands.

## Next mapping-only inspection
Compare existing architecture documentation and source route definitions without reading credentials or private data. Preserve any discrepancy; do not assume design intent from names.
