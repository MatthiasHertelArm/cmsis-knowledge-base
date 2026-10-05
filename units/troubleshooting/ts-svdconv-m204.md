---
id: "ts-svdconv-m204"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M204: Parse Error: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M204"
symptoms: ["M204", "Parse Error: '%VALUE%'"]
symptom_regex: "^Parse Error: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check value."
summary: "<cpu><revision> is not of the form rNpM with N and M from 0 to 255 (e.g. r0p1). svdconv also reports M325 because no valid revision is set."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:58-67", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:246-287", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:102-110", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:192-200", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:71"]
---

## Symptom

`M204`
`Parse Error: '%VALUE%'`

## Cause

<cpu><revision> is not of the form rNpM with N and M from 0 to 255 (e.g. r0p1). svdconv also reports M325 because no valid revision is set.

## Fix

Write the core revision as rNpM (N = major, M = minor revision), for example <revision>r1p0</revision>.

## Note

SvdDimension.cpp:360-363, 393-395 and 425-427 also log M204 for an invalid name/displayName/description expression, but the parser never returns that result at this commit.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:58-67`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:246-287`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:102-110`
- `tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:192-200`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:71`
