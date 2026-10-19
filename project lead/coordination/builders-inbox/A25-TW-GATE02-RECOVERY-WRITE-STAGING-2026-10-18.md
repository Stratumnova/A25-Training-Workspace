# A25 Workshop — Gate-02 terminal bridge recovery and write-tool staging
Date: 2026-10-18 (owner project date; later logs cross UTC midnight)
Author: A25-TW-GPT01 Workshop Lead
Status: VERIFIED observations plus IN-PROGRESS implementation; not a completion claim

## Purpose
Enable GPT terminal input on existing Gate-02 while retaining Gate-02 as terminal view/write and Gate-01 as Pocket Server / Zone 1 shared workspace with future security hardening assigned to leadership pool. Owner 18:44 directive prioritizes construction and assigns security issues to pool.

## Observed problems and evidence
1. GPT terminal_view(session='a25-test') returned returncode 1, 'can't find pane: a25-test'. This was not evidence that the entire bridge was down.
2. Termux screenshot showed tmux sessions a25-gpt, a25-bridge, a25-tunnel, but no a25-test. Owner recreated a25-test with tmux new-session.
3. After recreation, remote terminal_view(a25-test) returned returncode 0 but only a blank '~ $' prompt while owner commands executed in a separate Termux shell. Root cause of missing command output: physical Termux Terminal 4 was not attached to the a25-test tmux session. Owner ran tmux attach-session -t a25-test. Subsequent commands became visible remotely.
4. Attempt to start another src.chatgpt_readonly instance failed '[Errno 98] address already in use' on 127.0.0.1:8770. Screenshot ps output showed existing src.chatgpt_readonly process PID 32091. Do not claim duplicate bridge source failure; existing listener prevented second bind. Gate-02 bridge retained; no kill required.
5. Owner restarted cloudflared tunnel and posted logs showing four registered QUIC connections and successful connectivity prechecks. This is tunnel connectivity evidence, not proof of all end-to-end write functions.
6. Gate-01 Zone 1 Uvicorn PID 21440 on port 8766 remained separate and was not modified in this step.

## Recovery / source backup
- a25-test session recreated and attached; remote viewport read confirmed.
- Existing Gate-02 source backed up at ~/a25-workshop/gpt/backups/chatgpt_readonly-pre-write-20261018.py.
- Independent read-only remote viewport confirmed original source and backup identical SHA256 e85f2e4065c1d0ba6827f0d10f3429f89041069f9820fede4590422f26876519.
- Owner appended @mcp.tool() terminal_send(session, command) to ~/a25-workshop/gpt/src/chatgpt_readonly.py. Implementation uses tmux send-keys -l command then Enter, with named sessions a25-gpt, a25-test, a25-bridge, a25-tunnel.
- Remote viewport verified appended code and python -m py_compile src/chatgpt_readonly.py returned to shell without errors. Syntax PASS only.

## Crucial incomplete step
The new terminal_send definition was appended after the existing mcp.run block, so it is not registered during normal server startup. Source modification is staged only. No bridge restart, connector tool discovery, write invocation, or stop/interruption behavior has been verified. Need inspect exact line layout, relocate registration before mcp.run, syntax-check, controlled bridge restart, verify tool discovery and harmless test in a25-test. Owner chat stop capability remains UNKNOWN.

## Classification
ADOPTED: Gate-02 terminal view/write; Gate-01 shared workspace and later security track; owner prioritizes write bridge.
VERIFIED: tmux session recovery; viewport attachment fix; pre-write backup hash equality; staged appended function; py_compile no error; existing 8770 port conflict; tunnel connectivity logs.
UNKNOWN: running bridge registration, external connector tool visibility, terminal write success, reliable mid-run stop, Claude-side access.
Security observations are for leadership pool/security team, not treated as a completed review.
