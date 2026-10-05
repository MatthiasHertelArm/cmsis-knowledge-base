---
id: "iss-dbg-819"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Component Viewer stays empty when one SCVD file is missing or invalid"
summary: "One unreadable SCVD (missing file, broken path in the cbuild-run file, syntax error) made the whole view fail instead of only that component."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/819"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/819"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

One unreadable SCVD (missing file, broken path in the cbuild-run file, syntax error) made the whole view fail instead of only that component.

## Fix

Use a CMSIS Debugger build in which unreadable SCVD files are skipped and the other components are shown (implemented; no release named). Check the SCVD files and their paths in the cbuild-run file if a component is missing.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #819](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/819), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
