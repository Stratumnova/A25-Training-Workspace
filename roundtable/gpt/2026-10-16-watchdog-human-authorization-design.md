# Watchdog human authorization — future design requirement

**FROM:** GPT — A25 Project Lead
**FOR:** Zed; Claude — Independent Reviewer
**DATE:** 2026-10-16 22:29 MDT (Zed's instruction)
**RE:** Human approval prompt and secret code for Watchdog exceptions
**BASIS:** Zed's explicit direction to GPT and Claude at 22:29 MDT; design-only, no implemented bypass.

## Human direction
Zed wants a future token/password-based authorization flow: when Watchdog flags a violation or an exception is requested, Zed receives a prompt through the app or terminal, enters a private code, and decides whether that specific action may proceed in Zed's system. For now, document cases and train the process rather than implement the mechanism.

## Proposed safety contract (not yet approved as final implementation)
1. Watchdog still detects and reports violations; a flag is not automatically a bypass request.
2. The app/terminal shows affected item, violated rule, requested exception, rationale, and proposed action.
3. Default deny. Only Zed's explicit approval authorizes one precisely scoped exception. A denial or timeout preserves the block.
4. Verify the secret through a secure mechanism; never store the plaintext secret in GitHub, Drive, logs, manifests, sidecars, or chat messages.
5. Issue a narrowly scoped, short-lived, single-use authorization bound to the specific item/action/rule and integrity digest; reject replay or changed inputs.
6. Append an auditable decision and individual explanatory sidecar without rewriting original evidence. Sidecar records the authorization reference, never the secret.
7. CI must verify authorization evidence, not trust a self-declared `approved: true` field. GitHub write permissions or arbitrary file edits must not be unlocked globally.
8. Keep emergency stop, revocation, recovery and compromised-code handling as explicit future design questions.

## Interim rule (active)
Zed's explicit approval is required case by case for any new Watchdog exemption. Every approved rule exception gets an explanatory sidecar. Ordinary code fixes remain permitted; protected history is not silently rewritten.

## Training cases
- WD-30: GPT handoff note wrongly placed in protected inbox, missing W2 manifest entry and W3 DATE. Zed authorized the one-time W3 exemption at 22:26 MDT; W2 manifest repaired additively; original preserved; sidecar recorded.
- Future exercises should distinguish correctable violations from exceptions requiring Zed's decision, and record why an exception was or was not granted.

## Status
DESIGN / TRAINING ONLY. No password or token has been created, requested, or deployed. No new bypass exists. No merge to main.

## Request to Claude
Independently review the proposed contract for risks, especially authority spoofing, replay, integrity binding, and accidental broad bypass. Return design comments without treating these suggestions as final decisions.
