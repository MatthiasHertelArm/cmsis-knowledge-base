---
id: "iss-dbg-1106"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd run halts unexpectedly after reset unless reset_type=sysresetreq is used"
summary: "The device debug sequences always halt the CPU after a reset, so a plain pyocd run that resets the target stops the core even though the application is meant to run."
status: "draft"
tool: "pyocd"
symptoms: ["0001631 W Target core 0 unexpectedly halted at pc=0x00001092"]
symptom_regex: "Target\\s+core\\s+\\S+\\s+unexpectedly\\s+halted\\s+at\\s+pc=\\S+"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1106"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1106"
resolution: "workaround"
versions: "Open issue. The pyOCD provisions needed for the fix are expected in pyOCD 1.10.0, which is not yet confirmed as released in the thread."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001631 W Target core 0 unexpectedly halted at pc=0x00001092`

## Cause

The device debug sequences always halt the CPU after a reset, so a plain pyocd run that resets the target stops the core even though the application is meant to run. Normal debug sessions avoid this, but a manual run with some reset types does not. The debug description spec has no way to tell a sequence whether the reset should halt or continue running.

## Fix

Use the reset type that the workaround names: pass -O reset_type=sysresetreq to pyocd run on the affected boards. A permanent fix needs a debug sequence specification update and pyOCD 1.10.0 support, after which the device pack must be updated and validated.

## Source

Resolution: workaround

Versions: Open issue. The pyOCD provisions needed for the fix are expected in pyOCD 1.10.0, which is not yet confirmed as released in the thread.

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1106](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1106), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
