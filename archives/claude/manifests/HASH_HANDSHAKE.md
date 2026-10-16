# Cross-seat hash handshake

1. Claude prepares a source file without reformatting it after hashing. Claude records exact UTF-8 byte count and full SHA-256, if computation is available.
2. Zed transfers the **file**, not rendered text where possible. A text paste is explicitly marked `PASTE_RELAY` and may change newline bytes.
3. GPT or a deterministic runner computes SHA-256 on the received bytes **before** publication and again on the GitHub commit-pinned read-back. Store both full digests and byte counts.
4. If source and destination digests differ, mark `MISMATCH`, preserve both versions, and investigate newline, Unicode, clipping, or transport effects. Do not declare exact fidelity.
5. If Claude cannot compute a source digest, record `SOURCE_HASH_UNAVAILABLE`. Destination read-back match does not prove Claude-origin byte parity.
6. Claude independently opens a pinned raw link and checks source against its own retained copy. This is an independent review, not a replacement for SHA-256.
7. The final manifest states exact commit, original source, capture method, coverage, all digests, gaps and reviewer.

A Git object ID is not a SHA-256 digest. A GitHub commit timestamp is a repository event timestamp, **not** necessarily the time a message was originally authored.
