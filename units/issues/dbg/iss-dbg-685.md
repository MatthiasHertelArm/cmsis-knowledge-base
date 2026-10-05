---
id: "iss-dbg-685"
type: "troubleshooting"
domain: "debug"
title: "GDB: GDB warnings \"pc ... in read in CU, but not in symtab\" with Arm Compiler images"
summary: "The warnings come from GDB with AC6-built images and showed with RTOS views enabled."
status: "draft"
tool: "gdb"
symptoms: ["warning: (Internal error: pc 0x8020a6d8 in read in CU, but not in symtab.)", "warning: (Error: pc 0x8020a6d8 in address map, but not in symtab.)"]
symptom_regex: "\\(Internal\\s+error:\\s+pc\\s+\\S+\\s+in\\s+read\\s+in\\s+CU,\\s+but\\s+not\\s+in\\s+symtab\\.\\)"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/685"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/685"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["gdb"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning: (Internal error: pc 0x8020a6d8 in read in CU, but not in symtab.)`
`warning: (Error: pc 0x8020a6d8 in address map, but not in symtab.)`

## Cause

The warnings come from GDB with AC6-built images and showed with RTOS views enabled. A maintainer's tentative reading: the AC6 debug info looks sensible, but GDB treats every address in a CU's .debug_addr table as a code address, including const data placed in code sections, and a cross-check against the symbol table then fails.

## Fix

The warnings are harmless. Discarding them from the Debug Console through the CMSIS Debugger debug tracker was proposed and is addressed in PR #688 (no release named); GDB used from the command line outside VS Code still shows them.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #685](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/685), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
