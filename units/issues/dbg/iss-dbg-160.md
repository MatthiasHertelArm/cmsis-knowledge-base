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
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

GDB suppresses remote commands while the target runs; non-stop mode did not work well with RTOS threads.

## Fix

Use pyOCD 0.40+ with CDT GDB Adapter 2.4.0+ which opens an auxiliary GDB connection to the same port (auxiliaryGdb); set auxiliaryGdb false where the server does not allow it.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #160](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/160), summarized in own words; confidence high, not reviewed yet.
