---
id: "ts-svdconv-m231"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M231: Value <isDefault> not allowed for …."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M231"
symptoms: ["M231", "Value <isDefault> not allowed for %LEVEL%."]
symptom_regex: "^Value <isDefault> not allowed for .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "The SVD input contains an isDefault attribute on an element where svdconv does not accept it, so the tool rejects the value."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M231`
`Value <isDefault> not allowed for %LEVEL%.`

## Cause

The SVD input contains an isDefault attribute on an element where svdconv does not accept it, so the tool rejects the value. The message names the offending value and the element level (the %LEVEL% placeholder) where it appeared.

## Fix

Remove the isDefault attribute from the element named at that level in the SVD file, or move it to the level the SVD schema allows, then rerun svdconv. The README gives only 'Correct SVD', so check the SVD against the CMSIS-SVD schema for where isDefault is permitted.

## Note

Source lines were not available, so the trigger condition and the exact allowed levels are unverified. The README cause is generic. The message text alone indicates an isDefault attribute placed on an element that does not accept it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
