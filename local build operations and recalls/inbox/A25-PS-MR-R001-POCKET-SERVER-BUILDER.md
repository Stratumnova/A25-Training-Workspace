# A25-PS-MR-R001 — Pocket Server Builder Memory and Recovery Recall

**FROM:** Pocket Server GPT Builder  
**FOR:** Zed / GPT — A25 Project Lead  
**ORDER:** `local build operations and recalls/outbox/A25-PS-MR-O001-POCKET-SERVER-RECALL.md`  
**BRANCH:** `coord/a25-namespace-trial-001`  
**DATE:** 2026-10-17 MDT  
**MODE:** READ-ONLY RECALL / RECOVERY STUDY  
**PROVENANCE:** Phase A was frozen from builder memory before Pocket Server source inspection. Later sections use authorized GitHub sources plus conversation/checkpoint context already available to this builder. No live endpoint was called and no server, tunnel, phone file, configuration, credential, or protected branch was changed.

---

## Unassisted Recall

> Frozen before source inspection. Labels here intentionally preserve uncertainty and are not corrected in place.

### Purpose and architecture

- **RECALLED:** Pocket Server is a local-first Android/Termux staging server owned by Zed. The phone is authoritative; GPT and Claude are guests.
- **RECALLED:** The intended V1 direction is owner-controlled project/file intake, AI read-only project access, and a shared append-only Roundtable with separate GPT and Claude identities.
- **RECALLED:** Gate-01 is the earlier dummy-data Roundtable connectivity proof. It used separate GPT and Claude secret paths and a JSONL ledger.
- **RECALLED:** Gate-02A is the public OAuth/listening-wall line and remains fail-closed/deny-all on main.
- **RECALLED:** The auth-development branch is `build/gate02a-c1-auth-store`, last remembered at commit `1b578ee32532f99093ab906af52e8b485c90a7e4`. Registration, consent-related pieces, authorization-code storage and revocation foundations exist, but access/refresh token machinery is unfinished and the server still uses `DenyAllProvider`.
- **RECALLED:** Shared Space Stage 1 is on `build/shared-space-v0`, last remembered at `9a419e925dff2de64ef948b7d6d8304eccf8387d`; it moved private data outside the repo and hardened file access.
- **RECALLED:** Shared Space Stage 2 identity proposal is unmerged at `8ade3c00f4f5219182ec01b5154b4b89b71d3359`, with a remembered test result of 78 passed / 1 failed / 1 warning and a directory-creation race as the failure.
- **RECALLED:** A separate read-only observation viewport under `~/a25-workshop/gpt` was proven for Zed/GPT/Claude, then deliberately shut down. It is not the Pocket Server command gateway and was still uncommitted at the last checkpoint I remember.

### Android runtime and startup

- **RECALLED:** Runtime is Termux on Android.
- **RECALLED:** Gate-02A working directory was `~/pockettest/gate02`.
- **RECALLED:** Gate-02A Python environment was `~/pockettest/gate02/.venv`.
- **RECALLED:** Historical Gate-02A launch command was:
  `python -m uvicorn server:app --host 127.0.0.1 --port 8766 --proxy-headers --forwarded-allow-ips=127.0.0.1`
  after entering the Gate-02 directory/venv.
- **RECALLED:** Gate-02A public tunnel used Cloudflare and the stable public hostname `roundtable.rodsrcpark.com`.
- **RECALLED:** Tunnel launch used a token file on the phone rather than pasting the token into commands/chats.
- **RECALLED:** Gate-01 historically used local port 8765 and a Quick Tunnel during the proof period.
- **RECALLED:** The separate GPT bridge used 8769 and the temporary shared viewport used 8770; these are separate from Gate-02A.
- **UNKNOWN:** Whether any Pocket Server service is running now. My last remembered deliberate shutdown closed the terminal/service set; current state requires phone evidence.

### GPT/Claude connections and Roundtable

