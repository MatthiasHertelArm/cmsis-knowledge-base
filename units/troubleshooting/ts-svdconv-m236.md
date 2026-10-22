---
id: "ts-svdconv-m236"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M236: Expression for <…> '…' not allowed."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M236"
symptoms: ["M236", "Expression for <%TAG%> '%NAME%' not allowed."]
symptom_regex: "^Expression for <.+?> '.+?' not allowed\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "A <dimName> contains %s."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:587-594", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:103"]
---

## Symptom

`M236`
`Expression for <%TAG%> '%NAME%' not allowed.`

## Cause

A <dimName> contains %s. <dimName> is the type name generated for a dim cluster and must be a plain identifier, so svdconv drops the element.

## Fix

Remove %s from <dimName>, e.g. <dimName>CHANNEL</dimName>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDimension.cpp:587-594`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:103`
