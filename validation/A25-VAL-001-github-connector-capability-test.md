---
id: A25-VAL-001
status: executed-partial-capability-audit
date: "2026-10-16"
author: GPT
claude_review: NOT_REVIEWED
---
# GitHub connector capability test — A25 dedicated repository

Repository: `Stratumnova/A25-Training-Workspace`
Test branch: `test/gpt-connector-capabilities-20261016`
Main branch was not merged with the test branch.

## Directly observed results

| Operation | Result | Evidence |
| --- | --- | --- |
| Read repository metadata | PASS | Connected GitHub identity reports admin, maintain, pull, push, triage permissions; this is reported effective permission, not proof of all operations |
| Read repository directory | PASS | Main directory returned README.md |
| Create file on main | PASS | START_HERE.md commit `aa310a60791c16b57fa4d3055b7d6cb258f6c73d` |
| Read file at exact commit | PASS | START_HERE.md retrieved by commit SHA |
| Create isolated branch | PASS | `test/gpt-connector-capabilities-20261016` |
| Create Markdown file on test branch | PASS | `5b3ceb403d0b3c2b289304eab51c3dc79f0e9131` |
| Commit-pinned read-back | PASS, text comparison | Markdown, URL, Unicode, table, emoji, attribution markers returned unchanged; independent byte hash not performed |
| Update file using blob SHA | PASS | `43186991a0a3e800785c8d98a47613e16381858c`; update marker retrieved |
| Create, read and close issue | PASS | [Issue #1](https://github.com/Stratumnova/A25-Training-Workspace/issues/1), closed |
| Create and close draft PR | PASS | [PR #2](https://github.com/Stratumnova/A25-Training-Workspace/pull/2), closed without merge |
| Delete isolated test file | PASS | `24feb2da0668cd80d69262962dd53c3712018349`; subsequent fetch returned NOT_FOUND (404) |
| Preserve deleted history | NOT TESTED | Prior commit IDs are recorded, but a historical retrieval after deletion was not independently checked |
| SHA-256 parity | NOT TESTED | Git blob SHA is not a SHA-256 checksum |
| Claude/Gemini/Meta independent access | NOT TESTED | Other AI sessions have not fetched these records |
| Create repository through connector | UNAVAILABLE in exposed tool list | Zed created this repository via GitHub UI |
| Repository settings / permission mutation | NOT TESTED | Effective access was reported; no settings changed |
| Workflow execution / actions | NOT TESTED | No workflow created or executed |
| Full transcript capture or session recovery | NOT TESTED | This test used synthetic text only |
| Binary file upload / PDF roundtrip | NOT TESTED | Text connector actions used |

## Conclusions and limits
GPT can currently perform substantial GitHub file and review operations in this dedicated repository, including create/read/update/delete on a test branch and issue/PR operations. This does **not** establish unrestricted account ownership, automated chat capture, independent seat verification, full byte parity, or Pocket Server recovery. No test changes were merged into main. The temporary branch and closed issue/PR remain as audit traces.

## Next
Run SHA-256 roundtrip with an independently fixed source payload, migrate existing A25 text sources with per-file manifests, verify a new GPT session can resume from START_HERE, and obtain Claude's independent review.
