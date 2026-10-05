---
id: "iss-dbg-827"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Component Viewer shows thread names as addresses while the target is running"
summary: "While the target runs, GDB evaluations had no frame, and the string lookup for names fell back to showing the raw pointer."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/827"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/827"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

While the target runs, GDB evaluations had no frame, and the string lookup for names fell back to showing the raw pointer.

## Fix

Update CMSIS Debugger (fix PR 835 lets such calls run with an undefined frameId, handled by the driver).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #827](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/827), summarized in own words; confidence medium, not reviewed yet.
