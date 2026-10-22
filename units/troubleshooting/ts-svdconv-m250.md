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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct the dimension range or increment."
summary: "svdconv found a dimension element in the SVD whose index range or dimIncrement produces addresses or indexes that are invalid or that overflow the address space."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M250 text; trigger lines not provided)"]
---

## Symptom

`M250`
`Dimension '%NAME%' has an invalid or overflowing index/address range.`

## Cause

svdconv found a dimension element in the SVD whose index range or dimIncrement produces addresses or indexes that are invalid or that overflow the address space. The name shown in the message is the dimension name from the SVD. The source lines were not available, so this is inferred from the message text and the README cause only.

## Fix

Open the SVD and check the named dimension: dim (number of entries), dimIncrement and, if present, dimIndex. Make sure the range of dim entries times dimIncrement fits within the parent register or peripheral address space and that dimIndex values are valid and not overflowing. Correct the dim or dimIncrement values and rerun svdconv.

## Note

Trigger condition and exact check not verified against source because the clone was unavailable; cause and fix rely on the message text and the README entry 'Correct the dimension range or increment.'

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M250 text; trigger lines not provided)`
