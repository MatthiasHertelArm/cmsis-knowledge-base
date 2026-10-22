---
id: "ts-svdconv-m382"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M382: … '…': … '…' does not fit into … width: … Bit."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M382"
symptoms: ["M382", "%LEVEL% '%NAME%': %NAME2% '%HEXNUM%' does not fit into %LEVEL% width: %NUM% Bit."]
symptom_regex: "^.+? '.+?': .+? '.+?' does not fit into .+? width: .+? Bit\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a value in the SVD (a hexadecimal number such as a reset value or an address/offset) that is wider than the bit width declared for the enclosing element (a field or register, given by %NUM% bits)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)"]
---

## Symptom

`M382`
`%LEVEL% '%NAME%': %NAME2% '%HEXNUM%' does not fit into %LEVEL% width: %NUM% Bit.`

## Cause

svdconv found a value in the SVD (a hexadecimal number such as a reset value or an address/offset) that is wider than the bit width declared for the enclosing element (a field or register, given by %NUM% bits). The %LEVEL% names the element kind, %NAME% the element name, %NAME2% the property holding the value, and %HEXNUM% the offending value. The value cannot be represented in the declared width, so the SVD description is inconsistent.

## Fix

Open the SVD file at the element named in the message and check the value of the named property against the declared width of that element. Either correct the number so it fits in the stated number of bits, or correct the width (for example the bitWidth or size) if it was declared too small. Then run svdconv again.

## Note

Source lines were not available, so the cause is inferred from the message text and the parameter names only; the exact property checked and the element kinds involved are unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)`
