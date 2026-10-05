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
resolution: "user-error"
versions: "pyOCD 0.35.1"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["STM32G0 Series"], "device": ["STM32G071KBUx"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

STM32 option bytes live in flash and are protected by lock registers. A plain memory write to 0x1FFF7800 is ignored. The option bytes are loaded from flash into FLASH_OPTR and related registers at power-on and only rewritten through the flash controller.

## Fix

Program them through the flash controller. The maintainer suggested pyOCD's flash classes (MemoryLoader.program_binary_data, or MemoryLoader.add_data and commit); the user got it working with the reference-manual sequence: unlock FLASH_KEYR then FLASH_OPTKEYR, write the new value to FLASH_OPTR, start the update in FLASH_CR, and expect a reset from OBL_LAUNCH. An exception is raised and the session object is unusable afterwards, so create a new one. With firmware already in the chip the first FLASH_KEYR write raised a transfer fault until a chip erase was done.

## Source

Resolution: user-error

Versions: pyOCD 0.35.1

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1611](https://github.com/pyocd/pyOCD/issues/1611), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
