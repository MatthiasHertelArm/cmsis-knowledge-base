---
id: "iss-dbg-286"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Leftover pyOCD process blocks later sessions with \"Access denied\""
summary: "After a failed launch (for example missing GDB) the adapter left the pyOCD server running."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/286"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/286"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

After a failed launch (for example missing GDB) the adapter left the pyOCD server running.

## Fix

Update CDT GDB Adapter to 2.1.0 or later; as a workaround end the pyocd process.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #286](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/286), summarized in own words; confidence high, checked against the thread, not reviewed yet.
