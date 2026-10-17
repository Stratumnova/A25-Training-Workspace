# RN-001 Local Source Evidence Checkpoint 001
Date: 2026-10-17
Evidence class: Live read-only terminal observations via A25 GPT Terminal plus Zed's terminal relay and Android screenshots.
Observer: GPT lead (read-only viewer). Operator: Zed (ran commands).
Status: LOCAL METADATA VERIFIED; NOT FULL DEVICE INVENTORY OR LIVE SERVICE CERTIFICATION

## Git worktrees
1. ~/pockettest: Git top-level /data/data/com.termux/files/home/pockettest; branch main; HEAD f0a11d51968ad598691333d32971dfb483489073.
2. ~/pockettest-c1: Git top-level /data/data/com.termux/files/home/pockettest-c1; branch build/gate02a-c1-auth-store; HEAD 1b578ee32532f99093ab906af52e8b485c90a7e4.
3. ~/pockettest-shared: Git top-level /data/data/com.termux/files/home/pockettest-shared; branch build/shared-space-v0; HEAD 9a419e925dff2de64ef948b7d6d8304eccf8387d.

For all three, git status --porcelain=v1 -uno returned no entries and git diff --quiet returned exit 0. Tracked working-tree changes not reported. Untracked files excluded; this does not establish complete cleanliness or fresh test results. Staged changes would appear in status if present.

## Local workshop
~/a25-workshop/gpt exists and resolves to itself; ls -ld showed a directory (not symlink). git rev-parse failed: not a Git repository. Immediate entries observed: reports, backups, src, tests, logs, config. Names only; contents not inspected.

## Android shared storage
Zed screenshot showed Documents/AI_Workshop containing Checkpoints, Project_Zips, Roundtable_Backups. Separate screenshot showed a Markdown Claude review file in /storage/emulated/0/Download. This is not proof of identical files, backups, or symlinks.

## Gate-01 backup integrity
Observed path: ~/storage/shared/Documents/AI_Workshop/Roundtable_Backups/gate01_roundtable_2026-10-10.jsonl
Observed byte count: 441
Observed SHA256: 61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9
Matches previously recorded historical SHA256 exactly. This establishes equality with that reference digest assuming it was correctly attributed, NOT proof of live ledger equality, server health or recovery timestamp.

## Provenance and limits
The lead viewed output in read-only a25-gpt terminal after Zed ran commands. No terminal commands were sent by lead. No file contents, credentials or secrets read. Git status, directory and backup checks were owner-run read-only operations. No new code built or tested. Preserve distinct event time, observation time and recording time; exact command-run UTC timestamp not captured. This checkpoint is a leadership record, not a byte-for-byte archive of the entire terminal history.

## Next
Use this checkpoint as one input for an offline Archivist index, alongside pinned RN-001 original records. Prototype in existing approved paths only; no new directory or phone execution without authorization.
