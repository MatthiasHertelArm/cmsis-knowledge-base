---
id: "iss-dbg-799"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Component Viewer shows current instead of maximum stack with OS_STACK_WATERMARK"
summary: "The numeric conversion of the string returned by GDB for the values was wrong, so current and maximum came out identical on some devices (seen with the RTX library on Microchip and ST hardware)."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/799"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/799"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The numeric conversion of the string returned by GDB for the values was wrong, so current and maximum came out identical on some devices (seen with the RTX library on Microchip and ST hardware).

## Fix

Use a CMSIS Debugger build containing PR 854 (merged and confirmed working with a CI build; no release named).

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #799](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/799), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
