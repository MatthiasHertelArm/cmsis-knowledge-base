---
id: "iss-dbg-567"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Generated J-Link launch configuration on macOS uses JLinkGDBServerCLExe"
summary: "The debug adapter template generated the server name JLinkGDBServerCLExe on macOS, whereas JLinkGDBServerCL is more stable there; Load & Run was affected as well."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/567"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/567"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The debug adapter template generated the server name JLinkGDBServerCLExe on macOS, whereas JLinkGDBServerCL is more stable there; Load & Run was affected as well.

## Fix

Use a CMSIS Solution build with the updated debug adapter registry (PR 45, merged; validated with an internal build from main, no release named), or change the server name in launch.json to JLinkGDBServerCL.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #567](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/567), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
