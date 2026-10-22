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
summary: "svdconv prints this error when a <dim> element in the SVD file describes an array of registers or peripherals whose index list or address range is invalid or runs past the addressable space; the %NAME% placeholder is the name …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M250`
`Dimension '%NAME%' has an invalid or overflowing index/address range.`

## Cause

svdconv prints this error when a <dim> element in the SVD file describes an array of registers or peripherals whose index list or address range is invalid or runs past the addressable space; the %NAME% placeholder is the name of the dimensioned element. The exact trigger is not available here, so this is inferred from the message text alone.

## Fix

Open the SVD file, find the <dim> entry for the named element, and check that <dim> (the number of elements), <dimIncrement> and, if present, <dimIndex> are consistent with each other and do not place the last element beyond the peripheral's address space. Correct the values and rerun svdconv.

## Note

Trigger lines were not available; the cause and fix are inferred from the message wording and should be checked against the source. The README documents this message, but its text was not provided here.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
