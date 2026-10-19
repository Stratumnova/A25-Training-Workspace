# Cleanup Pass 04 — Restore Dependency and Evidence Gaps

DATE: 2026-10-19
FROM: A25-TW-GPT01
STATUS: GITHUB DOCUMENT REVIEW; NO TERMINAL COMMANDS
CUTOFF: 2026-10-18 15:00 MDT
OWNER RULE: post-cutoff current Workshop work is primary baseline; pre-cutoff or unused artifacts require Archives review. Technical claims remain subject to verification.

## Source
project lead/leadership/terminal-workshop/memory/02-ACTIONS-EVIDENCE-AND-CHECKPOINT-2026-10-18.md (GitHub branch coord/a25-namespace-trial-001). Also prior cleanup Pass 01–03 and their cited original GitHub reports.

## Confirmed by original continuity record
- Zed identifies October 18 final GPT terminal command/view arrangement as official Workshop baseline. Owner-adopted; not a tested restore.
- Historical runtime paths listed: ~/pockettest; ~/pockettest-c1; ~/pockettest-shared; ~/a25-workshop/gpt.
- Previously observed tmux sessions: a25-test, a25-gpt, a25-bridge, a25-tunnel. Not all rechecked live.
- Earlier process observations included Gate-02, Workshop bridge and tunnel processes. Process existence alone does not establish live routing, required imports or caller authentication.
- The recovery index warns that no verified complete disaster-recovery image is established.
- Earlier socket-inspection attempts were constrained: ss absent; netstat lacked expected support; no unapproved /proc inspection. Preserve these limits rather than inventing socket facts.

## Archives candidate register: recovery-first classification
| Item | Current evidence | Disposition now | Required proof before removal |
| --- | --- | --- | --- |
| ~/a25-workshop/gpt | Active GPT terminal tool workspace status and viewport; actual startup files untraced | PROTECT | Verified source/process/startup/backup map |
| ~/pockettest | Historical original server and docs | INVESTIGATE | Active process cwd/import checks and preserved archival copy |
| ~/pockettest-c1 | Historical Gate-02 worktree and process evidence | INVESTIGATE | Current process dependency and route mapping |
| ~/pockettest-shared | Historical shared server/source | INVESTIGATE | Current imports and any active deployment |
| a25-test | Recent live viewport and successful past commands | KEEP | No removal planned |
| a25-gpt | Recent live MCP request log viewport | KEEP | No removal planned |
| a25-bridge and a25-tunnel | Named in historical session inventory only | UNKNOWN | Current existence and service role |
| Older bridge.py snapshots and viewport archives | Filenames previously observed | ARCHIVES REVIEW | Content manifest, checksum, unique restore value |
| cloudflared config and historical credentials | Older metadata and process reports | SENSITIVE/PROTECT | Active tunnel/config reference and safe backup plan |
| External old connector registrations | Owner-reported, not enumerated | UNKNOWN | Platform-side list, endpoints and usage |

## Recovery acceptance criteria before any cleanup
1. Identify exact current bridge source and startup command without revealing secret routes.
2. Identify the active tunnel and connector chain, and whether Gate-02 or older trees are needed.
3. Create a manifest of unique old archives and verified backup locations, if separately authorized.
4. Document how a working bridge could be restored; do not claim restore PASS without a reproducible test.
5. Archives recommends KEEP / ARCHIVE / INVESTIGATE / PROPOSE REMOVE; Zed makes final decision.

## Limits
No process, port, archive extraction, credential read, terminal send, file move, delete, restart or live test occurred in this pass. Historic process details are not fresh verification. No artifact is presently designated safe to remove.
