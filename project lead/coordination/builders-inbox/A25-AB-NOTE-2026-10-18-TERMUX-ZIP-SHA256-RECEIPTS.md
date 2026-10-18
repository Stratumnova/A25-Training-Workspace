# A25-AB-NOTE — Termux-to-ZIP SHA-256 receipts

Seat: A25-AB-GPT01 (Archives Builder)  
Date: 2026-10-18 (calendar date from conversation; terminal execution time/timezone not captured)  
Related order: A25-AV-O001; subsequent A25-AV-O002 referenced by Zed, order text not yet retrieved  
Source: builder's A25 GPT Terminal plugin `terminal_view({})`, session `a25-gpt`, read_only=true, returncode=0; earlier user-supplied ZIP inspected in A25-AV-R001 commit `053d2e7868bfdd85d1659d40e8e7002e14d58a47`.  
Classification: **VERIFIED builder-observed terminal output**, **VERIFIED ZIP bytes in earlier offline inventory**, **UNKNOWN Archives-independent live phone attestation**.

## Original read-only commands supplied to Zed and observed executed

```bash
echo "===== GATE-01 LEDGER HASHES ====="
sha256sum \
  "$HOME/pockettest/gate01/roundtable.jsonl" \
  "$HOME/pockettest/gate01/roundtable.backup.jsonl"
echo
echo "===== SHARED SPACE ZIP HASH ====="
sha256sum \
  "$HOME/a25-workshop/gpt/backups/pockettest-build-shared-space-v0.zip"
echo
echo "===== CHECKPOINT PDF HASHES ====="
sha256sum \
  "$HOME/a25-data/shared-space/reports/checkpoints/"*.pdf
echo
echo "===== COMPLETE ====="
```

## Six mapping receipts

Phone-side paths are relative to `$HOME` (the terminal earlier identified `/data/data/com.termux/files/home`); sensitive credentials and configuration content excluded.

| # | Termux-side path | Corresponding uploaded main ZIP member | Terminal SHA-256 = offline ZIP SHA-256 |
|---|---|---|---|
| 1 | `pockettest/gate01/roundtable.jsonl` | `AI_Workshop/Roundtable_Backups/gate01_roundtable_2026-10-10.jsonl` | `61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9` |
| 2 | `pockettest/gate01/roundtable.backup.jsonl` | same Gate-01 backup member as #1 | `61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9` |
| 3 | `a25-workshop/gpt/backups/pockettest-build-shared-space-v0.zip` | `AI_Workshop/Project_Zips/pockettest-build-shared-space-v0.zip` | `94506d0f1980d52e8d2986ab910598cc142dfabb7cbf674110f6aeec70e909c6` |
| 4 | `a25-data/shared-space/reports/checkpoints/A25_Pocket_Server_Checkpoint_4_GPT_2026-10-11.pdf` | `AI_Workshop/Checkpoints/A25_Pocket_Server_Checkpoint_4_GPT_2026-10-11.pdf` | `1fb0d899e11b51d5966b29abf90ff6388bd6848da9ad020c82ca44db96079cff` |
| 5 | `a25-data/shared-space/reports/checkpoints/A25_Pocket_Server_Master_Checkpoint_2026-10-10.pdf` | `AI_Workshop/Checkpoints/A25_Pocket_Server_Master_Checkpoint_2026-10-10.pdf` | `72437b3d1390e8d31b15aadee7775aae851b5364b7e505b9085212a9f2d8f4b0` |
| 6 | `a25-data/shared-space/reports/checkpoints/Pocket_Server_Checkpoint_4_SharedSpace_Stage1_2026-10-11.pdf` | `AI_Workshop/Checkpoints/Pocket_Server_Checkpoint_4_SharedSpace_Stage1_2026-10-11.pdf` | `3ba5d35dbaf100457568c8c947966eebd9eae25637230af94c4e3f116e881c96` |

## Original terminal output evidence (safe excerpt; path prefixes shortened)

The `terminal_view` response returned `session=a25-gpt`, `read_only=true`, `returncode=0`, `error=""`. Terminal screen contained:

```text
===== GATE-01 LEDGER HASHES =====
61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9  .../pockettest/gate01/roundtable.jsonl
61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9  .../pockettest/gate01/roundtable.backup.jsonl
===== SHARED SPACE ZIP HASH =====
94506d0f1980d52e8d2986ab910598cc142dfabb7cbf674110f6aeec70e909c6  .../a25-workshop/gpt/backups/pockettest-build-shared-space-v0.zip
===== CHECKPOINT PDF HASHES =====
1fb0d899e11b51d5966b29abf90ff6388bd6848da9ad020c82ca44db96079cff  .../a25-data/shared-space/reports/checkpoints/A25_Pocket_Server_Checkpoint_4_GPT_2026-10-11.pdf
72437b3d1390e8d31b15aadee7775aae851b5364b7e505b9085212a9f2d8f4b0  .../a25-data/shared-space/reports/checkpoints/A25_Pocket_Server_Master_Checkpoint_2026-10-10.pdf
3ba5d35dbaf100457568c8c947966eebd9eae25637230af94c4e3f116e881c96  .../a25-data/shared-space/reports/checkpoints/Pocket_Server_Checkpoint_4_SharedSpace_Stage1_2026-10-11.pdf
===== COMPLETE =====
```

**Receipt limits:** The plugin supplies terminal screen text, not a signed command transcript, device filesystem snapshot, cryptographic phone attestation, or independent Archives Lead session. The viewport wraps long paths. Exact execution timestamp, device clock and full unwrapped stdout bytes cannot be recovered from the captured view. The earlier ZIP manifest's hashes provide a second source for *uploaded bytes*, not a second live phone read. No terminal operations were repeated to fill missing receipts.

**VERIFIED (bounded):** Six terminal-reported digests agree with offline archived-file digests; the two live ledger filenames are separate mappings to the *same* archive member. **UNKNOWN:** complete 1:1 workshop-to-Termux parity, live ledger recovery, server status, runtime identity, nested ZIP-to-GitHub parity, and whether these files changed after capture. **Next check:** separately approved full timestamped manifest; no current authorization for phone writes or new terminal operations. No secrets published.
