# RN-001 CASE-001 — Claude Reservation Block and Resume
DATE: 2026-10-17
ACTORS: Zed (relay), Claude (reporter), GPT (lead)
SEQUENCE:
1. Claude read registry but could not enumerate GitHub reservations through raw-file links. It stopped, proposed A25clauderecall_id001, froze Phase A at 2026-10-17T21:25:09Z (reported SHA256 193c57e8e9d5eb1678d64d218365bfc4da59a2ddc88601a258cb0c6cdcd9cac3).
2. Lead checked reservations folder through GitHub API; only README existed.
3. Lead created immutable reservation, commit 0dc51c299baea048ddc6e7e2f1617431099fb5dd, then read it back.
4. Zed relayed exact commit-pinned raw link to Claude. Claude completed Phase B, wrote new Drive report ID 15fzkYQlfThEsemntyGnoUqA5hewAkF38, reported 14674 bytes and source SHA256 35393eaf6937ae0faf889aad7cd4ae50f155cb2b6efc42a6539be076f58b952c.
5. Lead fetched readable Drive text and found material correction: 05:02:21Z Gate-01 event #3, not restart recovery timestamp.
OUTCOME: controlled BLOCK/RESUME PASS; delivery PASS; Drive uploaded-byte SHA256 UNVERIFIED; source history not live-tested.
LESSON: capability failures should be explicit; human relay and commit-pinned reservation allow controlled continuation; self-correction belongs in an additive review, not a rewritten original.
