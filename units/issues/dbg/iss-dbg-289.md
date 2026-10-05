---
id: "iss-dbg-289"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd erase says \"unrecognized arguments: --cbuild-run\""
summary: "A pyOCD without cbuild-run support was used, not the one shipped with the CMSIS Debugger extension."
status: "draft"
tool: "pyocd"
symptoms: ["pyocd: error: unrecognized arguments: --cbuild-run"]
symptom_regex: "pyocd:\\s+error:\\s+unrecognized\\s+arguments:\\s+\\-\\-cbuild\\-run"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/289"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/289"
resolution: "user-error"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pyocd: error: unrecognized arguments: --cbuild-run`

## Cause

A pyOCD without cbuild-run support was used, not the one shipped with the CMSIS Debugger extension.

## Fix

Use the pyOCD of the CMSIS Debugger extension (launch server "pyocd") and CMSIS Solution tasks that match it.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/vscode-cmsis-debugger #289](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/289), summarized in own words; confidence low, not reviewed yet.
