---
id: "iss-dbg-127"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CoreSight root components on APv2 are read from wrong addresses"
summary: "ap_address was passed to the memory interface for root components."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/127"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/127"
resolution: "fixed-in-release"
versions: "pyOCD v0.0.0-standalone-cbuild4"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

ap_address was passed to the memory interface for root components.

## Fix

Use a pyOCD that no longer passes ap_address when it creates root components, first provided in the standalone pyOCD build v0.0.0-standalone-cbuild4.

## Source

Resolution: fixed-in-release

Versions: pyOCD v0.0.0-standalone-cbuild4

From [Open-CMSIS-Pack/vscode-cmsis-debugger #127](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/127), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
