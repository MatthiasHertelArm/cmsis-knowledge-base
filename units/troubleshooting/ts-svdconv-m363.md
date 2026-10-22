---
id: "ts-svdconv-m363"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M363: CPU: <sauNumRegions> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M363"
symptoms: ["M363", "CPU: <sauNumRegions> not set."]
symptom_regex: "^CPU: <sauNumRegions> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "<cpu> contains <sauRegionsConfig> but no <sauNumRegions>."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:196", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:336", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:338", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:331", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:182"]
---

## Symptom

`M363`
`CPU: <sauNumRegions> not set.`

## Cause

<cpu> contains <sauRegionsConfig> but no <sauNumRegions>. The SAU region configuration is dropped.

## Fix

Add <sauNumRegions> to <cpu> with the number of SAU regions the device implements (1 to 255; 0 together with configured regions gives M387).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:196`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:336`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:338`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:331`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:182`
