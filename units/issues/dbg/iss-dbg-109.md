---
id: "iss-dbg-109"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Warning \"invalid control node\" and then connect crash on multi-core Infineon T2G"
summary: "pyOCD's native processing of pack debug sequences did not handle a control node without if or while and skipped it with a warning."
status: "draft"
tool: "pyocd"
symptoms: ["0001777 W invalid 'control' node in debug sequence 'PrintDeviceInfo' [cmsis_pack]", "0000954 C Error: <APv1Address@0x1a968104350 #1 dp=0> [__main__]"]
symptom_regex: "invalid\\s+'.*?'\\s+node\\s+in\\s+debug\\s+sequence\\s+'.*?'"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/109"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/109"
resolution: "configuration"
versions: "CMSIS Debugger v0.0.3 pre-release; Infineon T2G-B-E/T2G-B-H DFP 1.0.0; CMSIS-Toolbox 2.9.0 expected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001777 W invalid 'control' node in debug sequence 'PrintDeviceInfo' [cmsis_pack]`
`0000954 C Error: <APv1Address@0x1a968104350 #1 dp=0> [__main__]`

## Cause

pyOCD's native processing of pack debug sequences did not handle a control node without if or while and skipped it with a warning. With cbuild-run debug sequences, the multi-core device then failed because its debug topology was not described in the cbuild-run file.

## Fix

Use the pyOCD of the CMSIS Debugger v0.0.3 pre-release or later, which takes debug sequences from the cbuild-run file. For the multi-core device, describe debug ports, access ports and processors in the cbuild-run file: proper support was expected with CMSIS-Toolbox 2.9.0 and an updated extension, and meanwhile the reporter got it working by adding the preliminary 'debug:' section (debugports with apid and index per access port, processors with pname and apid) by hand.

## Source

Resolution: configuration

Versions: CMSIS Debugger v0.0.3 pre-release; Infineon T2G-B-E/T2G-B-H DFP 1.0.0; CMSIS-Toolbox 2.9.0 expected

From [Open-CMSIS-Pack/vscode-cmsis-debugger #109](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/109), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
