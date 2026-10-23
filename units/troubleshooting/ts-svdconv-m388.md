---
id: "ts-svdconv-m388"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M388: MVE Floating-Point support is set but MVE is not set"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M388"
symptoms: ["M388", "MVE Floating-Point support is set but MVE is not set"]
symptom_regex: "^MVE Floating\\-Point support is set but MVE is not set$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "<cpu> sets <mveFP> to true while <mvePresent> is missing or false; MVE floating point requires MVE."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:216-228", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCpu.cpp:377-381", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:209"]
---

## Symptom

`M388`
`MVE Floating-Point support is set but MVE is not set`

## Cause

<cpu> sets <mveFP> to true while <mvePresent> is missing or false; MVE floating point requires MVE.

## Fix

Add <mvePresent>true</mvePresent> to <cpu> when the core implements MVE with floating point, or set <mveFP> to false (or remove it) for an integer-only or no-MVE configuration.

## Note

Dead check at 30f5e81: the test (m_mveFP && !m_mvePresent) sits inside if(m_mvePresent), so svdconv never reports M388. mvePresent and mveFP are not in the CMSIS-SVD.xsd 1.3.9 of CMSIS 5.9.0.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCpu.cpp:216-228`
- `tools/svdconv/SVDModel/src/SvdCpu.cpp:377-381`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:209`
