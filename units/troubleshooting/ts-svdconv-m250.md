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
---

## Symptom

`M250`
`Dimension '%NAME%' has an invalid or overflowing index/address range.`

## Cause

Correct the dimension range or increment.

## Fix

_see Cause_
