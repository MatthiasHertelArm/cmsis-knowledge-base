---
id: "iss-dbg-1106"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Manual pyOCD run halts unexpectedly after reset unless reset_type=sysresetreq is used"
summary: "Debug sequences currently always halt the device after a reset, even when the user only wants the application to run."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["0001631 W Target core 0 unexpectedly halted at pc=0x00001092"]
symptom_regex: "Target\\s+core\\s+\\S+\\s+unexpectedly\\s+halted\\s+at\\s+pc=\\S+"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1106"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1106"
resolution: "workaround"
versions: "pyOCD 1.10.0 (expected; not yet released at the time of the thread)"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001631 W Target core 0 unexpectedly halted at pc=0x00001092`

## Cause

Debug sequences currently always halt the device after a reset, even when the user only wants the application to run. For some boards, a manual pyOCD run with the default or other reset methods can stop at an unexpected address, while reset_type=sysresetreq avoids the problem. A debug sequences specification update allowing the reset to be told whether the CPU should halt or keep running may be needed.

## Fix

For affected boards, run pyOCD with -O reset_type=sysresetreq as a workaround. The proper fix needs a debug description spec update (Open-CMSIS-Pack-Spec PR 419) and pyOCD support expected in 1.10.0; the thread notes this only helps after release.

## Source

Resolution: workaround

Versions: pyOCD 1.10.0 (expected; not yet released at the time of the thread)

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1106](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1106), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
