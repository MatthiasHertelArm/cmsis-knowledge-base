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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a field in the SVD register description whose bit range extends beyond the width of its enclosing register, so the field cannot be placed inside the register."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M324`
`Field '%NAME%' %BITRANGE% does not fit into Register '%NAME2%:%NUM%' %LINE%`

## Cause

svdconv found a field in the SVD register description whose bit range extends beyond the width of its enclosing register, so the field cannot be placed inside the register. The %NAME% is the field name, %BITRANGE% the offending bit range, %NAME2%:%NUM% the register name and its size, and %LINE% the location in the SVD file. The cause is inferred from the message text alone because the source lines were not available.

## Fix

Open the SVD file at the line reported and correct the field's bitOffset and bitWidth (or lsb and msb) so that the field lies within the register's size (for example 32 bits for a 32-bit register), or correct the register's size element if it was set too small. Then rerun svdconv.

## Note

Source lines were not provided, so the trigger condition is inferred from the message wording and the README was not consulted for its text; the cause and fix should be checked against the source before relying on them.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