- **RECALLED:** Gate-01 had separate GPT and Claude route identities and exposed `server_status`, `read_roundtable`, and `append_roundtable`.
- **RECALLED:** A post-restart Gate-01 recovery check preserved three events in order and recovered GPT's unseen classification/cursors.
- **RECALLED:** Roundtable append requires a prior read, successful append stores `cursor_through`, own events are excluded from unseen, and exact retry of the latest own message/references is duplicate-protected.
- **RECALLED:** Pending reads are intentionally in-memory and disappear on restart.
- **INFERRED:** Connector reconnection after a network/tunnel interruption depends on the endpoint becoming reachable again; I do not remember an automatic client-side reconnect supervisor being proven.

### Shared project files / ZIPs

- **RECALLED:** The project goal includes project listing/file listing/file reading and ZIP/project intake, but the last protected runtime I remember did not yet expose the complete six-operation V1 file API to authenticated GPT/Claude.
- **RECALLED:** Shared Space Stage 1 implemented private storage hardening and kept data outside the Git repo.
- **INFERRED:** ZIPs were used as checkpoint/handoff artifacts and manually inspected, but that is not the same as a working Pocket Server ZIP-intake API.
- **UNKNOWN:** Current live inventory of project ZIPs/files on the phone.

### Supervision, reconnects and reboot recovery

- **RECALLED:** Uvicorn and cloudflared were started manually in separate Termux terminals during the proven sessions.
- **RECALLED:** No production-grade process supervisor or Android boot autostart had been proven at the last checkpoint I remember.
- **RECALLED:** Gate-01 ledger crash-tail recovery runs once at server startup and quarantines an incomplete JSONL tail before truncating it.
- **INFERRED:** If Android kills Uvicorn/cloudflared or the phone reboots, manual restart is required unless newer work added supervision after my remembered checkpoint.
- **UNKNOWN:** Proven behavior for Wi-Fi-to-cellular switching, automatic tunnel reconnect, Termux sleep/doze survival, or boot recovery.
- **RECALLED:** The stable named Gate-02A Cloudflare hostname avoids the URL-changing behavior of Gate-01 Quick Tunnel, assuming the named tunnel/DNS remains configured.

### Last working tests and blockers

- **RECALLED:** Gate-01 passed a restart/recovery proof with the original three-event ledger preserved.
- **RECALLED:** Shared Space Stage 1 had a remembered 45-test green state.
- **RECALLED:** Auth branch had a remembered 110-test state before C4/C5 were completed.
- **RECALLED:** Gate-02A main is deliberately `ready:false` and deny-all; that is expected, not a failure.
- **RECALLED:** Main blockers: consent completion, access/refresh token issuance/validation/rotation, revocation enforcement, scopes/audit, authenticated identity integration with Shared Space, and later genuine execution isolation.
- **UNKNOWN:** Whether later sessions after my last checkpoint changed any of those blockers.

---

## Verified Current Build

### Repository refs inspected 2026-10-17

Authorized GitHub inspection of `Stratumnova/pockettest` shows:

| Component | Exact ref | Status | Evidence |
|---|---|---|---|
| Gate-02A main | `main` = `f0a11d51968ad598691333d32971dfb483489073` | IMPLEMENTED; historical runtime test known, current running state UNKNOWN | GitHub branch/ref + `gate02/server.py` |
| Auth work | `build/gate02a-c1-auth-store` = `1b578ee32532f99093ab906af52e8b485c90a7e4` | IMPLEMENTED PARTIAL; current runtime UNKNOWN | GitHub branch/ref + gate02 auth files |
| Shared Space Stage 1 | `build/shared-space-v0` = `9a419e925dff2de64ef948b7d6d8304eccf8387d` | IMPLEMENTED; historical tests recalled, current runtime UNKNOWN | GitHub branch/ref + `shared/` |
| Shared Space Stage 2 | `proposal/shared-space-stage-2-identity` = `8ade3c00f4f5219182ec01b5154b4b89b71d3359` | PROPOSED / UNMERGED | GitHub branch/ref |
| Gate-01 code on main | `gate01/server.py`, `gate01/README.md` | IMPLEMENTED; historical proof only | GitHub main |

### Verified source facts

