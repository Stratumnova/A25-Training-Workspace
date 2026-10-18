# A25 Archives Training and Recovery — Owner Exchange and Terminal Snapshot
DATE: 2026-10-18
RECORDED BY: A25-AG-GPT01 (Archives Lead)
PURPOSE: Durable training example and recovery handoff. Preserve evidence classes; do not substitute this report for original sources.
STATUS: REFERENCE RECORD; owner directions identified separately as ADOPTED.

## 1. Exchange chronology and owner decisions
- Zed clarified Zone 1's purpose: one shared daily read/write/build/test/debug workspace for GPT and Claude. GitHub and Google Drive are downstream storage, delivery, and GitHub Actions validation destinations, not the intended daily workspace. The current manual relay is a working reference method, **not** an improvement target. Owner direction was published in Archives, leadership, and Workshop inbox on the coordination branch.
- Zed asked Archives to retain its private advice for later rather than send potentially distracting recommendations to Workshop. This is an owner boundary; those recommendations are not adopted build orders.
- At approximately 17:00 MDT Zed relayed the Workshop's Gate-01 reopening update and asked Archives to obtain its own snapshot from the terminal.

## 2. Workshop originals independently fetched by Archives
A. Leadership decision:
Path: project lead/leadership/A25-TW-LEAD-DECISION-2026-10-18-1658-GATE01-REOPEN.md
Commit: e7a2c694308abea30a2636f83b83bf993e2f4363
Fetched blob SHA: f95a1224b7b48c81b846206bb288b002d7e31d50
Workshop record says Zed authorized reopening and extending Gate-01 on its existing foundation, preserving the original ledger/backup and Gate-02 terminal bridge/tunnel. Workshop reports original and backup ledger hash 61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9, pre-reopen archive hash ab7cdb174fb747121d6e0d08236689d9f12a6f16e4c0435d4fbf2799504c2e55, Shared Space 48 tests passed with one warning, no deployed shared connector.
B. Archive pool reference:
Path: project lead/coordination/pool/A25-TW-ARCHIVE-POOL-2026-10-18-GATE01-REOPEN.md
Commit: 0fea6eca20cdaf03cde426f9f5ba6fa7e826a355
Fetched blob SHA: 3f9601100caee11d8a3f7ec3f298e925111c217f
This is a Workshop-origin reference in the newly created coordination/pool directory, not an Archives-verified implementation result. Archives retrieved it without overwriting or moving the original.

## 3. Archives' independent terminal observation
Tool: A25 GPT Terminal terminal_status and terminal_view; both succeeded read-only. No terminal input was sent.
terminal_status reported:
- identity: gpt-workshop
- workspace_exists: true
- directories present: src, tests, logs, reports, backups, config
- mode: read-only
terminal_view reported:
- session: a25-gpt; read_only: true; returncode: 0; error: empty
- visible source diff adds workspace_inspect, workspace_read, workspace_create, workspace_edit, workspace_delete, workspace_command to shared/server.py.
- visible grep output also lists recover_once (line 49), make_mcp (147), server_status (151), read_roundtable (153), append_roundtable (155), workspace_inspect (158), workspace_read (162), workspace_create (166), workspace_edit (170), workspace_delete (175), workspace_command (179).
- visible shell commands created a disposable gate01-recovery directory and copied ~/pockettest/gate01/roundtable.jsonl to ~/a25-workshop/gpt/tests/gate01-recovery/roundtable.jsonl.
- visible Python JSONL parse output: Event count 3; IDs [1,2,3]; Authors ['claude','gpt','claude']; Cursor values [0,1,2].
- prompt ended in ~/.../tests/zone1-source.

## 4. Evidence classification
VERIFIED (Archives directly observed): successful terminal_status and terminal_view responses; reported identity/mode/directories; displayed source grep/diff; displayed disposable-ledger copy command and successful parse output; retrieval of the two GitHub records at specified commits.
ADOPTED (owner): reopen Gate-01 foundation; protect Gate-02; Zone 1 is the daily common development workspace; GitHub/Drive downstream; do not redirect first-phase build into relay optimization.
HISTORICAL CLAIM / WORKSHOP-REPORTED: original/backup hashes; tar integrity; 48 local tests passed; exact source checkout versions; prior phone process status. These were read from Workshop reports, not independently reproduced by Archives.
UNKNOWN / NOT VERIFIED: newer recover_once running successfully on disposable old ledger; actual original ledger byte hash from this terminal snapshot; live Shared Space server deployment; GPT and Claude connector discovery; same-file cross-seat editing; independent recovery of the archived tar; whether a third Gate existed.

## 5. Training lessons and recovery boundaries
- A source report can be independently retrieved without independently verifying all claims inside it.
- A terminal screen snapshot supports only the commands/output visible; it is not a complete shell audit.
- Parsing a copied ledger is **not** the same as exercising new recovery logic.
- Function definitions and local tests are **not** proof of live two-seat integration.
- Keep owner decisions, evidence observations, and implementation results separately classified.
- Do not touch the original ledger, restart Gate-02, deploy, issue new build orders, or treat this record as a live checkpoint.

## 6. Next evidence to collect (not an instruction to execute)
Capture exact input copy hash, newer recovery invocation, stdout/stderr, exit code, post-recovery event ordering/cursors, and original-file preservation evidence; then separate live connector tests under the appropriate authorization.

## 7. Recovery links
Leadership original: https://github.com/Stratumnova/A25-Training-Workspace/blob/e7a2c694308abea30a2636f83b83bf993e2f4363/project%20lead/leadership/A25-TW-LEAD-DECISION-2026-10-18-1658-GATE01-REOPEN.md
Workshop pool original: https://github.com/Stratumnova/A25-Training-Workspace/blob/0fea6eca20cdaf03cde426f9f5ba6fa7e826a355/project%20lead/coordination/pool/A25-TW-ARCHIVE-POOL-2026-10-18-GATE01-REOPEN.md
Owner Zone 1 directive (Archives): commit d717750b7a0652bf4ef53e8fe4fbbc87c03d82b6
Owner Zone 1 directive (leadership): commit 8984735961b70f53fb736eeb6757d94708cbb4e4
Owner Zone 1 directive (Workshop inbox): commit 5e84db513edc2d33c200278e91644c151a6175c0
