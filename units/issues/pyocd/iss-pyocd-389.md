---
id: "iss-pyocd-389"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb load through pyocd-gdbserver ends with AssertionError in progress reporting"
summary: "A progress-bar assertion introduced in 0.11 when progress reporting was unified could fire near the end of a load; flashing itself was unaffected."
status: "draft"
tool: "pyocd"
symptoms: ["0018874:ERROR:gdbserver:Unhandled exception in handleMsg:", "AssertionError"]
symptom_regex: "\\S+:ERROR:gdbserver:Unhandled\\s+exception\\s+in\\s+handleMsg:"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/389"
doc_source: "https://github.com/pyocd/pyOCD/issues/389"
resolution: "fixed-in-release"
versions: "0.11.x to 0.13.0b1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MK66FN2M0xxx18"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0018874:ERROR:gdbserver:Unhandled exception in handleMsg:`
`AssertionError`

## Cause

A progress-bar assertion introduced in 0.11 when progress reporting was unified could fire near the end of a load; flashing itself was unaffected.

## Fix

Use pyOCD 0.13.0b2 or later, where the assertion was disabled; 0.10.0 does not have it.

## Source

Resolution: fixed-in-release

Versions: 0.11.x to 0.13.0b1

From [pyocd/pyOCD #389](https://github.com/pyocd/pyOCD/issues/389), summarized in own words; confidence high, not reviewed yet.