- **IMPLEMENTED:** `START_HERE.md` defines the target V1 contract as server status, list projects, list files, read project files, read Roundtable, append Roundtable. AI project-file modification is forbidden in V1.
- **IMPLEMENTED:** Gate-01 source exposes only `server_status`, `read_roundtable`, and `append_roundtable`; it does not implement the project-file tools.
- **IMPLEMENTED:** Gate-01 identities are route-derived from `POCKET_GPT_PATH` and `POCKET_CLAUDE_PATH`; source rejects missing/short/equal placeholder paths.
- **IMPLEMENTED:** Gate-01 JSONL writes use append + flush + `fsync`; one asyncio append lock serializes appends; recovery quarantines and truncates a non-newline crash tail once during lifespan startup.
- **IMPLEMENTED:** Gate-02A main uses `DenyAllProvider`, registration disabled, auth resource at `https://roundtable.rodsrcpark.com/mcp`, DNS-rebinding allowlist, request body limits, and `/health` returning `{"status":"gate02a-deny-all","ready":false}`.
- **IMPLEMENTED:** Auth branch contains `auth_store.py`, `authorize_provider.py`, `client_registration.py`, `consent_views.py`, tests and admin helper, but its `gate02/server.py` blob is the same deny-all server blob as main. Therefore the auth components are not wired into the public server at this ref.
- **IMPLEMENTED:** Shared Space Stage 1 contains `shared/server.py`, `secure_files.py`, and `storage.py`. Storage defaults to `~/a25-data/shared-space`, requires an absolute resolved path outside the repository, creates directories at mode 0700, and opens ledger/quarantine files with no-follow regular-file checks and mode 0600.
- **IMPLEMENTED:** Shared Stage 1 still reports itself as Gate-01/dummy-data-only and still exposes only the three Roundtable tools. It is storage hardening, not yet the complete V1 project-file API.
- **UNKNOWN:** Live phone process state, live connector state, live tunnel state, Android battery/doze state, and current private data contents were not inspected under this order.

### Historical evidence available in conversation/checkpoint context

These are not re-executed tests in this recall:

- **TESTED (historical, 2026-10-07 context):** Gate-01 post-restart recovery preserved events 1–3, ordering, attribution, GPT cursor recovery and unseen classification.
- **TESTED (historical checkpoint context):** Shared Space Stage 1 was recorded green at 45 tests.
- **TESTED (historical checkpoint context):** auth branch was recorded at 110 tests before C4/C5 completion.
- **TESTED (historical checkpoint context):** Stage 2 proposal was recorded 78 passed / 1 failed / 1 warning; failure was a data-directory creation race.
- **RUNNING (historical only):** Gate-02A was previously observed on local port 8766 behind `roundtable.rodsrcpark.com`, with `/mcp` denied and `/health` ready:false. It was later deliberately shut down for the night. No claim is made that it is running now.

---

## Startup Procedure

No command below was executed in this recall.

### Gate-02A deny-all baseline — historical working procedure

- **Working directory:** `~/pockettest/gate02` — historical phone/checkpoint evidence.
- **Python environment:** `~/pockettest/gate02/.venv` — historical phone/checkpoint evidence.
- **ASGI module:** `server:app` — verified by `gate02/server.py`.
- **Bind:** `127.0.0.1:8766` — historical tested launch.
- **Historical command:**
  `cd ~/pockettest/gate02 && source .venv/bin/activate && python -m uvicorn server:app --host 127.0.0.1 --port 8766 --proxy-headers --forwarded-allow-ips=127.0.0.1`
- **Public origin:** `https://roundtable.rodsrcpark.com` — verified in source.
- **Tunnel method:** named Cloudflare tunnel, historically launched with a token file. The credential value is intentionally not recorded.
- **Historical tunnel command:** `cloudflared tunnel run --token-file ~/.cloudflared/pocket-gate02.token`.
- **URL behavior:** named Gate-02A hostname is intended to remain stable; Gate-01 Quick Tunnel hostname was temporary/changing.

### Gate-01 — source-documented historical procedure

- **Local port:** 8765.
- **Source-documented command:** `uvicorn server:app --host 127.0.0.1 --port 8765`.
- **Environment variable names:** `POCKET_GPT_PATH`, `POCKET_CLAUDE_PATH`, `POCKET_GATE_DIR`, `POCKET_ALLOWED_HOSTS`. Values are not recorded.
- **Tunnel:** source README describes Quick Tunnel for Gate-01 only and requires adding the exact tunnel host to transport security.
- **Startup recovery:** parent lifespan runs `recover_once()` once before serving both MCP session managers.

