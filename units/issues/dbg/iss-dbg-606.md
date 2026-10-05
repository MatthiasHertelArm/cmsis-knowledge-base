---
id: "iss-dbg-606"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: XRTOS view shows \"No RTOS detected\" or no threads for RTX5 while the application runs"
summary: "The RTOS view reads RTOS data only while the target is halted and after osKernelStart."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/606"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/606"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The RTOS view reads RTOS data only while the target is halted and after osKernelStart.

## Fix

Pause the target after the kernel started; the threads then show.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/vscode-cmsis-debugger #606](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/606), summarized in own words; confidence high, checked against the thread, not reviewed yet.
