---
id: "iss-dbg-383"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Execution stays stuck at a manually inserted BKPT instruction and cannot continue"
summary: "A BKPT instruction inserted into program code halts the core on each resume."
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

A BKPT instruction inserted into program code halts the core on each resume. Stepping leaves the PC at the BKPT address because the debugger did not advance past it, whereas uVision places the PC at the next instruction.

## Fix

Newer pyOCD behaves like uVision: step and continue run over the BKPT instruction, so the program proceeds past it.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #383](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/383), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
