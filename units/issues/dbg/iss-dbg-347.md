---
id: "iss-dbg-347"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD FreeRTOS thread awareness shows no threads; pxReadyTasksLists size warning"
summary: "pyOCD FreeRTOS kernel and thread awareness does not work for the CMSIS-FreeRTOS 11.3.0 project; the GDB server reports that pxReadyTasksLists size is unexpected and may be an unsupported FreeRTOS version."
status: "draft"
tool: "pyocd"
symptoms: ["FreeRTOS: pxReadyTasksLists size is unexpected, maybe an unsupported version of FreeRTOS. Try using the --elf option."]
symptom_regex: "FreeRTOS:\\s+pxReadyTasksLists\\s+size\\s+is\\s+unexpected,\\s+maybe\\s+an\\s+unsupported\\s+version\\s+of\\s+FreeRTOS\\.\\s+Try\\s+using\\s+the\\s+\\-\\-elf\\s+option\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/347"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/347"
resolution: "unresolved"
versions: "CMSIS-FreeRTOS 11.3.0 (ARM::CMSIS-FreeRTOS@11.3.0); FreeRTOS support expected soon after the 1.2.0 release"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "component": ["CMSIS-FreeRTOS"], "pack": ["ARM::CMSIS-FreeRTOS@11.3.0"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`FreeRTOS: pxReadyTasksLists size is unexpected, maybe an unsupported version of FreeRTOS. Try using the --elf option.`

## Cause

pyOCD FreeRTOS kernel and thread awareness does not work for the CMSIS-FreeRTOS 11.3.0 project; the GDB server reports that pxReadyTasksLists size is unexpected and may be an unsupported FreeRTOS version. The warning appears after the application has started and does not affect application execution.

## Fix

The thread gives no confirmed fix.

## Source

Resolution: unresolved

Versions: CMSIS-FreeRTOS 11.3.0 (ARM::CMSIS-FreeRTOS@11.3.0); FreeRTOS support expected soon after the 1.2.0 release

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #347](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/347), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
