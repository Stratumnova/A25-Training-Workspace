# CASE-001 — Addendum 002: GitHub Actions UI observation
FROM: GPT — A25 Project Lead
FOR: Zed / LB-GPT01 / future Claude reviewer
DATE: 2026-10-17, Zed relay 13:20 MDT
RE: Owner UI inspection after O004 dispatch blocker
BASIS: Two screenshots supplied by Zed of A25-Training-Workspace Actions page
STATUS: UI OBSERVATION; CI UNVERIFIED

## What screenshots show
- GitHub Actions page in `Stratumnova/A25-Training-Workspace` displays one workflow in left sidebar: `A25 Watchdog draft tests`.
- Main pane shows 65 workflow runs, with many green statuses, on `build/wd-02-watchdog-v0`. Some older red entries also visible.
- No `A25 NS O004 pinned synthetic verification` workflow appears in visible sidebar.
- Green Watchdog checks are unrelated to namespace prototype execution and do not validate `build/a25-ns-o002-synthetic-prototype`.

## Interpretation
The branch-only `workflow_dispatch` YAML was committed at `e5c9754eeebd4d7474fc6adfe259f75385bf38a6`, but no workflow run is evidenced. Absence from this UI view is consistent with GitHub default-branch workflow registration constraints, but does not independently prove the cause. Do not merge or modify main merely to enable it.

## Decision and next test
Before requesting any protected change, explore a read-only execution path that obtains exact committed files through a connector or GitHub API and runs them with SHA-256 evidence in an executable environment. If not available, explicitly request Zed's permission for a narrow workflow registration path, separately from a main merge. Record run ID and completed job logs before green claims.

## Case study / lead continuity
O001 design delivered; O002 code delivered but committed-byte execution unverified; O003 DNS blocked; O004 workflow committed but dispatch unavailable; owner UI inspection shows only Watchdog workflow. Lead continues coordination and records blocker without mislabeling Watchdog greens as prototype verification.
