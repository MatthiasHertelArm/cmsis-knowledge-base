---
id: "ts-svdconv-m248"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M248: C Expression: Referenced Object must be Register or Field!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M248"
symptoms: ["M248", "C Expression: Referenced Object must be Register or Field!"]
symptom_regex: "^C Expression: Referenced Object must be Register or Field!$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A name in a peripheral's <disableCondition> resolves to a peripheral or cluster instead of a register or field, for example 'DCB == 0' or a path that stops at a cluster."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:94", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:104", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:35", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/data/disablecondition/DisableCondTest.svd:85"]
---

## Symptom

`M248`
`C Expression: Referenced Object must be Register or Field!`

## Cause

A name in a peripheral's <disableCondition> resolves to a peripheral or cluster instead of a register or field, for example 'DCB == 0' or a path that stops at a cluster. Only register and field values can be evaluated, so the disable condition is dropped.

## Fix

Extend the path down to a register or field, for example DCB->DSCSR->CDS == 0 or DCB->DSCSR_Clust->DSCSR->CDS == 0 (with '->' escaped as '-&gt;' in XML).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:94`
- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:104`
- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:35`
- `tools/svdconv/test/data/disablecondition/DisableCondTest.svd:85`
