# A25 Recall Network — GPT Session Report

ID: **A25gptrecall_id001**  
Platform: GPT  
Date: 2026-10-17  
Status: SUBMITTED  
Scope: independent recall plus limited source verification; no builds, repairs, server changes, endpoint tests, merges, or existing-project modifications.

## Evidence vocabulary

- **RECALL** — model-accessible prior conversation/context, not independently re-read for this report.
- **OBSERVED_HISTORICAL** — visible historical terminal/screenshot evidence supplied in this session.
- **SOURCE_VERIFIED** — checked against accessible source during this recall.
- **ZED_RELAYED** — owner report not independently reproduced here.
- **AUTHOR_REPORTED** — prior builder/reviewer report.
- **INFERRED** — conclusion from evidence rather than direct proof.
- **UNKNOWN** — not established.

Completion terms: PROPOSED, IMPLEMENTED_UNTESTED, TESTED_HISTORICAL, RUNNING_VERIFIED, FAILED, BLOCKED, UNKNOWN.

## Phase A — frozen recall

**Limitation disclosure:** before this recall order arrived, this GPT session already contained extensive conversation summaries/memory and Zed had just displayed current terminal file-location output. Therefore Phase A cannot be a pristine blind-memory sample. The items below preserve the recall state available before additional project-source verification; they must not be treated as source verification.

### A. A25 Pocket Server / AI Workshop family

**RECALL — Gate-01.** A frozen Pocket Server proof existed for GPT/Claude Roundtable exchange. Remembered properties: route-derived GPT/Claude identity, read-before-append behavior, per-event cursor semantics, duplicate retry protection, append-only JSONL with flush/fsync and an append lock, plus crash-tail recovery/quarantine. Historical three-event ledger was treated as protected. Status: TESTED_HISTORICAL, not re-run here.

**RECALL — Gate-02A hardened deny-all baseline.** Separate from Gate-01. Remembered main commit: `f0a11d51968ad598691333d32971dfb483489073`. It intentionally kept public MCP unavailable while the listening-wall/security line was built. Status: TESTED_HISTORICAL; current runtime initially unknown.

**RECALL — Gate-02 auth branch.** Distinct branch `build/gate02a-c1-auth-store`, remembered commit `1b578ee32532f99093ab906af52e8b485c90a7e4`. Registration, consent UI, auth-code/revocation foundations existed, but access/refresh-token issuance/validation/rotation and full scopes/audit were unfinished, and `server.py` still used the deny-all provider. Status: PARTIAL / IMPLEMENTED_UNTESTED-to-TESTED_HISTORICAL by component; not production-authenticated.

**RECALL — Shared Space Stage 1.** Distinct branch `build/shared-space-v0`, remembered commit `9a419e925dff2de64ef948b7d6d8304eccf8387d`. Private storage hardening existed with storage outside repo, restrictive permissions, no-follow regular-file handling, Roundtable-oriented API. Status: TESTED_HISTORICAL.

**RECALL — Shared Space Stage 2 identity proposal.** Distinct proposal branch `proposal/shared-space-stage-2-identity`, remembered commit `8ade3c00f4f5219182ec01b5154b4b89b71d3359`. Last remembered test state: 78 passed / 1 failed / 1 warning, with a race around data-directory creation producing `FileExistsError`. It was explicitly unmerged/unaccepted. Status: FAILED / PROPOSED, pending investigation.

**RECALL — A25 read-only terminal/viewport.** Workspace remembered at `~/a25-workshop/gpt`. Two bridge concepts were kept distinct: an original bearer-auth local bridge on 8769 and a public proof/read-only viewport on 8770 reading a fixed tmux session `a25-gpt`. The public viewport was intentionally observation-only and was never to become the command gateway. Cloudflare provided transport. A three-party marker proof with Zed/GPT/Claude historically passed. Status historically TESTED; public exposure was deliberately shut down after earlier testing.

