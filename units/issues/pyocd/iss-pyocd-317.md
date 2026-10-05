---
id: "iss-pyocd-317"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb 'Cannot access memory' when setting breakpoint on Realtek RTL8195AM SDRAM code"
summary: "Code lives in SDRAM at 0x3xxxxxxx, outside the hardware breakpoint range, so a software breakpoint is needed, and SDRAM is not accessible until the bootloader has initialised it after reset."
status: "draft"
tool: "pyocd"
symptoms: ["Cannot access memory at address 0x3001c660"]
symptom_regex: "Cannot\\s+access\\s+memory\\s+at\\s+address\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/317"
doc_source: "https://github.com/pyocd/pyOCD/issues/317"
resolution: "workaround"
versions: "pyocd-gdbserver 0.8.x"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd", "gdb"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Cannot access memory at address 0x3001c660`

## Cause

Code lives in SDRAM at 0x3xxxxxxx, outside the hardware breakpoint range, so a software breakpoint is needed, and SDRAM is not accessible until the bootloader has initialised it after reset.

## Fix

Break early after boot first (for example at the platform start function), run to it, then set breakpoints in SDRAM code. Full target support was not available in pyocd.

## Source

Resolution: workaround

Versions: pyocd-gdbserver 0.8.x

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #317](https://github.com/pyocd/pyOCD/issues/317), summarized in own words; confidence low, not reviewed yet.
