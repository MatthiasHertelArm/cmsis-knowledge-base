---
id: "ts-svdconv-m327"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M327: NVIC Prio Bits not set or wrong value, must be 2..8. Using default (4)"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M327"
symptoms: ["M327", "NVIC Prio Bits not set or wrong value, must be 2..8. Using default (4)"]
symptom_regex: "^NVIC Prio Bits not set or wrong value, must be 2\\.\\.8\\. Using default \\(4\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The <cpu> section has no <nvicPrioBits>, or its value is outside 2..8; svdconv uses 4."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:129", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:326", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:327", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:220", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:125", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:146"]
---

## Symptom

`M327`
`NVIC Prio Bits not set or wrong value, must be 2..8. Using default (4)`

## Cause

The <cpu> section has no <nvicPrioBits>, or its value is outside 2..8; svdconv uses 4. The value becomes __NVIC_PRIO_BITS in the generated header.

## Fix

Add <nvicPrioBits> with the number of NVIC priority bits the device implements, for example <nvicPrioBits>3</nvicPrioBits>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:129`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:326`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:327`
- `tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:220`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:125`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:146`
