---
id: "ts-svdconv-m322"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M322: … … '…' is meaningless text. Deleted."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M322"
symptoms: ["M322", "%LEVEL% %ITEM% '%NAME%' is meaningless text. Deleted."]
symptom_regex: "^.+? .+? '.+?' is meaningless text\\. Deleted\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An element's <description> is the placeholder text 'no description available' (in any case). svdconv deletes the description."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1283", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1284", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1285", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:141", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:236"]
---

## Symptom

`M322`
`%LEVEL% %ITEM% '%NAME%' is meaningless text. Deleted.`

## Cause

An element's <description> is the placeholder text 'no description available' (in any case). svdconv deletes the description. Warning by default, error with --strict.

## Fix

Write a real description of the element, or leave <description> out.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdItem.cpp:1283`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1284`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1285`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:141`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:236`