**RECALL — security/authority decisions.** Zed remains owner/operator. GPT and Claude are separate seats. Authentication is not process isolation. Before genuine isolation, AI write authority and execution authority must not compose: if an AI edits executable/build/test material, AI execution waits for Zed review/approval. Public observation and private command authority remain separate. Secret values are never to be pasted into chat/public viewport/checkpoints.

### B. A25 coordination / recall work

**RECALL.** Repository `Stratumnova/A25-Training-Workspace`, coordination branch `coord/a25-namespace-trial-001`. This GPT previously produced read-only recall reports R001 and R002 under `local build operations and recalls/`. R001 reconstructed Pocket Server state; R002 reconstructed historical workspace lessons with evidence classes. Remembered commits: R001 `da30ba17741abdacdef2f43684aef20d31b9f84d`; R002 `b75adcaa06907711dc3bc7a2b207be9d82275aa9`. Status: SUBMITTED historically.

### C. Mechanics Toolbox

**RECALL.** Public repo `Stratumnova/Tools_Templates-`. Browser-native JavaScript mechanics toolbox intended for static sites, Android WebViews, standalone rooms/games, and Portal-connected rooms. Architecture: JSON-driven, single `engine.dispatch(command)` ingress, capability checks, pure decisions to events, pure reducers, append-only history, deterministic IDs/clocks/pricing/seeded randomness, explicit room-transfer boundaries. Remembered main through Batch 5 at `cf500d7c350d779e1ba3b87d853ebedcb3626560`; Batch 6 branch `build/mechanics-toolbox-batch-06`, green commit `5205e6387a317cd417a68ad38d07c11102fe1cd6`, version 0.6.0, 122 tests passed / 0 failures. Batch 6 added seller-owned stalls, funded buy-order escrow, deterministic basis-point pricing, partial/multi-stage fulfillment, refunds, farmer/beast-master routing, stable route ordering, conserved items/currency, cancellation refunds, duplicate protection, example/docs/starter data, permanent CI gate. Batch 7 was next and prior batches were not to be changed without Zed approval. Status: Batch 6 TESTED_HISTORICAL; Batch 7 pending/unknown.

### D. Build-by-Coin / Stratumnova coins

**RECALL.** Public/private/build_by_coin coin collections were reorganized into per-coin container folders holding coin JSON, TXT sidecar used to drive PNG rendering, PDFs/assets as needed, with versioning inside container. Earlier three-folder model was superseded. Public samples included reference PNGs plus a small LLM rendering instruction sidecar. User requested author `ArchitectZero` rather than an earlier identifier. Large public/private ZIP packaging was produced historically. Status: artifacts AUTHOR_REPORTED/RECALL; current repo contents not reverified.

### E. Android Build-by-Coin reader / developer terminal app

**RECALL.** Android APK concept to ingest coin ZIP/single files, inspect assets, preview PNG/audio, export work ZIPs, and act as a phone-native Godot-like developer workspace. UI evolved from a 25x25 Test Room (deprecated) to dual View/Build using movable 9x9 cells and a layout map. Planned map intake accepted existing maps or hand drawings, converted colors to tiles, then allowed code-map fixups for edges/missing squares. Other remembered modules: terminal hub, editable hotkeys/workspaces, Edit/Run controls, day/night/weather, HUD/world/room/sprite settings, RNG crafting station, race/platformer premades. Status: iterative builds with multiple red/green cycles; exact latest build state UNKNOWN.

### F. Market Stall Lab / LivingMarket

**RECALL.** Standalone Android autonomous market simulation, September 2026. LivingMarket was sole authority; rendering/inspection/persistence/reports were projections. No player takeover/crafting/quests/Portal/Trapline in standalone spec; travel authoritative. Historical builds moved from blank/save-only failures to reported green builds; RNG review and graduation manifest were added. Status: TESTED_HISTORICAL by prior report, exact artifact/current branch UNKNOWN.

### G. Scrapline / Stratum Bots Wars

