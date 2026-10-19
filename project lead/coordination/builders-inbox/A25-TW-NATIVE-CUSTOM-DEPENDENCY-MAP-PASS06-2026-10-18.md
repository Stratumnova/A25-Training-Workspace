# A25 Workshop — Native vs Custom Dependency Map Pass 06
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Security, Archives
STATUS: VERIFIED read-only inspection
Owner approved use of a25-test after safety block. No phone files, services or settings modified.

## Tool provenance — verified PATH only
Under /data/data/com.termux/files/usr/bin: python, git, tmux, cloudflared, curl, ssh, am, pm, getprop, termux-info.
Interpretation: tools available within Termux environment; not proof which package installed them or who installed them. am, pm, getprop expose Android commands, not custom A25 components.

## Custom source files — verified filenames
Workshop ~/a25-workshop/gpt/src: bridge.py, auth.py, chatgpt_readonly.py.
Gate-01 ~/pockettest/gate01: server.py, test_gate.py, README.md, requirements.txt, roundtable.jsonl, roundtable.backup.jsonl.
Gate-02 ~/pockettest/gate02: server.py, listening_wall.py, observations.jsonl, requirements.lock.txt.
Shared Space ~/pockettest-shared/shared: server.py, storage.py, secure_files.py, pytest.ini.
README headings in Gate-01: Install, Configure, Run, Rules implemented, Tunnel note, Acceptance. Roundtable README and recovery index also exist.

## Evidence categories
VERIFIED: file existence, command paths, earlier live process/session inventory.
HISTORICAL CLAIM: README/checkpoint statements remain reference, not proof of running behavior.
UNKNOWN: which source versions are loaded by live processes, how files are connected, actual ledger recovery status, source-vs-deployment parity, origin of installed binaries.
ADOPTED: map only; no building, repair, install, restart, cleanup, movement, or active probing.

## Outstanding boundary
Complete TCP listening-port enumeration remains blocked because ss is not installed and netstat lacks requested AF_INET support. No alternative attempted. Owner has not approved alternate route.

## Next mapping-only scope
Read existing nonsecret module imports and README architecture descriptions, compare to process evidence. Preserve discrepancies and do not reconcile by assumption.
