---
id: A25-CORR-README-001
source_seat: Claude
captured_by: GPT
relay: Zed
date: "2026-10-16"
status: correction-recorded
---
# Legacy README checksum terminology correction

Claude identified the exact sentence in `legacy/pockettest/a25-training/README.md`, section "Read path":

> The index pins its children to the prior content commit and includes SHA-256 checksums.

**Correction:** The index at `legacy/pockettest/a25-training/INDEX.md` contains Git blob object IDs, not SHA-256 checksums. The index itself explicitly makes this distinction. Do not interpret the README's sentence as evidence of SHA-256 verification.

The legacy source remains unchanged as an evidence-preserving import. This correction is a separate, linked record. Claude's independent review was relayed by Zed, not obtained by GPT directly.
