---
id: "iss-dbg-567"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Generated J-Link launch configuration on macOS uses JLinkGDBServerCLExe"
summary: "The debug adapter template used the Windows-style CLExe name, which is not the stable binary on macOS."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/567"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/567"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The debug adapter template used the Windows-style CLExe name, which is not the stable binary on macOS.

## Fix

Use a CMSIS Solution release with the updated debug adapter registry (template now uses JLinkGDBServerCL), or edit the server name in launch.json.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #567](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/567), summarized in own words; confidence medium, not reviewed yet.
