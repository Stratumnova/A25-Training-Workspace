# A25 Workshop — Multi-terminal viewport implementation and expansion

Date: 2026-10-18. Owner authorized bridge extension and requested durable project documentation plus visibility of Terminals 2 and 3.

## VERIFIED — working two-terminal bridge

- Existing source: `~/a25-workshop/gpt/src/chatgpt_readonly.py`, FastMCP read-only service on localhost 8770; Cloudflare tunnel existing. `terminal_view()` originally hardcoded `tmux capture-pane -t a25-gpt -p`.
- Terminal 1 tmux: `a25-gpt`; Terminal 4 tmux: `a25-test`. Both sessions confirmed by `tmux list-sessions` and user screenshots.
- Backup made at `~/a25-workshop/gpt/backups/chatgpt_readonly-pre-multiview.py`; original and backup SHA256 matched: `dbe028e77e96d3134a660013a63bd4d870977becd99bb742d03d83b6ef93c85b`.
- Candidate made at `~/a25-workshop/gpt/tests/chatgpt_multiview_candidate.py`, preserving no-argument default `a25-gpt`, adding optional `session: str = 'a25-gpt'`, allowlisting `a25-gpt` and `a25-test`, returning error for all other names. subprocess remains fixed `tmux capture-pane`, not command execution. `session` response uses selected session.
- Candidate passed syntax/static checks; first functional test harness erroneously used `.fn` and failed; corrected direct function invocation passed: both sessions return code 0, nonempty screen, read_only True; `not-allowed` return code 1 and empty screen.
- Candidate copied over `src/chatgpt_readonly.py`; py_compile passed, backup preserved. Existing bridge in Terminal 2 stopped via Ctrl+C and restarted with `cd ~/a25-workshop/gpt && ~/pockettest/gate02/.venv/bin/python -m src.chatgpt_readonly`.
- New bridge PID 28276 reported by startup logs; Uvicorn on 127.0.0.1:8770, session manager startup complete.
- ChatGPT independently called terminal_view default and terminal_view(session='a25-test') successfully after restart. **LIVE TWO-VIEWPORT PASS.** Existing Zone 1 test server on 127.0.0.1:8766 remained running.
- Existing Pydantic lifespan warning persists and was not resolved by this change. Cloudflare tunnel logs showed stream cancellations; live tool nevertheless worked.

## ADOPTED expansion request, not yet implemented

Owner wants Terminal 2 (bridge logs) and Terminal 3 (cloudflared logs) captured through the same existing bridge so GPT can inspect all four terminal text streams. Preserve Terminal 1 and Terminal 4 working viewports, running bridge and tunnel, no extra tunnel, no command execution. Need inspect whether Terminals 2/3 are currently attached to tmux, and migrate their running processes safely if not; never blindly wrap or restart them. Extend allowlist only after actual tmux sessions exist; verify separately and through live connector.

## Caveats

A tmux capture reads only visible pane/history, not all Android UI. Text captured may contain sensitive information (paths, logs, tokens); minimize output and keep access read-only. Implementation/adoption not equivalent to deployment verification. Do not claim Terminals 2/3 connected until independently tested.
