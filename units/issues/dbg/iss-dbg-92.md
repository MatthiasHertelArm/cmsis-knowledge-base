---
id: "iss-dbg-92"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: monitor reset halt fails on LPC55S69 with CMSIS-Pack debug support"
summary: "Handling of __errorcontrol and __ap in sequences was wrong; two APs must be declared."
status: "draft"
tool: "pyocd"
symptoms: ["0007776 E Error while running debug sequence 'ResetSystem' (core cm33_core0): Memory transfer fault [pack_target]"]
symptom_regex: "Error\\s+while\\s+running\\s+debug\\s+sequence\\s+'.*?'\\s+\\(core\\s+cm33_core0\\):\\s+Memory\\s+transfer\\s+fault"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/92"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/92"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0007776 E Error while running debug sequence 'ResetSystem' (core cm33_core0): Memory transfer fault [pack_target]`

## Cause

Handling of __errorcontrol and __ap in sequences was wrong; two APs must be declared.

## Fix

Use pyOCD with the fix and give two accessports (apid 0 index 0, apid 1 index 1) with cm33_core0/cm33_core1.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #92](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/92), summarized in own words; confidence high, not reviewed yet.
