# A25 legacy import verification — 2026-10-16

Source: `Stratumnova/pockettest`, branch `a25/training-workspace`, directory `a25-training/`.
Destination: `Stratumnova/A25-Training-Workspace`, branch `main`, directory `legacy/pockettest/a25-training/`.

## Verification
- 19 source files and 19 destination files.
- All 19 Git blob SHA-1 IDs and reported byte sizes match, independently enumerated through GitHub directory API after writing.
- No missing or differing files in this comparison.
- This establishes matching Git blob content, **not** native transcript completeness, independent Claude review, or separate SHA-256 calculation.
- The legacy `INDEX.md` and `CURRENT_STATE.md` are historical snapshots; do not use them as the live new-repository index.
- Original files remain in pockettest. No server code copied.
- Source branch last known prior documentation commit: `cff8848d40b55cd3f682342212f64ab7ae4c5a85`. The import was enumerated from the branch; it is not claimed as a commit-pinned source snapshot.
- The new repo's active `START_HERE.md` and `validation/A25-VAL-001-github-connector-capability-test.md` are separate from this import.

## Next
Add active navigation and task ledger, establish exact source commit cutover, run SHA-256 archive test and Claude independent review. Do not treat migration parity as seat-level message parity.
