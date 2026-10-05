---
id: "iss-dbg-890"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Run control becomes unresponsive while Component Viewer is open on a multi-core target"
summary: "Requests that the Component Viewer sent to GDB could leave the CDT GDB Adapter or GDB unresponsive while running and stepping; Reset Target did not always recover."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/890"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/890"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Requests that the Component Viewer sent to GDB could leave the CDT GDB Adapter or GDB unresponsive while running and stepping; Reset Target did not always recover.

## Fix

Update to CMSIS Debugger 1.4.1 or later, which contains the fix (#888); error messages may still appear occasionally, but run control no longer hangs as easily.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #890](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/890), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