### Shared Space Stage 1

- **Environment variable name:** `A25_SHARED_DATA` (value omitted).
- **Default private data root in source:** `~/a25-data/shared-space`.
- **Startup:** storage is configured during lifespan, then crash-tail recovery runs once.
- **Launch command/port:** UNKNOWN from the inspected Stage 1 source alone; do not invent one.

### Startup automation / supervision

- **Manual:** historical sessions used manually started Uvicorn/cloudflared terminals.
- **Scripted:** UNKNOWN; no startup script was verified in the inspected refs.
- **Automatic boot:** UNKNOWN / not proven.
- **Independent process supervision:** ABSENT from inspected application source; external Android/Termux supervision is UNKNOWN.
- **Health check:** Gate-02A `GET /health` is implemented and intentionally returns ready:false. Gate-01 source has MCP `server_status`, not a separate HTTP health route in the inspected file.

---

## Network and Self-Recovery

### Network drop / switch

- Named Cloudflare tunnel should preserve the public hostname across tunnel process reconnects, but **automatic recovery after Wi-Fi/cellular changes is UNKNOWN** because no dated network-switch test was found or run.
- Gate-01 Quick Tunnel URLs can change when a new quick tunnel is created; connector URLs then require manual update.
- Gate-02A's named hostname reduces that URL-change problem, but does not itself prove Android process survival or cloudflared supervision.
- No live reconnect test was authorized by this order.

### Android sleep, process kill and reboot

- Application source contains no Android wake lock, boot receiver, Termux:Boot integration, systemd-like supervisor, or process resurrection logic.
- Therefore automatic recovery from Android killing Uvicorn/cloudflared is **UNKNOWN and not evidenced**.
- Historical practice was manual process launch. Treat phone reboot recovery as **MANUAL/UNKNOWN** until explicitly tested.
- Persistent Git files and JSONL data survive process restart; in-memory `pending_read` state does not.

### Ledger/cursor recovery

- Gate-01 and Shared Stage 1 parse only complete newline-terminated JSONL records.
- On startup, a partial tail is copied to quarantine and the ledger is truncated to the last complete newline.
- Reads do not repair.
- Cursor position is reconstructed from each actor's last persisted event's `cursor_through`.
- A pending read is intentionally ephemeral and vanishes on restart.
- A restart with unread messages should therefore reconstruct unseen messages from persisted events and the actor's last persisted cursor. Historical Gate-01 recovery evidence supports this for the three-event proof.

### Logs

- Gate-01: `quarantine.log` for recovered partial tail; no structured service/process log subsystem verified.
- Gate-02A: `listening_wall.py` defines `observations.jsonl` with bounded fields, 1 MB cap, no-follow open and mode 0600, but main server comments state observation is disabled and `DenyAllProvider` does not call the observer.
- Uvicorn/cloudflared terminal output was used historically; persistent supervision/log rotation is UNKNOWN.
- The separate observation viewport previously lacked timestamps in its logs, but that is not the Pocket Server server log.

---

## Capability Matrix

WORKING requires dated evidence, not merely code presence.

