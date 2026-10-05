---
id: "iss-dbg-520"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: HE core on Alif E7 does not start after flashing"
summary: "Implicit resets between multiple loaded images and a missing clean post-load reset left the core in a bad state."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/520"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/520"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["Alif E7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Implicit resets between multiple loaded images and a missing clean post-load reset left the core in a bad state.

## Fix

Use pyOCD 0.40 / CMSIS Debugger 1.2.0 or later (reset catch on all cores, no implicit resets between images, hardware reset after flashing).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #520](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/520), summarized in own words; confidence high, not reviewed yet.
