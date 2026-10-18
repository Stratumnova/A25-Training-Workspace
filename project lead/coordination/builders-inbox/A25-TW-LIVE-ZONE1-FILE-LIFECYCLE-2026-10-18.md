# A25 Workshop — live Termux Zone 1 direct-class lifecycle
Date: 2026-10-18 MDT. Evidence: owner commands directly observed using read-only A25 GPT Terminal terminal_view.
Source: isolated worktree at b264897199b23d2692ccb1b399f4c7fd03390672.
Root: ~/a25-workshop/gpt/tests/zone1-data, exported A25_ZONE1_ROOT in owner shell.
Used ~/pockettest/gate02/.venv/bin/python to instantiate zone1_workspace.Workspace and call write, read, inspect, command('pwd'), delete on disposable Shared/live-test.txt.
VERIFIED output:
READ: {'path': 'Shared/live-test.txt', 'content': 'Zone 1 live test'}
VIEW: {'path': 'Shared', 'entries': [{'name': 'live-test.txt', 'type': 'file'}]}
COMMAND: {'action': 'pwd', 'exit_code': 0, 'stdout': '/data/data/com.termux/files/home/a25-workshop/gpt/tests/zone1-data\n', 'stderr': ''}
FILE LIFECYCLE: PASS
This proves actual local class behavior on phone, NOT MCP connector tool discovery or cross-AI access. Existing viewport not modified. Next: determine existing shared service start configuration and stage live MCP without disturbing terminal bridge; backup and log before 22:00 MDT.
