---
id: "iss-dbg-93"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: LPC55S69 flash download via GDB fails with memory transfer fault"
summary: "The flash download over GDB failed in the ResetSystem debug sequence run after loading; the maintainers linked it to the reset sequence problem of issue #92."
status: "draft"
tool: "pyocd"
symptoms: ["0007677 E Error while running debug sequence 'ResetSystem' (core cm33_core0): Memory transfer fault [pack_target]"]
symptom_regex: "Error\\s+while\\s+running\\s+debug\\s+sequence\\s+'.*?'\\s+\\(core\\s+cm33_core0\\):\\s+Memory\\s+transfer\\s+fault"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/93"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/93"
resolution: "unresolved"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0007677 E Error while running debug sequence 'ResetSystem' (core cm33_core0): Memory transfer fault [pack_target]`

## Cause

The flash download over GDB failed in the ResetSystem debug sequence run after loading; the maintainers linked it to the reset sequence problem of issue #92.

## Fix

Follow the resolution of issue #92 on the ResetSystem sequence; this thread only links to it.

## Source

Resolution: unresolved

From [Open-CMSIS-Pack/vscode-cmsis-debugger #93](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/93), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
