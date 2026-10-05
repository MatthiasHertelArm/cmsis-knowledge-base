---
id: "ts-svdconv-m324"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M324: Field '…' … does not fit into Register '…:…' …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M324"
symptoms: ["M324", "Field '%NAME%' %BITRANGE% does not fit into Register '%NAME2%:%NUM%' %LINE%"]
symptom_regex: "^Field '.+?' .+? does not fit into Register '.+?:.+?' .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A field's bit range does not fit into its register: the field is wider than the register's effective <size>, or bit offset + width goes beyond it; LINE is the register's line."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:498", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:510", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:511", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:624", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:634", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:143"]
---

## Symptom

`M324`
`Field '%NAME%' %BITRANGE% does not fit into Register '%NAME2%:%NUM%' %LINE%`

## Cause

A field's bit range does not fit into its register: the field is wider than the register's effective <size>, or bit offset + width goes beyond it; LINE is the register's line. The field is dropped. M345 reports the same condition from the register's own check, and M324 appears for fields that check did not reach.

## Fix

Correct the field's bit position (<bitRange>, <lsb>/<msb> or <bitOffset>/<bitWidth>) or the register's <size>, which may be inherited from the peripheral or device, so that every field lies within bits 0 to size-1.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:498`
- `tools/svdconv/SVDModel/src/SvdField.cpp:510`
- `tools/svdconv/SVDModel/src/SvdField.cpp:511`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:624`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:634`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:143`
