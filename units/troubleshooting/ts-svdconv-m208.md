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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Generate an array."
summary: "The SVD register or cluster has a dimIndex element, but the tool was asked to generate something that requires array generation for the named item, so the dimIndex is dropped."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)"]
---

## Symptom

`M208`
`Ignoring <dimIndex> because specified <name> requires Array generation.`

## Cause

The SVD register or cluster has a dimIndex element, but the tool was asked to generate something that requires array generation for the named item, so the dimIndex is dropped. The README attributes it to the request to generate an array, which is the only cause the documentation gives.

## Fix

Check the SVD entry named in the message: if a dimIndex is present and array output is not wanted, remove the dimIndex element; if array output is wanted, enable array generation for that item in the svdconv configuration so the dimIndex is honoured.

## Note

Source lines were not available, so the trigger condition and the exact option name for enabling array generation are not verified. The fix wording is inferred from the message and README and should be confirmed against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)`