| Capability | Status | Evidence / limit |
|---|---|---|
| `server_status` | **WORKING** | Gate-01 source + historical live Gate-01 tests, including 2026-10-07 recovery context |
| `read_roundtable` | **WORKING** | Gate-01 source + historical three-event/restart evidence |
| `append_roundtable` | **WORKING** | Gate-01 source + historical interleaved events; append is serialized and read-first |
| Event persistence | **WORKING** | JSONL + fsync source; historical restart retained three events |
| Cursor recovery | **WORKING** | Source reconstructs cursor from persisted own events; 2026-10-07 historical recovery evidence |
| GPT/Claude actor separation | **WORKING (Gate-01 path identity)** | Separate route-derived identities historically tested; this is not OAuth identity |
| `list_projects` | **ABSENT in inspected runtime refs** | Target appears in START_HERE contract; no such MCP tool in Gate-01/Shared Stage 1 inspected server |
| `list_files` | **ABSENT in inspected runtime refs** | Same |
| `read_file` | **ABSENT in inspected runtime refs** | Same |
| ZIP intake | **UNKNOWN / not found in inspected refs** | ZIP checkpoint use is not server intake |
| Shared workspace | **PARTIAL** | Stage 1 private storage + hardened ledger implemented; full project-file V1 not present |
| HTTP health | **IMPLEMENTED / historically tested** | Gate-02A `/health` returns ready:false; current live state unknown |
| Uvicorn restart supervision | **ABSENT/UNKNOWN** | No app-level supervisor; historical restart manual |
| Tunnel restart supervision | **UNKNOWN** | cloudflared may internally reconnect, but no external restart supervisor verified |
| Reconnect after network switch | **UNKNOWN** | No dated Wi-Fi/cellular switch proof found |
| Reboot recovery | **UNKNOWN / historically manual startup** | Persistent data recovery exists; process autostart not verified |
| Logs | **PARTIAL** | quarantine log; dormant bounded observation helper; terminal logs historically |
| Path traversal controls | **PARTIAL / IMPLEMENTED for Shared storage** | Shared root must be outside repo; no-follow regular-file opens. Project-file API absent, so its traversal policy cannot be marked working |
| Secret controls | **PARTIAL / IMPLEMENTED** | Gate-01 validates route secrets; secrets are env-based/not committed. Gate-02A OAuth is deny-all. Full token/auth line unfinished |

---

## Failure Scenarios

| Scenario | Expected behavior | Source / evidence | Data-loss risk | Recovery |
|---|---|---|---|---|
| Uvicorn crash | Service becomes unavailable; persisted complete JSONL events remain; on next startup partial tail is recovered | Gate-01/Shared source; historical restart proof | Low for fsynced complete events; pending read lost by design | **MANUAL** process restart; ledger recovery automatic at startup |
| Tunnel disconnect | Local server may remain up; remote connector unavailable until tunnel returns | Architecture/history; no supervisor source | No direct ledger loss | **UNKNOWN** for automatic cloudflared reconnect; manual restart historically available |
| Wi-Fi -> cellular | Desired outcome is tunnel re-establishment without changing named Gate-02A hostname | No dated switch test found | No direct stored-data loss; in-flight request may fail | **UNKNOWN** |
| Android kills process | Uvicorn/tunnel stop unless externally supervised; disk data persists | No app supervisor found | Pending read/in-flight operation can be lost; fsynced events should persist | **MANUAL/UNKNOWN** |
| Phone reboot | Processes stop; files persist; Gate-01/Shared startup recovery handles crash tail when server is manually/automatically relaunched | Source + historical manual workflow | Same as process kill; credentials/config persistence not inspected | **MANUAL/UNKNOWN**; no boot automation proven |
| Append timeout | Client may not know whether server committed before timeout; exact retry of latest own message+refs can return duplicate instead of appending again | Gate-01 source duplicate logic | Low if retry is exact; ambiguous client UX possible | **MANUAL client retry**, server duplicate guard automatic |
| Incomplete JSONL tail | Reads ignore incomplete tail; startup quarantines tail and truncates to last newline | Gate-01/Shared source | Partial last record lost/quarantined; earlier complete events preserved | **AUTO at server startup** |
| Concurrent append | One-process asyncio lock serializes append logic | Gate-01/Shared source | Low within one process; multi-process behavior not supported/proven | **AUTO within one process** |
| Tunnel URL changes | Gate-01 Quick Tunnel requires connector/allowed-host update; named Gate-02A hostname intended stable | Gate-01 README + Gate-02A source | No ledger loss; connectivity loss | Gate-01 **MANUAL**; Gate-02A named URL should persist, tunnel recovery still UNKNOWN |
| Restart with unread messages | Persisted cursor from last own event reconstructs unseen; pending read disappears | Gate-01 source + historical 3-event recovery | No persisted-event loss expected; uncommitted pending-read state lost intentionally | **AUTO ledger/cursor reconstruction** after manual/automatic process restart |

---

## Recall Corrections

Phase A is preserved above; these are corrections/precision added after inspection.

