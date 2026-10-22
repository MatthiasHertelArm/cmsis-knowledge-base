---
id: "ts-svdconv-m231"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M231: Value <isDefault> not allowed for …."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M231"
symptoms: ["M231", "Value <isDefault> not allowed for %LEVEL%."]
symptom_regex: "^Value <isDefault> not allowed for .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "An <enumeratedValue> inside <dimArrayIndex> uses <isDefault>."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdEnum.cpp:152-160", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:207-218", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:98"]
---

## Symptom

`M231`
`Value <isDefault> not allowed for %LEVEL%.`

## Cause

An <enumeratedValue> inside <dimArrayIndex> uses <isDefault>. Each array index needs its own explicit <value>, so svdconv drops that enumeratedValue.

## Fix

Replace the <isDefault>true</isDefault> entry with one <enumeratedValue> per array index, each with an explicit <value>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdEnum.cpp:152-160`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:207-218`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:98`
