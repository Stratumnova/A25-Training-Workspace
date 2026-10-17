# A25-NS-O002 — Synthetic Offline Prototype
STATUS: Experimental. No real registry, service authentication, migration or Watchdog integration.
Branch: build/a25-ns-o002-synthetic-prototype
Base commit: 51e018d5eb5e7abdab36b32ee17450a41456039f

## Run
Python 3 standard library only:
```sh
cd "project lead/archivist/namespace/prototype"
python3 -m unittest discover -v
```

## Usage
```python
from registry import Registry
r=Registry()
a=r.reserve("PS","TEST")
r.add(a,{"repo":"SYNTHETIC/fixtures","commit":"a"*40,"path":"fake/example"},"PUBLIC",alias="Gate-01")
print(r.search("Gate-01"))
```
Queries return only PUBLIC-safe ID/alias/context; UNKNOWN, REAL-PRIVATE and normal TEST-SENSITIVE retrieval are denied. All examples and fake tokens are SYNTHETIC.

## Limitations
Single writer, in-memory only. Sequential allocation is deterministic within an instance, not durable or globally unique across instances. No concurrency control, distributed allocation, authenticated principal validation, real cryptographic seat identity, disk persistence, external integrations, or automatic migrations. Caller-supplied `principal` is merely a synthetic test fixture: NEVER use this interface for real authorization. Ledger digests detect only certain conflicts; no durable tamper-evident chain. Source commit format is checked but repository existence and hashes are not externally verified. In-memory record revisions mutate latest state; no persisted immutable revision snapshots. Public search returns source context from PUBLIC fixtures only. Not production safe.
