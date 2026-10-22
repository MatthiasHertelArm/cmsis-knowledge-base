---
id: "ts-svdconv-m239"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M239: Dim-ed … '…' must have an expression."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M239"
symptoms: ["M239", "Dim-ed %LEVEL% '%NAME%' must have an expression."]
symptom_regex: "^Dim\\-ed .+? '.+?' must have an expression\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "An element has <dim> but its <name> contains no placeholder: neither %s nor [%s] at the end. svdconv cannot name the instances and drops the element; a [%s] that is not at the end of the name is not …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:609-625", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:134-165", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:106", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:230"]
---

## Symptom

`M239`
`Dim-ed %LEVEL% '%NAME%' must have an expression.`

## Cause

An element has <dim> but its <name> contains no placeholder: neither %s nor [%s] at the end. svdconv cannot name the instances and drops the element; a [%s] that is not at the end of the name is not recognised and also lands here.

## Fix

Add the placeholder: [%s] at the end for an array (REG[%s]) or %s for a list (CH%s_CTRL); otherwise remove <dim> and <dimIncrement>.

## Note

Error under --strict.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDimension.cpp:609-625`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:134-165`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:106`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:230`
