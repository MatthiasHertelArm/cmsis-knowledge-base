---
id: "iss-dbg-685"
type: "troubleshooting"
domain: "debug"
title: "GDB: GDB warnings \"pc ... in read in CU, but not in symtab\" with Arm Compiler images"
summary: "GDB treats all addresses in a CU address table as code addresses, including const objects placed in code sections of AC6 images, then fails a cross-check; reading objects such as osRtxConfig triggers it."
status: "draft"
tool: "gdb"
symptoms: ["warning: (Internal error: pc 0x8020a6d8 in read in CU, but not in symtab.)", "warning: (Error: pc 0x8020a6d8 in address map, but not in symtab.)"]
symptom_regex: "\\(Internal\\s+error:\\s+pc\\s+\\S+\\s+in\\s+read\\s+in\\s+CU,\\s+but\\s+not\\s+in\\s+symtab\\.\\)"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/685"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/685"
resolution: "workaround"
versions: "AC6 .axf images"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["gdb"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning: (Internal error: pc 0x8020a6d8 in read in CU, but not in symtab.)`
`warning: (Error: pc 0x8020a6d8 in address map, but not in symtab.)`

## Cause

GDB treats all addresses in a CU address table as code addresses, including const objects placed in code sections of AC6 images, then fails a cross-check; reading objects such as osRtxConfig triggers it. The debug info itself looks fine.

## Fix

The warnings are harmless. CMSIS Debugger 1.3.0 filters this GDB output from the console; GDB CLI use outside VS Code still shows it.

## Source

Resolution: workaround

Versions: AC6 .axf images

From [Open-CMSIS-Pack/vscode-cmsis-debugger #685](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/685), summarized in own words; confidence medium, not reviewed yet.
