---
id: "iss-pyocd-1150"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Wall of warnings on 'pyocd pack -u' and a missing STM32G0 pack"
summary: "Many vendor packs contain malformed PDSC data and the underlying cmsis-pack-manager prints a warning for each; it also did not know the preIncludeLocal file category."
status: "draft"
tool: "pyocd"
symptoms: ["WARN the XML is invalid, an element was wrongly closed", "WARN Unknown file catogory preIncludeLocal, Group: Unity, Class: Tes"]
symptom_regex: "the\\s+XML\\s+is\\s+invalid,\\s+an\\s+element\\s+was\\s+wrongly\\s+closed"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1150"
doc_source: "https://github.com/pyocd/pyOCD/issues/1150"
resolution: "workaround"
versions: "seen with pyocd 0.30.3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["STM32G071RB"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`WARN the XML is invalid, an element was wrongly closed`
`WARN Unknown file catogory preIncludeLocal, Group: Unity, Class: Tes`

## Cause

Many vendor packs contain malformed PDSC data and the underlying cmsis-pack-manager prints a warning for each; it also did not know the preIncludeLocal file category. With 0.30.3 the STM32G071 device was additionally not found through the index.

## Fix

The warnings are harmless. If the device is not found, download the DFP .pack file manually and pass it with `--pack <file.pack>`; later pyOCD/pack-manager releases find Keil.STM32G0xx_DFP normally.

## Source

Resolution: workaround

Versions: seen with pyocd 0.30.3

From [pyocd/pyOCD #1150](https://github.com/pyocd/pyOCD/issues/1150), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
