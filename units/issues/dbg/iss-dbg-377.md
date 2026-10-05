---
id: "iss-dbg-377"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Attach to a core without program image is refused"
summary: "The CDT GDB Adapter required a program for attach requests."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/377"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/377"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CDT GDB Adapter required a program for attach requests.

## Fix

Use a CDT GDB Adapter release containing the fix (PR 262), so attach works without "program".

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #377](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/377), summarized in own words; confidence medium, not reviewed yet.
