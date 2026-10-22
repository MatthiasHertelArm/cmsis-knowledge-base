---
id: "iss-dbg-999"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Restarted debug session fails with 'PC register is not available' on Alif DevKit-E7"
summary: "The pyOCD GDB server appears to be forcefully terminated during disconnect before it finishes."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["error response to 'launch': PC register is not available"]
symptom_regex: "error\\s+response\\s+to\\s+'.*?':\\s+PC\\s+register\\s+is\\s+not\\s+available"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/999"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/999"
resolution: "workaround"
versions: "Debugger extension 1.6.1"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"], "board": ["Alif DevKit-E7"], "core": ["Cortex-M55"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error response to 'launch': PC register is not available`

## Cause

The pyOCD GDB server appears to be forcefully terminated during disconnect before it finishes. The thread suspects the CDT GDB Adapter's server disconnect timeout is too short on slower machines, and that some disconnect problem specific to this board may also be involved. The thread does not explain why the next launch fails with 'PC register is not available'.

## Fix

Increase serverDisconnectTimeout in the launch configuration's target section, for example to 3000 ms. This is the initial workaround; a managed-launch-configuration change to set a higher timeout is in progress (#1293). Using the manual RESET button or power-cycling the board restores debugging in the meantime.

## Source

Resolution: workaround

Versions: Debugger extension 1.6.1

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #999](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/999), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
