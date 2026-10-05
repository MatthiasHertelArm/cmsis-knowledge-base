---
id: "ts-svdconv-m364"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M364: CPU: <sauNumRegions> value '…' greater than SAU max num (…)"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M364"
symptoms: ["M364", "CPU: <sauNumRegions> value '%NUM%' greater than SAU max num (%NUM2%)"]
symptom_regex: "^CPU: <sauNumRegions> value '.+?' greater than SAU max num \\(.+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:347", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:349", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:350", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/include/SvdCpu.h:11", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:355", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:255", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:183"]
---

## Symptom

`M364`
`CPU: <sauNumRegions> value '%NUM%' greater than SAU max num (%NUM2%)`

## Cause

<cpu><sauNumRegions> is greater than 255, the most svdconv allows. The value is discarded together with the SAU region configuration, so generating the partition file then also reports M219 ('Number of SAU regions not set').

## Fix

Set <sauNumRegions> to the number of SAU regions the device really implements (at most 255).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:347`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:349`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:350`
- `tools/svdconv/SVDModel/include/SvdCpu.h:11`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:355`
- `tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:255`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:183`
