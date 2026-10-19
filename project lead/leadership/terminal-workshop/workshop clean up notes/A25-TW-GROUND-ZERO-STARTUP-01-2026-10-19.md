# A25 Ground Zero — Startup Ledger 01 — Minimum GPT Bootstrap

**Owner:** Zed
**Lead:** A25-TW-GPT01
**Ground Zero:** 2026-10-19 10:24 AM MDT, owner-sealed
**Record status:** PROPOSED COMMANDS; NOT YET EXECUTED OR VERIFIED
**Source:** Owner-provided `pockettest-main (2).zip`, Git archive header `f0a11d51968ad598691333d32971dfb483489073`, plus verified pre-shutdown process paths in the 2026-10-19 shutdown records.

## Goal
Restore minimum GPT terminal access from a fully stopped Termux, then audit every other service against real startup needs. The old Pocket Server repository is REFERENCE only under Ground Zero; its historical plans are not adopted automatically.

## Owner commands — execute in fresh Termux

```sh
cd ~/a25-workshop/gpt
tmux new-session -d -s a25-bridge '~/pockettest/gate02/.venv/bin/python -m src.chatgpt_readonly'
tmux new-session -d -s a25-tunnel 'cloudflared tunnel --config ~/a25-workshop/gpt/config/cloudflared.yml run'
tmux list-sessions
```

**Important:** Commands are a recovery hypothesis based on observed pre-shutdown module path, virtualenv and tunnel config. The exact cold-start invocation has not yet been tested. Do not assume tmux session existence proves working connectivity. Do not execute these if duplicate sessions already exist.

## Minimum startup order and checks

| Order | Component | Purpose | Evidence before boot | Status |
|---|---|---|---|---|
| 1 | `src.chatgpt_readonly` | GPT terminal tool bridge | pre-shutdown Python PID 30032, module source in `~/a25-workshop/gpt`, port 8770 | PENDING |
| 2 | `cloudflared` using `~/a25-workshop/gpt/config/cloudflared.yml` | Expose GPT bridge through existing configured tunnel | pre-shutdown cloudflared PID 30319, tunnel service configured to local port 8770 | PENDING |
| 3 | GPT tool `terminal_status` and controlled `terminal_send` + `terminal_view` | Verify command capability | previously worked pre-shutdown | PENDING |
| 4+ | Other services | Decide individually after live audit | unknown | NOT AUTHORIZED TO START YET |

## Old main snapshot triage

The uploaded `pockettest-main (2).zip` contains `gate01/server.py`, `gate02/server.py`, `gate02/listening_wall.py`, `protocol/POCKET_SERVER_V1.md`, and Roundtable/shared_context records. The `gate02/server.py` source labels itself a public deny-all OAuth skeleton, with `DenyAllProvider` and `ready: false` health route. Therefore **do not boot this historical Gate-02 skeleton as part of minimum GPT terminal recovery**. This is a source-code classification, not a proof that the phone's current Gate-02 code is identical. Gate-01 and shared files remain historical reference and require live dependency checks before disposition.

## Logging and archive rules

Record each actual command, terminal result, process/tmux identity, endpoint check, failures, dependencies, and used/unused classification in new append-only GitHub startup records alongside shutdown notes. Archive candidates are not automatically approved for deletion. Preserve credentials and secret routes; never publish them to GitHub.

## Next checkpoint

Owner performs minimum bootstrap and returns with `Check terminal`. Workshop Lead then verifies access and continues the boot ledger. If the connector is unreachable, owner provides bounded local Termux error output, excluding secrets. No success is claimed before testing.
