---
id: "iss-dbg-347"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD does not show FreeRTOS threads (kernel awareness) with CMSIS-DAP"
summary: "The tool reports that the pxReadyTasksLists size is unexpected and may be an unsupported FreeRTOS version, so kernel/thread awareness does not show the running threads."
status: "draft"
tool: "pyocd"
symptoms: ["FreeRTOS: pxReadyTasksLists size is unexpected, maybe an unsupported version of FreeRTOS. Try using the --elf option."]
symptom_regex: "FreeRTOS:\\s+pxReadyTasksLists\\s+size\\s+is\\s+unexpected,\\s+maybe\\s+an\\s+unsupported\\s+version\\s+of\\s+FreeRTOS\\.\\s+Try\\s+using\\s+the\\s+\\-\\-elf\\s+option\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/347"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/347"
resolution: "unresolved"
versions: "CMSIS-FreeRTOS 11.3.0 (ARM::CMSIS-FreeRTOS@11.3.0)"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "component": ["CMSIS-FreeRTOS"], "pack": ["ARM::CMSIS-FreeRTOS"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`FreeRTOS: pxReadyTasksLists size is unexpected, maybe an unsupported version of FreeRTOS. Try using the --elf option.`

## Cause

The tool reports that the pxReadyTasksLists size is unexpected and may be an unsupported FreeRTOS version, so kernel/thread awareness does not show the running threads.

## Fix

The tool output suggests trying the --elf option; the thread does not confirm that this works. FreeRTOS kernel awareness support is expected soon after the 1.2.0 release.

## Source

Resolution: unresolved

Versions: CMSIS-FreeRTOS 11.3.0 (ARM::CMSIS-FreeRTOS@11.3.0)

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #347](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/347), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
