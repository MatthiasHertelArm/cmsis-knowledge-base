---
id: "ts-svdconv-m311"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M311: Field '…': Calculation: MSB or LSB == -1"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M311"
symptoms: ["M311", "Field '%NAME%': Calculation: MSB or LSB == -1"]
symptom_regex: "^Field '.+?': Calculation: MSB or LSB == \\-1$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:84", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:98", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:114", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:173", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:473", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:474", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:130"]
---

## Symptom

`M311`
`Field '%NAME%': Calculation: MSB or LSB == -1`

## Cause

A field has no complete bit position: none of <bitRange>, the pair <lsb>+<msb> or the pair <bitOffset>+<bitWidth> is given in full (for example only <lsb>, or <bitOffset> without <bitWidth>). The text speaks of MSB or LSB == -1 whichever style is used. The field is dropped.

## Fix

Give the field one complete bit position, for example <bitRange>[7:4]</bitRange>, or <lsb>4</lsb><msb>7</msb>, or <bitOffset>4</bitOffset><bitWidth>4</bitWidth>. svdconv needs <bitWidth> together with <bitOffset> although the schema marks it optional.

## Note

Misleading text: it is raised whenever offset or width is missing, not only for <lsb>/<msb>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:84`
- `tools/svdconv/SVDModel/src/SvdField.cpp:98`
- `tools/svdconv/SVDModel/src/SvdField.cpp:114`
- `tools/svdconv/SVDModel/src/SvdField.cpp:173`
- `tools/svdconv/SVDModel/src/SvdField.cpp:473`
- `tools/svdconv/SVDModel/src/SvdField.cpp:474`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:130`
