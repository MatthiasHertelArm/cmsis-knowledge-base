---
id: "ts-svdconv-m326"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M326: Endianess is not set, using default (little)"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M326"
symptoms: ["M326", "Endianess is not set, using default (little)"]
symptom_regex: "^Endianess is not set, using default \\(little\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The <cpu> section has no <endian> element; svdconv assumes little-endian."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:102", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:321", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:322", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:112", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:145"]
---

## Symptom

`M326`
`Endianess is not set, using default (little)`

## Cause

The <cpu> section has no <endian> element; svdconv assumes little-endian.

## Fix

Add <endian>little</endian> to <cpu> (other allowed values: big, selectable, other).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:102`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:321`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:322`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:112`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:145`
