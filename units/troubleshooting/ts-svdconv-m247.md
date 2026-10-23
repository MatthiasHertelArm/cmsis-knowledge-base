---
id: "ts-svdconv-m247"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M247: C Expression: Error occurred during generation!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M247"
symptoms: ["M247", "C Expression: Error occurred during generation!"]
symptom_regex: "^C Expression: Error occurred during generation!$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "While writing the System Viewer (SFD) file, an operand of a peripheral's <disableCondition> resolved to an SVD element that is neither a register nor a field, and svdconv wrote '<Error in expression Object>' in its place."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:162", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:163", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:94", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:221"]
---

## Symptom

`M247`
`C Expression: Error occurred during generation!`

## Cause

While writing the System Viewer (SFD) file, an operand of a peripheral's <disableCondition> resolved to an SVD element that is neither a register nor a field, and svdconv wrote '<Error in expression Object>' in its place. Such operands are normally rejected earlier with M248; M247 is the fallback when that check did not apply.

## Fix

Change the operand to a path that ends at a register or field, for example PERIPH->REG or PERIPH->REG->FIELD (escaped as -&gt; in XML).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:162`
- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:163`
- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:94`
- `tools/svdconv/SVDGenerator/src/SfdData_SingleItems.cpp:221`
