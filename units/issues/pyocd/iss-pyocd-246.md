---
id: "iss-pyocd-246"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: eraseAll error 104 on a KL25Z chip erase"
summary: "Error 104 is the Kinetis SDK flash driver status for a protection violation: sectors are protected through the flash configuration field at 0x400, which blocks a chip erase."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR:root:eraseAll error: 104"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/246"
doc_source: "https://github.com/pyocd/pyOCD/issues/246"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["MKL25Z128xxx4"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR:root:eraseAll error: 104`

## Cause

Error 104 is the Kinetis SDK flash driver status for a protection violation: sectors are protected through the flash configuration field at 0x400, which blocks a chip erase.

## Fix

Run a mass erase: connect with pyocd-tool and run `unlock` (the unlock option of pyocd-flashtool was not implemented).

## Source

Resolution: workaround

From [pyocd/pyOCD #246](https://github.com/pyocd/pyOCD/issues/246), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
