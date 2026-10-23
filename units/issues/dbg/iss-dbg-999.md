---
id: "iss-dbg-999"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Restart of debug session on Alif DevKit-E7 fails with 'PC register is not available'"
summary: "Suspected timing issue: pyOCD appears to be forcefully terminated by the GDB adapter before its disconnect completes, since the server disconnect timeout is short."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["error response to 'launch': PC register is not available"]
symptom_regex: "error\\s+response\\s+to\\s+'.*?':\\s+PC\\s+register\\s+is\\s+not\\s+available"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/999"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/999"
resolution: "workaround"
versions: "vscode-cmsis-debugger 1.6.1; AlifSemiconductor::Ensemble 2.2.2-dev28; no fixed version yet"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger", "pyocd"], "family": ["Alif Ensemble"], "board": ["Alif DevKit-E7"], "core": ["Cortex-M55"], "toolchain": ["AC6"], "pack": ["AlifSemiconductor::Ensemble"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error response to 'launch': PC register is not available`

## Cause

Suspected timing issue: pyOCD appears to be forcefully terminated by the GDB adapter before its disconnect completes, since the server disconnect timeout is short. Slow hosts seem more likely to hit this. Not confirmed; the stage of the disconnect that is missed is still under investigation.

## Fix

Increase serverDisconnectTimeout (for example to 3000 ms) in the launch configuration's target section as an initial workaround. Power-cycling the board restores debugging. A higher timeout in managed launch configurations is tracked separately.

## Source

Resolution: workaround

Versions: vscode-cmsis-debugger 1.6.1; AlifSemiconductor::Ensemble 2.2.2-dev28; no fixed version yet

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #999](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/999), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
