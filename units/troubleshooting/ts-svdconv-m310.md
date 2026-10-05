---
id: "ts-svdconv-m310"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M310: Field '…': BitWidth error: …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M310"
symptoms: ["M310", "Field '%NAME%': BitWidth error: %NUM%"]
symptom_regex: "^Field '.+?': BitWidth error: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:90", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:175", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:486", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:487", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/include/SvdField.h:13", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:129"]
---

## Symptom

`M310`
`Field '%NAME%': BitWidth error: %NUM%`

## Cause

A field's width (from <bitWidth>, or <msb> - <lsb> + 1) is more than 64 bits. The field is dropped.

## Fix

Set the field's <bitWidth> (or <lsb>/<msb>, <bitRange>) to the real width of the bit field; it must fit into its register's <size>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:90`
- `tools/svdconv/SVDModel/src/SvdField.cpp:175`
- `tools/svdconv/SVDModel/src/SvdField.cpp:486`
- `tools/svdconv/SVDModel/src/SvdField.cpp:487`
- `tools/svdconv/SVDModel/include/SvdField.h:13`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:129`
