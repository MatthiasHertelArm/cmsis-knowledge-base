---
id: "ts-svdconv-m377"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M377: … '…' (<enumeratedValues> '…'): '…' container conflicts with '…' …."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M377"
symptoms: ["M377", "%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): '%USAGE%' container conflicts with '%NAME3%' %LINE%."]
symptom_regex: "^.+? '.+?' \\(<enumeratedValues> '.+?'\\): '.+?' container conflicts with '.+?' .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found an enumeratedValues container whose usage (read, write or read-write) conflicts with another enumeratedValues container of the same field, so the SVD field declares overlapping enumerations for the same access direction."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in this clone; message text only)"]
---

## Symptom

`M377`
`%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): '%USAGE%' container conflicts with '%NAME3%' %LINE%.`

## Cause

svdconv found an enumeratedValues container whose usage (read, write or read-write) conflicts with another enumeratedValues container of the same field, so the SVD field declares overlapping enumerations for the same access direction. The %NAME% and %NAME2% placeholders identify the element and the enumeratedValues name, %USAGE% is the conflicting usage, and %NAME3% is the other container it clashes with.

## Fix

Open the SVD file at the field named in the message and make the enumeratedValues usages consistent: keep one enumeratedValues per access direction (read, write or read-write) for that field, and rename or remove the duplicate container so no two containers claim the same usage.

## Note

The source clone was not available, so the trigger condition is inferred from the message text and the README was not checked. Treat the cause as a reading of the message, not confirmed from code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in this clone; message text only)`
