---
id: "iss-dbg-160"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Memory reads and views fail while the CPU runs (SIGINT interrupts)"
summary: "GDB suppresses remote commands while the target runs; non-stop mode did not work well with RTOS threads."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/160"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/160"
resolution: "fixed-in-release"
versions: "pyOCD 0.40.0 and CDT GDB Adapter 2.4.0 (tested)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

GDB suppresses remote commands while the target runs; non-stop mode did not work well with RTOS threads.

## Fix

Use pyOCD 0.40.0 with CDT GDB Adapter 2.4.0 or later: pyOCD's GDB server accepts several clients on one port (PR 1835), so an auxiliary GDB connection reads memory while the main connection keeps run control.

## Source

Resolution: fixed-in-release

Versions: pyOCD 0.40.0 and CDT GDB Adapter 2.4.0 (tested)

From [Open-CMSIS-Pack/vscode-cmsis-debugger #160](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/160), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
