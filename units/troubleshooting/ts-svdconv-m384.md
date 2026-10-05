---
id: "ts-svdconv-m384"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M384: Number of PMU Event Counters (found val: '…') not set or outside range [2..31]. Ignoring PMU entry."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M384"
symptoms: ["M384", "Number of PMU Event Counters (found val: '%NUM%') not set or outside range [2..31]. Ignoring PMU entry."]
symptom_regex: "^Number of PMU Event Counters \\(found val: '.+?'\\) not set or outside range \\[2\\.\\.31\\]\\. Ignoring PMU entry\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "<cpu> has <pmuPresent>true</pmuPresent> for a core that has a PMU, but <pmuNumEventCnt> is missing or outside the accepted range. svdconv then ignores the PMU entry."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:360-372", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:197-230", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:205"]
---

## Symptom

`M384`
`Number of PMU Event Counters (found val: '%NUM%') not set or outside range [2..31]. Ignoring PMU entry.`

## Cause

<cpu> has <pmuPresent>true</pmuPresent> for a core that has a PMU, but <pmuNumEventCnt> is missing or outside the accepted range. svdconv then ignores the PMU entry.

## Fix

Add <pmuNumEventCnt> with the number of PMU event counters of the core, a value from 2 to 31, e.g. <pmuNumEventCnt>8</pmuNumEventCnt>.

## Note

The message says [2..31] but the check rejects only <2 or >32, so 32 passes (SvdCpu.cpp:368). pmuPresent and pmuNumEventCnt are parsed by svdconv but are not in the CMSIS-SVD.xsd 1.3.9 of CMSIS 5.9.0.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:360-372`
- `tools/svdconv/test/unittests/src/SvdCpuModelTest.cpp:197-230`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:205`
