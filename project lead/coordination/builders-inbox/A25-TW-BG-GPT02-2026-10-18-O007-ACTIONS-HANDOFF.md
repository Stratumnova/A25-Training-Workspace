# G2 → G1 — O007 separate Actions entry

Lead release read at f95a199aa8f648aff3c1dfa7ea989c8c41bd6c2d. G1 R006 source corrections at 57597e694ca98a33066ad8757b3454d629c3dbf8; tests NOT RUN per R006.

G2 added `shared/zone1_actions_entry.json`, `shared/ZONE1_ACTIONS_ENTRY.md`, and `shared/check_zone1_actions_contract.py` to **existing** `Stratumnova/pockettest` branch `build/shared-space-v0`, latest G2 source SHA `b264897199b23d2692ccb1b399f4c7fd03390672`. This is a separate **ChatGPT-side MCP connector configuration** referencing the existing GPT Pocket MCP endpoint; no new server/route and no changes to A25 GPT Terminal viewport.

Direct fetched-source assertions: six unique names in manifest, six `server.py` registrations, existing GPT mount, no-new-server/route flags and four command IDs all PASS. Python script and pytest NOT RUN; phone/tool discovery NOT TESTED.

G1: please run `python shared/check_zone1_actions_contract.py` and `python -m pytest -q shared/tests` in a suitable checkout/Termux when separately authorized; report results. Preserve exact six workspace signatures and existing viewport. Owner/Lead must install second ChatGPT MCP connector and authorize live update separately. Do not publish secret URL/path.
