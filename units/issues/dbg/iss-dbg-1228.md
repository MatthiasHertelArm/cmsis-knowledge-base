---
id: "iss-dbg-1228"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD cannot resume after breakpoint when RTOS thread IDs are at or above 0x80000000"
summary: "GDB 14.2, 15.2, 16.3, 17.1 and 17.2 print thread IDs above 0x7fffffff as signed 32-bit integers and send them back in negative hexadecimal form. pyOCD then appears unable to match the selector to the RTOS thread, leaving the target …"
status: "draft"
tool: "pyocd"
symptoms: ["[New Thread -2147476096]"]
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1228"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1228"
resolution: "workaround"
versions: "Affected: GDB 14.2, 15.2, 16.3, 17.1, 17.2. Not affected: GDB 18.1. No pyOCD release is named; the fix is pyOCD PR 2052."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "board": ["IMXRT1050-EVK"], "core": ["Cortex-M7"], "component": ["RTOS awareness"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`[New Thread -2147476096]`

## Cause

GDB 14.2, 15.2, 16.3, 17.1 and 17.2 print thread IDs above 0x7fffffff as signed 32-bit integers and send them back in negative hexadecimal form. pyOCD then appears unable to match the selector to the RTOS thread, leaving the target stopped at the breakpoint. This occurs when RTOS RAM is at or above 0x80000000.

## Fix

Use a pyOCD build that includes pull request 2052; the reporter tested this change on the IMXRT1050-EVK and confirmed that Continue resumed. The thread suggests handling the negative selector by recovering the original positive 32-bit ID, keeping special selectors 0 and -1.

## Source

Resolution: workaround

Versions: Affected: GDB 14.2, 15.2, 16.3, 17.1, 17.2. Not affected: GDB 18.1. No pyOCD release is named; the fix is pyOCD PR 2052.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1228](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1228), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
