# A25 Ground Zero — Startup 02: Shell Control Verified

**Owner:** Zed
**Lead:** A25-TW-GPT01
**Date:** October 19, 2026
**Ground Zero:** October 19, 2026 at 10:24 AM MDT (owner sealed)
**Status:** VERIFIED live command-shell execution

## Test

Zed created a separate tmux session named `a25-gpt`. Workshop Lead sent a read-only command via GPT terminal_send to session `a25-gpt`, then independently inspected terminal_view. The screen showed the exact sentinel `A25_GROUND_ZERO_SHELL_PASS` and ending sentinel `A25_GROUND_ZERO_SHELL_END`, with executed output between them.

### Observed output
```text
A25_GROUND_ZERO_SHELL_PASS
/data/data/com.termux/files/home/a25-workshop/gpt
a25-bridge:python
a25-gpt:tmux
a25-tunnel:cloudflared
 6882  6881 /data/data/com.termux/files/home/pockettest/gate02/.venv/bin/python
 6965  6881 cloudflared
A25_GROUND_ZERO_SHELL_END
```

## Findings

- VERIFIED: actual command execution and return output in dedicated `a25-gpt` tmux shell.
- VERIFIED: `a25-bridge` is running Python PID 6882; `a25-tunnel` is running cloudflared PID 6965; `a25-gpt` is command shell.
- VERIFIED: only these three tmux sessions appeared in the check.
- NOT OBSERVED in the limited Python/cloudflared process scan: additional Gate-01/Gate-02/Claude processes. This is **not** proof that no other services exist or that these components are unneeded.
- Owner-sealed Ground Zero applies: prior Pocket Server plans are concepts/reference; only verified needed components advance to the operative plan.

## Next
Read-only inventory of current runtime, local files and dependencies against historical `Stratumnova/pockettest` reference. Record use/need/unused classification. No archive, deletion, service launch or code modification without appropriate authorization.

**Source:** live GPT terminal tool outputs in this conversation, October 19, 2026.
