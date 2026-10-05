---
id: "iss-dbg-132"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Debug sequence fails with invalid __apid on Access Port v2 devices"
summary: "The AP address classes lacked apid handling for APv2."
status: "draft"
tool: "pyocd"
symptoms: ["E Error while running debug sequence 'ResetSystem' (core M55_HP): __apid has invalid value (2097152)"]
symptom_regex: "E\\s+Error\\s+while\\s+running\\s+debug\\s+sequence\\s+'.*?'\\s+\\(core\\s+M55_HP\\):\\s+__apid\\s+has\\s+invalid\\s+value\\s+\\(\\S+\\)"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/132"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/132"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["Alif E7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E Error while running debug sequence 'ResetSystem' (core M55_HP): __apid has invalid value (2097152)`

## Cause

The AP address classes lacked apid handling for APv2.

## Fix

Use a pyOCD whose AP address classes handle apid, first in the standalone build v0.0.0-standalone-cbuild3.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #132](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/132), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
