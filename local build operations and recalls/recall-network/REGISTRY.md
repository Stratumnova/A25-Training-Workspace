# A25 Recall Registry — RN-001
STATUS: ACTIVE
LAST REVIEW: 2026-10-17
AUTHORITATIVE ID SOURCE: this registry plus confirmed reservation files in `reservations/` and submitted report files.

## Numbering
GPT: A25gptrecall_id001, A25gptrecall_id002, ...
Claude: A25clauderecall_id001, A25clauderecall_id002, ...
Each platform has its own independent counter, starting at 001. Historical PS-MR/PS-CR reports are not retroactively numbered.

## Confirmed assignments
None yet. Example RN-001-S001/S002 entries in the earlier SESSION-INDEX.md are unassigned placeholders and are NOT reservations.

## Next ID algorithm
1. Read this registry, `reservations/` and both report lanes. For the chosen platform, determine the highest **confirmed** ID from reservations and reports. The candidate is highest + 1 (initially 001).
2. GPT sessions with GitHub create access must create exactly one NEW `reservations/<ID>.md` on coordination branch. The creation must succeed, and the session must read back the exact file at its returned commit. If creation fails due to a collision, refresh the registry and try the next free number; if a safety block occurs, STOP without retry.
3. Claude sessions cannot be assumed to have GitHub write access. Claude reads registry and reservation directory, proposes a candidate, and asks Zed/lead to reserve it on GitHub BEFORE using the ID for a final report. A Drive file alone is not an atomic reservation. If no reservation is possible, use `UNASSIGNED` as a provisional label and do not assert exclusivity.
4. Never reuse an ID even if a report is withdrawn or fails. A reservation is immutable. No session may change the registry, indexes or another reservation; lead appends confirmed assignment metadata in a new index revision.
5. No two sessions should be launched concurrently without confirmed reservations. Read-before-write alone does not prevent races.

## Receipt statuses
PROPOSED, RESERVED, SUBMITTED, VERIFIED_RECEIPT, REVIEWED, BLOCKED. Receipt verification does not certify factual correctness.
