---
id: "ts-svdconv-m241"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M241: Parse Error: '…' invalid for Array generation"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M241"
symptoms: ["M241", "Parse Error: '%VALUE%' invalid for Array generation"]
symptom_regex: "^Parse Error: '.+?' invalid for Array generation$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "svdconv prints this warning when it cannot parse a value given for array generation (the dim/dimIncrement or related array settings it expands into multiple registers) in the input SVD."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)"]
---

## Symptom

`M241`
`Parse Error: '%VALUE%' invalid for Array generation`

## Cause

svdconv prints this warning when it cannot parse a value given for array generation (the dim/dimIncrement or related array settings it expands into multiple registers) in the input SVD. The %VALUE% placeholder is the offending text that could not be read as the expected array value. The README only says the SVD is incorrect, and the source lines were not available, so the exact field involved is not confirmed.

## Fix

Open the SVD file, find the peripheral or register declaration that uses array notation (dim, dimIncrement, dimIndex) and correct the value shown in the message so it is a valid number or index list as the SVD schema requires, then run svdconv again.

## Note

Source lines were not provided, so the trigger condition and the exact array field are inferred from the message text and the README; the cause is not verified against the code. The README cause 'Correct SVD.' is terse and does not name the field.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)`
