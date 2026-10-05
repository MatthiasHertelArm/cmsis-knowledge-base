---
id: "iss-pyocd-1262"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: flash erase sector failure (result code 0x67) on micro:bit V2"
summary: "The micro:bit uses a Nordic SoftDevice, which locks its flash sectors once installed, so the normal erase refuses."
status: "draft"
tool: "pyocd"
symptoms: ["flash erase sector failure (address 0x00000000; result code 0x67)"]
symptom_regex: "flash\\s+erase\\s+sector\\s+failure\\s+\\(address\\s+\\S+;\\s+result\\s+code\\s+\\S+\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1262"
doc_source: "https://github.com/pyocd/pyOCD/issues/1262"
resolution: "workaround"
versions: "pyocd 0.32.1"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["nRF52833"], "core": ["Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`flash erase sector failure (address 0x00000000; result code 0x67)`

## Cause

The micro:bit uses a Nordic SoftDevice, which locks its flash sectors once installed, so the normal erase refuses.

## Fix

Run a mass erase (pyocd erase --mass -t nrf52833) once, then flash normally. Chip erase leaves the SoftDevice in place.

## Source

Resolution: workaround

Versions: pyocd 0.32.1

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1262](https://github.com/pyocd/pyOCD/issues/1262), summarized in own words; confidence high, checked against the thread, not reviewed yet.
