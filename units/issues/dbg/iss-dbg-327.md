---
id: "iss-dbg-327"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Target reset button disappears when a second core is attached"
summary: "The launch configuration of the second core had no customResetCommands."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/327"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/327"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The launch configuration of the second core had no customResetCommands.

## Fix

Use a CMSIS Solution release with the updated debug adapter templates, or add customResetCommands to the attach configuration.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #327](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/327), summarized in own words; confidence high, not reviewed yet.
