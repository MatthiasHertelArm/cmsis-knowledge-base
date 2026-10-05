---
id: "ts-svdconv-m308"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M308: Number of <dimIndex> Elements '…' is different to number of <dim> instances '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M308"
symptoms: ["M308", "Number of <dimIndex> Elements '%NUM%' is different to number of <dim> instances '%NUM2%'"]
symptom_regex: "^Number of <dimIndex> Elements '.+?' is different to number of <dim> instances '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:193", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:212", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:564", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:567", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:283", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:127"]
---

## Symptom

`M308`
`Number of <dimIndex> Elements '%NUM%' is different to number of <dim> instances '%NUM2%'`

## Cause

An element with <dim> (register, cluster, field or peripheral) has a comma-separated <dimIndex> list whose number of entries differs from <dim>.

## Fix

Make <dim> equal to the number of <dimIndex> entries, for example <dim>3</dim> with <dimIndex>A,B,C</dimIndex>, and check that <dimIncrement> matches the spacing of the instances.

## Note

Ranges such as 0-3 or A-D are not counted here: a range whose length differs from <dim> silently yields no index list and no M308.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDimension.cpp:193`
- `tools/svdconv/SVDModel/src/SvdDimension.cpp:212`
- `tools/svdconv/SVDModel/src/SvdDimension.cpp:564`
- `tools/svdconv/SVDModel/src/SvdDimension.cpp:567`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:283`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:127`
