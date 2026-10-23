---
id: "ts-svdconv-m235"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M235: … '…' cannot be an array."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M235"
symptoms: ["M235", "%LEVEL% '%NAME%' cannot be an array."]
symptom_regex: "^.+? '.+?' cannot be an array\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "A <field> has <dim> and a <name> ending in [%s]."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:199-212", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:214-230", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:102"]
---

## Symptom

`M235`
`%LEVEL% '%NAME%' cannot be an array.`

## Cause

A <field> has <dim> and a <name> ending in [%s]. Fields cannot be arrays, so svdconv drops the field.

## Fix

Use the list form with %s, e.g. <name>EN%s</name> with <dim>, <dimIncrement> as the bit distance and optionally <dimIndex>, which creates fields EN0, EN1, ...

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:199-212`
- `tools/svdconv/SVDModel/src/SvdField.cpp:214-230`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:102`
