---
id: "iss-dbg-1273"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: CSV viewer Notes column: header and data cells misalign when the column is resized"
summary: "The last (Notes) column used different minimum-width behavior for the header and the data rows."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1273"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1273"
resolution: "fixed-in-release"
versions: "1.9.1-9-gda28d9a"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The last (Notes) column used different minimum-width behavior for the header and the data rows. Shrinking it made the data cells keep narrowing while the header stopped, so their right edges no longer lined up. The data rows also did not extend to the viewport edge when the combined column widths were smaller than the available space.

## Fix

The thread reports validation on CMSIS Debugger build 1.9.1-9-gda28d9a and closes the issue; it describes no code change, so use that build and do not assume a specific patch.

## Source

Resolution: fixed-in-release

Versions: 1.9.1-9-gda28d9a

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1273](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1273), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
