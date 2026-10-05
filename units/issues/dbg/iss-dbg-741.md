---
id: "iss-dbg-741"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd gdb accepts only one client connection; dual-core semihosting output missing"
summary: "Without --persist pyOCD ends its GDB server after the first client disconnects, so a second attach fails."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/741"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/741"
resolution: "user-error"
versions: "CMSIS Debugger 1.3.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Without --persist pyOCD ends its GDB server after the first client disconnects, so a second attach fails. Semihosting for the second core only worked while both cores were attached, a known pyOCD limitation tracked separately.

## Fix

Add --persist when starting pyocd gdbserver, or use the generated CMSIS Run task which passes the required options. Attach both cores for semihosting output.

## Source

Resolution: user-error

Versions: CMSIS Debugger 1.3.0

From [Open-CMSIS-Pack/vscode-cmsis-debugger #741](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/741), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
