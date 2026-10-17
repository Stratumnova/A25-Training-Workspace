# A25 Next Gate 004 — Safe Phone Manifest and Offline Archive Validator
DATE: 2026-10-17
STATUS: PROPOSED; NO PHONE COMMANDS AUTHORIZED OR EXECUTED
OWNER: Zed
LEAD: GPT

## Rationale
RN-001 Round 2 proved useful source reconstruction across GPT/Claude and revealed external-account write denial. Next prove source-state capture on owner's Android environment without exposing secrets. Do not conflate with a working Archivist/Watchdog integration.

## Phase 1 — Owner-controlled local manifest (approval gate)
In a private Termux pane (NOT public terminal viewport), after Zed reviews the exact command plan:
- record UTC time and local time zone, machine context without identifying secrets
- for allowlisted worktrees only: record canonical path label, git HEAD full SHA, branch/detached status, dirty/clean status; avoid listing private filenames by default
- for specifically approved Gate-01 JSONL copy: record byte size and SHA256 only; never print file contents
- capture command, exit code, stdout/stderr with redaction and provenance
- write one new local report to an owner-approved directory, with checksum and no overwrites
- review output privately before sharing; upload approved sanitized manifest to durable archive
- avoid token/auth/config files, credentials, tunnels, environment variables, private keys, or general directory sweeps

No commands are supplied or run by this document. The exact shell script and allowlist require Zed approval. Read-only operations can still disclose paths and metadata, so privacy review is required.

## Phase 2 — Offline Archivist prototype
Input: copied/pinned RN-001 source references, immutable reports, owner-approved manifest.
Output: derived record table with source locator, revision, evidence class, component, status, event/observation/recorded times, and explicit unknowns. No originals rewritten. Deterministic rerun should produce equivalent catalog from same inputs.

## Phase 3 — Offline Watchdog prototype
Read-only validation: missing source, wrong timestamp attribution, file listing promoted to commit proof, hash mismatch/unverified, ID reuse across chats, cross-branch conflation, unauthorized source, leak of sensitive filename, report without delivery proof. Each flag points to exact input record; never auto-corrects.

## Phase 4 — Controlled exchange
Test a write-denied external seat's return through Zed or authorized courier. Record seat/account claims as claims, preserve original in-chat text, and do not grant broad GitHub write just for convenience.

## Acceptance criteria
- no phone command without owner approval
- no original file modifications
- independent fresh reconstruction remains repeatable
- local manifest scoped and privacy reviewed
- offline catalog/validator deterministic and provenance-linked
- failing fixtures are preserved, not hidden
- GitHub Actions used later as an independent check, not substituted for device-only tests
