---
id: "iss-pyocd-1532"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: flashing a FRDM-K66F fails with core not halted when writing flash algorithm registers"
summary: "pyOCD could not halt the core before calling the flash algorithm."
status: "draft"
tool: "pyocd"
symptoms: ["pyocd.core.exceptions.CoreRegisterAccessError: cannot write registers pc, r0, r1, r2, r9, sp, lr because core #0 is not halted"]
symptom_regex: "pyocd\\.core\\.exceptions\\.CoreRegisterAccessError:\\s+cannot\\s+write\\s+registers\\s+pc,\\s+r0,\\s+r1,\\s+r2,\\s+r9,\\s+sp,\\s+lr\\s+because\\s+core\\s+\\#\\S+\\s+is\\s+not\\s+halted"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1532"
doc_source: "https://github.com/pyocd/pyOCD/issues/1532"
resolution: "workaround"
versions: "pyOCD 0.34.3"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MK66FN2M0VMD18"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pyocd.core.exceptions.CoreRegisterAccessError: cannot write registers pc, r0, r1, r2, r9, sp, lr because core #0 is not halted`

## Cause

pyOCD could not halt the core before calling the flash algorithm. The maintainer suspects connecting to a locked or secured device, which has been troublesome.

## Fix

Try connecting in attach mode, e.g. pyocd flash -M attach <file>. If the device is locked, unlock it with a mass erase first.

## Source

Resolution: workaround

Versions: pyOCD 0.34.3

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1532](https://github.com/pyocd/pyOCD/issues/1532), summarized in own words; confidence low, not reviewed yet.
