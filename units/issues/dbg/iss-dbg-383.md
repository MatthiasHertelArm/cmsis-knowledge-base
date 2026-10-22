---
id: "iss-dbg-383"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Execution stops again at a manually inserted BKPT instruction and cannot continue"
summary: "A BKPT instruction written into the source halts the core, and pyOCD did not advance the program counter past it, so resuming re-triggered the same breakpoint and Step left the PC unchanged. uVision advances the PC to the next instruction."
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

A BKPT instruction written into the source halts the core, and pyOCD did not advance the program counter past it, so resuming re-triggered the same breakpoint and Step left the PC unchanged. uVision advances the PC to the next instruction.

## Fix

pyOCD was changed so that Step steps over the BKPT instruction and Continue runs past it, behaving similarly to uVision.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #383](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/383), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