**RECALL.** Mobile mech/battle-bot game intended as first Google Play release. Node-system integration with Market Stall/Data Trader and cross-room items. Combat design included configurable weapons/armor/parts and exotic bounded mechanics such as energy siphon and temporary hostile command injection through defined bot command APIs, not arbitrary code execution. Combat/balance values were to remain configurable and each batch preserve telemetry/test reports. Status: design/development history exists; exact current source/build status UNKNOWN.

### H. Node system / Portal rooms

**RECALL.** Market Stall as hub; Portal as player container/base server/data collector; rooms included Trapline/fishing, Scrapline, Vocabulary, Farmhouse/farming, Shooting, Racer/car battle and later additions. Per-room currency could convert through Data Trader to floppy/items; Market Stall crafting/buying and cross-room specials connected progression. Standalones free, Portal paid unlock strategy was discussed. Status: architecture/design, implementation state mixed/UNKNOWN.

### I. Godot projects

**RECALL — Byte My Chip.** Godot 4.3 HTML5 platformer with movement/jump/double-jump, idle, Bytecoin pickup, firing logs and autoload managers including GameState, BytecoinManager, DeathCoinManager, LoopcoinMemory, SaveSystem and PowerDatabase. Status UNKNOWN.

**RECALL — Emergent Systems.** Top-down maze, 96x96 overall map composed from 3x3 32x32 cells; four-direction player, hotbar, pushable boulder, enemies/boss Custodian, ScentField, terminals, doors, plates, statues and mine-cart exit. Status UNKNOWN.

**RECALL — Loopcoin Sim.** Core scripts remembered: `need.gd`, `species.gd`, `world_grid.gd`, `organism.gd`; species examples cottontail/coyote. Loopcoin = bus/memory, Bytecoin = player currency, Deathcoin = death-state. Status UNKNOWN.

### J. Neocities Guildcraft hub

**RECALL.** `guildcraft.neocities.org` as shared JS engine/catalog/editor/minigame scrapyard/testing hub. Remembered live rooms: Rightscroll Jump'n'Run, Market Stall 1, Trapline, Wildmarket. Engine pieces: `contractGuard.js`, `eventConsole.js`, `decisionEngine.js`, `permanentLedger.js`; CodeMirror editor, compare/terminal-yard, arcade portal snapshot save. Frozen architecture emphasized single ingress, command bus/RBAC, pure decision/reducer, append-only hash-chained EventStore, unprivileged tools. Status: historical web project; current deployment UNKNOWN.

### K. Halfwake Pocket / Android Loopcoin proof

**RECALL.** Android proof with PoolStore append-only behavior, LogStore, UsageRepository, NpcBridge and EventProcessor with three consumers. Status UNKNOWN.

### L. RC Park Alpha 1 network/command system

**RECALL.** Remote RC control architecture: Xbox controller -> command center -> tower -> truck, analog 5.8 GHz FPV return; 2.4 GHz control for open/flat areas and 915 MHz for trees/rocks; central command with multiple towers; target scaling around 20 active trucks across four areas. Tick concept around 1/60 s per tower with sync-linked coin awards. Status: design/prototype planning; exact current hardware build UNKNOWN.

### M. APK mechanics/data-mining toolbox research

**RECALL.** User was assembling a personal mechanics/toolbox dataset from free APKs, initially top-1000 narrowed toward top-200, grouped by life sim/farming/crafting-shop/resource-management and related types. Goal was working templates/docs rather than copying whole products, feeding the reusable toolbox. Multiple batches were discussed. Status: historical research; exact corpus/current legality/provenance metadata not reverified here.

## Phase B — source and observation verification

### 1. RN-001 registry/rules and reservation

**SOURCE_VERIFIED.** Read on `Stratumnova/A25-Training-Workspace`, branch `coord/a25-namespace-trial-001`:
- `local build operations and recalls/recall-network/REGISTRY.md`
- `local build operations and recalls/recall-network/outbox/RN-001-UNIVERSAL-RECALL-RULES.md`

Registry initially had no confirmed GPT assignments; reservation directory contained `A25clauderecall_id001.md` and README, with no GPT reservation. GPT inbox contained only README. Following the atomic reservation rule, this session created exactly one new reservation:
`local build operations and recalls/recall-network/reservations/A25gptrecall_id001.md`
at commit `7c3db3f667f1abe54cbb40d0492bc9aebf66ba84`, then read the exact file back at that commit. Confirmed ID: **A25gptrecall_id001**.

