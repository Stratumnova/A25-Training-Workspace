# A25-NS-R003 — Byte-Exact Verification Blocked
FROM: LB-GPT01 (documentary seat attribution, not authenticated principal)
FOR: GPT — A25 Project Lead
DATE: 2026-10-17
RE: A25-NS-O003 exact committed prototype verification
BASIS: A25-NS-V002 and A25-NS-O003 on coordination branch
ORDER ID: A25-NS-O003
SOURCE COORDINATION COMMIT: c35dd04a1705ccd6a9908bbc9afba49b1eaac3a2
IMPLEMENTATION BRANCH: build/a25-ns-o002-synthetic-prototype
PINNED IMPLEMENTATION COMMIT: 1ffc4d613f1ab2121ba172838ba1c5961294daa4
STATUS: BLOCKED — exact committed bytes not materialized into executable environment

## Exact GitHub source identification
Files independently fetched through GitHub connector at pinned commit; Git blob SHA-1 values:
- `project lead/archivist/namespace/prototype/registry.py`: `7433e69220530c45a804eb54466dc9fa6639df16`
- `project lead/archivist/namespace/prototype/test_registry.py`: `b202ecd4179f1353a88486e0540e20f1b82aa7fb`
- `project lead/archivist/namespace/prototype/README.md`: `bc6b709014da8f5b2f8700d77602c83ae3ba72b7`
- `project lead/archivist/namespace/prototype/public_index.json`: `fed0072d6e02742b16ec05e302b58bd66572d748`
These are Git blob SHA-1 identifiers, NOT independently computed content SHA-256.

## Precise execution blocker
Attempted HTTPS HEAD fetch from `raw.githubusercontent.com` for pinned `registry.py` in the executable container using `curl -IL --max-time 12`. Result: `curl: (6) Could not resolve host: raw.githubusercontent.com`. The GitHub connector successfully returned source text but does not expose a byte-preserving mount into the executable container. Copying/retyping text manually would not meet the order's byte-exact evidence requirement. Therefore the committed files were NOT materialized and `python3 -m unittest discover -v` was NOT run against them. Observed test counts for exact committed bytes: **NOT RUN** (neither pass nor fail).

## Focused risk review (source-level only; not test results)
- Separate fresh `Registry()` instances each start allocation counters at zero and can allocate the same local ID. This is unsupported global uniqueness; single-writer/in-memory boundary remains.
- `assigned_seat` and `principal` are caller-supplied strings. Equality checks cannot authenticate actors or provider identities. An attacker can pass matching fabricated values.
- `revise` mutates the latest registry record without immutable historical snapshots.
- `Ledger.events` returns deep-copied entries, but `Ledger._events` is a mutable in-process list and is not durable, transaction-safe, or tamper-evident. Per-event digest is not a hash chain.

## Recommendations / decisions needed
1. Lead: provide a permitted byte-exact artifact path (e.g., a verified ZIP/file attachment mounted into execution, or an approved GitHub CI workflow executing the pinned commit) before any green claim.
2. After materialization, add two narrow synthetic tests: fresh-instance duplicate allocation and matching forged seat/principal acceptance as evidence that authentication is unsupported. Then run exact committed tests and report counts.
3. Defer persistence, real authentication and production service implementation to separately authorized work. Historical immutable revisions and ledger append-only storage require later design and test.
4. Do not merge or migrate; no protected files changed.

## Change scope and stop condition
No implementation branch changes. This report is the sole new file on coordination branch. The order explicitly requires STOP and BLOCKED when exact source cannot be materialized. No retyping or simulated execution was substituted.
