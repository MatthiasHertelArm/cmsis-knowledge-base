---
id: "ts-svdconv-m243"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M243: … '…' <dimArrayIndex> found, but <dim> does not describe an array"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M243"
symptoms: ["M243", "%LEVEL% '%NAME%' <dimArrayIndex> found, but <dim> does not describe an array"]
symptom_regex: "^.+? '.+?' <dimArrayIndex> found, but <dim> does not describe an array$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "The SVD contains a dimArrayIndex element on a register, cluster or field, but no dim element (or dim set to a value that does not define an array) for the same node. svdconv warns that the array index description …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M243`
`%LEVEL% '%NAME%' <dimArrayIndex> found, but <dim> does not describe an array`

## Cause

The SVD contains a dimArrayIndex element on a register, cluster or field, but no dim element (or dim set to a value that does not define an array) for the same node. svdconv warns that the array index description is ignored because the node is not an array. The %LEVEL% and %NAME% placeholders are the element kind and name where the mismatch was found.

## Fix

Open the SVD at the element named in the message and either add a valid dim element (number of array entries) to make it an array, or remove the dimArrayIndex element if the register is not meant to be an array. Then rerun svdconv.

## Note

Only the message text and the trigger were available, not the surrounding source lines, so the exact trigger condition is inferred. The README cause text 'Correct SVD' is not specific; this entry sharpens it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
