---
id: "ts-svdconv-m335"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M335: Value '…:…' does not fit into field '…' …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M335"
symptoms: ["M335", "Value '%NAME%:%NUM%' does not fit into field '%NAME2%' %BITRANGE%."]
symptom_regex: "^Value '.+?:.+?' does not fit into field '.+?' .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <enumeratedValue>'s <value> is larger than the largest number the field can hold (2^width - 1)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:525", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:622", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:623", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:154", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:242"]
---

## Symptom

`M335`
`Value '%NAME%:%NUM%' does not fit into field '%NAME2%' %BITRANGE%.`

## Cause

An <enumeratedValue>'s <value> is larger than the largest number the field can hold (2^width - 1). The enumerated value is dropped. Warning by default, error with --strict.

## Fix

Correct the <value> or the field's width. The value is the raw content of the field, not shifted to the field's bit position in the register.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:525`
- `tools/svdconv/SVDModel/src/SvdField.cpp:622`
- `tools/svdconv/SVDModel/src/SvdField.cpp:623`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:154`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:242`
