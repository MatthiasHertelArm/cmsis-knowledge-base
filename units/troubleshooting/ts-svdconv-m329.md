---
id: "ts-svdconv-m329"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M329: CPU Type is not set, using default (Cortex-M3)"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M329"
symptoms: ["M329", "CPU Type is not set, using default (Cortex-M3)"]
symptom_regex: "^CPU Type is not set, using default \\(Cortex\\-M3\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The <cpu> section has no <name>, or a name svdconv does not know (then M202 is reported as well). svdconv falls back to Cortex-M3 and its limits, for example 240 external interrupts."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:89", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:332", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:795", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/include/EnumStringTables.h:16", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:211", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:148"]
---

## Symptom

`M329`
`CPU Type is not set, using default (Cortex-M3)`

## Cause

The <cpu> section has no <name>, or a name svdconv does not know (then M202 is reported as well). svdconv falls back to Cortex-M3 and its limits, for example 240 external interrupts.

## Fix

Set <cpu><name> to a supported core, for example CM0, CM0PLUS, CM3, CM4, CM7, CM23, CM33, CM35P, CM55 or CM85.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:89`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:332`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:795`
- `tools/svdconv/SVDModel/include/EnumStringTables.h:16`
- `tools/svdconv/test/unittests/src/SvdInterruptTest.cpp:211`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:148`
