---
id: "iss-dbg-890"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Run control becomes unresponsive while Component Viewer is open on a multi-core target"
summary: "The Component Viewer sent requests to GDB at inconvenient moments (during run and step) that could leave the CDT GDB Adapter or GDB hanging; Reset Target sometimes did not recover it."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/890"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/890"
resolution: "fixed-in-release"
versions: "fixed in CMSIS Debugger 1.4.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Component Viewer sent requests to GDB at inconvenient moments (during run and step) that could leave the CDT GDB Adapter or GDB hanging; Reset Target sometimes did not recover it.

## Fix

Update to CMSIS Debugger 1.4.1 or later, which throttles those requests.

## Source

Resolution: fixed-in-release

Versions: fixed in CMSIS Debugger 1.4.1

From [Open-CMSIS-Pack/vscode-cmsis-debugger #890](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/890), summarized in own words; confidence medium, not reviewed yet.
