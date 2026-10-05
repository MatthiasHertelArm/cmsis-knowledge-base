---
id: "iss-pyocd-1611"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: write_memory to STM32G0 option bytes address has no effect"
summary: "STM32 option bytes live in flash and are protected by lock registers."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1611"
doc_source: "https://github.com/pyocd/pyOCD/issues/1611"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["STM32G0 Series"], "device": ["STM32G071KBUx"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

STM32 option bytes live in flash and are protected by lock registers. A plain memory write to 0x1FFF7800 is ignored. The option bytes are loaded from flash into FLASH_OPTR and related registers at power-on and only rewritten through the flash controller.

## Fix

Either program them via pyOCD's flash classes (MemoryLoader.program_binary_data or MemoryLoader.add_data and commit), or follow the reference-manual sequence: unlock FLASH_KEYR then FLASH_OPTKEYR, write the new value to FLASH_OPTR, start the update in FLASH_CR, and expect a reset from OBL_LAUNCH. The session is invalid afterwards, so open a new one. Make sure flash is not busy first.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1611](https://github.com/pyocd/pyOCD/issues/1611), summarized in own words; confidence medium, not reviewed yet.
