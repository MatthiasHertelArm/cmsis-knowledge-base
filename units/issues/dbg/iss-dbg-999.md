---
id: "iss-dbg-999"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Restarted debug session on Alif DevKit-E7 fails with PC register not available"
summary: "The thread suggests a timing issue: the debug adapter's disconnect timeout may expire before pyOCD finishes its disconnect sequence, so pyOCD is forcefully terminated."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["error response to 'launch': PC register is not available"]
symptom_regex: "error\\s+response\\s+to\\s+'.*?':\\s+PC\\s+register\\s+is\\s+not\\s+available"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/999"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/999"
resolution: "workaround"
versions: "vscode-cmsis-debugger 1.6.1"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"], "board": ["Alif DevKit-E7"], "core": ["Cortex-M55"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error response to 'launch': PC register is not available`

## Cause

The thread suggests a timing issue: the debug adapter's disconnect timeout may expire before pyOCD finishes its disconnect sequence, so pyOCD is forcefully terminated. The reporter found this reproducible on a slowed-down machine with a lowered timeout, and noted it may also involve genuine disconnect trouble with this board. The root cause is not confirmed.

## Fix

Workaround: raise serverDisconnectTimeout in the launch configuration (3000 ms in the example given). Pressing the board RESET button or power-cycling the board restores debugging. A higher timeout for managed launch configurations is tracked in #1293.

## Source

Resolution: workaround

Versions: vscode-cmsis-debugger 1.6.1

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #999](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/999), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
