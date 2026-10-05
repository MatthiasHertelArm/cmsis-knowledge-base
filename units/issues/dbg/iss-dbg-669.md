---
id: "iss-dbg-669"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: GDB internal error at breakpoint and unreadable peripherals without a cbuild-run file"
summary: "The debugger ran standalone with a makefile build and no *.cbuild-run.yml, so the debug sequences of the device pack (on the STM32G474 the DBGMCU_CR setup) were missing, which can make memory and core register accesses fail; once a cbuild-run.yml …"
status: "draft"
tool: "cmsis-debugger"
symptoms: ["internal-error: get_frame_id: Assertion `stashed' failed.", "Failed to read peripheral GPIOA: Error: readMemory failed @ 0x48000000 for 24 bytes: CodeExpectedError: Unable to read memory.", "Internal error: Failed to update peripheral GPIOA after memory reads: Attempt to access memory outside buffer bounds"]
symptom_regex: "internal\\-error:\\s+get_frame_id:\\s+Assertion\\s+`stashed'\\s+failed\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/669"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/669"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger", "pyocd", "gdb"], "family": ["STM32G4 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`internal-error: get_frame_id: Assertion `stashed' failed.`
`Failed to read peripheral GPIOA: Error: readMemory failed @ 0x48000000 for 24 bytes: CodeExpectedError: Unable to read memory.`
`Internal error: Failed to update peripheral GPIOA after memory reads: Attempt to access memory outside buffer bounds`

## Cause

The debugger ran standalone with a makefile build and no *.cbuild-run.yml, so the debug sequences of the device pack (on the STM32G474 the DBGMCU_CR setup) were missing, which can make memory and core register accesses fail; once a cbuild-run.yml was in place the GDB crash went away. The 'outside buffer bounds' error is a separate Peripheral Inspector bug.

## Fix

Provide a *.cbuild-run.yml. Without a CMSIS Solution build, create an example or blank solution for the board with the CMSIS Solution extension and reuse its generated *.cbuild-run.yml, *.dbgconf, launch.json and tasks.json, adjusted to your build output.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-debugger #669](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/669), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
