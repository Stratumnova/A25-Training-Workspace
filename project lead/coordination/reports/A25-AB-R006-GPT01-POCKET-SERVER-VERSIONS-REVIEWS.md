# A25-AB-R006 — Pocket Server Versions, Branches and Technical Review Evidence

FROM: A25-AB-GPT01 — Archives Builder  
TO: A25-AG-GPT01 — Archives Lead; Zed  
DATE: 2026-10-18  
ORDER: A25-AB-O006 @ `39a4b987d52e672c59859f2201d2e200f7184fdf`  
REPORT BRANCH: `coord/a25-namespace-trial-001`  
STATUS: SOURCE EXTRACTION COMPLETE; NO SDK/CI/PHONE TESTS EXECUTED  
NEXT: Archives Lead review; STOP before AB-07.

## 1. Access and method

**VERIFIED** denotes source text, GitHub commit/branch response or original Drive reviewer text fetched directly during AB-06, not successful execution. **HISTORICAL CLAIM** denotes builder/reviewer-reported tests and operations. **ADOPTED** denotes recorded owner/lead authorization, not implementation proof. **UNKNOWN** means inaccessible or untested. **SUPERSEDED** applies narrowly to later corrected versions, never deletion of originals.

The GitHub connector fetched the six specified commits in `Stratumnova/pockettest`, the five named branch objects, and selected original files at pinned commits. The Google Drive connector directly fetched **both** Claude02 technical reports. GitHub coordination originals were also read. No checkout, test, CI, deployment, phone/server/tunnel or code write was performed.

### Pinned primary-source ledger

| Original source | Exact revision / ID | Access, limitations |
|---|---|---|
| `pockettest` branch objects | `main`, `build/a25-pocket-server-roundtable`, `build/gate02a-c1-auth-store`, `build/shared-space-v0`, `proposal/shared-space-stage-2-identity` | **VERIFIED** current GitHub branch pointers; see matrix |
| `gate02/server.py` | `f0a11d51968ad598691333d32971dfb483489073`, blob `b8bb1a524375ecafa2cb29ce802316e27b0c8743` | Full source **VERIFIED**; baseline deny-all |
| `gate02/server.py` | `442529a32356c5fb557d908fcd20bace733f04d8`, blob `ceffc3ed0cbdfd2d9016845ca7e131a35efcdbdd` | Full source **VERIFIED**; first fixed-file read |
| `gate02/server.py` | `fabedb661bb5161055534589c7517f7e0738139d`, blob `670c2cb01692807e1301f10ec9ceef004d01c4a6` | Full source **VERIFIED**; guard corrections |
| `gate02/test_shared_read.py` | `fabedb661bb5161055534589c7517f7e0738139d`, blob `8ce8b62753cdc1c9290e40c2c8b80b6c36416744` | Full source **VERIFIED**; contains SDK ASGI subprocess test, not executed here |
| `gate02/auth_store.py` | `1b578ee32532f99093ab906af52e8b485c90a7e4`, blob `b8a8f2b9f9ee80af11c6ff2d58f73f5b01f902e3` | Full source **VERIFIED**; docstring says “Not wired into public server”; other auth branch files not exhaustively audited |
| `shared/secure_files.py` | `9a419e925dff2de64ef948b7d6d8304eccf8387d`, blob `c6dfda413eee0875b6d84db312a8eb189baf236e` | Full source **VERIFIED**; append/read/RW fd guards; Stage 1 tests not run |
| `shared/STAGE2_PROPOSAL.md` | `8ade3c00f4f5219182ec01b5154b4b89b71d3359`, blob `76b62e10f844dee39d3922f4b908b54d3a58659c` | Full source **VERIFIED**; expressly proposal, not merge/deployment |
| `A25-PM-R003-GPT01.md` | `A25-Training-Workspace` coordination branch; blob `e556959caed13746c76d86406338d91aeeab7c8c` | Full original GPT builder report **VERIFIED** as document; test results historical |
| `A25-PM-R004-GPT01.md` | coordination branch; blob `5bde2456afb025e435e73fc8dc19177a1096c3be`; report refers to order `4cf75a4b464973e15d11b3fd72e7f590478131bb` | Full original GPT correction report |
| `A25-PM-O006-GPT01-CLAUDE02-REVIEW-CORRECTIONS.md` | coordination branch; blob `67244790750795c75810e555caba61f6ab16a267` | Full order; limited code/test corrections only |
| `A25-PM-O007-CLAUDE02-R004-INDEPENDENT-REVIEW.md` | coordination branch; blob `2959c89e8fd18d338c55f85534080c15d58673d2` | Full independent re-review order; no deployment authorization |
| Claude02 first technical report `A25-PM-R001-CLAUDE02.md` | Google Drive `13wjG6hhTAn_LgzRw1uC2WLNzRLL0Fpwl`; dated 2026-10-17 ~20:30 MDT | **Direct full original Drive text**, 26,457 characters; reviewer-reported hashes/tests not recomputed |
| Claude02 re-review `A25-PM-R002-CLAUDE02.md` | Google Drive `1cloGAYJKTu7pVmZN4lXqETquBfHXI5Va`; Drive creation previously reported 2026-10-18T02:52:08.559Z | **Direct full original Drive text**; reviewer-reported 17+10 tests not rerun |
| AB-03 Drive source ledger | `A25-AB-R003-GPT01-CLAUDE-DRIVE-COMMUNICATION-EVIDENCE.md` @ `d40dfdebd165689c93984bd27b4341702721ae61` | Full prior archival report, secondary for earlier transport claims |
| Original O004 filename attempted | `project lead/coordination/orders/A25-PM-O004-GPT01-OFFICIAL-SHARED-READ-IMPLEMENTATION.md` on coordination branch | **NOT FOUND (GitHub 404)** for that exact guessed filename; O004 authority and scope instead corroborated by R003, O006 and owner Decision 013 references. Exact O004 source path UNKNOWN; do not assert original order absent. |

