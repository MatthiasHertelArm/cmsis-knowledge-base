---
id: "ts-svdconv-m391"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M391: CPU: configured number of SAU regions '…' greater than <sauNumRegions> value: '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M391"
symptoms: ["M391", "CPU: configured number of SAU regions '%NUM%' greater than <sauNumRegions> value: '%NUM2%'"]
symptom_regex: "^CPU: configured number of SAU regions '.+?' greater than <sauNumRegions> value: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:348-358", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:367-380", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:212"]
---

## Symptom

`M391`
`CPU: configured number of SAU regions '%NUM%' greater than <sauNumRegions> value: '%NUM2%'`

## Cause

<cpu><sauRegionsConfig> lists more <region> entries than <sauNumRegions> allows.

## Fix

Raise <sauNumRegions> to the number of SAU regions the device has, or remove the surplus <region> entries.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:348-358`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:367-380`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:212`
