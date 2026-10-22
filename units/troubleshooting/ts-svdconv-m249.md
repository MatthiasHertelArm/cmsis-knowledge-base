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
summary: "The SVD input declares a dimension (a dim array, for example a register or peripheral replicated with dimIncrement and dim) whose expansion produces more generated indices and model copies than svdconv allows for one input file."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M249`
`Dimension expansion exceeds the per-input limit of %NUM% generated indices and model copies.`

## Cause

The SVD input declares a dimension (a dim array, for example a register or peripheral replicated with dimIncrement and dim) whose expansion produces more generated indices and model copies than svdconv allows for one input file. The %NUM% in the message is the limit value. The source lines were not available, so this is inferred from the message text and the general meaning of dimension expansion, not checked against the code.

## Fix

Check the dim and dimIndex elements of the SVD input for very large dimension counts or nested dimension arrays and reduce them, or split the dimension array into smaller groups that stay under the limit. Then rerun svdconv on the corrected file.

## Note

The source lines were not provided, so the trigger condition and the exact limit could not be verified; the cause and fix above are an inference from the message text and should be confirmed against the README and the source before relying on them.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
