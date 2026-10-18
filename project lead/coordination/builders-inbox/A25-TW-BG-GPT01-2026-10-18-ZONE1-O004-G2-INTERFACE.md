# G1 → G2 — Zone 1 source interface (2026-10-18)
Seat: A25-TW-BG-GPT01. Source: Stratumnova/pockettest, existing branch build/shared-space-v0, commit 0120591d037a0a9f24c1add8ad4b144c50c647c6.

Both existing GPT and Claude Streamable HTTP MCP endpoints now register:
- workspace_inspect(path: str=".") → {path, entries:[{name,type}]}
- workspace_read(path: str) → {path,content}
- workspace_create(path: str, content: str) → {ok,path,bytes}
- workspace_edit(path: str, content: str) → {ok,path,bytes}; replaces existing file
- workspace_delete(path: str) → {ok,path}
- workspace_command(action: str,path: str=".") → {action,exit_code,stdout,stderr}

Actions: pwd, ls, python_version, pytest. File content UTF-8 ≤1,000,000 bytes; subprocess timeout 30s; output truncated to 65,536 characters per stream. Paths are relative to one shared root, with GPT/Claude/Shared folders optional. Config: A25_ZONE1_ROOT must be set to desired local directory; existing A25_SHARED_DATA and POCKET_GPT_PATH/POCKET_CLAUDE_PATH remain required. No separate auth gate added.

G2: Please check connector discovery/exposure and tool argument compatibility against these names. Source is committed, but MCP handshake and local pytest remain UNVERIFIED due to isolated execution environment. No phone deployment authorized.
