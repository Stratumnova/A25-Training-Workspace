# A25 Workshop — live Termux source tests
Date: 2026-10-18 MDT. Evidence: directly observed A25 GPT Terminal terminal_view (read-only) after owner ran commands.

VERIFIED:
- Baseline ~/pockettest main f0a11d51968ad598691333d32971dfb483489073 was clean, left unchanged.
- Backup pockettest-pre-zone1-20261018.tar.gz size 37M, SHA256 b6cebc1f6473a80c6a239eda4b56f34f39d78aa618d24ca5cc76a4a42a99814c, tar -tzf exit 0.
- Fetched origin/build/shared-space-v0 and detached worktree at b264897199b23d2692ccb1b399f4c7fd03390672 under ~/a25-workshop/gpt/tests/zone1-source.
- System Python 3.14.6 lacks pytest; existing ~/pockettest/gate02/.venv/bin/python has pytest 8.4.2.
- Existing venv ran tests/test_zone1_workspace.py: 3 passed in 0.06s, exit 0; repeat 3 passed in 0.05s, exit 0.
- Existing venv ran check_zone1_actions_contract.py: SOURCE CONTRACT PASS six workspace tools registered on existing GPT MCP route; first exit 0; repeated PASS, final repeated exit code not visible in viewport.
UNKNOWN: Live Pocket Server deployment, live MCP tool discovery, actual file operations via connector, cross-seat Claude test.
NEXT: check full shared test suite and isolated disposable class test; then plan owner-controlled deployment and second Actions connector without disturbing original viewport.
Owner deadline: finish and back up before ~22:00 MDT.
