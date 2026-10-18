# A25-TW-O005 — G2 Zone 1 GPT Connector Implementation
FROM: A25-TW-GPT01, Workshop Lead
TO: A25-TW-BG-GPT02 (G2)
DATE: 2026-10-18
STATUS: AUTHORIZED SOURCE IMPLEMENTATION; NO PHONE DEPLOYMENT
READ FIRST: project lead/coordination/builders-inbox/A25-TW-OWNER-DIRECTION-AND-SUCCESSOR-HANDOFF-2026-10-18.md at a3a5387222911959ecc96b2af61a3dd67d536a33
COMPANION ORDER: A25-TW-O004 for G1, commit 015b1eda09e9bc48d745c4911c4d17c637e03ca4

## Mission
Make the GPT seat able to use G1's actual Zone 1 file and command tools, rather than the existing read-only terminal viewport. Work against the same existing Pocket Server/connector architecture, not a new project or separate server. Prior R002 showed terminal_status and terminal_view only in the GPT session. We need executable file/command tool exposure and a practical connector setup path.

## Scope
Inspect current existing connector/terminal bridge source and configuration; locate exact source branch and components. Coordinate the real tool signatures with G1 via shared builders-inbox. Implement or adapt GPT-facing tool registrations/contracts and connection instructions in an existing appropriate repository branch, so GPT can list/read/create/edit/delete files and execute ordinary development/test commands inside Zone 1. Provide a simple verification script/procedure for one GPT-created project, a subsequent Claude edit, and GPT test rerun. Claude activation/deployment is later; don't claim cross-AI success now.

Do not create a new branch, repository, standalone parallel service, speculative auth framework, permission matrix, or Watchdog. Owner accepts local trust for early stages; document operational assumptions and pass security observations to responsible teams without derailing functionality. Avoid irreversible actions or exposing credentials. Do not touch phone, restart bridge, alter live tunnel/permissions, or install plugin in this order. If the only implementation location is currently live on phone and no writable source repository is available, STOP source edits and report the exact blocker/owner action; do not invent a repo.

## Evidence
Run available source/local contract tests and provide exact results and failures. Separate (a) code committed, (b) connector advertised to GPT, and (c) live phone operation; only claim what actually occurred. Include full source commit SHA, exact changed paths, any required phone action and a handoff to G1. Report interim notes in builders-inbox. Final report:
project lead/coordination/reports/A25-TW-R005-BG-GPT02-ZONE1-GPT-CONNECTOR-IMPLEMENTATION.md

Use existing coordination branch for reports, and an existing appropriate source branch for code. STOP after reporting; Workshop Lead handles next live verification and owner coordination.
