---
id: "ts-svdconv-m213"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M213: Expression for '…' incomplete, <…> missing."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M213"
symptoms: ["M213", "Expression for '%NAME%' incomplete, <%TAG%> missing."]
symptom_regex: "^Expression for '.+?' incomplete, <.+?> missing\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Add tag."
summary: "An element has dim data but lacks <dim> or <dimIncrement>; both are required as soon as any dim element (<dim>, <dimIncrement>, <dimIndex>, <dimName>) is present. svdconv drops the element."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:571-582", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:251-257", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:80"]
---

## Symptom

`M213`
`Expression for '%NAME%' incomplete, <%TAG%> missing.`

## Cause

An element has dim data but lacks <dim> or <dimIncrement>; both are required as soon as any dim element (<dim>, <dimIncrement>, <dimIndex>, <dimName>) is present. svdconv drops the element.

## Fix

Add the missing element, e.g. <dim>4</dim> and <dimIncrement>0x4</dimIncrement>, or remove the other dim elements if the element does not repeat.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDimension.cpp:571-582`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:251-257`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:80`
