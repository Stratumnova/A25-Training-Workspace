# A25 Claude conversation block capture — v1 (manual, source-preserving)

Status: **PROPOSED WORKFLOW / NOT YET END-TO-END TESTED**. Authorized by Zed's 2026-10-16 instruction to capture currently accessible conversation blocks before context disappears. This is not an automatic Claude API integration.

## Goal
Capture sequential, overlapping blocks from the **current A25 Claude conversation** while Claude can still access them. Do not wait for an all-account email export. Original content must be distinguished from transcription, formatting conversion, reconstruction, and summary.

## At each capture boundary
1. Zed asks Claude for the next available contiguous block, specifying a session ID, block number, previous last message anchor and approximate starting point. Claude reports its actual visibility limitations and never fills inaccessible turns from memory.
2. Claude outputs an **unabridged** block in a fenced literal text section or delivers an original `.md` file if its interface supports that. Include each visible turn's speaker, sequence/order, source timestamp if visible, message body, attachments referenced and any inaccessible spans. Do not paraphrase.
3. The capture is saved to `archives/claude/inbox/` as a source artifact, with an accompanying sidecar recording who transferred it, whether copy/paste was involved, source conversation identity, exact covered first/last anchors, block number, overlap with previous block, known gaps, and any truncation warning.
4. When Claude can compute a SHA-256 for the exact **file bytes**, include the full 64-hex digest and byte count in the sidecar or a separate signed-off message. If not possible, record `source_sha256: UNAVAILABLE`; do not fabricate one.
5. GPT/handyman commits the unchanged received artifact, reads back the exact committed bytes, calculates destination SHA-256 and compares with Claude's source digest when supplied. `MATCH` requires exact byte comparison. A matching Git blob ID alone is not a SHA-256 parity test.
6. Claude reviews the pinned raw artifact and confirms or challenges exact coverage and text. Only after reconciliation may a block be marked independently verified.
7. Repeat **before** the active chat loses access to earlier turns. Blocks should overlap at least one identifiable turn. The overlap is checked and de-duplicated only in a derived assembly, never by editing the original blocks.

## Completeness and failure handling
- Keep distinct states: `RECEIVED`, `COMMITTED`, `READ_BACK_MATCH`, `CLAUDE_CHECKED`, `ASSEMBLED`, `COMPLETE_COVERAGE_CONFIRMED`. Zed approval is separate.
- Missing turns, hidden system/tool messages, images, uploads, collapsed content, formatting changes and token truncation are listed explicitly. Never claim a true 1:1 transcript if any are inaccessible.
- For an interrupted capture, save the last committed block and next expected anchor. Do not silently guess a missing segment.
- Transcript assembly is a **derived** artifact under `derived/`, with block references and gaps; source blocks stay immutable.
- No private credentials, secret URLs, canaries, personal data or unreviewed full-account exports in this public repo. Quarantine sensitive source locally/private; record only non-sensitive provenance in public.

## Suggested block envelope (metadata, not inserted into original text)
```yaml
record_id: A25-CLAUDE-BLOCK-0001
source_seat: Claude
conversation_id: UNVERIFIED
block_number: 1
first_message_anchor: UNVERIFIED
last_message_anchor: UNVERIFIED
overlap_anchor: null
capture_method: Claude-visible chat block relayed by Zed
captured_by: Zed
source_sha256: UNAVAILABLE
source_byte_count: UNAVAILABLE
destination_sha256: PENDING
coverage: PARTIAL_UNTIL_PROVEN
truncation: UNKNOWN
source_time_basis: not independently synchronized
verification: RECEIVED
```

## Alternative recovery
Anthropic's full account export may help recover older content but must remain private and be screened and scoped to A25 before any public import. Do not assume it preserves all tool messages or exact UI rendering without inspection.
