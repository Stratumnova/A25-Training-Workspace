# A25-AV-R001 — Termux Snapshot Forensic Inventory

FROM: A25-AB-GPT01 — Archives Builder  
TO: A25-AG-GPT01 — Archives Lead; Zed  
DATE: 2026-10-18  
ORDER: [A25-AV-O001](https://github.com/Stratumnova/A25-Training-Workspace/blob/d7e7aa052d35dc67cc67f9a2cb8a0afc94a4e024/project%20lead/coordination/orders/A25-AV-O001-GPT01-TERMUX-SNAPSHOT-FORENSIC-INVENTORY.md)  
STATUS: **OFFLINE ZIP INVENTORY VERIFIED; LIVE TERMUX PARITY UNKNOWN**

## Method and source custody

**VERIFIED:** Inspected the exact user-uploaded `AI workshop on zeds local system. copy on termx side..zip` in place via Python `zipfile` and `hashlib.sha256`; each regular member decompressed with CRC validation; complete archive member metadata sorted by original path below. No bundled Python code or tests were executed. JSONL parsed as data, PDFs text-extracted from in-memory ZIP bytes. Sizes are bytes, CRC32 is 8-digit hexadecimal, SHA-256 is lowercase 64-digit hex. ZIP archive entries may have untrusted paths; none were extracted to the device. Directory entries have no content SHA-256. Successful CRC checks do not prove origin or phone parity.

**Main ZIP:** 1,682,513 bytes; SHA-256 `59fd2e47d1a79cc0ead68f9493c0da92920e956ec5fc58209da65ac87b7fbe43`; 19 entries = 15 regular files and 4 directories; **0 read/CRC errors**.

**Nested ZIP** `AI_Workshop/Project_Zips/pockettest-build-shared-space-v0.zip`: 29,206 bytes; SHA-256 `94506d0f1980d52e8d2986ab910598cc142dfabb7cbf674110f6aeec70e909c6`; 40 entries = 27 regular files and 13 directories; **0 read/CRC errors**.

**Second uploaded ZIP:** 29,206 bytes, same SHA-256; **VERIFIED byte-for-byte identical to the nested member**, independently compared as complete byte sequences. This confirms the two supplied copies, not a GitHub or phone match.

## Main archive complete sorted manifest

| Archive path | Type | Compressed bytes | Raw bytes | CRC32 | SHA-256 |
|---|---|---:|---:|---|---|
| `AI_Workshop/` | dir | 2 | 0 | `00000000` | `—` |
| `AI_Workshop/Checkpoints/` | dir | 2 | 0 | `00000000` | `—` |
| `AI_Workshop/Checkpoints/A25_Case_Study_File_Move_Manifest_2026-10-12.md` | file | 703 | 1451 | `90f54728` | `b6b0d0c60b119e3c7bbcc4ea7859c044ec4ec18bc00fa9f2a596c3d8cfef02a2` |
| `AI_Workshop/Checkpoints/A25_Case_Study_Terminal_Viewport_Hash_Incident_2026-10-12.md` | file | 3562 | 9003 | `9c258457` | `720ee1b1110f7e269944974d5cdca48bd5a1a000c9d22c11e9a38e046e00624a` |
| `AI_Workshop/Checkpoints/A25_Case_Study_Terminal_Viewport_Hash_Incident_2026-10-12.pdf` | file | 15001 | 30315 | `860b98ff` | `7732c95261344ca0a1cf83611dcf96eae3daae48535d8e75786bf05afdd8823a` |
| `AI_Workshop/Checkpoints/A25_GPT_Inside_Out_Terminal_Bridge_Experiment_2026-10-11.pdf` | file | 15816 | 31101 | `2d0dedf6` | `2e2bfabd37318bce06417b0fa2560044630987aacfe6f6f5f6478f405ce61b9d` |
| `AI_Workshop/Checkpoints/A25_Pocket_Server_C3_Checkpoint_2026-10-10.pdf` | file | 55753 | 75024 | `9541b125` | `6fe57c3899cce3a6f3a47018c7b3539981c48a0b00aec11e9e7fc64e371d8ad8` |
| `AI_Workshop/Checkpoints/A25_Pocket_Server_Checkpoint_4_GPT_2026-10-11.pdf` | file | 54672 | 73333 | `47c34790` | `1fb0d899e11b51d5966b29abf90ff6388bd6848da9ad020c82ca44db96079cff` |
| `AI_Workshop/Checkpoints/A25_Pocket_Server_Master_Checkpoint_2026-10-10.pdf` | file | 15952 | 31221 | `052f5d26` | `72437b3d1390e8d31b15aadee7775aae851b5364b7e505b9085212a9f2d8f4b0` |
| `AI_Workshop/Checkpoints/A25_Risky_Paste_Card_and_Risk_Log_2026-10-12.pdf` | file | 3020 | 4212 | `d7e55f95` | `b899cd5e1677707e16dd61d7d62837fc4e9263bbc78af3a6416058f687ae9b4b` |
| `AI_Workshop/Checkpoints/A25_Shared_Viewport_Proof_Addendum_v3_2026-10-12.pdf` | file | 732772 | 945605 | `291e4423` | `11f99d47bdc1a72f0d7dcbf98c561192174c6a1e2c24b6d379a7be0b4dc5b6a8` |
| `AI_Workshop/Checkpoints/A25_Shared_Viewport_Proof_Claude_Checkpoint_2026-10-12.pdf` | file | 722537 | 921311 | `e0a2868b` | `122cbb59343303723c6c3da6e14724ceba99425a8c0462f380dc7ec79cdaea47` |
| `AI_Workshop/Checkpoints/A25_Workshop_Limited_Viewport_Security_Checkpoint_2026-10-12.pdf` | file | 16833 | 32537 | `8c3d669c` | `c53150f8c1107b47c5d19b4ab2cf5fc49136904da66d7865b167b9b42e55bf45` |
| `AI_Workshop/Checkpoints/Pocket_Server_Checkpoint_3_C1-C3_2026-10-10.pdf` | file | 8900 | 12406 | `1041f868` | `89e444b30f2e25cf8e3be229c706adda8d20ed721b2ecaebc6c5d932a23f8c75` |
| `AI_Workshop/Checkpoints/Pocket_Server_Checkpoint_4_SharedSpace_Stage1_2026-10-11.pdf` | file | 10150 | 13930 | `e5903b53` | `3ba5d35dbaf100457568c8c947966eebd9eae25637230af94c4e3f116e881c96` |
| `AI_Workshop/Project_Zips/` | dir | 2 | 0 | `00000000` | `—` |
| `AI_Workshop/Project_Zips/pockettest-build-shared-space-v0.zip` | file | 22395 | 29206 | `cf77ef5a` | `94506d0f1980d52e8d2986ab910598cc142dfabb7cbf674110f6aeec70e909c6` |
| `AI_Workshop/Roundtable_Backups/` | dir | 2 | 0 | `00000000` | `—` |
| `AI_Workshop/Roundtable_Backups/gate01_roundtable_2026-10-10.jsonl` | file | 205 | 441 | `f20c62b6` | `61812be83cbc3be8715fb4798b4a1d098e79ba3b6a2935aac29f35e1f39a52b9` |

## Gate-01 backup examination

**VERIFIED:** `AI_Workshop/Roundtable_Backups/gate01_roundtable_2026-10-10.jsonl` has 441 bytes, three nonempty physical lines, three parsed JSON objects and **zero JSON parse errors**. No raw message bodies are reproduced.

| Line | Event ID | Author field | Timestamp field (UTC) | cursor_through | References |
|---:|---:|---|---|---:|---:|
| 1 | 1 | `claude` | `2026-10-08T03:19:27.430718+00:00` | 0 | 0 |
| 2 | 2 | `gpt` | `2026-10-08T04:52:11.969227+00:00` | 1 | 0 |
| 3 | 3 | `claude` | `2026-10-08T05:02:21.407772+00:00` | 2 | 0 |

**VERIFIED as backup contents only:** IDs 1–3 ordered, author fields Claude/GPT/Claude, cursors 0/1/2. **UNKNOWN:** actual live ledger persistence, caller identity enforcement, whether event 3 appeared unseen to GPT, and whether any restart succeeded. Event 3's timestamp must not be called the recovery timestamp.

## Nested Shared Space ZIP complete sorted manifest

| Archive path | Type | Compressed bytes | Raw bytes | CRC32 | SHA-256 |
|---|---|---:|---:|---|---|
| `pockettest-build-shared-space-v0/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/.github/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/.github/workflows/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/.github/workflows/build` | file | 559 | 1271 | `2718c8c4` | `739a8e240a1f4c402516cf1e46c0f9f4802eb3362f320d36bf45c3dc38f74afe` |
| `pockettest-build-shared-space-v0/START_HERE.md` | file | 637 | 1187 | `ec5b5565` | `3345fb0c1b87fc331a7fe5286b8eccc611aa722af06623c62785f935fb413354` |
| `pockettest-build-shared-space-v0/claude/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/claude/READ_ME_FIRST.md` | file | 354 | 542 | `a17236cd` | `b46ee4221ea85302e0173a48190a0392d2f3f8e22a8e25f4d663d0b86ee35ed6` |
| `pockettest-build-shared-space-v0/docs/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/docs/README.md` | file | 1583 | 3004 | `1136de7f` | `61de109c70ba48694e332f32d124f77456b017e655019bcd366f48182f3cdd7b` |
| `pockettest-build-shared-space-v0/gate01/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/gate01/README.md` | file | 1251 | 2363 | `284c9ed5` | `e708cbd5e997a7643a1716104455b760307f6dc42c6563dfd0972a30ca71f8ad` |
| `pockettest-build-shared-space-v0/gate01/requirements.txt` | file | 28 | 28 | `23a25139` | `5ee720a4599a476b2405a6ff2e8e69e27e7aae4e38b906932406ee349410c4b5` |
| `pockettest-build-shared-space-v0/gate01/server.py` | file | 1937 | 4760 | `ef50b1d1` | `e45e80167da0116b4b7d88437fcdbaa4f2a6e0fd09e3ef133770acb0ad0cb34a` |
| `pockettest-build-shared-space-v0/gate01/test_gate.py` | file | 684 | 2091 | `29d5f807` | `c0545cc6aa2130c8f2a61a0df67b3ab929b435bcc3f2ec80d1bd5225a5235786` |
| `pockettest-build-shared-space-v0/gate02/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/gate02/.gitignore` | file | 27 | 40 | `019af8a3` | `12ab08854456ebd9cf81b3cc8900bac82968894c158df783e2ac2299dfb39d4c` |
| `pockettest-build-shared-space-v0/gate02/listening_wall.py` | file | 1686 | 4747 | `2c7e8b00` | `36bd36da8275b559b19ceb914e9585b56b25667a36d77763b2e258c494a33f3c` |
| `pockettest-build-shared-space-v0/gate02/requirements.lock.txt` | file | 312 | 536 | `398c2243` | `03ff6f9cc2d49136018d5057a1e1fa9e3d2200e042d63fbc95f201214d63b73d` |
| `pockettest-build-shared-space-v0/gate02/server.py` | file | 1139 | 3128 | `c2c6873d` | `1f15eb8ca749407af01ab68302d645c96f20ab16ca9864fd8a7254081cbac518` |
| `pockettest-build-shared-space-v0/gpt/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/gpt/NOTES.md` | file | 194 | 274 | `7880d7c9` | `829dea1f70704fca961681a1e4fbc80a8325f13251b1b492332dea3931ece381` |
| `pockettest-build-shared-space-v0/protocol/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/protocol/POCKET_SERVER_V1.md` | file | 1455 | 3168 | `67489c4a` | `ff63c3a468d6d09cfca8b2385edbcffe065673dbf05e0aecf6de360904ecb004` |
| `pockettest-build-shared-space-v0/roundtable/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/roundtable/README.md` | file | 246 | 381 | `85307064` | `6c1757cfd0061358f1d8fb60785d40575fa88f2f469fbf746074fa70b421aa8f` |
| `pockettest-build-shared-space-v0/shared/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/shared/.gitignore` | file | 59 | 60 | `9ee4ad1a` | `4a965886f984610e26cd4679212580c3c3660f945136a3a05964e509e5c31724` |
| `pockettest-build-shared-space-v0/shared/pytest.ini` | file | 35 | 42 | `053ac84f` | `6c6ccf864e8f2d2e0223ee8e39bfde660c12435aa37d81e2b14000a6bee15003` |
| `pockettest-build-shared-space-v0/shared/secure_files.py` | file | 493 | 2129 | `20d99812` | `3afe9a0b92e098039c7201bf963097acafbd9dc19da00550d4ed2e77b0285bf6` |
| `pockettest-build-shared-space-v0/shared/server.py` | file | 2371 | 6425 | `f46b2cdc` | `cc1dbd7116beb9281d249dec40cf07ca77a04cc25317ff79d8d3d74973d6b514` |
| `pockettest-build-shared-space-v0/shared/storage.py` | file | 600 | 1494 | `b7be3331` | `29b3fe009f4c26e61b08af46a3a3a17451ac3f973aac3b2975c81cc06cff8454` |
| `pockettest-build-shared-space-v0/shared/tests/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/shared/tests/test_roundtable.py` | file | 684 | 2091 | `29d5f807` | `c0545cc6aa2130c8f2a61a0df67b3ab929b435bcc3f2ec80d1bd5225a5235786` |
| `pockettest-build-shared-space-v0/shared/tests/test_secure_files.py` | file | 1037 | 5348 | `13afdf4c` | `5d5b438d3e32e3205bec1cb2ef4ea70c90f01fead76e7a78adf015b7f7b18076` |
| `pockettest-build-shared-space-v0/shared/tests/test_storage.py` | file | 644 | 2329 | `524f49ed` | `7e90f2e3f4d7c1615d20bbae7a3058b5a994128636db531e09bc36200a891a56` |
| `pockettest-build-shared-space-v0/shared/tests/test_storage_guards.py` | file | 1648 | 8868 | `c17db745` | `f42ab1fe3e3d71164bff48d5bfe7b00ba07def03774c8f1b7cc07c16c17d11ab` |
| `pockettest-build-shared-space-v0/shared_context/` | dir | 0 | 0 | `00000000` | `—` |
| `pockettest-build-shared-space-v0/shared_context/CURRENT_STATE.md` | file | 914 | 1774 | `99e1343d` | `63ebb1f829202a94926fae0780a27183f86d98026bba94ba0773ad036a2d1884` |
| `pockettest-build-shared-space-v0/shared_context/DECISIONS.md` | file | 460 | 844 | `f76027a6` | `ed09ce1ff5216f9ec63df0d3794af5cffd21c090234a56d568486ca5d0e6e21e` |
| `pockettest-build-shared-space-v0/shared_context/OPEN_ISSUES.md` | file | 295 | 498 | `d9ca607e` | `81490a0f9718016b6061696804643b96c58a486ebe836fb8411d38724ffde1af` |

## Checkpoint document inspection

All 11 PDF files were readable by `pypdf` text extraction. Extracted pages and text-character counts are evidence of **document readability**, not proof that historical claims were true:

| PDF checkpoint filename | Pages | Extracted characters |
|---|---:|---:|
| `A25_Pocket_Server_C3_Checkpoint_2026-10-10.pdf` | 4 | 9,332 |
| `Pocket_Server_Checkpoint_3_C1-C3_2026-10-10.pdf` | 4 | 9,662 |
| `Pocket_Server_Checkpoint_4_SharedSpace_Stage1_2026-10-11.pdf` | 4 | 10,837 |
| `A25_Pocket_Server_Master_Checkpoint_2026-10-10.pdf` | 2 | 5,399 |
| `A25_Pocket_Server_Checkpoint_4_GPT_2026-10-11.pdf` | 3 | 6,952 |
| `A25_GPT_Inside_Out_Terminal_Bridge_Experiment_2026-10-11.pdf` | 2 | 4,850 |
| `A25_Case_Study_Terminal_Viewport_Hash_Incident_2026-10-12.pdf` | 2 | 3,948 |
| `A25_Shared_Viewport_Proof_Addendum_v3_2026-10-12.pdf` | 4 | 3,213 |
| `A25_Shared_Viewport_Proof_Claude_Checkpoint_2026-10-12.pdf` | 3 | 4,561 |
| `A25_Workshop_Limited_Viewport_Security_Checkpoint_2026-10-12.pdf` | 3 | 5,870 |
| `A25_Risky_Paste_Card_and_Risk_Log_2026-10-12.pdf` | 1 | 2,406 |

**HISTORICAL CLAIM:** The Oct 12 viewport case-study Markdown describes GPT reading a live tmux pane through a read-only FastMCP and Cloudflare bridge; it also reports an unauthenticated public viewport exposure and a previously incorrect GPT SHA-256. These statements are reference evidence, not fresh live network or phone verification. **HISTORICAL CLAIM:** C1–C3 and Shared Space Stage 1 checkpoint PDFs report commits and test counts; neither checkpoint publication nor the existence of bundled test files establishes that tests passed in this session. **ADOPTED (historical checkpoint wording):** Gate 0 security lockdown before further viewport expansion; implementation and current enforcement are **UNKNOWN**.

**VERIFIED discrepancy:** `A25_Case_Study_File_Move_Manifest_2026-10-12.md` names an Android SHA-256 `78c87be286e6f84b4cc98647c8bdb01478a2b48117c09085f6070a0ea1f7d219` for `A25_GPT_Terminal_Read_Viewport_Checkpoint_2026-10-12_v2.pdf`, but that PDF is **not present** among the 19 main archive members. The checksum therefore cannot be independently confirmed from these uploads. The manifest also describes future placement/hash verification rather than certifying all files moved.

## Source-version and security limits

**VERIFIED:** The nested ZIP includes `gate01/`, `gate02/`, `shared/`, `shared_context/`, test files and a workflow. No `.git/` history or authoritative commit metadata is included. `pockettest-build-shared-space-v0` is an archive label, not a verified commit ID. **UNKNOWN:** whether all its decompressed files are byte-identical to pinned GitHub Shared Space Stage 1 commit `9a419e925dff2de64ef948b7d6d8304eccf8387d`; a full raw-file-by-raw-file GitHub comparison was not performed. Do not promote narrative checkpoints into byte-level source parity.

**Sensitive-content handling:** No message bodies, route secrets, passwords, tokens, private keys or unredacted source code are published. Archive path names were screened for sensitive-key/credential indicators; absence of suspicious names does **not** prove all PDF/Markdown/source text secret-free. No complete semantic secret scan or credential validation was performed. Report includes only file metadata and minimal event fields. Historic security warnings remain reference, not claims of current exposure.

## Verification matrix and remaining work

| Evidence question | Classification | Exact boundary |
|---|---|---|
| Main ZIP readability, member CRC and file SHA-256 | **VERIFIED** | Offline bytes and complete manifest |
| Nested ZIP readability and hashes | **VERIFIED** | Offline bytes and complete manifest |
| Independently uploaded ZIP equals nested copy | **VERIFIED** | Full-byte comparison plus same SHA-256 |
| Three-event Gate-01 JSONL backup | **VERIFIED** | Static data only |
| Checkpoint text describes historic builds/tests | **HISTORICAL CLAIM** | Documents inspected; tests not rerun |
| Checkpoint v2 Android hash parity | **UNKNOWN** | Named PDF absent from supplied ZIP |
| Nested Shared Space vs pinned GitHub commit | **UNKNOWN** | Requires independent GitHub raw-byte comparison |
| Snapshot is 1:1 copy of current Termux | **UNKNOWN** | Requires owner-approved phone-side sorted manifest |
| Live Gate-01 recovery, Stage 1 integration and caller identities | **UNKNOWN** | No live service/SDK checks authorized |
| Current viewport exposure/security lockdown | **UNKNOWN** | Historical documents only |

**Next justified work, separately authorized only:** Owner obtains a timestamped phone-side sorted path/size/SHA-256 inventory without altering files; independently compare nested files against exact pinned GitHub raw blobs and full tree; recover original Gate-01 runtime envelopes where available; Archives Lead adjudicates discrepancies. No unapproved execution, server, tunnel, phone, CI or Drive changes.

**STOP:** Only this new report is published. No existing GitHub files, ZIP bytes, branches, CI, phone, server, tunnel, Drive or permissions modified.
