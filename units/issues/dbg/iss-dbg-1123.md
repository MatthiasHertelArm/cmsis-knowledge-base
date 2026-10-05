---
id: "iss-dbg-1123"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Memory Inspector cells do not re-render: no periodic update, no edit, no keyboard nav"
summary: "The Memory Inspector memoized cell and row data that did not change identity although the contents changed, so the view showed stale cells."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1123"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1123"
resolution: "fixed-in-release"
versions: "Memory Inspector 1.2.0 affected, fixed in 1.3.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Memory Inspector memoized cell and row data that did not change identity although the contents changed, so the view showed stale cells.

## Fix

Update the Memory Inspector extension to 1.3.0 or later, which contains the fix.

## Source

Resolution: fixed-in-release

Versions: Memory Inspector 1.2.0 affected, fixed in 1.3.0

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1123](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1123), summarized in own words; confidence medium, not reviewed yet.
