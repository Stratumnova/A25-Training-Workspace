# A25-TW-O004 — G1 Zone 1 Workspace Implementation
FROM: A25-TW-GPT01, Workshop Lead
TO: A25-TW-BG-GPT01 (G1)
DATE: 2026-10-18
STATUS: AUTHORIZED SOURCE IMPLEMENTATION; NO PHONE DEPLOYMENT
READ FIRST: project lead/coordination/builders-inbox/A25-TW-OWNER-DIRECTION-AND-SUCCESSOR-HANDOFF-2026-10-18.md at a3a5387222911959ecc96b2af61a3dd67d536a33

## Mission
Construct the functional server-side foundation for ONE local Android/Termux Zone 1 workspace, analogous to a D: drive, so GPT and Claude can work on actual shared project files. This is construction, not security-team identity design. Use existing Stratumnova/pockettest source and branches; no new repository, branch, or separate server. Start from verified G1 R001 source map; check the branch before changing it. Coordinate with G2 via shared inbox.

## Scope
Implement, in an existing appropriate pockettest source branch, working MCP-accessible operations to list/read/create/edit/delete regular workspace files and inspect a workspace directory. Provide bounded command execution for ordinary development tasks in the workspace (e.g. pwd, list, Python version, run tests), with practical Android/Termux compatibility. Prefer simple clear interfaces over speculative security policy. A single root directory, with optional GPT/Claude/Shared subfolders as conventions, is acceptable; don't build an identity gate or complicated access matrix. Both AIs must be able to work on the same shared project. Use existing transport, avoid disrupting Gate-01 contracts.

Choose a working root via configuration, not a fabricated absolute phone path. Make setup repeatable and provide exact deployment instructions, but DO NOT deploy to phone, restart services, change tunnel, or expose public ports in this order. Do not delete existing user data or silently change older code contracts. Document minimal runtime assumptions and limitations. Ordinary coding/test commands should be possible; report any capability limitations honestly. Don't block on security architecture or Watchdog.

## Evidence and acceptance
Implement code and local tests for file create/read/update/delete and command execution using a temporary test root; demonstrate one sample shared project lifecycle. Preserve test stdout/stderr, failures and fixes. Report exact repo branch, full commit SHA, changed files, commands, results, and any inaccessible dependency. Distinguish source tests from phone runtime. If source edit is blocked by repository permissions, post a blocker with exact error and minimum owner action, rather than inventing success.

## Coordination
G2 owns connector/tool exposure and GPT-side invocation. Publish a short interface handoff to existing builders-inbox for G2 including tool names, arguments, responses, and configuration. Do not wait for G2 to design identity verification. Interim notes go to builders-inbox; final report path:
project lead/coordination/reports/A25-TW-R004-BG-GPT01-ZONE1-WORKSPACE-IMPLEMENTATION.md

Use existing coordination branch for notes/reports. Source changes belong only in an existing appropriate pockettest branch. Do not create branches, PRs, repos, folders outside the intended workspace layout, or deploy. STOP after reporting; Workshop Lead will coordinate next phone/live phase.
