---
id: "iss-pyocd-1313"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Picoprobe unreliable with pyocd (PC register not available)"
summary: "Probable signal-integrity trouble; the picoprobe optimizes by assuming target acknowledgements."
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
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`PC register is not available`

## Cause

Probable signal-integrity trouble; the picoprobe optimizes by assuming target acknowledgements.

## Fix

Lower the SWD clock (-f 400000), try -Opicoprobe.safeswd=True, replug the probe, or use a CMSIS-DAP firmware on the Pico.

## Source

Resolution: workaround

Versions: 0.32.3

From [pyocd/pyOCD #1313](https://github.com/pyocd/pyOCD/issues/1313), summarized in own words; confidence medium, not reviewed yet.