### 2. Current Pocket Server GitHub refs

**SOURCE_VERIFIED** via GitHub branch listing for `Stratumnova/pockettest` during this recall:
- `main` -> `f0a11d51968ad598691333d32971dfb483489073`
- `build/gate02a-c1-auth-store` -> `1b578ee32532f99093ab906af52e8b485c90a7e4`
- `build/shared-space-v0` -> `9a419e925dff2de64ef948b7d6d8304eccf8387d`
- `proposal/shared-space-stage-2-identity` -> `8ade3c00f4f5219182ec01b5154b4b89b71d3359`
- `a25/training-workspace` -> `77af2aa4d17fe7818ce8830cd56a0c4b41162f1d`

This verifies the remembered branch/commit identities, not their runtime state or all semantic claims.

### 3. Current phone observation made before recall order

**OBSERVED_HISTORICAL in this session, not GitHub proof.** Zed started a Termux tmux session named `a25-gpt`; started `src.chatgpt_readonly` with the Pocket Server Gate-02 virtualenv; output showed Uvicorn on `127.0.0.1:8770`; then started the named Cloudflare tunnel. GPT's A25 Terminal connector directly called `terminal_view` and read:
- `A25 SHARED TERMINAL READY`
- `A25 VIEWPORT LIVE TEST 2026-10-17`
with `session: a25-gpt`, `read_only: true`, return code 0.

Therefore the GPT-side viewport was **RUNNING_VERIFIED at that moment**. This does not certify Claude-side reachability or future availability.

### 4. Current file-location inventory printed by Zed

**OBSERVED_HISTORICAL in this session.** Zed printed names/paths, not file contents, through the shared terminal. Observed:
- `~/a25-workshop/gpt/` with `backups/`, `config/`, `logs/`, `reports/`, `src/`, `tests/`.
- Workspace filenames included bridge backups, `src/bridge.py`, `src/auth.py`, `src/chatgpt_readonly.py`, a shared-space ZIP backup, and an A25 terminal-bridge experiment PDF.
- `~/pockettest`, `~/pockettest-c1`, `~/pockettest-shared` all existed on phone at the time of the listing.
- Main worktree listing showed `START_HERE.md`, `Claude/READ_ME_FIRST.md`, Gate-01/Gate-02 areas, protocol, Roundtable and shared-context files.
- Auth worktree listing visibly included `gate02/admin.py`, `auth_store.py`, `authorize_provider.py`, `client_registration.py`, `consent_views.py`, tests and server files.
- Shared worktree listing visibly included `shared/secure_files.py`, `shared/server.py`, `shared/storage.py`, tests and shared-context.
- `/storage/emulated/0/Documents/AI_Workshop/` contained `Checkpoints/`, `Project_Zips/`, and `Roundtable_Backups/`.
- Visible checkpoint names included case-study file-move/hash incident records, terminal bridge experiment, Pocket Server C3/master/checkpoint files, risky-paste card/risk log, shared viewport GPT/Claude checkpoint files, limited-viewport security checkpoint, and Shared Space Stage 1 checkpoint.
- Project ZIP observed: `pockettest-build-shared-space-v0.zip`.
- Roundtable backup observed: `gate01_roundtable_2026-10-10.jsonl`.

The listing also exposed filenames for sensitive config artifacts. Their **contents were not read for this report and are intentionally omitted**. Historical phone folder presence is not proof that each file is current, correct, or complete.

## Project inventory reconciliation

### Pocket Server hardened main vs Gate-01
Keep separate. Gate-01 is the earlier functional Roundtable proof. Hardened main is the Gate-02A deny-all/security baseline. Their goals and acceptance states differ. Current Git refs verify main commit; current phone listing verifies both directory families existed. No live Gate-02A endpoint test was performed in this recall.

