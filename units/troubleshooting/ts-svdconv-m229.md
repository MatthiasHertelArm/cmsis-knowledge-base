---
id: "ts-svdconv-m229"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M229: Register '…' is not an array, <dimArrayIndex> is not applicable"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M229"
symptoms: ["M229", "Register '%NAME%' is not an array, <dimArrayIndex> is not applicable"]
symptom_regex: "^Register '.+?' is not an array, <dimArrayIndex> is not applicable$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "The SVD register named in the message has a dimArrayIndex element but no dim element that makes it an array, so svdconv rejects the index definition."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M229`
`Register '%NAME%' is not an array, <dimArrayIndex> is not applicable`

## Cause

The SVD register named in the message has a dimArrayIndex element but no dim element that makes it an array, so svdconv rejects the index definition. The README only says the SVD is incorrect, which is consistent with this, but the exact trigger condition could not be checked against the source here.

## Fix

Open the SVD file at the register named in the message and check its dimArrayIndex element. Either add the matching dim (array count) and dimIncrement elements to make the register an array, or remove the dimArrayIndex element if the register is not meant to be an array.

## Note

The clone was not available, so the trigger was not read from the source. The cause and fix come from the message text and the README's one-line cause only. The README's cause 'Correct SVD' is not specific enough on its own.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
