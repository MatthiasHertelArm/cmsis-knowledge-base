---
id: "ts-svdconv-m250"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M250: Dimension '…' has an invalid or overflowing index/address range."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M250"
symptoms: ["M250", "Dimension '%NAME%' has an invalid or overflowing index/address range."]
symptom_regex: "^Dimension '.+?' has an invalid or overflowing index/address range\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct the dimension range or increment."
summary: "svdconv prints this error when a dimension element (dim, dimIndex, dimIncrement) in the SVD file describes an index or address range that is invalid or overflows the address space for the named dimension."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M250`
`Dimension '%NAME%' has an invalid or overflowing index/address range.`

## Cause

svdconv prints this error when a dimension element (dim, dimIndex, dimIncrement) in the SVD file describes an index or address range that is invalid or overflows the address space for the named dimension. The %NAME% placeholder is the name of the peripheral, register or cluster whose dimension is at fault. The exact trigger condition could not be checked because the source lines were not available, so this is inferred from the message text.

## Fix

Open the SVD file, find the element named in the message, and check its dimension settings: dim (count), dimIncrement (step between entries) and dimIndex (index list or range). Make sure the count and increment keep every generated address inside the peripheral's address block, and that dimIndex values are consistent with dim. Correct the values and run svdconv again.

## Note

Source lines were unavailable, so the trigger and the user-facing cause are inferred from the message text only. The stated cause and fix should be verified against the actual check in SVDConv_Msgs.cpp and its caller before relying on them.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
