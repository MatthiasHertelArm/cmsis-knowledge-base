---
id: "ts-svdconv-m362"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M362: … … '…': 'RESERVED' items must not be defined."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M362"
symptoms: ["M362", "%LEVEL% %ITEM% '%NAME%': 'RESERVED' items must not be defined."]
symptom_regex: "^.+? .+? '.+?': 'RESERVED' items must not be defined\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An element's <description> is just 'reserved' (in any case), which marks a placeholder for an unused register, field or value. svdconv only warns and keeps the element."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1279", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1280", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:181"]
---

## Symptom

`M362`
`%LEVEL% %ITEM% '%NAME%': 'RESERVED' items must not be defined.`

## Cause

An element's <description> is just 'reserved' (in any case), which marks a placeholder for an unused register, field or value. svdconv only warns and keeps the element.

## Fix

Delete the element if it only describes unused space, or write a description of what it really does.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdItem.cpp:1279`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1280`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:181`