1. **File API was less complete than broad project-goal memory could imply.** `START_HERE.md` specifies six V1 operations, but inspected Gate-01 and Shared Stage 1 servers expose only status/read/append Roundtable. `list_projects`, `list_files`, and `read_file` are not present in those runtime refs.
2. **Shared Space Stage 1 is storage hardening, not full shared-project access.** It secures the Roundtable ledger/private data root and still identifies itself as Gate-01/dummy-data-only.
3. **Auth branch is definitely not wired into the server at its current Git ref.** Its `gate02/server.py` blob matches main's deny-all server while auth modules exist alongside it.
4. **Gate-02A observation helper exists but main observation is disabled.** `listening_wall.py` contains bounded logging code; the deny-all provider inspected does not call it.
5. **Automatic restart/network recovery remains unverified.** My memory of manual terminals is supported by historical context, but no source inspected here proves Termux boot/start supervision or network-switch recovery.
6. **Current running state cannot be inferred from old PIDs or shutdown screenshots.** No live endpoint/process check was allowed or performed in this recall.
7. **Gate-01 secret-path identity is working historical separation, not authenticated identity in the final security sense.** OAuth identity remains unfinished.

---

## Evidence References

### A25 coordination order
- Repo: `Stratumnova/A25-Training-Workspace`
- Branch: `coord/a25-namespace-trial-001`
- Order: `local build operations and recalls/outbox/A25-PS-MR-O001-POCKET-SERVER-RECALL.md`
- Branch head observed before report creation: `5074ac4958fd69053fdfa242899069b6ffd13480`
- Evidence date: 2026-10-17

### Pocket Server GitHub
- Repo: `Stratumnova/pockettest`
- `main`: `f0a11d51968ad598691333d32971dfb483489073`
  - `START_HERE.md`
  - `gate01/README.md`
  - `gate01/server.py`
  - `gate02/server.py`
  - `gate02/listening_wall.py`
- `build/gate02a-c1-auth-store`: `1b578ee32532f99093ab906af52e8b485c90a7e4`
  - `gate02/auth_store.py`
  - `gate02/authorize_provider.py`
  - `gate02/client_registration.py`
  - `gate02/consent_views.py`
  - `gate02/server.py`
- `build/shared-space-v0`: `9a419e925dff2de64ef948b7d6d8304eccf8387d`
  - `shared/server.py`
  - `shared/secure_files.py`
  - `shared/storage.py`
- `proposal/shared-space-stage-2-identity`: `8ade3c00f4f5219182ec01b5154b4b89b71d3359`
- GitHub inspection date: 2026-10-17

### Historical conversation/checkpoint evidence available to this builder
- Gate-01 post-restart recovery study: 2026-10-07 context, original three-event ledger.
- Pocket Server / viewport reconciliation and shutdown checkpoint: 2026-10-12 context.
- These are cited as historical evidence only; this order did not rerun them.

No secret values, private data contents, bearer paths, or credentials were inspected or recorded.

---

## Recommended Tests

These are proposals only; none were executed.

1. **Cold-start inventory test:** after explicit authorization, record process state before starting anything, then prove startup from documented commands without duplicate services.
2. **Named-tunnel network switch test:** while using non-sensitive dummy data, switch Wi-Fi -> cellular -> Wi-Fi and measure tunnel recovery, hostname stability, connector retry behavior and any failed in-flight call.
3. **Uvicorn crash/restart test:** append dummy events, kill only the test server, restart, verify event ordering/cursors/unseen and process recovery method.
4. **cloudflared crash/restart test:** leave local test server running, stop tunnel only, verify local health remains and remote access recovers after tunnel restart.
5. **Android process-kill test:** under a disposable test ledger, let Android/Termux process termination occur and document which processes survive and which require manual restart.
6. **Phone reboot test:** verify whether any authorized boot mechanism exists; measure exact manual steps if none.
7. **Append ambiguity test:** force a client-side timeout around an append, retry the exact message+references and verify no duplicate event.
8. **Crash-tail test:** use only a temporary test ledger to append an incomplete JSON fragment, restart, verify quarantine/truncation and no loss of earlier complete events.
9. **Concurrent append test:** simultaneous GPT/Claude dummy appends in one process; verify monotonic IDs, no interleaving corruption and cursor semantics.
10. **V1 file-capability test after implementation:** list_projects/list_files/read_file with traversal, symlink, absolute-path, encoded traversal, ZIP extraction and secret-boundary negatives.
11. **Auth integration test:** only after C4/C5 are built, prove GPT and Claude authenticated identities cannot cross scopes and that revocation takes effect.
12. **Persistent logging test:** add/verify timestamped non-secret process logs and bounded rotation before relying on logs for recovery evidence.

