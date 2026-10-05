---
id: "iss-pyocd-d1510"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Writing a single UICR word after flashing with the API leaves an nRF52 unbootable"
summary: "The user suspected that the FlashLoader (chip_erase='sector', smart_flash=True) erased more flash than intended for the small UICR write; the same write done with write16 in commander left a bootable device."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1510"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1510"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["nRF52832_xxAA"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The user suspected that the FlashLoader (chip_erase='sector', smart_flash=True) erased more flash than intended for the small UICR write; the same write done with write16 in commander left a bootable device.

## Fix

After FileProgrammer has loaded the image, program the extra bytes with the low-level Flash class: create Flash(target, boot_memory.algo), set flasher.region to the boot memory region, call init(operation=Flash.Operation.PROGRAM), then program_phrase(address, bytes), and reset the target.

## Source

Resolution: workaround

From [pyocd/pyOCD discussion 1510](https://github.com/pyocd/pyOCD/discussions/1510), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
