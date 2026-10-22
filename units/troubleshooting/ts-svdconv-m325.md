---
id: "ts-svdconv-m325"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M325: CPU Revision is not set"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M325"
symptoms: ["M325", "CPU Revision is not set"]
symptom_regex: "^CPU Revision is not set$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The <cpu> section has no <revision>, or its value is not of the form rNpM (for example r0p1, both numbers 0 to 255); a malformed value is also reported as M204."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:58", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:65", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:98", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:318", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:246", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:102", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:112", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:144"]
---

## Symptom

`M325`
`CPU Revision is not set`

## Cause

The <cpu> section has no <revision>, or its value is not of the form rNpM (for example r0p1, both numbers 0 to 255); a malformed value is also reported as M204.

## Fix

Add the core revision to <cpu>, for example <revision>r0p1</revision>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:58`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:65`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:98`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:318`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:246`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:102`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:112`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:144`
