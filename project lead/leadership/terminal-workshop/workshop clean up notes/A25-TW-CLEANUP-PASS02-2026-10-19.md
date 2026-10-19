# Cleanup Pass 02 — Zone 1 Source vs Working Terminal Bridge

DATE: 2026-10-19
FROM: A25-TW-GPT01
SCOPE: GitHub historical reports only; NO terminal commands or phone changes.
STATUS: REFERENCE/HISTORICAL SOURCE ANALYSIS; deployment dependencies UNKNOWN.
CUTOFF: 2026-10-18 15:00 MDT. Original reports date Oct 18 but lack exact time; do not assign before/after cutoff without commit timestamp.

## Sources read on existing coordination branch
- project lead/coordination/builders-inbox/A25-TW-ZONE1-CONNECTOR-DOCUMENT-MAP-PASS12-2026-10-18.md
- project lead/coordination/builders-inbox/A25-TW-HISTORICAL-SOURCE-INDEX-PASS13-2026-10-18.md
- project lead/coordination/builders-inbox/A25-TW-EARLY-PROTOCOL-DECISIONS-MAP-PASS14-2026-10-18.md

## Critical distinction: three different capability contracts

### Original Pocket Server V1 (historical design)
PASS14 read original docs under ~/pockettest. POCKET_SERVER_V1.md describes server_status, list_projects, list_files, read_file, read_roundtable and append_roundtable. Project files read-only; Roundtable append-only. DECISIONS.md described owner-controlled files and server-derived caller identity. This is historical design, not evidence that V1 currently serves the working terminal tools.

### Zone 1 workspace (source contract, not deployed proof)
PASS12 read ~/a25-workshop/gpt/tests/zone1-source/shared/ZONE1_GPT_CONNECTOR.md. The document explicitly identifies itself as SOURCE CONTRACT DOCUMENTATION ONLY, not live connector installation. It describes six proposed workspace operations: workspace_inspect, workspace_read, workspace_create, workspace_edit, workspace_delete, workspace_command. Its command allowlist is pwd, ls, python_version, pytest; timeout 30 seconds. PASS13 inventoried zone1_workspace.py, secure_files.py, server.py, storage.py, and contract/tests. Existence is not proof of live installation or passing tests.

### Working Workshop terminal tools (post-cutoff behavior)
The October 19 exchange verified GPT terminal_status, terminal_view and terminal_send, with file copy, delete and append through the a25-test shell; Claude reported and the shared terminal output supported parallel use. This tool surface is distinct from both original V1 and proposed Zone 1 six-tool interface. Therefore the file exchange does NOT establish Zone 1 deployment.

## Cleanup candidates and Archives instructions
1. ~/a25-workshop/gpt/tests/zone1-source/: SOURCE/TEST REVIEW CANDIDATE, not proven runtime dependency. Before proposing archival, verify whether any deployed service imports, starts, or references these files; preserve version, tests and origin.
2. ~/pockettest/gpt, ~/pockettest/claude, ~/pockettest/protocol, ~/pockettest/shared_context: LEGACY DESIGN REFERENCE. Preserve as historical provenance; runtime relevance unverified.
3. Historical Pocket Server read-only and append-only policies: preserve as historical decisions; do not apply automatically to present terminal controls or silently mark superseded without owner adoption.
4. External GPT/Claude connector registrations: UNKNOWN. Old registrations may exist even if no local filenames match. Do not deactivate until endpoint, caller and live-use comparison.
5. Working Workshop terminal bridge and current MCP tools: PROTECT CURRENT BASELINE; exact deployed process/source still requires bounded inspection.

## Questions for later read-only dependency tracing
- What process/command line serves terminal_status/view/send?
- Does any live process load zone1_workspace.py or run shared/server.py?
- Which active external connector points to which local process and tunnel?
- Which Gate-01/Gate-02 components remain running and are they required by terminal operation?
- Are any historical archives the only known restore source for current configuration?

## Disposition
No safe-to-remove determination. Archive recommendations require independent dependency verification and Zed approval. This pass changes only GitHub documentation.
