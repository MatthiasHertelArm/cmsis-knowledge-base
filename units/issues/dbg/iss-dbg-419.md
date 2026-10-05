---
id: "iss-dbg-419"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: How to get Event Recorder output without a graphical viewer in VS Code"
summary: "The CMSIS Debugger extension has no graphical Event Recorder view yet."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/419"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/419"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger", "cmsis-view"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CMSIS Debugger extension has no graphical Event Recorder view yet.

## Fix

Select the component variant CMSIS-View:Event Recorder with Semihosting and build for semihosting; run the application with the debugger attached, which writes EventRecorder.log into the project directory. Decode that log with the eventlist utility from the CMSIS-View tools (shipped with the CMSIS-Toolbox).

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #419](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/419), summarized in own words; confidence medium, not reviewed yet.
