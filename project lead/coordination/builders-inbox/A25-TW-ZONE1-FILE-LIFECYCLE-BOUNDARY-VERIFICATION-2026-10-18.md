# A25 Workshop — Zone 1 file lifecycle and boundary verification
Date: 2026-10-18
Reporter: A25-TW-GPT01
Evidence: read-only observation of owner-run Terminal 4 output via terminal_view(session="a25-test").

## VERIFIED (local test server, not production)
- GPT endpoint workspace_create Shared/a25-cross-ai-test.txt succeeded; Claude endpoint workspace_read returned exact expected content.
- Claude endpoint workspace_create Shared/a25-claude-to-gpt-test.txt succeeded; GPT endpoint workspace_read returned exact expected content.
- Both endpoints workspace_read rejected ../a25-outside-test.txt, /etc/passwd, and Shared/../../a25-outside-test.txt with isError=true and explicit path-boundary error.
- Both endpoints workspace_create rejected ../a25-write-boundary-test.txt and /tmp/a25-write-boundary-test.txt with isError=true and explicit path-boundary error.
- GPT workspace_create attempted on existing Shared/a25-cross-ai-test.txt returned isError=true; before/after read showed original content unchanged.
- GPT workspace_create Shared/a25-edit-lifecycle-test.txt returned success, GPT workspace_edit updated its content, Claude workspace_read returned exact updated content.
- Claude workspace_delete Shared/a25-edit-lifecycle-test.txt returned isError=false and ok=true; both GPT and Claude subsequent workspace_read calls returned isError=true.
- Tool schemas inspected: workspace_create/edit require path,content; delete requires path; workspace_command requires action and optional path default ".".

## Scope and limits
One local Python MCP client invoked both labeled routes on 127.0.0.1:8766; this does NOT verify independent GPT and Claude account connections, authenticated identities, remote connector behavior, persistence across restart, complete symlink/path hardening, concurrent-write safety, or workspace_command restrictions. Error response after delete did not explicitly say 'not found'; combined with successful delete supports expected absence but no independent filesystem inspection performed.

## Next justified actions
Review workspace_command action allowlist and implementation read-only before invoking it. Test remaining boundary and symlink cases with controlled disposable fixtures and plan a restart/recovery test. Preserve existing Gate-01 original data; no production deployment authorized.
