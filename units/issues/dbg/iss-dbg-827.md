---
id: "iss-dbg-827"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Component Viewer shows thread names as addresses while the target is running"
summary: "While the target ran, the Component Viewer showed thread names as addresses and showed the names again after a pause; the fix lets the viewer's GDB calls run without a frame ID, which points to those calls failing while …"
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/827"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/827"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

While the target ran, the Component Viewer showed thread names as addresses and showed the names again after a pause; the fix lets the viewer's GDB calls run without a frame ID, which points to those calls failing while the target runs.

## Fix

Use a CMSIS Debugger build with PR 835, which allows GDB calls with an undefined frameId and leaves them to the driver; no release is named. Pausing the target shows the names.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #827](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/827), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
