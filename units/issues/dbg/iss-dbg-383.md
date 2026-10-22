---
id: "iss-dbg-383"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Execution stuck at a manually inserted BKPT instruction; continue halts again immediately"
summary: "A BKPT instruction placed in the source halts the core when it is executed."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/383"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/383"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A BKPT instruction placed in the source halts the core when it is executed. On resume the program counter was not advanced past the instruction, so continuing halted again at the same address.

## Fix

pyOCD now steps over a BKPT instruction on both Step and Continue, matching the behaviour of uVision.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #383](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/383), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
