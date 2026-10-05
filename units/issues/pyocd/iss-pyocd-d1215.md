---
id: "iss-pyocd-d1215"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Locking an nRF52 (enabling APPROTECT) with pyOCD"
summary: "Debug port protection on nRF52 is controlled by the APPROTECT field in the UICR flash region."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1215"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1215"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["nRF52840_xxAA"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Debug port protection on nRF52 is controlled by the APPROTECT field in the UICR flash region. The pyOCD security notes only describe unlocking.

## Fix

Create a 1 KiB file filled with 0xFF, set the byte at offset 0x208 to 0x00 (the PALL field of APPROTECT), and load it to the start of UICR with pyocd load -a 0x10001000 <file>.bin. After a reset the device should no longer be connectable (the tool then reports that no cores were found). The answer was derived from the datasheet and not tested on a full lock.

## Source

Resolution: configuration

From [pyocd/pyOCD discussion 1215](https://github.com/pyocd/pyOCD/discussions/1215), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
