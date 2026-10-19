# A25-TW-GPT01 — Android / Termux Capability Mapping, Read-only Pass 3
Date: 2026-10-18
FROM: A25-TW-GPT01 Workshop Lead
FOR: Zed, A25 Project Lead, Archives, security pool, builders
BASIS: Owner-authorized read-only reconnaissance; terminal output independently observed via terminal_view in a25-test.
STATUS: VERIFIED within stated scope; UNKNOWN where untested. This is a new additive report, not a replacement for prior reconnaissance.

## Owner restrictions (ADOPTED)
No moving, editing, deleting, creating, installing, restarting, invoking apps, privilege escalation, or access-bypass attempts on the phone. Terminal use is only to read existing state and report. Do not perform active access tests. For denied or sensitive areas, inspect once or twice at most, document, and stop. Report proposed testing areas separately for owner authorization. This GitHub note is explicitly owner-requested; no phone modification authorized.

## Commands observed (read-only)
Through terminal_send to tmux session a25-test and subsequent terminal_view:
- id; getprop ro.build.version.release; getprop ro.build.version.sdk
- ls -ld ~/storage ~/storage/shared ~/storage/downloads
- command -v for selected Android/Termux tools
- pm list packages 2>&1 | wc -l (output-line count only; no package inventory established)
- ls -ld /data/user/0 /data/data/com.termux and named Google app directories
- dumpsys package com.termux 2>&1 | grep ... | head (no matching output)
- id -u; test -r on two private app directories.
No files or settings changed; no application launch; no private data read.

## VERIFIED findings
- Android 14, SDK 34.
- Termux Linux UID/GID 10376 (u0_a376); SELinux context untrusted_app_27. No root identity shown.
- Termux shared storage symlinks: ~/storage/shared -> /storage/emulated/0; ~/storage/downloads -> /storage/emulated/0/Download.
- Installed executable paths found for termux-info, am, pm, cmd, su, ssh, git, python; termux-setup-storage and termux-open also found. Presence does NOT prove permission or successful invocation.
- /data/data/com.termux directory is accessible to its own UID. /data/user/0 parent metadata showed system ownership and traversable permissions, not authorization to read other app data.
- ls on /data/data/com.google.android.apps.docs and /data/data/com.google.android.gm returned Permission denied. test -r on both returned not-readable. Treat those private app paths as STOP boundaries; do not retry.
- pm list packages 2>&1 | wc -l printed 1. This is a count of stdout/stderr lines, NOT a count of installed packages; the actual output was not captured.
- dumpsys package com.termux filtered for selected permissions returned no matching lines. Effective Android permission grants are UNKNOWN.

## Boundaries for teams
SAFE FOR READ-ONLY INSPECTION: A25 source/workspace files, non-secret directory metadata, known tmux process/session metadata, Android/Termux version and identity, shared-storage symlink metadata.
SENSITIVE — METADATA ONLY: Android shared storage (do not enumerate personal downloads/media); app package metadata (only when read-only and approved); private configurations (permissions only, never credential contents).
STOP / DO NOT REVISIT: Google Drive and Gmail private app directories denied by Android sandbox; no repeated attempts, no alternative bypass routes.
NOT AUTHORIZED: invoking Android intents, content providers, exported components, Termux storage permission setup, root/su execution, app launch, OAuth/account login, network probing, privilege escalation, modification of any phone state.
POSSIBLE FUTURE CONTROLLED TEST AREAS (not approved): dedicated dummy Workshop folder; non-sensitive package visibility; deliberately shared test file; Android intent interaction using a test-only app; separately authorized Google Drive connector. None of these were tested.

## Important distinction
A readable shared-storage link is not permission to browse every file. An installed shell utility is not evidence of granted Android permissions. App-private storage and Google Drive cloud account are separate access paths. A denied filesystem path does not prove all possible integrations unavailable; it is a boundary to respect, not a challenge to bypass.

## Open questions (UNKNOWN)
Actual package inventory, effective Android permission grants, accessible Android providers/intents, Google Drive cloud connector scope, ability to interact with other apps, root availability, security controls beyond the observed shell identity.

## Recovery and evidence classification
VERIFIED means direct terminal output or source observed; HISTORICAL CLAIMS from earlier reports are not automatically verified. No adoption of broader permissions or production readiness. Preserve this report alongside prior leadership/security reports.
Prior reports:
- project lead/leadership/A25-TW-TERMUX-STORAGE-SECURITY-RECON-2026-10-18.md
- project lead/leadership/A25-TW-GATE02-OPERATIONS-RECOVERY-2026-10-18.md
- project lead/coordination/builders-inbox/A25-TW-GATE02-SECURITY-LEADERSHIP-HANDOFF-2026-10-18.md

## Next justified action
Continue read-only capability mapping with explicit boundaries; avoid repeated private-app path checks. Send proposed active tests to owner for separate approval. No changes to phone, Gate-01, Gate-02, or existing GitHub reports.
