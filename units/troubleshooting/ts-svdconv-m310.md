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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this when a field in the SVD file has a bit width that cannot be used, so the field's bitWidth value is not valid for its register."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M310`
`Field '%NAME%': BitWidth error: %NUM%`

## Cause

svdconv prints this when a field in the SVD file has a bit width that cannot be used, so the field's bitWidth value is not valid for its register. The %NAME% is the field name from the SVD and %NUM% is the offending width value as parsed from the file. The exact validity rule is not visible in the lines provided, so the precise limit is unconfirmed.

## Fix

Open the SVD file, find the field named in the message and check its bitWidth (or msb/lsb range) against the register size; correct the value so the field fits inside the register width and rerun svdconv.

## Note

Source lines were not available; the cause and fix are inferred from the message text and the README entry only, so confidence is capped at medium. The README was documented as covering this message but its text was not supplied for comparison.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
