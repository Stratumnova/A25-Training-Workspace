# Claude archive — authoritative handling rules

This is the Claude-specific archival area, parallel to GPT's future native archive.

**Purpose:** preserve Claude's original text and complete conversation exports when available, with explicit provenance, not GPT reconstructions.

## Structure
- `inbox/`: verbatim received files from Claude via Zed, awaiting validation. Keep original bytes and source filename. A Zed relay is labeled as relay, not direct Claude export.
- `transcripts/`: complete source transcript exports when supplied. Do not claim complete coverage without start/end boundaries and a completeness declaration.
- `reviews/`: Claude-authored review source files, distinct from GPT's summaries in `reviews/claude/` at repository root.
- `handoffs/`: Claude's original continuity notes, labeled by source.
- `manifests/`: provenance and SHA-256 inventories referencing exact source paths and commit IDs.
- `derived/`: explicitly labeled conversions for AI reading; do not replace original files with conversions.

## Integrity
Preserve original submissions byte-for-byte; record `source_seat=Claude`, `captured_by`, transport, date/time source, coverage, attachments, original hash, destination commit, and verification state. A Git blob ID is **not** a SHA-256 digest. Do not add missing turns or normalize punctuation/newlines in the original. Any correction is a new linked record.

## MD versus PDF
Markdown/text is the AI-first reading format. If Claude supplies Markdown directly, preserve it as original. If the source is a PDF or another export, retain the original and place any extracted Markdown under `derived/`, marked as derived and requiring fidelity review. PDFs are for Zed's reading on request, not a substitute for original text or evidence.

## Access and verification
GPT can create infrastructure and preserve Zed-delivered files but cannot claim to have directly retrieved Claude's chat history. Claude independently verifies archive content when able. Zed remains the authority on permissions and release. Public repo: never upload secrets, private personal records, credentials or unreviewed sensitive content.

## Status
Structure initialized. No complete Claude transcript is yet archived. The Claude review currently recorded at `reviews/claude/A25-REV-001-return-review-2026-10-16.md` is a GPT-authored, Zed-relayed attributed report, **not** an original Claude archive file.

## Incremental capture (2026-10-16)
Zed directs that Claude's **currently visible conversation be captured in sequential blocks before it drops out of context**, instead of treating a full-account email export as the normal method. See [block capture protocol](transcripts/BLOCK_CAPTURE_PROTOCOL.md), [intake sidecar](inbox/BLOCK_INTAKE_TEMPLATE.md), [hash handshake](manifests/HASH_HANDSHAKE.md) and [capture queue](handoffs/CAPTURE_QUEUE.md). The root [reviews/claude](../../reviews/claude/README.md) folder holds GPT-authored attributed summaries, not Claude originals. This is a documented manual workflow, not yet a working automated capture tool.
