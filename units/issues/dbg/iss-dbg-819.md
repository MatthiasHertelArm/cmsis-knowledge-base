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
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

One unreadable SCVD (missing file, broken path in the cbuild-run file, syntax error) made the whole view fail instead of only that component.

## Fix

Update CMSIS Debugger; unreadable SCVD files are now skipped and the others are shown. Check the SCVD paths in the cbuild-run file if a component is missing.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #819](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/819), summarized in own words; confidence medium, not reviewed yet.
