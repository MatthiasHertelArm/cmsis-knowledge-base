---
id: "iss-pyocd-874"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: KV11Z flash erase_sector fails with error 105 on second programming"
summary: "Error 105 is the flash driver's command-failure status (erase verify failed), typically worn flash."
status: "draft"
tool: "pyocd"
symptoms: ["FlashEraseFailure: erase_sector(0x400) error: 105"]
symptom_regex: "FlashEraseFailure:\\s+erase_sector\\(\\S+\\)\\s+error:\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/874"
doc_source: "https://github.com/pyocd/pyOCD/issues/874"
resolution: "workaround"
versions: "0.26.1"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["MKV11Z128VFM7"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`FlashEraseFailure: erase_sector(0x400) error: 105`

## Cause

Error 105 is the flash driver's command-failure status (erase verify failed), typically worn flash. Sector erase failed while chip erase worked on the same board.

## Fix

Add -O chip_erase=auto (or choose chip erase) so the whole chip is erased instead of sector by sector; also try another board to rule out worn flash.

## Source

Resolution: workaround

Versions: 0.26.1

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #874](https://github.com/pyocd/pyOCD/issues/874), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
