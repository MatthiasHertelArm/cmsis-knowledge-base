---
id: "iss-dbg-377"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Attach to a core without program image is refused"
summary: "The Disassembly view opens only for the selected core; opening it for a second, attached core from the CALL STACK context menu failed (a UX problem)."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/377"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/377"
resolution: "workaround"
versions: "CMSIS Debugger v0.40 (as written in the thread)"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Disassembly view opens only for the selected core; opening it for a second, attached core from the CALL STACK context menu failed (a UX problem).

## Fix

Select the second core in the CALL STACK view first, then open the Disassembly view; the multi-core debug section of the CMSIS Debugger README describes this.

## Source

Resolution: workaround

Versions: CMSIS Debugger v0.40 (as written in the thread)

From [Open-CMSIS-Pack/vscode-cmsis-debugger #377](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/377), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
