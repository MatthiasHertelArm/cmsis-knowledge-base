---
id: "ts-svdconv-m242"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M242: … '…' <dimArrayIndex> found, but no <dim>"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M242"
symptoms: ["M242", "%LEVEL% '%NAME%' <dimArrayIndex> found, but no <dim>"]
symptom_regex: "^.+? '.+?' <dimArrayIndex> found, but no <dim>$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "The SVD file contains a dimArrayIndex element for a register, cluster or field named by the message, but no matching dim element is present."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M242`
`%LEVEL% '%NAME%' <dimArrayIndex> found, but no <dim>`

## Cause

The SVD file contains a dimArrayIndex element for a register, cluster or field named by the message, but no matching dim element is present. In SVD the dimArrayIndex only has meaning when the dim element that declares the array size and increment is also given, so the tool flags the orphaned index. The exact placeholder meanings for LEVEL and NAME are not verifiable here since the source lines were not available.

## Fix

Open the SVD entry named in the message and either add the dim element that goes with the dimArrayIndex (dim, dimIncrement and dimIndex for that element), or remove the dimArrayIndex if the element is not an array. Then rerun svdconv.

## Note

The source clone was not available, so the trigger condition and placeholder meanings are inferred from the message text and the README cause (Correct SVD) only. The README cause is generic and was sharpened with the SVD dim/dimArrayIndex relationship from the SVD standard, not from source lines.
