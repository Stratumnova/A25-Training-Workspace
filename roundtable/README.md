# A25 Roundtable — durable relay and 1:1 message records

**Status:** Zed-authorized workflow, 2026-10-16 14:38 MDT (Zed-provided time). This is a manual GitHub-backed relay, **not** automated native chat capture.

## Working agreement
1. Zed sends input to GPT in ChatGPT. GPT preserves the input as supplied and its complete response in an immutable-by-convention Markdown roundtable record, with a stable message ID and clear role attribution. The full record is published to GitHub and read back before GPT claims success.
2. GPT replies in ChatGPT with a **tiny summary** and a single commit-pinned raw link to the record for Claude. This reduces repeat text and copy/paste loss.
3. Claude opens the raw record, prepares its own complete response as a **plain Markdown source file** (no PDF as primary, no elaborate chat formatting), with a full header and exact source attribution. Claude gives Zed only a tiny summary plus the source file or a link if it has a working write path.
4. Zed relays Claude's response to GPT. GPT preserves the exact Claude-provided text as a source record if the transport is text, marking `PASTE_RELAY` and `source_byte_parity: NOT_VERIFIED`; if an actual source file is delivered, preserve its bytes and compare hashes. GPT commits and reads back, then returns one pinned raw link.
5. No seat impersonates another. A Zed-relayed Claude report is marked as relayed until independently checked. Zed retains project and governance authority.

## Directories
- `sessions/`: numbered turn records with source, complete GPT response, Claude response when received, and clear provenance.
- `inbox/`: untouched Claude source messages/files as delivered; never silently normalize source.
- `indexes/`: commit-pinned raw link maps. Create each index *after* content commits.
- `protocol/`: relay format and validation rules.

## Integrity and scope
- `1:1` means faithfully preserving the **text actually received and generated** for each recorded turn, not access to hidden model reasoning, erased tool outputs, or all historical chat.
- For pasted text, rendered UI may alter line endings or formatting; do not claim byte-identical origin.
- If a response was originally displayed with rich UI, the Markdown archive may represent its content and structure but not reproduce the rendered widget pixel-for-pixel. Label such differences.
- Capture original user text and complete assistant report, not merely a summary. Never substitute the short ChatGPT acknowledgment for the archived response.
- Use source seat, recipient, date/time with source, topic, basis, source coverage, relay method, exact commit and read-back status. Git blob ID is not SHA-256.
- Never publish secrets, private credentials, private personal data or full-account exports to this public repo. Screen before commit and report exclusions.
- A GitHub commit alone does not prove independent Claude review or cross-seat SHA-256 parity.

## Initial status
First entry: `sessions/2026-10-16/RT-001-gpt-status-and-zed-workflow.md`. This entry includes a faithful Markdown rendering of GPT's 14:30 status response, the latest Zed directive and the action taken. The original response used rich UI components; see its capture limitations.

## Claude output format
Use one Markdown source document with header `FROM / FOR / DATE (time source) / RE / BASIS`, then substantive sections. Avoid PDF and tables unless needed. In chat, give Zed only a short summary and the Markdown file/link. If a source file cannot be produced safely, provide plain Markdown text with explicit paste-relay limitations. Do not attempt mass transcript extraction in a paused chat.
