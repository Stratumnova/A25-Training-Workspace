# A25-TW-GPT01 — Termux Storage, System Walls, and Security Reconnaissance
Date: 2026-10-18
Scope: Read-only inspection through Gate-02 terminal_send to a25-test and terminal_view. Owner explicitly prohibited moving, editing, deleting, or creating files in Termux. No Termux files or services were changed by this investigation.

## VERIFIED — Paths and storage
Termux HOME=/data/data/com.termux/files/home; PREFIX=/data/data/com.termux/files/usr; TMPDIR=/data/data/com.termux/files/usr/tmp.
Main trees: ~/pockettest, ~/pockettest-c1, ~/pockettest-shared, ~/a25-workshop/gpt, ~/a25-data/shared-space.
Workshop subdirectories: src, tests, backups, reports, logs, config. Pockettest contains gate01, gate02, gpt, claude, protocol, roundtable, shared_context, docs.
~/storage symlinks: downloads -> /storage/emulated/0/Download; shared -> /storage/emulated/0; dcim, pictures, music, movies map to corresponding shared storage directories. Readability checks for downloads and shared succeeded; personal content was not enumerated.
Termux home and relevant project directories showed mode drwx------ (700). Bridge token and cloudflared.yml showed -rw------- (600); Cloudflare tunnel JSON -r-------- (400). Secrets' contents were not read.

## VERIFIED — Runtime and tooling
tmux sessions: a25-bridge, a25-gpt, a25-test, a25-tunnel.
Process list: Python uvicorn server:app on 127.0.0.1:8766 (Gate-01 test service), Python -m src.chatgpt_readonly (Gate-02 bridge), and two cloudflared processes using the same config path. Relationship between tunnel processes UNKNOWN.
Current GPT terminal connector has terminal_status, terminal_view, terminal_send. terminal_send sends tmux keys to allowed sessions a25-gpt, a25-test, a25-bridge, a25-tunnel. Successful harmless echo test from this conversation was independently seen in terminal_view. Receipt is key-delivery only, not command exit status.
Source ~/a25-workshop/gpt/src/chatgpt_readonly.py has explicit session allowlist, subprocess tmux capture/send and FastMCP HTTP transport. terminal_view captures last 12,000 characters. Source uses ROOT = Path.home() / 'a25-workshop' / 'gpt', but this does not constrain shell command filesystem access.

## VERIFIED — Other security-related source present
~/a25-workshop/gpt/src/auth.py includes token verifier using hmac.compare_digest and terminal:status scope. No evidence observed that the active chatgpt_readonly bridge actually wires this verifier into terminal_send.
~/pockettest/gate02/server.py is a separate deny-all OAuth skeleton (source describes no clients, codes or tokens), with host/origin settings; do NOT equate its controls with active GPT bridge.
~/pockettest/gate02/listening_wall.py has request size checks and observation logic; active use on terminal bridge not established.
~/a25-workshop/gpt/tests/zone1-source/shared/secure_files.py contains secure_read, secure_append, secure_rdwr with no-follow/regular-file handling. Source presence is not proof of deployment or complete path containment.
~/a25-workshop/gpt/tests/zone1-source/gate01/server.py contains distinct secret path checks for GPT/Claude. These are source findings; runtime identity guarantees not tested.

## Security findings / boundaries
VERIFIED: Linux filesystem permissions 700/600/400 exist on inspected paths; these do not isolate processes sharing Termux UID.
VERIFIED: session allowlist limits tmux target names but does not sandbox shell commands within the Workshop directory.
VERIFIED: terminal_send implementation returns tmux key delivery status; no command exit-status capture or interruption tool exposed.
UNKNOWN: active caller authentication and authorization for terminal_send; no binding of separate auth.py verifier was found in inspected active bridge source. Treat as security gap requiring leadership review, not as proven exploit.
UNKNOWN: command audit/provenance, caller identity separation, effective network ingress controls, exact Android app permissions, Cloudflare double-process impact, path/symlink containment in deployed Gate-01 shared workspace.
UNKNOWN: whether older pockettest copies are active or merely reference snapshots.

## Evidence and handling
Commands used: pwd, find, ls, tmux list-sessions/list-panes, ps, ss, grep, sed, test -r, printf. Commands only read metadata/source and printed output to the test pane. No service or filesystem modifications authorized or performed. No destructive tests or attempts to bypass controls.
No secrets or private storage contents were included in this report.
A25 reference rule: VERIFIED here means directly observed output/source; it does not mean production readiness. Do not adopt source comments as proof of implemented security.

## Next justified action
Leadership/security pool reviews and independently verifies the active bridge's authorization, audit, session permissions and external exposure without blocking owner-directed Workshop construction. Continue mapping only with owner authorization and read-only methods.
