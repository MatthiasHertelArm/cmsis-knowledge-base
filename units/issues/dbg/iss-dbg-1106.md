---
id: "iss-dbg-1106"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd run halts unexpectedly after reset unless reset_type=sysresetreq is used"
summary: "The debug sequences always halt the device after reset, so a plain pyocd run right after reset can stop at an unexpected address."
status: "draft"
tool: "pyocd"
symptoms: ["0001631 W Target core 0 unexpectedly halted at pc=0x00001092"]
symptom_regex: "Target\\s+core\\s+\\S+\\s+unexpectedly\\s+halted\\s+at\\s+pc=\\S+"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1106"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1106"
resolution: "workaround"
versions: "pyOCD 1.10.0 (needed for the fix); the debug description spec change is required too. Not released at the time of the thread."
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

The debug sequences always halt the device after reset, so a plain pyocd run right after reset can stop at an unexpected address. The thread does not explain why the sysresetreq reset type avoids this; it only reports that it works on these boards.

## Fix

Workaround: run pyocd run with -O reset_type=sysresetreq for affected boards such as the Microchip PL10-CNANO (already in the modified CMSIS Run task) and the Infineon T2G-B-H. A complete fix needs the debug description spec update and pyOCD 1.10.0 support, then a DFP update; this is not yet released.

## Source

Resolution: workaround

Versions: pyOCD 1.10.0 (needed for the fix); the debug description spec change is required too. Not released at the time of the thread.

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1106](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1106), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
