# A25 Phone Inventory — Evidence Request, Not a Phone Scan
DATE: 2026-10-17
STATUS: BLOCKED — CURRENT DEVICE FILESYSTEM NOT ACCESSIBLE
Observed interface tests: A25 GPT Terminal terminal_status and terminal_view failed internally; Pocket Gate server_status connection unavailable. Neither interface exposes recursive filesystem enumeration. No claim of current Android folder coverage is possible.

## Separate source lines
- Hardened Pocket Server / Gate-02A authentication and shared workspace.
- Gate-01 legacy Roundtable and Gate-02A separate test runtime.
- Lightweight terminal/viewport/bridge and owner-pasted Termux instructions.
- Owner-executed Downloads to Documents/AI_Workshop and other file copies.
- Zed's on-phone uncommitted worktrees, APKs, ZIPs, PDFs and checkpoints.

## Future read-only owner-controlled inventory
When Zed has approved a trusted phone-side export method, collect a **redacted** manifest: relative folder names under explicitly chosen safe roots, file types/counts, file sizes, timestamps, git worktree/branch/revision where applicable, and optionally SHA-256 for nonsecret project artifacts. Do not sweep whole phone, app-private directories, credentials, tunnel configs, tokens, personal Downloads or unrelated files into public GitHub. Review locally before publishing. Never infer current files from GitHub/Drive mirrors.

Current known historical paths are pointers only, not verified present: `~/a25-workshop/gpt`, `~/a25-data/shared-space`, Termux `pockettest-c1` and `pockettest-shared`, and `Documents/AI_Workshop/Checkpoints`.
