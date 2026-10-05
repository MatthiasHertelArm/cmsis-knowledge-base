---
id: "iss-dbg-472"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd load with a missing cbuild-run file continues with a generic target and crashes"
summary: "The cbuild-run file path was wrong, the access error was only logged, and pyOCD went on with a generic Cortex-M target."
status: "draft"
tool: "pyocd"
symptoms: ["0000927 C Error: 'CoreSightTarget' object has no attribute 'debugger_clock' [__main__]", "0000883 W Generic 'cortex_m' target type is selected by default; is this intentional? You will be able to debug most devices, but not program flash."]
symptom_regex: "Error:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/472"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/472"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000927 C Error: 'CoreSightTarget' object has no attribute 'debugger_clock' [__main__]`
`0000883 W Generic 'cortex_m' target type is selected by default; is this intentional? You will be able to debug most devices, but not program flash.`

## Cause

The cbuild-run file path was wrong, the access error was only logged, and pyOCD went on with a generic Cortex-M target.

## Fix

Check the path of the --cbuild-run file. From pyOCD 0.39.0 the missing file ends the command instead.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #472](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/472), summarized in own words; confidence high, checked against the thread, not reviewed yet.
