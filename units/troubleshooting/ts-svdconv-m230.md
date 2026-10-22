---
id: "ts-svdconv-m230"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M230: Value '…:…' out of Range for … '…[…]'."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M230"
symptoms: ["M230", "Value '%NAME%:%NUM%' out of Range for %LEVEL% '%NAME2%[%NUM2%]'."]
symptom_regex: "^Value '.+?:.+?' out of Range for .+? '.+?\\[.+?\\]'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "svdconv prints this when a value in the SVD input, named by the first %NAME%:%NUM% pair, falls outside the range allowed for the register structure level named by %LEVEL% and %NAME2%[%NUM2%]."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M230`
`Value '%NAME%:%NUM%' out of Range for %LEVEL% '%NAME2%[%NUM2%]'.`

## Cause

svdconv prints this when a value in the SVD input, named by the first %NAME%:%NUM% pair, falls outside the range allowed for the register structure level named by %LEVEL% and %NAME2%[%NUM2%]. The SVD file contains a field or register value that does not fit the bit width or address range its enclosing element declares. The README only states 'Correct SVD', and the source lines were not available, so the exact check is not confirmed here.

## Fix

Open the SVD file at the element named in the message (the %LEVEL% and %NAME2% identify it, %NUM2% is its index) and correct the offending value so it fits the declared width or range, for example a bitOffset or bitWidth that exceeds the register size, or an address that lies outside the enclosing block. Then rerun svdconv.

## Note

Source lines were not provided, so the trigger condition is inferred from the message text and README only. The exact range rule and which SVD element types are checked should be confirmed against SVDConv_Msgs.cpp and the code that emits M230.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
