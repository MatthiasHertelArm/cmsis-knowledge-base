---
id: "ts-svdconv-m383"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M383: Number of PMU Event Counters set but PMU present not set"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M383"
symptoms: ["M383", "Number of PMU Event Counters set but PMU present not set"]
symptom_regex: "^Number of PMU Event Counters set but PMU present not set$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:203-215", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:373-375", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:246-256", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:204"]
---

## Symptom

`M383`
`Number of PMU Event Counters set but PMU present not set`

## Cause

<cpu> sets <pmuNumEventCnt> but <pmuPresent> is missing or false, so the counter number has nothing to apply to.

## Fix

Add <pmuPresent>true</pmuPresent> to <cpu> if the core has a PMU, or remove <pmuNumEventCnt>.

## Note

pmuPresent and pmuNumEventCnt are parsed by svdconv (SvdCpu.cpp:203-215) but are not in the CMSIS-SVD.xsd 1.3.9 shipped with CMSIS 5.9.0; they belong to a later schema version. The message has no line number.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:203-215`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:373-375`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:246-256`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:204`
