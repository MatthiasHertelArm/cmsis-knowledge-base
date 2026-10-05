---
id: "iss-dbg-1001"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Live Watch, Component Viewer, Core Peripherals stale after variable or memory write"
summary: "The views did not react to the DAP events (invalidated, memory) that the adapter sends when memory changes through variable edits or GDB set commands, so only the built-in Watch refreshed."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1001"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1001"
resolution: "fixed-in-release"
versions: "fixed with CDT GDB Adapter 2.9.0 and CMSIS Debugger 1.7.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The views did not react to the DAP events (invalidated, memory) that the adapter sends when memory changes through variable edits or GDB set commands, so only the built-in Watch refreshed.

## Fix

Use CDT GDB Adapter 2.9.0 together with CMSIS Debugger 1.7.1 or later.

## Source

Resolution: fixed-in-release

Versions: fixed with CDT GDB Adapter 2.9.0 and CMSIS Debugger 1.7.1

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1001](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1001), summarized in own words; confidence high, checked against the thread, not reviewed yet.
