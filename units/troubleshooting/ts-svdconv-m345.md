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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a field in an SVD register whose bit range extends beyond the register's size (the bit offset plus bit width is larger than the register width, or the field is otherwise outside the register)."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M345`
`Field '%NAME%' %BITRANGE% does not fit into Register '%NAME2%:%NUM%'`

## Cause

svdconv found a field in an SVD register whose bit range extends beyond the register's size (the bit offset plus bit width is larger than the register width, or the field is otherwise outside the register). The %NAME% is the field name, %BITRANGE% describes the offending bit range, and %NAME2%:%NUM% identifies the register and its number. The SVD input is the cause, not svdconv itself.

## Fix

Open the SVD file, find the register named in the message and the field named in the message, and correct the field's bitOffset/bitWidth (or msb/lsb) so it lies within the register's size field (default 32 bits). If the register size is wrong, fix the register's size element; otherwise shrink or move the field so it fits.

## Note

The source lines were not available, so the trigger and the exact bit-range check could not be verified from source; the cause and fix are inferred from the message text and the CMSIS-SVD field/register model. Treat the wording of %BITRANGE% as unverified.
