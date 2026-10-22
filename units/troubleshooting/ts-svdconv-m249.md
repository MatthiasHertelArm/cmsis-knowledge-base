---
id: "ts-svdconv-m249"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M249: Dimension expansion exceeds the per-input limit of … generated indices and model copies."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M249"
symptoms: ["M249", "Dimension expansion exceeds the per-input limit of %NUM% generated indices and model copies."]
symptom_regex: "^Dimension expansion exceeds the per\\-input limit of .+? generated indices and model copies\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Reduce the total expanded model size."
summary: "svdconv expands dim arrays in the SVD (dim, dimIncrement, dimIndex) into individual register or peripheral copies."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the provided lines)"]
---

## Symptom

`M249`
`Dimension expansion exceeds the per-input limit of %NUM% generated indices and model copies.`

## Cause

svdconv expands dim arrays in the SVD (dim, dimIncrement, dimIndex) into individual register or peripheral copies. The message is printed when the number of generated indices exceeds a fixed per-input limit, which is named in the message as %NUM%. The README attributes it to a large total expanded model size, so the SVD likely contains a dim value that is very large or several nested or stacked dim arrays that multiply together.

## Fix

Reduce the total number of expanded entries in the SVD: lower the dim count on the large dim arrays, or split the input into smaller SVD files so each stays under the limit. Then rerun svdconv on the reduced input.

## Note

The clone was not available, so the trigger condition and the exact limit could not be checked against the source. The cause is inferred from the message text and the README only. The message contains a %NUM% placeholder which the tool fills with the limit value.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the provided lines)`
