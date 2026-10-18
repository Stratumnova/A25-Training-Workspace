# A25-TW Gate-02 Viewport Source Backup — Verification Record
Date: 2026-10-18
Seat: A25-TW-GPT01
Evidence: live read-only terminal_view(session="a25-test") capture of owner-executed commands.
Status: VERIFIED archive creation/listing/hashes; UNKNOWN extraction/restart restore.

## Scope
Owner requested preservation of Gate-02 four-session read-only viewport implementation for reuse as a reference by Gate-01 view/control bridge builders. This is a SOURCE backup, not a complete system backup.

## Verified commands and outputs
Working directory: ~/a25-workshop/gpt
- tar -czf backups/a25-gate02-viewport-20261018.tar.gz src/chatgpt_readonly.py tests/chatgpt_fourview_candidate.py backups/chatgpt_readonly-pre-fourview.py — completed without reported error.
- sha256sum backups/a25-gate02-viewport-20261018.tar.gz:
  5c504d82cf8a7694d7178d34d1de18a4079bcd768f737245e8130af7882864ae
- tar -tzf archive — listed exactly:
  src/chatgpt_readonly.py
  tests/chatgpt_fourview_candidate.py
  backups/chatgpt_readonly-pre-fourview.py
- sha256sum src/chatgpt_readonly.py:
  e85f2e4065c1d0ba6827f0d10f3429f89041069f9820fede4590422f26876519
- sha256sum tests/chatgpt_fourview_candidate.py:
  e85f2e4065c1d0ba6827f0d10f3429f89041069f9820fede4590422f26876519
  Hence candidate and installed source were byte-identical at the time of the check.

## Boundary
VERIFIED: tar readable and entries present, matching source/candidate hashes, source backup file included.
UNKNOWN: extracted file bytes verified against source; clean restoration; restart from backup; persistence across phone reboot; full Gate-02 data/credentials/Termux environment restoration. Archive is on same phone, so not off-device redundancy.
No private tunnel credentials or ledger data were intentionally included in this archive.

## Builder instructions / proposals, not deployed changes
Use as reference for a Gate-01 scoped viewport, retaining strict server-side allowlists and read-only capture. A control bridge must be separately designed and owner-approved with principal-specific authorization, bounded commands, and auditing. No builder may assume this archive grants execution privileges.
Keep this archive and its hash in recovery planning; copy to approved private/off-device storage before claiming disaster recovery.

## Related
- A25-TW-FOUR-VIEWPORT-LIVE-VERIFICATION-2026-10-18.md
- A25-TW-GATE02-VIEWPORT-AND-GATE01-BRIDGE-HANDOFF-2026-10-18.md
