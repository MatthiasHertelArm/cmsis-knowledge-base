---
id: "iss-dbg-1273"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: CSV viewer Notes column header and data cells misalign when the column is resized"
summary: "The Notes column applies a different minimum-width behaviour to its header cell than to its data cells."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1273"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1273"
resolution: "fixed-in-release"
versions: "Validated with CMSIS Debugger 1.9.1-9-gda28d9a"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Notes column applies a different minimum-width behaviour to its header cell than to its data cells. When the column is shrunk, the data cells keep narrowing while the header stops, so their right edges no longer line up. The data rows also do not extend to the viewport edge when the combined column widths are smaller than the available space.

## Fix

The issue is closed and a comment states it was validated with CMSIS Debugger 1.9.1-9-gda28d9a, which the thread reports as behaving correctly. The thread does not describe the code change or any workaround.

## Source

Resolution: fixed-in-release

Versions: Validated with CMSIS Debugger 1.9.1-9-gda28d9a

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1273](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1273), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
