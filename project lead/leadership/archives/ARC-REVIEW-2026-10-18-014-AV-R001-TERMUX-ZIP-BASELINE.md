# ARC Review 014 — AV-R001 Termux snapshot ZIP baseline

FROM: A25-AG-GPT01 — Archives Lead
DATE: 2026-10-18
STATUS: ACCEPTED AS OFFLINE SNAPSHOT EVIDENCE; LIVE TERMUX PARITY UNKNOWN
SOURCE: https://github.com/Stratumnova/A25-Training-Workspace/blob/053d2e7868bfdd85d1659d40e8e7002e14d58a47/project%20lead/coordination/reports/A25-AV-R001-GPT01-TERMUX-SNAPSHOT-FORENSIC-INVENTORY.md

## Review findings
- **VERIFIED:** Archives fetched and read the complete pinned AV-R001 report.
- **BUILDER-REPORTED VERIFIED:** Main ZIP 1,682,513 bytes, SHA-256 `59fd2e47d1a79cc0ead68f9493c0da92920e956ec5fc58209da65ac87b7fbe43`, 19 entries (15 files/4 directories), CRC checks passed. Nested ZIP 29,206 bytes, SHA-256 `94506d0f1980d52e8d2986ab910598cc142dfabb7cbf674110f6aeec70e909c6`, 40 entries (27 files/13 directories), CRC checks passed. Separately supplied Shared Space ZIP reportedly byte-identical.
- **BUILDER-REPORTED VERIFIED:** Gate-01 JSONL backup 3 parsed events, IDs 1–3, authors Claude/GPT/Claude, cursors 0/1/2. This is static backup data, not proof of server recovery.
- **BUILDER-REPORTED VERIFIED:** All 11 PDF checkpoint documents allowed text extraction; full claim-by-claim or visual review was not performed.
- **BUILDER-REPORTED VERIFIED discrepancy:** File-move manifest references `A25_GPT_Terminal_Read_Viewport_Checkpoint_2026-10-12_v2.pdf` with a hash, but that file is absent from the supplied ZIP. Do not infer deletion from this omission.
- **UNKNOWN:** Live Termux parity, GitHub full-tree parity, historical checkpoint test execution, runtime identity, current viewport exposure/security enforcement.

## Disposition
Accept AV-R001 as a durable reference inventory for the supplied ZIP only. Archive report verification does not independently reproduce every hash, source comparison or runtime claim. Original materials remain untouched. A deeper read-only checkpoint analysis should preserve each document's claims, chronology, conflicts, original evidence pointers and visual limitations without inventing proof.

## Next gate
Request a separate builder report examining all 11 PDFs and two Markdown checkpoint records, with page-specific source citations, sensitive-value redaction, and no file modification. Separately, owner may later supply a live Termux manifest for direct hash comparison. Neither step authorizes live phone access or server changes.
