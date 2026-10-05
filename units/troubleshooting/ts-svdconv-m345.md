---
id: "ts-svdconv-m345"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M345: Field '…' … does not fit into Register '…:…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M345"
symptoms: ["M345", "Field '%NAME%' %BITRANGE% does not fit into Register '%NAME2%:%NUM%'"]
symptom_regex: "^Field '.+?' .+? does not fit into Register '.+?:.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:612", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:634", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:635", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:164"]
---

## Symptom

`M345`
`Field '%NAME%' %BITRANGE% does not fit into Register '%NAME2%:%NUM%'`

## Cause

A field's bit offset plus width exceeds the register's effective <size> (which may be inherited from the peripheral or device), so the field does not fit into its register. The field is dropped.

## Fix

Correct the field's bit position (<bitRange>, <lsb>/<msb> or <bitOffset>/<bitWidth>) or the register's <size> so that every field lies within bits 0 to size-1.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:612`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:634`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:635`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:164`