---

## Unresolved Questions

1. Is any Pocket Server process currently running on the phone on 2026-10-17? **UNKNOWN under this read-only/no-live-test order.**
2. Has any work after the 2026-10-12 checkpoint added startup scripts, Termux:Boot, wake-lock handling, or external supervision? **UNKNOWN.**
3. Has consent/C4/C5 advanced beyond GitHub auth ref `1b578ee...` in an uncommitted phone worktree? **UNKNOWN.**
4. Is the uncommitted observation viewport under `~/a25-workshop/gpt` now preserved in Git or still phone-only? **UNKNOWN from inspected sources.**
5. Are `list_projects`, `list_files`, `read_file`, or ZIP intake implemented anywhere outside the inspected refs? **UNKNOWN; absent from inspected runtime refs.**
6. What is the exact behavior of cloudflared under Android Wi-Fi/cellular transitions and Doze on this phone? **UNKNOWN; needs a controlled test.**
7. Is there a defined maximum JSONL ledger size/rotation policy? **UNKNOWN from inspected Gate-01/Shared source.**
8. Does the intended production design remain one Uvicorn process? The append lock is process-local; multi-worker/multi-process append safety is **not proven**.
9. What persistent service-log location and rotation policy should be authoritative for recovery studies? **UNRESOLVED.**

---

## Final State Summary

**CURRENT RUNNING STATE:** **UNKNOWN.** No live endpoint, process list, phone shell or tunnel was queried. Historical 2026-10-12 evidence ended with a deliberate shutdown, but that cannot establish 2026-10-17 runtime state.

**LAST VERIFIED VERSION:** GitHub refs inspected 2026-10-17: Gate-02A main `f0a11d51968ad598691333d32971dfb483489073`; auth branch `1b578ee32532f99093ab906af52e8b485c90a7e4`; Shared Space Stage 1 `9a419e925dff2de64ef948b7d6d8304eccf8387d`; Stage 2 proposal `8ade3c00f4f5219182ec01b5154b4b89b71d3359`.

**STARTUP METHOD:** Historically manual Termux Uvicorn + cloudflared processes. Gate-02A historical local bind `127.0.0.1:8766`; Gate-01 source-documented bind `127.0.0.1:8765`. Automatic boot/supervision not verified.

**NETWORK RECOVERY:** Named Gate-02A hostname is stable by design relative to Gate-01 Quick Tunnel, but actual Wi-Fi/cellular/drop recovery and external process supervision are **UNKNOWN / untested in evidence available here**.

**SELF-REPAIR:** Limited to deterministic startup ledger crash-tail recovery in Gate-01/Shared Stage 1. No evidence of general server/tunnel self-restart or autonomous repair. Pending reads intentionally do not survive restart.

**SHARED FILE ACCESS:** Target contract exists, but inspected runtime refs do not yet expose `list_projects`, `list_files`, or `read_file`. Shared Space Stage 1 is partial storage hardening. ZIP intake is not verified.

**CONFIDENCE:** **HIGH** for repository refs/source behavior and Gate-01 ledger semantics; **MEDIUM** for historical phone startup/test facts preserved in conversation/checkpoint context; **LOW/UNKNOWN** for current live runtime, Android process survival and network-switch recovery.

**BLOCKERS:** unfinished OAuth consent/token/scope/audit integration; full authenticated GPT/Claude identity integration; missing/unknown V1 project-file API and ZIP intake in inspected refs; no proven Android boot/process/tunnel supervision; no controlled network-switch/reboot recovery evidence; Stage 2 proposal remains unmerged with a remembered failing race test.

**STOP:** Report complete. No server changes, restarts, repairs, merges, credential access, or live endpoint tests were performed.
