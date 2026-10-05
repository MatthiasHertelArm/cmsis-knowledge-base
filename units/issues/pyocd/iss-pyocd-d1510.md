---
id: "iss-pyocd-d1510"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Writing a single UICR word after flashing with the API leaves an nRF52 unbootable"
summary: "FlashLoader with sector chip-erase mode erased and rewrote more flash than intended for the small UICR write."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1510"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1510"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["nRF52832_xxAA"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

FlashLoader with sector chip-erase mode erased and rewrote more flash than intended for the small UICR write. The command line commander writes only the requested words.

## Fix

Program the extra bytes with the low-level Flash class: create Flash(target, boot_region.algo), set flasher.region to the region, call init(operation=Flash.Operation.PROGRAM), then program_phrase(address, bytes), and finally uninit/reset. Do this after FileProgrammer has loaded the image.

## Source

Resolution: configuration

From [pyocd/pyOCD discussion 1510](https://github.com/pyocd/pyOCD/discussions/1510), summarized in own words; confidence medium, not reviewed yet.
