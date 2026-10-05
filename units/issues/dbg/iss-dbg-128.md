---
id: "iss-dbg-128"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flash programming fails on LPC55S69 when the device is erased"
summary: "Reading erased flash for the compare step produced bus errors."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/128"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/128"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S69"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Reading erased flash for the compare step produced bus errors.

## Fix

Use a pyOCD that skips reading erased sectors when the algorithm has Verify (CMSIS Debugger 0.2+).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #128](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/128), summarized in own words; confidence high, not reviewed yet.
