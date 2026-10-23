---
id: "iss-dbg-1228"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Continue hangs in RTOS thread when RAM is at or above 0x80000000 (negative thread ID)"
summary: "GDB sends RTOS thread IDs at or above 0x80000000 as negative hexadecimal selectors (for example -7fffe280 for thread 80001d80) in vCont packets, which appears to stop the pyOCD GDB server from matching the selected thread, leaving execution stopped at …"
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1228"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1228"
resolution: "unresolved"
versions: "GDB releases 14.2, 15.2, 16.3, 17.1 and 17.2 send the negative encoding; GDB 18.1 does not. The thread names no pyOCD release; the board is IMXRT1050-EVK."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "board": ["IMXRT1050-EVK"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

GDB sends RTOS thread IDs at or above 0x80000000 as negative hexadecimal selectors (for example -7fffe280 for thread 80001d80) in vCont packets, which appears to stop the pyOCD GDB server from matching the selected thread, leaving execution stopped at the breakpoint.

## Fix

Use a pyOCD build that includes pull request #2052. The thread reports that, with this change, resume works after a breakpoint in an RTOS thread on an IMXRT1050-EVK board; the thread does not describe the mechanism or name a release containing it.

## Source

Resolution: unresolved

Versions: GDB releases 14.2, 15.2, 16.3, 17.1 and 17.2 send the negative encoding; GDB 18.1 does not. The thread names no pyOCD release; the board is IMXRT1050-EVK.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1228](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1228), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
