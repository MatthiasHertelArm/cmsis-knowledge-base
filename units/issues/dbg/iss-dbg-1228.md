---
id: "iss-dbg-1228"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Cannot resume from a breakpoint in an RTOS thread when thread IDs are above 0x80000000"
summary: "With RTOS awareness enabled, thread IDs at or above 0x80000000 are valid positive 32-bit values."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1228"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1228"
resolution: "unresolved"
versions: "Affected GDB releases: 14.2, 15.2, 16.3, 17.1, 17.2. GDB 18.1 changes the encoding. The pyOCD release containing PR #2052 is not named in the thread."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With RTOS awareness enabled, thread IDs at or above 0x80000000 are valid positive 32-bit values. In the inspected source of GDB 14.2, 15.2, 16.3, 17.1 and 17.2, GDB sends such IDs to the GDB server as negative hexadecimal numbers, which appears to stop pyOCD from matching the selector to the thread, leaving execution stopped at the breakpoint.

## Fix

Use a pyOCD build that includes the fix from PR #2052. The reporter confirmed on an NXP IMXRT1050-EVK that execution resumes after a breakpoint in an RTOS thread with this fix. The thread does not name a pyOCD release that contains it.

## Source

Resolution: unresolved

Versions: Affected GDB releases: 14.2, 15.2, 16.3, 17.1, 17.2. GDB 18.1 changes the encoding. The pyOCD release containing PR #2052 is not named in the thread.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1228](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1228), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
