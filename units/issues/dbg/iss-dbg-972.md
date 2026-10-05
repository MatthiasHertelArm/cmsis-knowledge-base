---
id: "iss-dbg-972"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD gdbserver TypeError after adding an extra access port to debug-topology"
summary: "Adding a further access port (for example an APB-AP for the debug/trace subsystem) to the debug-topology of a cbuild-run file made pyOCD gdbserver stop with a TypeError while opening its listening socket, because the port it tried to bind …"
status: "draft"
tool: "pyocd"
symptoms: ["0001483 C Error: 'NoneType' object cannot be interpreted as an integer [__main__]"]
symptom_regex: "Error:\\s+'.*?'\\s+object\\s+cannot\\s+be\\s+interpreted\\s+as\\s+an\\s+integer"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/972"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/972"
resolution: "workaround"
versions: "pyOCD 0.44.0 (CMSIS Debugger 1.6.0, CMSIS Solution 1.67.1) affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001483 C Error: 'NoneType' object cannot be interpreted as an integer [__main__]`

## Cause

Adding a further access port (for example an APB-AP for the debug/trace subsystem) to the debug-topology of a cbuild-run file made pyOCD gdbserver stop with a TypeError while opening its listening socket, because the port it tried to bind was None. The problem affects ADIv5 and ADIv6 devices.

## Fix

Use a pyOCD build with PR 1965 (confirmed with a manually triggered pyOCD nightly build; no release named). On ADIv5 devices the extra access port can be reached instead by setting __ap to its index in the debug sequences; ADIv6 needs the apid declared in the debug-topology.

## Source

Resolution: workaround

Versions: pyOCD 0.44.0 (CMSIS Debugger 1.6.0, CMSIS Solution 1.67.1) affected

From [Open-CMSIS-Pack/vscode-cmsis-debugger #972](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/972), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
