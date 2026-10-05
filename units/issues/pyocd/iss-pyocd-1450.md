---
id: "iss-pyocd-1450"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: flash algorithm overflowed stack after converting a Keil FLM to a built-in target"
summary: "pyOCD programmed pages of 0x800 bytes (the sector size) although the FLASH_ALGO generated for STM32C031 gave 0x400, so the page buffers it used overlapped the flash algorithm's stack."
status: "draft"
tool: "pyocd"
symptoms: ["C flash algorithm overflowed stack (4096 bytes) [__main__]"]
symptom_regex: "C\\s+flash\\s+algorithm\\s+overflowed\\s+stack\\s+\\(\\S+\\s+bytes\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1450"
doc_source: "https://github.com/pyocd/pyOCD/issues/1450"
resolution: "workaround"
versions: "pyocd 0.36.0"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["STM32C031"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C flash algorithm overflowed stack (4096 bytes) [__main__]`

## Cause

pyOCD programmed pages of 0x800 bytes (the sector size) although the FLASH_ALGO generated for STM32C031 gave 0x400, so the page buffers it used overlapped the flash algorithm's stack.

## Fix

Adjust the generated target so the stack does not overlap the page buffers: one user added 0x1000 to begin_stack and end_stack; another resized page_buffers for 0x800-byte pages and moved begin_stack and end_stack clear of them. Using the pack directly picked the correct page and sector sizes.

## Source

Resolution: workaround

Versions: pyocd 0.36.0

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1450](https://github.com/pyocd/pyOCD/issues/1450), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
