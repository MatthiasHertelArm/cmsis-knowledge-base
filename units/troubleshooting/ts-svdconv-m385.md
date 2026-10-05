---
id: "ts-svdconv-m385"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M385: PMU not supported for CPU '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M385"
symptoms: ["M385", "PMU not supported for CPU '%NAME%'"]
symptom_regex: "^PMU not supported for CPU '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:360-367", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdTypes.cpp:104-135", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:232-244", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:206"]
---

## Symptom

`M385`
`PMU not supported for CPU '%NAME%'`

## Cause

<cpu> sets <pmuPresent>true</pmuPresent> but the core named in <cpu><name> has no PMU in svdconv's CPU table; only CM52, CM55, CM85, ARMV81MML, SMC2 and SMC3 have one. svdconv drops the PMU setting.

## Fix

Remove <pmuPresent> and <pmuNumEventCnt> for this core, or correct <cpu><name> if the device really uses a core with a PMU (e.g. CM55 or CM85).

## Note

No line number in the message. pmuPresent and pmuNumEventCnt are parsed by svdconv but are not in the CMSIS-SVD.xsd 1.3.9 of CMSIS 5.9.0.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:360-367`
- `tools/svdconv/SVDModel/src/SvdTypes.cpp:104-135`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:232-244`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:206`
