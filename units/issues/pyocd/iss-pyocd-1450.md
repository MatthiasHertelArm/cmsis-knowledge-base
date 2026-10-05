---
id: "iss-pyocd-1450"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: flash algorithm overflowed stack after converting a Keil FLM to a built-in target"
summary: "The generated FLASH_ALGO uses a page size different from the sector size, and the page buffers pyOCD sets up overlap the stack."
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
applies_to: {"tool": ["pyocd"], "device": ["STM32C031"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C flash algorithm overflowed stack (4096 bytes) [__main__]`

## Cause

The generated FLASH_ALGO uses a page size different from the sector size, and the page buffers pyOCD sets up overlap the stack. For STM32C031 the page was 0x400 but pyOCD assumed 0x800.

## Fix

Adjust the page_buffers, begin_stack and end_stack values in the generated target so the stack does not overlap the page buffers (one user shifted them by 0x1000), and set page_size explicitly. Using the pack directly picked the correct sizes.

## Source

Resolution: workaround

Versions: pyocd 0.36.0

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1450](https://github.com/pyocd/pyOCD/issues/1450), summarized in own words; confidence low, not reviewed yet.
