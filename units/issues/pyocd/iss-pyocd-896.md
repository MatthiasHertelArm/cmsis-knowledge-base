---
id: "iss-pyocd-896"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32H743 'No cores were discovered' in Mbed Studio"
summary: "STM32H7 needs the DBGMCU CR bits set (TRACECLKEN, D1DBGCKEN, D3DBGCKEN and the DBGSLEEP/STOP/STBY bits) for CoreSight discovery to work."
status: "draft"
tool: "pyocd"
symptoms: ["0000721:CRITICAL:__main__:No cores were discovered!"]
symptom_regex: "\\S+:CRITICAL:__main__:No\\s+cores\\s+were\\s+discovered!"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/896"
doc_source: "https://github.com/pyocd/pyOCD/issues/896"
resolution: "workaround"
versions: "Mbed Studio 1.0.0"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["STM32H7 Series"], "device": ["STM32H743ZITx"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000721:CRITICAL:__main__:No cores were discovered!`

## Cause

STM32H7 needs the DBGMCU CR bits set (TRACECLKEN, D1DBGCKEN, D3DBGCKEN and the DBGSLEEP/STOP/STBY bits) for CoreSight discovery to work.

## Fix

Suggested by the maintainer, not confirmed in the thread: use a pyocd user script that writes DBGMCU_CR, or set the bits at the start of your firmware and load the first image by drag and drop. A branch with CMSIS-Pack debug sequences configured it automatically. Mbed Studio's bundled pyocd is customised, so also ask that team.

## Source

Resolution: workaround

Versions: Mbed Studio 1.0.0

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #896](https://github.com/pyocd/pyOCD/issues/896), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
