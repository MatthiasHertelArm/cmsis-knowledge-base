---
id: "iss-dbg-126"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flash programming fails when erased flash reads as 0x00"
summary: "If PC reads 0 after reset the Thumb bit in xPSR is clear, so running the algorithm faults."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/126"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/126"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

If PC reads 0 after reset the Thumb bit in xPSR is clear, so running the algorithm faults.

## Fix

Use a pyOCD that sets the Thumb bit in xPSR before algorithm calls.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #126](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/126), summarized in own words; confidence high, not reviewed yet.
