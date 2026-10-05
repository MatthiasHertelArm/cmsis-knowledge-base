---
id: "iss-dbg-972"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD gdbserver TypeError after adding an extra access port to debug-topology"
summary: "Adding a further access port (for example an APB-AP for the debug/trace subsystem) to the debug-topology of a cbuild-run file made pyOCD create a GDB server for an entry without a port, which crashed at socket bind."
status: "draft"
tool: "pyocd"
symptoms: ["0001483 C Error: 'NoneType' object cannot be interpreted as an integer [__main__]"]
symptom_regex: "Error:\\s+'.*?'\\s+object\\s+cannot\\s+be\\s+interpreted\\s+as\\s+an\\s+integer"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/972"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/972"
resolution: "fixed-in-release"
versions: "pyOCD 0.44.0 affected"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001483 C Error: 'NoneType' object cannot be interpreted as an integer [__main__]`

## Cause

Adding a further access port (for example an APB-AP for the debug/trace subsystem) to the debug-topology of a cbuild-run file made pyOCD create a GDB server for an entry without a port, which crashed at socket bind. The problem affects ADIv5 and ADIv6 devices.

## Fix

Use a pyOCD build with the fix (pyOCD PR 1965, available from the nightly after 0.44.0).

## Source

Resolution: fixed-in-release

Versions: pyOCD 0.44.0 affected

From [Open-CMSIS-Pack/vscode-cmsis-debugger #972](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/972), summarized in own words; confidence high, not reviewed yet.
