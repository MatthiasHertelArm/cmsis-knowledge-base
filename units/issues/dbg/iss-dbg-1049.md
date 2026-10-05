---
id: "iss-dbg-1049"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Mark Active Source Lines switches itself off after every debug session"
summary: "The CDT GDB Adapter extension wrote cdt.debug.sourceHighlighting=false to the persisted settings when a GDB session ended."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1049"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1049"
resolution: "fixed-in-release"
versions: "CDT GDB Adapter 2.9.0 affected, fixed in 2.9.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CDT GDB Adapter extension wrote cdt.debug.sourceHighlighting=false to the persisted settings when a GDB session ended.

## Fix

Update the CDT GDB Adapter extension (eclipse-cdt.cdt-gdb-vscode) to 2.9.1 or later. As a stopgap, re-enable the highlighting through the editor context menu, which sets the setting again.

## Source

Resolution: fixed-in-release

Versions: CDT GDB Adapter 2.9.0 affected, fixed in 2.9.1

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1049](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1049), summarized in own words; confidence high, not reviewed yet.
