---
id: "iss-dbg-93"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: LPC55S69 flash download via GDB fails with memory transfer fault"
summary: "Same root cause as the monitor reset halt failure: ResetSystem handling and missing multi-core topology."
status: "draft"
tool: "pyocd"
symptoms: ["0007677 E Error while running debug sequence 'ResetSystem' (core cm33_core0): Memory transfer fault [pack_target]"]
symptom_regex: "Error\\s+while\\s+running\\s+debug\\s+sequence\\s+'.*?'\\s+\\(core\\s+cm33_core0\\):\\s+Memory\\s+transfer\\s+fault"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/93"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/93"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0007677 E Error while running debug sequence 'ResetSystem' (core cm33_core0): Memory transfer fault [pack_target]`

## Cause

Same root cause as the monitor reset halt failure: ResetSystem handling and missing multi-core topology.

## Fix

Use CMSIS Debugger 0.2+ pyOCD and ensure the cbuild-run debug-topology lists both APs.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #93](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/93), summarized in own words; confidence high, not reviewed yet.