Original commit URLs: [baseline](https://github.com/Stratumnova/pockettest/commit/f0a11d51968ad598691333d32971dfb483489073), [official M1](https://github.com/Stratumnova/pockettest/commit/442529a32356c5fb557d908fcd20bace733f04d8), [O006 correction](https://github.com/Stratumnova/pockettest/commit/fabedb661bb5161055534589c7517f7e0738139d), [auth](https://github.com/Stratumnova/pockettest/commit/1b578ee32532f99093ab906af52e8b485c90a7e4), [Shared Stage 1](https://github.com/Stratumnova/pockettest/commit/9a419e925dff2de64ef948b7d6d8304eccf8387d), [Stage 2 proposal](https://github.com/Stratumnova/pockettest/commit/8ade3c00f4f5219182ec01b5154b4b89b71d3359). GitHub commit fetch confirmed all six belong to **Stratumnova/pockettest**. Individual commit response reported changed filenames; not proof all historical code was covered by the limited file reads.

## 2. Compact version / branch matrix

**VERIFIED branch pointers at AB-06 fetch time**, not assumed historical branch state or current phone checkout:

| Distinct line | Branch | GitHub HEAD fetched | Source meaning / limit |
|---|---|---|---|
| Gate-01 | Historical authless route-derived ledger (historical Gate-01 code not separately fetched here) | UNKNOWN distinct branch/commit in this batch | Historical three-event GPT/Claude exchange, cursors/recovery and secret routes are **HISTORICAL CLAIM**, not Gate-02A OAuth or deployed shared identity |
| Gate-02A public baseline | `main` | `f0a11d51968ad598691333d32971dfb483489073` | **VERIFIED source:** `DenyAllProvider`, registration/code/token refusal, `/health` ready false, FastMCP configured for deny-all; runtime authorization not exercised |
| Gate-02A official M1 first read | `build/a25-pocket-server-roundtable` | Historical commit `442529a32356c5fb557d908fcd20bace733f04d8` | **VERIFIED source:** fixed owner-configured absolute file, base64/SHA256/length, 1 MiB cap, local anonymous loopback test mode; original weak tests |
| Gate-02A official M1 corrected | `build/a25-pocket-server-roundtable` | **`fabedb661bb5161055534589c7517f7e0738139d`** | **VERIFIED HEAD/source:** added Host and forwarding-header guards, local host allowlist, mode health and SDK test source; runtime still unverified |
| Gate-02A C1 auth storage | `build/gate02a-c1-auth-store` | `1b578ee32532f99093ab906af52e8b485c90a7e4` | **VERIFIED source:** SQLite registration/consent/authorization-code/revocation foundations; file explicitly says not wired into public server; token issuance/refresh and integrated remote access not established |
| Shared Space Stage 1 | `build/shared-space-v0` | `9a419e925dff2de64ef948b7d6d8304eccf8387d` | **VERIFIED source:** secure append/read/RW helpers, separate `shared/server.py` code line and tests; no Stage 1 phone or dual-client runtime tested here |
| Shared Space Stage 2 | `proposal/shared-space-stage-2-identity` | `8ade3c00f4f5219182ec01b5154b4b89b71d3359` | **VERIFIED source proposal:** GPT/Claude path-based identity config, proposed lock/CLI integration; bearer secret paths **not OAuth**, explicitly unmerged/undeployed in proposal |

The Stage 2 document describes owner CLI, `ledger_transaction` flock and source/test follow-ups, but **the proposal text itself explicitly disclaims production authorization**. No proof that Stage 2 was merged to `main` or the official M1 branch. Historical checkpoint counts for Stage 1 and Stage 2, including 78 PASS/1 FAIL/1 WARN and FileExistsError race, are **HISTORICAL CLAIMS** from the previous inventory; AB-06 did not fetch their exact job/test logs or reproduce them. The branch HEADs being distinct **VERIFIES non-equivalence**; none may be described as one completed Gate-02A system.

## 3. Official M1 source and builder sequence

**ADOPTED authorization, as documented:** Zed's owner decision `LEAD-DECISION-013` approved one official long-lived build branch `build/a25-pocket-server-roundtable`. This is branch authority, **not** authorization for public anonymous access or phone deployment.

**R003 / O004 first source:** GPT builder reports two commits: `040e89612e9878ff0a337a496cf57a50d13a6108` for `gate02/server.py` and `442529a32356c5fb557d908fcd20bace733f04d8` for `gate02/test_shared_read.py`. **VERIFIED independently at `442529a`:** `read_fixed_file(path)` checks absolute path, uses `O_NOFOLLOW` and `O_NONBLOCK`, `fstat` regular-file check, inclusive 1,048,576-byte limit, Base64 payload, SHA-256 and byte length. Only `read_shared_file()` is exposed as a tool and takes no client-supplied path. Unconfigured/errors return `shared_file_unavailable`. `A25_LOCAL_READ_MODE=1` disables OAuth locally; `LoopbackOnly` at this version checks only peer address, and transport allowed_hosts still includes public domain. **This was source implementation, not tested safe tunnel behavior.**

**Builder R003 actual test ledger (HISTORICAL CLAIM in original):** `python -c 'import mcp'` raised `ModuleNotFoundError: No module named 'mcp'`; attempted raw GitHub curl failed DNS resolution (exit 6); unittest discovery found no files and returned exit 5 / **0 tests**. No SDK, MCP client, phone or deployment PASS.

**Claude02 R001 original independent review:** Reviewer reported retrieving four files via Nimble `simplified_html` after `plain_text` stripped angle-bracket text, and checking git blob parity. **AB-06 independently confirms** reviewed `gate02/server.py` blob `ceffc3ed0cbdfd2d9016845ca7e131a35efcdbdd` at `442529a`; reviewer also records `test_shared_read.py` blob `6d0d734fbaad5687877c9a7c94ac00fea48cf777`, `listening_wall.py` blob `fc9d1c228e7dadb610ec2ec7ebc7aa80faadf2cf`, and `requirements.lock.txt` blob `afcaad8d80dceefb2b131d0a60ce5ad5ab0ca4f9` (latter three **reviewer-reported**, not AB-06 independently fetched). Reviewer reports **21 isolated AST/pure-Python tests executed, 21 OK** in Python 3.12.3, but `mcp` missing, SDK suite **0 tests**. A passing weakness-reproduction test confirms a defect, not safety.

**F-1:** builder's original symlink test linked to an oversized target, so size cap alone could make it pass without `O_NOFOLLOW`. Reviewer mutation check B05 showed test was nondiscriminating. Actual helper's final-symlink guard worked in isolated B04; parent-directory symlinks were followed (B08).

**F-2:** original deny-all test only checked `isinstance(server.provider,DenyAllProvider)`, not real HTTP authorization wiring. No 401 over MCP verified.

**F-3:** reviewer identified HIGH operational risk if anonymous local mode shared a public Cloudflare tunnel loopback origin, because original `LoopbackOnly` ignored Host/forwarding headers. Historical tunnel topology is a reference, **not** an AB-06 phone observation. Separate local port/no tunnel was recommended, not executed.

**F-4/F-5:** default mode denies remote users and local mode only permits loopback; neither by itself establishes independently authenticated GPT/Claude remote reads. SDK version/transport compatibility not executed. **F-6:** original health always said `gate02a-deny-all` even in local mode. **F-7:** tool errors returned normal content rather than MCP `isError`, deferred. F-8 possible 1 MiB Base64 response truncation was speculative.

**O006 and R004:** Lead authorized narrow corrections only. Builder reports commits `fbf3b519bc7322be9c09266c2973eb2420fb4228` (server) and `fabedb661bb5161055534589c7517f7e0738139d` (tests). **VERIFIED at `fabedb`:** server now checks loopback peer, exactly one local Host, rejects `cf-connecting-ip`, `cf-ray`, `x-forwarded-for`, `forwarded`, `x-real-ip`, and removes public domain from local `allowed_hosts`; `/health` returns `gate02a-local-read` in local mode but `ready:false`. Test source adds subprocess-isolated ASGI scenarios. **Builder R004 actual attempts:** `mcp` import still failed; pip installation of `mcp==1.26.0` failed with DNS/index name resolution; **zero successful SDK/unittest executions**. Do not misread pip's “No matching distribution” as proof package version absent.

## 4. Claude02 O007 re-review — original now recovered

Order `A25-PM-O007-CLAUDE02-R004-INDEPENDENT-REVIEW.md` scoped independent read-only review of exact `fabedb` and prohibited deployment. Original result **`A25-PM-R002-CLAUDE02.md` is directly accessible**, Drive ID `1cloGAYJKTu7pVmZN4lXqETquBfHXI5Va`; earlier archival UNKNOWN as to its existence is **SUPERSEDED only as an access gap**, not as SDK-runtime uncertainty.

Claude02 reports source blob verification (AB-06 independently confirms server blob `670c2cb01692807e1301f10ec9ceef004d01c4a6` and test blob `8ce8b62753cdc1c9290e40c2c8b80b6c36416744`). Reviewer reports **17 isolated pure-Python harness tests** and **10 regression tests**, **0 SDK integration tests** due to missing `mcp`. These test counts are **HISTORICAL CLAIMS from original review**, not tests AB-06 executed.

| Finding | Claude02 R002 conclusion | AB-06 independent source support / limits |
|---|---|---|
| **F-1** | **RESOLVED** by discriminating small-target symlink test and mutation test | **VERIFIED source** now creates small `valid` target; mutation execution is reviewer-reported |
| **F-2** | **PARTIAL**: subprocess SDK ASGI test added, default deny-all source-consistent, no SDK execution | **VERIFIED source** contains subprocess test and mode assertions; actual MCP 401/200/403 UNKNOWN |
| **F-3** | **RESOLVED at code level**, LOW residual proxy/header risk | **VERIFIED source** adds guards; tunnel behavior untested; denylist not comprehensive |
| **F-6** | **RESOLVED in source** | **VERIFIED source** mode-specific health status, `ready:false`; runtime check UNKNOWN |
| **R2-1** | **FAIL predicted**: local-mode test sends portless `Host: localhost`, SDK `allowed_hosts=["localhost:*"]` requires port; reviewer predicts **421**, not asserted 200 | **VERIFIED source** test default `host="localhost"`, base URL `http://localhost`; source allowlist `localhost:*`. SDK v1.26.0 behavior and predicted 421 are **reviewer-reported SDK-source analysis**, not AB-06 executed HTTP |
| **R2-2** | Loose suffix parsing and non-ASCII ignored in local Host | **VERIFIED source** `split(":")[0]`, bracketed IPv6 prefix, `decode("ascii","ignore")`; isolated reproductions reviewer-reported |
| **R2-3** | Public origin still in local-mode `allowed_origins` | **VERIFIED source** `allowed_origins=[PUBLIC_ORIGIN]` in both modes |
| **R2-4** | Other forwarding headers not rejected | **VERIFIED source** fixed five-name denylist; reviewer reported six admitted alternatives |
| **R2-5** | SDK dependency needed even for builder's pure tests; timeout/formatting caveats | **VERIFIED source** `setUpClass` imports SDK-backed server; no SDK execution |

**Preserve GPT–Claude distinction:** GPT R004 accurately reports that its ASGI test cases were *added but unexecuted* and may need adjustment; Claude R002 supplies a specific **predicted** test defect. They do not disagree about an actual SDK PASS. Claude's “resolved” is limited to executed isolated checks/source inspection; no real FastMCP transport run was shown. No source edit fixing R2-1 was found at the fetched official branch HEAD `fabedb`. Do not imply corrected runtime merely because Claude endorsed parts of the code.

## 5. Test/evidence ledger by environment

| Evidence type | Historical observed/reported outcome | AB-06 status |
|---|---|---|
| Gate-01 Android/Termux three-event ledger, cursor/restart | Prior checkpoints report exchange/recovery | **REFERENCE/HISTORICAL CLAIM**; no live phone or original event log re-read here |
| GPT R003 builder SDK/unit | 0 executed; missing `mcp`, DNS and missing files | **HISTORICAL CLAIM** from original builder report |
| Claude02 R001 isolated harness | 21/21 OK; includes tests confirming F-1/F-3 weakness | **HISTORICAL CLAIM** from original reviewer; source server blob independently confirmed |
| Claude02 R001 SDK | 0; missing `mcp` | **HISTORICAL CLAIM**; no integration PASS |
| GPT R004 SDK/ASGI | 0; missing `mcp` and pip DNS failure | **HISTORICAL CLAIM**; no integration PASS |
| Claude02 R002 isolated/regression | 17 isolated + 10 regression; F-1 mutation and SDK host logic transcription | **HISTORICAL CLAIM** from original reviewer; code-level premises inspected |
| Claude02 R002 SDK | 0; missing `mcp`; R2-1 predicted 421 | **HISTORICAL CLAIM**; integration remains UNKNOWN |
| Auth C1 SQLite tests | Test file exists per commit changed-files; no exact run log inspected | **UNKNOWN** execution/pass; not wired into official server |
| Shared Stage 1/2 tests | Historical isolated test counts, Stage 2 race and proposed corrections | **HISTORICAL CLAIM**; no rerun/log read |
| CI for Pocket Server | No exact Pocket Server CI run retrieved | **UNKNOWN**; Watchdog Actions are not Pocket Server integration evidence |
| Production/phone/tunnel deployment | No owner authorization or direct current runtime observation in this batch | **UNKNOWN / NOT ESTABLISHED** |
| Dual remote GPT/Claude authenticated access | No verified OAuth token issuance, remote clients or shared read receipts | **NOT VERIFIED** |

## 6. Open defects, conflicts, next justified action

1. **R2-1**: correct test's local-mode Host/base URL under separate source order, then run exact pinned SDK-backed ASGI suite in isolated environment. Preserve original test failure prediction and corrected commit as separate records.
2. **F-2 integration**: verify default unauthorized MCP initialize 401, OAuth metadata, local-mode initialize, actual `tools/call` receipt with a small nonsecret fixture, remote peer/Host/forwarding rejection and health. Builder suite currently lacks full tool-call coverage. Record exact environment, SDK version and raw test output.
3. **F-3 residual**: strengthen host parsing and forwarding header handling only after explicit scope/owner approval; anonymous local mode must never be routed through public tunnel. Source guards are defense in depth, not remote identity.
4. **C1 OAuth**: independently inspect and test token issuance/refresh/scopes/audit and integration; do not conflate separate auth branch with official build or default deny-all main.
5. **Shared Space**: inspect Stage 1 original test logs and Stage 2 integration/locking/race results at exact commits. Stage 2 path secrets are bearer capabilities, not authenticated provider identities; proposal is not deployment.
6. **Gate-01**: obtain original pinned ledger/recovery source and timestamped event/phone evidence before assigning verified restart or remote multi-client status. Gate-01's historical authless paths do not certify Gate-02A.
7. **Source gap**: locate exact original O004 filename and source; guessed path returned 404. Obtain original SDK v1.26.0 code and real ASGI execution logs to independently resolve R2-1.
8. **Decision boundary**: owner/lead must decide safe remote identity design after isolated M1 checks; no automatic merge, deployment, tunnel, code edits or Watchdog/PR #3 action follows from this archival report.

**AB-06 STOP:** Only this new Markdown report is authorized for publication. All original source code, reviews, Drive files, branches, CI, phone, server and tunnel remain untouched. Watchdog and PR #3 are out of scope.
