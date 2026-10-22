---
id: "ts-svdconv-m367"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M367: Access Type: Field '…' (…) does not match Register '…' (…)"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M367"
symptoms: ["M367", "Access Type: Field '%NAME%' (%ACCESS%) does not match Register '%NAME2%' (%ACCESS2%)"]
symptom_regex: "^Access Type: Field '.+?' \\(.+?\\) does not match Register '.+?' \\(.+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv compares the access type of a field with the access type of the register that contains it, and prints this warning when the two differ."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M367`
`Access Type: Field '%NAME%' (%ACCESS%) does not match Register '%NAME2%' (%ACCESS2%)`

## Cause

svdconv compares the access type of a field with the access type of the register that contains it, and prints this warning when the two differ. The field's access (for example read-only or write-only) does not match the register's access (for example read-write), so the SVD describes an access rule on the field that the register does not allow or does not share. The names in the message are the field and register names from the SVD file, and the access values are the ones written in the SVD for each.

## Fix

Open the SVD file, find the register named in the message and its field named in the message, and make the <access> values consistent: either set the field's <access> to match the register's, or remove the field-level <access> element so the field inherits the register's access. Then run svdconv again to confirm the warning is gone.

## Note

The source lines were not available, so the trigger condition is inferred from the message text only; the exact comparison rule and whether inheritance applies are not verified. The README documents this message, but its cause and fix text was not provided to me for checking.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
