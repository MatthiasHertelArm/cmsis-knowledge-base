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
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

ap_address was passed to the memory interface for root components.

## Fix

Use CMSIS Debugger 0.2+ pyOCD.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #127](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/127), summarized in own words; confidence high, not reviewed yet.
