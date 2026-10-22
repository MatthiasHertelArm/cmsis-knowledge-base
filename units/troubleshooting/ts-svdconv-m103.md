---
id: "ts-svdconv-m103"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M103: Internal Error: …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M103"
symptoms: ["M103", "Internal Error: %REF%"]
symptom_regex: "^Internal Error: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Please contact support."
summary: "An internal consistency check of svdconv failed; REF names the check."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:150-181", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:40"]
---

## Symptom

`M103`
`Internal Error: %REF%`

## Cause

An internal consistency check of svdconv failed; REF names the check. In this version it is raised only while generating the C expression of a <disableCondition>, when an item referenced at field level is not a field.

## Fix

Check that every name in the <disableCondition> refers to an existing register or field. If the SVD is correct, report the message together with the SVD file to Open-CMSIS-Pack/devtools.

## Note

Only call site SvdCExpression.cpp:179; how an SVD reaches it is not evident from the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:150-181`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:40`
