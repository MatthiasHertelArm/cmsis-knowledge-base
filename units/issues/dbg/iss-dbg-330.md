---
id: "iss-dbg-330"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Peripheral view does not update during single stepping"
summary: "The debug-tracker-vscode extension (dependency of RTOS Views) clashed with the Peripheral Inspector, which could not tell session IDs apart."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/330"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/330"
resolution: "fixed-in-release"
versions: "fixed in Peripheral Inspector 1.8.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The debug-tracker-vscode extension (dependency of RTOS Views) clashed with the Peripheral Inspector, which could not tell session IDs apart.

## Fix

Update Peripheral Inspector to 1.8.1 or later; disabling mcu-debug.debug-tracker-vscode also helps.

## Source

Resolution: fixed-in-release

Versions: fixed in Peripheral Inspector 1.8.1

From [Open-CMSIS-Pack/vscode-cmsis-debugger #330](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/330), summarized in own words; confidence high, checked against the thread, not reviewed yet.
