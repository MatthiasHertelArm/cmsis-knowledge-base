---
id: "iss-dbg-754"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: No \"Show in Memory Inspector\" entry in the Watch view"
summary: "The context menu entry needs VS Code 1.103 or newer, a Memory Inspector release that supports it, and a debug adapter that returns memory references for evaluated expressions."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/754"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/754"
resolution: "workaround"
versions: "Fixed by Memory Inspector 1.3.0; seen with Memory Inspector 1.2.0 and CMSIS Debugger 1.3.0"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The context menu entry needs VS Code 1.103 or newer, a Memory Inspector release that supports it, and a debug adapter that returns memory references for evaluated expressions. Support was missing in the Memory Inspector extension.

## Fix

Update the Memory Inspector extension to 1.3.0 or later; the entry then appears in the WATCH view. The variable name column in the Inspector still stays empty for such entries.

## Source

Resolution: workaround

Versions: Fixed by Memory Inspector 1.3.0; seen with Memory Inspector 1.2.0 and CMSIS Debugger 1.3.0

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #754](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/754), summarized in own words; confidence low, not reviewed yet.
