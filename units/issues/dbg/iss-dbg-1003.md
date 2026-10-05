---
id: "iss-dbg-1003"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Memory Inspector cannot load back a hex file dumped from addresses above 0x80000000"
summary: "The Memory Inspector mishandled addresses in the upper half of the 32-bit range when re-importing a dumped hex file; this was an upstream defect of the extension."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1003"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1003"
resolution: "fixed-in-release"
versions: "fixed in Memory Inspector 1.3.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Memory Inspector mishandled addresses in the upper half of the 32-bit range when re-importing a dumped hex file; this was an upstream defect of the extension.

## Fix

Update Memory Inspector to 1.3.0 or later.

## Source

Resolution: fixed-in-release

Versions: fixed in Memory Inspector 1.3.0

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1003](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1003), summarized in own words; confidence medium, not reviewed yet.
