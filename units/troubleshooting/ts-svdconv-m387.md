---
id: "ts-svdconv-m387"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M387: CPU: <sauNumRegions> set to 0 but regions are configured."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M387"
symptoms: ["M387", "CPU: <sauNumRegions> set to 0 but regions are configured."]
symptom_regex: "^CPU: <sauNumRegions> set to 0 but regions are configured\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "<cpu> contains a <sauRegionsConfig> but <sauNumRegions> is 0. svdconv ignores the SAU region configuration."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:337-346", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:343-353", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:208"]
---

## Symptom

`M387`
`CPU: <sauNumRegions> set to 0 but regions are configured.`

## Cause

<cpu> contains a <sauRegionsConfig> but <sauNumRegions> is 0. svdconv ignores the SAU region configuration.

## Fix

Set <sauNumRegions> to the number of SAU regions the device implements (at least the number of <region> entries), or remove <sauRegionsConfig> if the device has no SAU.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:337-346`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:343-353`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:208`
