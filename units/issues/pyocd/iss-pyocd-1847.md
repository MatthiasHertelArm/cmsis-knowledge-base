---
id: "iss-pyocd-1847"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: EFR32BG22 pack: 'Memory regions must have a non-zero length'"
summary: "The Silicon Labs DFP 2025.6.2 contained a faulty memory region definition and a flash loader problem."
status: "draft"
tool: "pyocd"
symptoms: ["C Error: Memory regions must have a non-zero length. [__main__]"]
symptom_regex: "C\\s+Error:\\s+Memory\\s+regions\\s+must\\s+have\\s+a\\s+non\\-zero\\s+length\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1847"
doc_source: "https://github.com/pyocd/pyOCD/issues/1847"
resolution: "fixed-in-release"
versions: "fixed in DFP 2025.12.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "family": ["EFR32BG22"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Error: Memory regions must have a non-zero length. [__main__]`

## Cause

The Silicon Labs DFP 2025.6.2 contained a faulty memory region definition and a flash loader problem.

## Fix

Install the DFP version 2025.12.1 or later, which fixes both. Passing -O adi.v5.max_invalid_ap_count=0 helped with non-responsive APs during enumeration.

## Source

Resolution: fixed-in-release

Versions: fixed in DFP 2025.12.1

From [pyocd/pyOCD #1847](https://github.com/pyocd/pyOCD/issues/1847), summarized in own words; confidence high, checked against the thread, not reviewed yet.
