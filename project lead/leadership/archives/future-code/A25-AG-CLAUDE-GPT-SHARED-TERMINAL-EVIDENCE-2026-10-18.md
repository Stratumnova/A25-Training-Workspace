# A25 Archives — Claude/GPT Shared Terminal Evidence Study
Date: 2026-10-18 (owner local)
Seat: A25-AG-GPT01
Scope: read-only terminal observation and archival report. No terminal_send invoked.

## Sources
1. Live direct Archives `terminal_view({session:"a25-test"})`, success with session a25-test, read_only true, returncode 0.
2. Live direct Archives `terminal_view({session:"a25-bridge"})`, success with session a25-bridge, read_only true, returncode 0.
3. Workshop GitHub report `project lead/coordination/builders-inbox/A25-TW-CLAUDE-TERMINAL-CROSS-SEAT-VERIFICATION-2026-10-18.md`, commit `7fd6cdf02c0b0c80c6455691caee1a9d0f4eb77d`, independently retrieved by Archives.
4. Owner-relayed Claude report `A25-CL-CLAUDE01-2026-10-18-TERMINAL-TEST-001-RESULT.md`, Drive ID `1-lv51kpTk9baEQ6KHJXuzxOypTLRAKNC`. Its raw Drive content was not fetched during this study.

## VERIFIED — direct Archives terminal evidence
- The a25-test screen ends with:
```text
~/a25-workshop/gpt $ pwd
/data/data/com.termux/files/home/a25-workshop/gpt
~/a25-workshop/gpt $
```
- The same screen contains earlier shell commands and output for Workshop Android/Termux mapping, including `id`, `getprop ro.build.version.release`, `getprop ro.build.version.sdk`, `ls -ld` on storage and app paths, `command -v` checks, `pm list packages 2>&1 | wc -l`, and `dumpsys package com.termux` filtering.
- The visible output includes Android 14 / SDK 34, UID 10376, Termux shared-storage symlinks, and Permission denied for two Google app-private directories. The `pm ... | wc -l` value 1 is a count of output lines, not installed packages.
- The a25-bridge viewport contains MCP CallToolRequest entries and HTTP 200/202 activity. These do not identify the caller or associate a particular HTTP request with the `pwd` command.

## HISTORICAL CLAIMS and corroboration
- Claude reported sending a single `pwd` through `terminal_send` to `a25-test`, receiving an ok result, and viewing the resulting output. The live terminal output corroborates the command and result, but not the submitting caller's authenticated identity.
- Workshop reported independently seeing the same `pwd` result in the terminal. Archives has now separately observed it.
- The previous attempt targeting `a25-gpt` was reportedly unsuccessful because that viewport displayed logs rather than an interactive shell; this study did not repeat that attempt.

## Findings
- VERIFIED: a shared a25-test shell viewport contains the expected `pwd` execution and output.
- VERIFIED: earlier Workshop read-only mapping command output is preserved in visible scrollback.
- SUPPORTED, not independently authenticated: Claude submitted the `pwd` command, followed by GPT and Archives viewing the same result.
- UNKNOWN: authenticated Claude-versus-GPT command provenance, caller-specific access controls, session isolation, and the enforcement meaning of `terminal_status` mode `read-only`. That status label must not be interpreted as proof that commands cannot execute.
- UNKNOWN: full command history beyond the currently visible scrollback; no claim of exhaustive audit.

## Owner authorization and changes
The owner authorized Archives to inspect the terminal and log findings for the study. Archives used terminal_view only, sent no shell commands, and made no phone file, service, permission, or configuration changes. This GitHub note is an additive archival record; originals remain unchanged.

## Next justified action
Preserve this as cross-seat shared-terminal evidence. Any further identity or permission-enforcement test requires a separately defined, owner-authorized scope. Do not infer secure identity separation from shared output.
