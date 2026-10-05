---
id: "iss-dbg-669"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: GDB internal error at breakpoint and unreadable peripherals without a cbuild-run file"
summary: "The debugger was used standalone with a makefile project and no *.cbuild-run.yml."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["internal-error: get_frame_id: Assertion `stashed' failed.", "Failed to read peripheral GPIOA: Error: readMemory failed @ 0x48000000 for 24 bytes: CodeExpectedError: Unable to read memory.", "Internal error: Failed to update peripheral GPIOA after memory reads: Attempt to access memory outside buffer bounds"]
symptom_regex: "internal\\-error:\\s+get_frame_id:\\s+Assertion\\s+`stashed'\\s+failed\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/669"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/669"
resolution: "workaround"
versions: "CMSIS Debugger 1.2.0, GDB 14.3"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger", "pyocd", "gdb"], "family": ["STM32G4 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`internal-error: get_frame_id: Assertion `stashed' failed.`
`Failed to read peripheral GPIOA: Error: readMemory failed @ 0x48000000 for 24 bytes: CodeExpectedError: Unable to read memory.`
`Internal error: Failed to update peripheral GPIOA after memory reads: Attempt to access memory outside buffer bounds`

## Cause

The debugger was used standalone with a makefile project and no *.cbuild-run.yml. Without it the debug sequences from the device pack are missing (for an STM32G4 the DBGMCU configuration), so memory and core register accesses can fail while the target is halted, which also made GDB lose its frames in optimized code. The remaining bounds error comes from the Peripheral Inspector extension and is a separate bug.

## Fix

Provide a *.cbuild-run.yml. Easiest route when not using the CMSIS Solution for the build: create a blank or example solution for the same board with the CMSIS Solution extension, copy the generated cbuild-run, dbgconf, launch.json and tasks.json, and point them at your own build output. After doing this the crash and the unreadable-memory errors disappeared for the reporter.

## Source

Resolution: workaround

Versions: CMSIS Debugger 1.2.0, GDB 14.3

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #669](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/669), summarized in own words; confidence medium, not reviewed yet.
