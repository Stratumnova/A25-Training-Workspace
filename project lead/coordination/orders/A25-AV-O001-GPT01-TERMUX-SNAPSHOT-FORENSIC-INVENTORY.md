# A25-AV-O001 — Termux workshop snapshot verification

FROM: A25-AG-GPT01 Archives Lead
TO: A25-AB-GPT01 Archives Builder
DATE: 2026-10-18
STATUS: OWNER APPROVED — READ-ONLY
BRANCH: coord/a25-namespace-trial-001
REPORT: project lead/coordination/reports/A25-AV-R001-GPT01-TERMUX-SNAPSHOT-FORENSIC-INVENTORY.md

## Source
Zed will provide the ZIP named `AI workshop on zeds local system. copy on termx side..zip` to the builder. Zed describes it as a 1:1 copy of the Termux-side workshop. That parity is UNKNOWN until independently checked against a live phone manifest. If the exact ZIP is unavailable in the builder session, stop and report the blocker; do not substitute another ZIP.

## Required read-only work
1. Verify ZIP readability and integrity. Record input file size and SHA-256. Inventory all original archive paths, types, compressed/uncompressed sizes and CRC values; compute SHA-256 for every regular file. Include a sorted reproducible manifest in the report.
2. Inspect the Gate-01 JSONL backup as data. Record number of lines, JSON parse errors, event identifiers, authors and cursor fields when present. Do not infer live server recovery.
3. Inspect the nested Shared Space project ZIP without executing scripts. Check integrity, record its SHA-256, inventory contents, and identify any embedded version or commit marker.
4. Review checkpoint documents as historical source material, preserving their claims separately from independently verified ZIP facts. Identify discrepancies and evidence still needed.
5. Compare directly available source bytes or checksums with pinned GitHub originals when feasible, recording the exact comparison method. A narrative claim is not a byte-level match.
6. Screen for secrets or sensitive data. Never publish secret values or unredacted sensitive source contents. Record redactions and limitations.
7. Produce a verification matrix distinguishing archive integrity, file hashes, nested source parity, historical claims, and live Termux parity. Mark unsupported findings UNKNOWN.

## Limits
Do not modify the ZIP, execute included scripts, access or change the phone, server, tunnel, Drive, CI, GitHub source files or permissions. Do not create a branch, merge or deploy. Use REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED and UNKNOWN accurately.

## Output
Create exactly one new Markdown report at the REPORT path on the existing coordination branch. Return its path and full commit SHA, then STOP.
