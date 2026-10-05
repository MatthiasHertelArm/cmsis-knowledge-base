---
id: "ts-svdconv-m309"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M309: Field '…': Offset error: …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M309"
symptoms: ["M309", "Field '%NAME%': Offset error: %NUM%"]
symptom_regex: "^Field '.+?': Offset error: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A field's bit offset (from <bitOffset>, <lsb> or <bitRange>) is above 63, the highest bit svdconv handles."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:481", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:482", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/include/SvdField.h:13", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/include/SvdField.h:14", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:128"]
---

## Symptom

`M309`
`Field '%NAME%': Offset error: %NUM%`

## Cause

A field's bit offset (from <bitOffset>, <lsb> or <bitRange>) is above 63, the highest bit svdconv handles. The field is dropped.

## Fix

Give the field's position relative to bit 0 of its own register, for example <bitRange>[7:4]</bitRange> or <bitOffset>4</bitOffset><bitWidth>4</bitWidth>; a field always lies inside the register's <size>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:481`
- `tools/svdconv/SVDModel/src/SvdField.cpp:482`
- `tools/svdconv/SVDModel/include/SvdField.h:13`
- `tools/svdconv/SVDModel/include/SvdField.h:14`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:128`
