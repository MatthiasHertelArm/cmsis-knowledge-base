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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv reports this when a register field in the input SVD has an offset that is invalid for its register: the bit offset places the field outside the register width or the field overlaps a field that is already …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M309`
`Field '%NAME%': Offset error: %NUM%`

## Cause

svdconv reports this when a register field in the input SVD has an offset that is invalid for its register: the bit offset places the field outside the register width or the field overlaps a field that is already defined. %NAME% is the field name from the SVD and %NUM% is the offending offset value. The exact check cannot be confirmed here because the source lines were not available.

## Fix

Open the SVD file, find the <field> named in the message and check its <bitOffset> (or <lsb>) and <bitWidth> (or <msb>) against the parent register's <size>. Correct the offset so the field lies within the register width and does not overlap other fields, then run svdconv again.

## Note

Source lines were not available; the cause and fix are inferred from the message text and the name of the field offset check, not read from the trigger. The README documents this message, but its text was not provided to confirm the wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
