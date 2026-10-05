---
id: "ts-svdconv-m208"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M208: Ignoring <dimIndex> because specified <name> requires Array generation."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M208"
symptoms: ["M208", "Ignoring <dimIndex> because specified <name> requires Array generation."]
symptom_regex: "^Ignoring <dimIndex> because specified <name> requires Array generation\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Generate an array."
summary: "A dim element uses the array form [%s] in its <name> and also has <dimIndex>."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:182-240", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:75", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:222"]
---

## Symptom

`M208`
`Ignoring <dimIndex> because specified <name> requires Array generation.`

## Cause

A dim element uses the array form [%s] in its <name> and also has <dimIndex>. Arrays are always indexed 0..dim-1, so svdconv ignores the <dimIndex>.

## Fix

Remove <dimIndex>, or, if the custom indices are wanted, switch to the list form with %s (e.g. <name>CH%s</name>), which creates separate elements named with the <dimIndex> values.

## Note

Error under --strict. Not raised for elements that got the dim data through derivedFrom.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDimension.cpp:182-240`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:75`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:222`
