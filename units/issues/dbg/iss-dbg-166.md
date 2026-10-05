---
id: "iss-dbg-166"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: monitor reset leaves GUI out of sync; use monitor reset halt"
summary: "pyOCD monitor commands change the CPU state without GDB async records, so the GUI does not learn about running or stopped."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/166"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/166"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD monitor commands change the CPU state without GDB async records, so the GUI does not learn about running or stopped.

## Fix

Use "monitor reset halt" and the adapter reset button (resetDeviceCommands/customResetCommands such as monitor reset halt hardware). Step once to resync.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #166](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/166), summarized in own words; confidence medium, not reviewed yet.
