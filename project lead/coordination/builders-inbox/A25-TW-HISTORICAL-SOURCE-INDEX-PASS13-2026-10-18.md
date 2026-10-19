# A25 Workshop — Historical Source Index Pass 13
Date: 2026-10-18
FROM: A25-TW-GPT01
FOR: Zed, Project Lead, Security, Archives
STATUS: VERIFIED bounded read-only filename inventory

## Zone 1 source worktree
In ~/a25-workshop/gpt/tests/zone1-source/shared:
- check_zone1_actions_contract.py
- secure_files.py
- server.py
- storage.py
- zone1_workspace.py
- tests/test_roundtable.py
- tests/test_secure_files.py
- tests/test_storage.py
- tests/test_storage_guards.py
- tests/test_zone1_workspace.py
These are source/test filenames, not evidence of live deployment or successful tests.

## Original Pocket Server historical documents
- ~/pockettest/gpt/NOTES.md
- ~/pockettest/claude/READ_ME_FIRST.md
- ~/pockettest/protocol/POCKET_SERVER_V1.md
- ~/pockettest/shared_context/CURRENT_STATE.md
- ~/pockettest/shared_context/DECISIONS.md
- ~/pockettest/shared_context/OPEN_ISSUES.md
Contents not yet inspected.

## Bounded negative
No .md files returned under ~/a25-workshop/gpt/reports at maxdepth 2. This does not establish absence elsewhere.

## Status
VERIFIED: filename existence in stated scope.
UNKNOWN: file contents, historical plugin inventory, live Zone 1 installation and test results.
OWNER-REPORTED: multiple early GPT/Claude plugins; emulator and Documents/Local AI workshop PDFs.
ADOPTED: mapping only, phone read-only, stop on blocks.

## Next
Read selected historical Markdown files, filtering out secrets/private data, to map design evolution and plugin/viewport references. Do not run tests or inspect credentials.