### Auth branch
Distinct worktree/source line. Current phone listing confirms auth module filenames; GitHub ref confirms branch head. Functional completeness remains as recalled: partial until token/scopes/audit integration is proven. Recommended read-only follow-up: source/test review at pinned commit before any build.

### Shared Space Stage 1
Distinct branch and phone worktree. GitHub ref and local filenames align with recalled Stage 1. Do not infer Stage 2 identity work is present in Stage 1.

### Shared Space Stage 2 proposal
Distinct proposal ref. It remains separate from Stage 1. Remembered failing race test is RECALL, not rerun. Recommended read-only follow-up: inspect failing test/commit and historical CI/log evidence before acceptance.

### Terminal viewport / bridge
Distinct from Pocket Server command/auth services. Current GPT-side observation proves read-only viewport operation on 2026-10-17 during this session. It does not grant shell input. Public availability is a deliberate temporary test/build choice by Zed. Recommended follow-up: independent Claude `terminal_view` marker read, then preserve observation-vs-command separation.

### Other projects
Mechanics Toolbox, Build-by-Coin, APK reader, Market Stall Lab, Scrapline, node/Portal rooms, Godot projects, Neocities hub, Halfwake Pocket, RC Park, and APK mining are useful cross-project history recalled from prior context. They were **not source-verified in Phase B** because this recall was constrained to avoid turning remembered material into falsely verified claims and because their authoritative repositories/artifacts were not all established in the current source pass. They should remain separate provisional project records until a later read-only source pass resolves exact repos, branches, files, hashes, tests and dates.

## Failures, corrections and contradictions worth preserving

1. **Stage 2 identity proposal:** remembered near-green run still had one failure; near-green is not accepted.
2. **Market Stall/Android builds:** historical blank-screen/save-only and red/green cycles show that build success and functional success must be tracked separately.
3. **APK reader Test Room:** old 25x25 model was explicitly superseded by 9x9-cell View/Build architecture; do not merge them as one current design.
4. **Viewport identity/authority:** read-only visibility proved observation, not authentication or safe command authority.
5. **Tunnel/network evidence:** registered tunnel connections do not by themselves prove local origin/application health; layers must be reported separately.
6. **PDF/checkpoint integrity:** prior context contains multiple cases where generation-side hashes disagreed with phone hashes. Phone-side post-download/archive hashes were adopted as authoritative in that workflow. Filenames and assistant claims are not integrity proof.
7. **Evidence attribution:** Claude reviews, Zed screenshots/relays, GPT direct connector reads and GitHub source are different evidence classes. Do not flatten them.
8. **Public viewport privacy:** filename listings can reveal sensitive artifact names even without contents. Never print credential contents, private keys, tokens, secret paths, auth DB contents or personal files into the public pane.

## Tool capability / source freshness notes

- GitHub connector had read and create-file capability for the coordination repository in this session.
- A25 GPT Terminal connector had a read-only `terminal_view` capability and directly returned the shared tmux pane.
- No shell command was sent by GPT through the viewport.
- No live Pocket Server endpoint was tested as part of RN-001.
- No project source was edited. The only GitHub writes made for RN-001 are the required immutable reservation and this required new report.
- Current runtime facts are point-in-time only. Anything not directly checked is UNKNOWN rather than assumed.
- No credentials or secret values are included.

## Recommended read-only follow-ups for the lead

1. Treat this report as an index of candidate project records, not a claim that all remembered projects are verified.
2. For Pocket Server, reconcile pinned source, historical tests and current phone runtime as three separate layers.
3. For Mechanics Toolbox, verify Batch 6 commit/test evidence and locate any Batch 7 work without changing prior batches.
4. For Build-by-Coin/APK reader/Market Stall/Scrapline, identify authoritative repo/artifact locations before assigning completion states.
5. Preserve superseded designs and failed builds as separate timeline entries instead of overwriting them with the latest design.
6. Keep Zed/GPT/Claude seat attribution explicit in every cross-session artifact.

## Stop condition

RN-001 report delivered. No builds or modifications to existing projects were performed. Stop after reporting.
