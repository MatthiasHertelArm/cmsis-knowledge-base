---
id: "iss-pyocd-1313"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Picoprobe unreliable with pyocd (PC register not available)"
summary: "Probable signal-integrity trouble; the picoprobe code speeds up SWD by assuming positive acknowledgements from the target, and the firmware leaves the pins at a fast slew rate."
status: "draft"
tool: "pyocd"
symptoms: ["PC register is not available"]
symptom_regex: "PC\\s+register\\s+is\\s+not\\s+available"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1313"
doc_source: "https://github.com/pyocd/pyOCD/issues/1313"
resolution: "workaround"
versions: "0.32.3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`PC register is not available`

## Cause

Probable signal-integrity trouble; the picoprobe code speeds up SWD by assuming positive acknowledgements from the target, and the firmware leaves the pins at a fast slew rate.

## Fix

Lower the SWD clock (-f 400000) and replug the probe when problems show; -Opicoprobe.safeswd=True disables the assumed acknowledgements (much slower).

## Source

Resolution: workaround

Versions: 0.32.3

From [pyocd/pyOCD #1313](https://github.com/pyocd/pyOCD/issues/1313), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
