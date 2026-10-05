---
id: "iss-dbg-109"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Warning \"invalid control node\" and then connect crash on multi-core Infineon T2G"
summary: "Old native pack sequence handling skipped a control node without if/while; and multi-core devices need a debug-topology in the cbuild-run file."
status: "draft"
tool: "pyocd"
symptoms: ["0001777 W invalid 'control' node in debug sequence 'PrintDeviceInfo' [cmsis_pack]", "0000954 C Error: <APv1Address@0x1a968104350 #1 dp=0> [__main__]"]
symptom_regex: "invalid\\s+'.*?'\\s+node\\s+in\\s+debug\\s+sequence\\s+'.*?'"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/109"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/109"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001777 W invalid 'control' node in debug sequence 'PrintDeviceInfo' [cmsis_pack]`
`0000954 C Error: <APv1Address@0x1a968104350 #1 dp=0> [__main__]`

## Cause

Old native pack sequence handling skipped a control node without if/while; and multi-core devices need a debug-topology in the cbuild-run file.

## Fix

Use pyOCD with cbuild-run debug sequences (0.0.3 pre-release and later) and a CMSIS-Toolbox 2.9+ cbuild-run file with debug-topology (debugports, accessports, processors).

## Source

Resolution: configuration

From [Open-CMSIS-Pack/vscode-cmsis-debugger #109](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/109), summarized in own words; confidence medium, not reviewed yet.
