---
id: "iss-pyocd-246"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: eraseAll error 104 on a KL25Z chip erase"
summary: "Error 104 is the flash driver status for a protection violation: sectors are write-protected through the flash configuration field at 0x400, which blocks a normal chip erase."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR:root:eraseAll error: 104"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/246"
doc_source: "https://github.com/pyocd/pyOCD/issues/246"
resolution: "workaround"
versions: "0.7.x"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MKL25Z128xxx4"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR:root:eraseAll error: 104`

## Cause

Error 104 is the flash driver status for a protection violation: sectors are write-protected through the flash configuration field at 0x400, which blocks a normal chip erase.

## Fix

Run a mass erase that clears protection: connect with pyocd-tool and run `unlock` (the flashtool unlock option was not implemented).

## Source

Resolution: workaround

Versions: 0.7.x

From [pyocd/pyOCD #246](https://github.com/pyocd/pyOCD/issues/246), summarized in own words; confidence high, not reviewed yet.
