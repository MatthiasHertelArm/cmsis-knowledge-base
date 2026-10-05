---
id: "iss-pyocd-1532"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: flashing a FRDM-K66F fails with core not halted when writing flash algorithm registers"
summary: "pyOCD timed out waiting for the core to halt after reset and then could not write the registers needed to call the flash algorithm."
status: "draft"
tool: "pyocd"
symptoms: ["pyocd.core.exceptions.CoreRegisterAccessError: cannot write registers pc, r0, r1, r2, r9, sp, lr because core #0 is not halted"]
symptom_regex: "pyocd\\.core\\.exceptions\\.CoreRegisterAccessError:\\s+cannot\\s+write\\s+registers\\s+pc,\\s+r0,\\s+r1,\\s+r2,\\s+r9,\\s+sp,\\s+lr\\s+because\\s+core\\s+\\#\\S+\\s+is\\s+not\\s+halted"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1532"
doc_source: "https://github.com/pyocd/pyOCD/issues/1532"
resolution: "unresolved"
versions: "pyOCD 0.34.3"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "device": ["MK66FN2M0VMD18"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pyocd.core.exceptions.CoreRegisterAccessError: cannot write registers pc, r0, r1, r2, r9, sp, lr because core #0 is not halted`

## Cause

pyOCD timed out waiting for the core to halt after reset and then could not write the registers needed to call the flash algorithm. The maintainer wondered whether the device is locked, since connecting to locked devices had been troublesome; this was not confirmed.

## Fix

Suggested, not confirmed: add -M attach (connect mode attach) to the pyocd flash command.

## Source

Resolution: unresolved

Versions: pyOCD 0.34.3

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1532](https://github.com/pyocd/pyOCD/issues/1532), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
