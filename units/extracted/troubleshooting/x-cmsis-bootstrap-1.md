---
id: "x-cmsis-bootstrap-1"
type: "troubleshooting"
domain: "project"
title: "No folder open or no solution loaded: NO_WORKSPACE and CMSIS_NO_SOLUTION"
status: "draft"
symptoms: ["Workspace: no folder is open", "[NO_WORKSPACE]", "[CMSIS_NO_SOLUTION]", "contains no *.csolution.yml", "A solution file exists"]
extracted_from: "proc-cmsis-bootstrap"
source: "cmsis-bootstrap/SKILL.md"
license: "Apache-2.0"
---

| Sign | State |
|---|---|
| `Workspace: no folder is open`, or `[NO_WORKSPACE]` from a tool | No project is open in the window |
| `[CMSIS_NO_SOLUTION]` with "contains no *.csolution.yml" | A folder without a solution |
| `[CMSIS_NO_SOLUTION]` with "A solution file exists" | The solution is not loaded |

A window needs some seconds after it opens. Call `get_session_status`. When `cmsis_action build` still answers `[CMSIS_NO_SOLUTION]` with "A solution file exists", wait ten seconds and try again, at most three times; then read `get_recent_problems` and report what the extension said.
