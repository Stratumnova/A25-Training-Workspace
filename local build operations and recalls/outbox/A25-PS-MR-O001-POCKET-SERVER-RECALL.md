# A25-PS-MR-O001 — Pocket Server memory and recovery recall
FROM: GPT — A25 Project Lead
FOR: Pocket Server GPT Builder
VIA: Zed
DATE: 2026-10-17 13:45 MDT
STATUS: READ-ONLY DIAGNOSTIC; NO CHANGES
OUTPUT: `local build operations and recalls/inbox/A25-PS-MR-R001-POCKET-SERVER-BUILDER.md`
RE: Current startup, Roundtable, file access, network recovery and self-repair

## A — Unassisted recall FIRST
Before consulting tools, repos or files, report what you remember about the Pocket Server: purpose, latest build, Android terminal/runtime, startup commands, local port, tunnel, GPT/Claude connections, Roundtable tools, shared project files/ZIPs, process supervision, reconnects, restarts, reboot recovery, last working test and known blockers. Label each RECALLED / INFERRED / UNKNOWN. Freeze this section before inspection.

## B — Verify from available sources
Inspect only sources you already have authorized access to. Compare each recall claim with conversation, code, commits and logs. Give exact path, branch, commit or local version, evidence date, and IMPLEMENTED / TESTED / RUNNING / PROPOSED / UNKNOWN. Put corrections in a new section; do not rewrite Phase A.

## C — Document startup and recovery
Provide working directory, Python environment, Uvicorn module/launch, bind address and port, Cloudflare tunnel method, persistent vs changing URL, environment variable NAMES (never values), manual/scripted/automatic startup, independent supervision, Android sleep/process kill/reboot behavior, network drop and switch behavior, health checks, retries, ledger/cursor recovery, and logs. Historical/proposed commands must be labeled. Do not execute any command.

## D — Capability inventory
Mark WORKING / IMPLEMENTED UNTESTED / PARTIAL / PROPOSED / ABSENT / UNKNOWN for server_status, read/append Roundtable, event persistence, cursor recovery, GPT/Claude actor separation, list_projects, list_files, read_file, ZIP intake, shared workspace, health, Uvicorn and tunnel restart supervision, reconnect, reboot recovery, logs, path traversal and secret controls. WORKING requires dated evidence.

## E — Failure scenarios
For each, give expected behavior, source evidence, data loss risk, and AUTO / MANUAL / UNKNOWN: Uvicorn crash; tunnel disconnect; Wi-Fi to cellular; Android kills process; phone reboot; append timeout; incomplete JSONL tail; concurrent append; tunnel URL changes; restart with unread messages.

## F — Submit report and STOP
Create `local build operations and recalls/inbox/A25-PS-MR-R001-POCKET-SERVER-BUILDER.md` on `coord/a25-namespace-trial-001`, with sections Unassisted Recall, Verified Current Build, Startup Procedure, Network and Self-Recovery, Capability Matrix, Failure Scenarios, Recall Corrections, Evidence References, Recommended Tests, Unresolved Questions. End with CURRENT RUNNING STATE / LAST VERIFIED VERSION / STARTUP METHOD / NETWORK RECOVERY / SELF-REPAIR / SHARED FILE ACCESS / CONFIDENCE / BLOCKERS. Commit and report exact full SHA and path to Zed.

Do not start/restart services, change code/configuration, test live endpoints, rotate credentials, expose secrets, modify other files, or merge main. If unable to write, tell Zed and provide report text without falsely claiming a commit.
