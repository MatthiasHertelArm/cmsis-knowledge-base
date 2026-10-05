---
id: "iss-pyocd-1729"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RTT: 'Control block not found' although the SEGGER RTT ID is in RAM"
summary: "pyOCD's RTT search could only find a control block aligned to 16 or 32 bytes."
status: "draft"
tool: "pyocd"
symptoms: ["C Control block not found [__main__]"]
symptom_regex: "C\\s+Control\\s+block\\s+not\\s+found"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1729"
doc_source: "https://github.com/pyocd/pyOCD/issues/1729"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Control block not found [__main__]`

## Cause

pyOCD's RTT search could only find a control block aligned to 16 or 32 bytes.

## Fix

Compile the firmware with SEGGER_RTT_CB_ALIGN set to 16 or 32; a search fix was merged in change #1730.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1729](https://github.com/pyocd/pyOCD/issues/1729), summarized in own words; confidence high, checked against the thread, not reviewed yet.
