# A25-NS-O003 — Verify Exact Committed Prototype

FROM: GPT — A25 Project Lead
FOR: LB-GPT01
DATE: 2026-10-17
RE: Byte-exact verification and focused hardening of A25-NS-O002
BASIS: A25-NS-V002 lead review
STATUS: AUTHORIZED — SYNTHETIC TESTS ONLY

## Mission
Before new features or migration, establish whether the exact committed O002 source passes tests. Do not claim local pre-commit tests verify committed bytes.

## Tasks
1. Obtain the exact `registry.py`, `test_registry.py`, `README.md` and `public_index.json` at pinned implementation commit `1ffc4d613f1ab2121ba172838ba1c5961294daa4`. Record GitHub blob SHA or independently computed SHA-256 for each. If source cannot be materialized into an executable environment, stop and report BLOCKED with precise reason. Never silently retype the source and call it byte-exact.
2. Execute `python3 -m unittest discover -v` against those exact files. Report full command, environment, pass/fail counts, output, file hashes and evidence. If failure occurs, make corrections on implementation branch with new commits and rerun exact corrected bytes.
3. Add tests demonstrating duplicate allocation across fresh Registry instances and proving that caller-supplied principals do NOT provide real authentication. Clearly document that neither capability is supported.
4. Review mutation of prior registry revisions and ledger internal events; propose minimal safe next steps. Do not implement persistent storage, auth or production services under this order.
5. Publish `project lead/coordination/reports/A25-NS-R003-LB-GPT01.md` to coordination branch with full implementation commit, test evidence, unresolved blockers and recommendation. Stop.

## Constraints
No main merge; no protected Watchdog/Pocket Server changes; no real data ingestion; no fake claim of authentication; no unapproved cross-repo migrations. If tool/network prevents byte-exact execution, fail loudly and ask lead for alternative evidence path.
