---
id: "iss-pyocd-863"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32F7 (F746) 'No cores were discovered' in Mbed Studio"
summary: "STM32F7 and H7 parts need special handling to wake from low-power modes before discovery; the F746 target lacked it, while the F767 target had the DBGMCU handling."
status: "draft"
tool: "pyocd"
symptoms: ["0000421:CRITICAL:__main__:No cores were discovered!"]
symptom_regex: "\\S+:CRITICAL:__main__:No\\s+cores\\s+were\\s+discovered!"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/863"
doc_source: "https://github.com/pyocd/pyOCD/issues/863"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["STM32F7 Series"], "device": ["STM32F746ZGTx"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000421:CRITICAL:__main__:No cores were discovered!`

## Cause

STM32F7 and H7 parts need special handling to wake from low-power modes before discovery; the F746 target lacked it, while the F767 target had the DBGMCU handling.

## Fix

Use a pyocd with the F767 support (master at the time) and select -t stm32f767zi on an F746 (worked for one user; it only reports a dual-bank error and continues). Use debug builds that do not sleep, or set DBGMCU_CR early in firmware. Be careful with dual-bank option bytes (nDBANK=0): sector erase may then erase too little; use chip erase or switch to single bank.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #863](https://github.com/pyocd/pyOCD/issues/863), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
