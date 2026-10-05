---
id: "iss-devtools-2569"
type: "troubleshooting"
domain: "pack"
title: "svdconv: SVDConv M227 says enumerated values exceed 256 elements for narrow fields"
summary: "The real limit for generating enumerated value lists for the SFR/MDK5 output is a field width of 6 bits (64 entries), chosen to keep the debugger combo box usable."
status: "draft"
tool: "svdconv"
symptoms: ["SFD Code generation warning: Enumerated values list for field 'MYFIELD1' exeeds maximum of 256 elements. List will not be generated."]
symptom_regex: "SFD\\s+Code\\s+generation\\s+warning:\\s+Enumerated\\s+values\\s+list\\s+for\\s+field\\s+'.*?'\\s+exeeds\\s+maximum\\s+of\\s+\\S+\\s+elements\\.\\s+List\\s+will\\s+not\\s+be\\s+generated\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2569"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2569"
resolution: "fixed-in-release"
versions: "seen in 3.3.39 to 3.3.50"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`SFD Code generation warning: Enumerated values list for field 'MYFIELD1' exeeds maximum of 256 elements. List will not be generated.`

## Cause

The real limit for generating enumerated value lists for the SFR/MDK5 output is a field width of 6 bits (64 entries), chosen to keep the debugger combo box usable. The message wrongly named 256 entries.

## Fix

The message now states the field width and the 6-bit limit. For wide fields describe the unlisted values with an enumeratedValue carrying isDefault true, which other tools can interpret without a full list. Message corrected in the svdconv shipped after 3.3.50.

## Source

Resolution: fixed-in-release

Versions: seen in 3.3.39 to 3.3.50

From [Open-CMSIS-Pack/devtools #2569](https://github.com/Open-CMSIS-Pack/devtools/issues/2569), summarized in own words; confidence high, not reviewed yet.
