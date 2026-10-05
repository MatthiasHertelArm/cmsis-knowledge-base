---
id: "iss-devtools-2569"
type: "troubleshooting"
domain: "pack"
title: "svdconv: SVDConv M227 says enumerated values exceed 256 elements for narrow fields"
summary: "The real limit for generating enumerated value lists in the SfrCC/MDK5 output is a field width of 6 bits (64 entries), chosen to keep the combo-box control usable; the M227 message wrongly named 256 entries."
status: "draft"
tool: "svdconv"
symptoms: ["SFD Code generation warning: Enumerated values list for field 'MYFIELD1' exeeds maximum of 256 elements. List will not be generated."]
symptom_regex: "SFD\\s+Code\\s+generation\\s+warning:\\s+Enumerated\\s+values\\s+list\\s+for\\s+field\\s+'.*?'\\s+exeeds\\s+maximum\\s+of\\s+\\S+\\s+elements\\.\\s+List\\s+will\\s+not\\s+be\\s+generated\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2569"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2569"
resolution: "fixed-in-release"
versions: "svdconv 3.3.39 and 3.3.50 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`SFD Code generation warning: Enumerated values list for field 'MYFIELD1' exeeds maximum of 256 elements. List will not be generated.`

## Cause

The real limit for generating enumerated value lists in the SfrCC/MDK5 output is a field width of 6 bits (64 entries), chosen to keep the combo-box control usable; the M227 message wrongly named 256 entries.

## Fix

The M227 message was corrected to state the field width and the 6-bit limit (available in a CMSIS-Toolbox nightly). Unlisted values can be described with an enumeratedValue carrying isDefault true; SVDConv expands it for SfrCC/MDK5, while other tools can interpret it directly for fields wider than 6 bits.

## Source

Resolution: fixed-in-release

Versions: svdconv 3.3.39 and 3.3.50 affected

From [Open-CMSIS-Pack/devtools #2569](https://github.com/Open-CMSIS-Pack/devtools/issues/2569), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
