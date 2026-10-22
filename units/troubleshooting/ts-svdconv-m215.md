---
id: "ts-svdconv-m215"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M215: Size of <dim> is only one element for '…', is this intended?"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M215"
symptoms: ["M215", "Size of <dim> is only one element for '%NAME%', is this intended?"]
symptom_regex: "^Size of <dim> is only one element for '.+?', is this intended\\?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check single element."
summary: "The SVD register or peripheral description declares a dimension (dim) with only one element for the named item, which is usually unintended because a single-element dimension array adds nothing."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M215`
`Size of <dim> is only one element for '%NAME%', is this intended?`

## Cause

The SVD register or peripheral description declares a dimension (dim) with only one element for the named item, which is usually unintended because a single-element dimension array adds nothing. The warning names the item through the NAME placeholder. The source lines were not available, so this reading relies on the message text and the README note only.

## Fix

Open the SVD file at the element named in the message and check its dimElement/dim settings. If the dim value of 1 is a mistake, remove the dim and dimIncrement elements (or set dim to the intended count). If a single element is deliberate, the warning can be accepted as intended.

## Note

Trigger lines were not available; the cause and fix are inferred from the message text and the README's one-line cause. Confidence capped at medium.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
