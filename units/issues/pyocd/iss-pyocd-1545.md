---
id: "iss-pyocd-1545"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: S32K3xx hard-faults on gdb attach because the pack's RAMInitialize clears the vector table"
summary: "The Keil S32K3xx pack's RAMInitialize sequence, controlled by the debug variable DoRAMInitialize, clears RAM, and the reset sequence that should return the core to reset state does not run."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1545"
doc_source: "https://github.com/pyocd/pyOCD/issues/1545"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "family": ["S32K3 Series"], "device": ["S32K344"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Keil S32K3xx pack's RAMInitialize sequence, controlled by the debug variable DoRAMInitialize, clears RAM, and the reset sequence that should return the core to reset state does not run. A vector table moved to RAM is wiped and the core faults.

## Fix

Set the debug variable off: -Opack.debug_sequences.debugvars="DoRAMInitialize=0;". For attach after flashing, also use --connect under-reset and, as a pack patch, alias ResetCatchClear to ResetHardwareDeassert.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1545](https://github.com/pyocd/pyOCD/issues/1545), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
