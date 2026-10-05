---
id: "iss-devtools-1264"
type: "troubleshooting"
domain: "pack"
title: "svdconv: SVDConv M382 reset mask does not fit for a 64-bit register"
summary: "The check of the reset mask against the register width was calculated wrongly for 64-bit registers."
status: "draft"
tool: "svdconv"
symptoms: ["*** WARNING M382: RESET_MASK.svd (Line 51)\n  Register 'ABS': Reset Mask '0xFFFFFFFFFFFFFFFF' does not fit into Register width: 64 Bit."]
symptom_regex: "RESET_MASK\\.svd\\s+\\(Line\\s+\\S+\\)\\\\s+Register\\s+'.*?':\\s+Reset\\s+Mask\\s+'.*?'\\s+does\\s+not\\s+fit\\s+into\\s+Register\\s+width:\\s+\\S+\\s+Bit\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1264"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1264"
resolution: "fixed-in-release"
versions: "3.3.46"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** WARNING M382: RESET_MASK.svd (Line 51)
  Register 'ABS': Reset Mask '0xFFFFFFFFFFFFFFFF' does not fit into Register width: 64 Bit.`

## Cause

The check of the reset mask against the register width was calculated wrongly for 64-bit registers.

## Fix

Fixed in a later SVDConv release (64-bit mask calculation corrected). Note that 64-bit registers are not officially supported by svdconv.

## Source

Resolution: fixed-in-release

Versions: 3.3.46

From [Open-CMSIS-Pack/devtools #1264](https://github.com/Open-CMSIS-Pack/devtools/issues/1264), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
