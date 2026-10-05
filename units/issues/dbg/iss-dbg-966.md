---
id: "iss-dbg-966"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: GDB Python pretty printers fail: bundled arm-none-eabi-gdb has no Python support"
summary: "The GDB used by the extension is the non-Python build of the Arm GNU Toolchain GDB."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["printer.py:1: Error in sourced command file:", "Undefined command: \"\".  Try \"help\"."]
symptom_regex: "printer\\.py:\\S+:\\s+Error\\s+in\\s+sourced\\s+command\\s+file:"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/966"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/966"
resolution: "workaround"
versions: "CMSIS Debugger 1.4.1, Arm GNU Toolchain GDB"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-debugger", "gdb"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`printer.py:1: Error in sourced command file:`
`Undefined command: "".  Try "help".`

## Cause

The GDB used by the extension is the non-Python build of the Arm GNU Toolchain GDB. Sourcing a .py file therefore fails. The Python-enabled sibling arm-none-eabi-gdb-py needs a separately installed Python 3.8; without it the executable silently exits (a missing python38.dll on Windows) and the gdbserver is killed.

## Fix

Install Python 3.8 and set "gdb": "arm-none-eabi-gdb-py" in the launch configuration. Copying a Python 3.8 embeddable package next to the GDB executable also worked for one user. The maintainers only test the non-Python build and planned a troubleshooting note.

## Source

Resolution: workaround

Versions: CMSIS Debugger 1.4.1, Arm GNU Toolchain GDB

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #966](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/966), summarized in own words; confidence high, checked against the thread, not reviewed yet.
