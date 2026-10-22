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
summary: "An <enumeratedValue> in <dimArrayIndex> has a <value> that is not a valid array index: it is greater than or equal to <dim>. svdconv drops that enumeratedValue."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:582-603", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1431-1452", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:450-470", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:97"]
---

## Symptom

`M230`
`Value '%NAME%:%NUM%' out of Range for %LEVEL% '%NAME2%[%NUM2%]'.`

## Cause

An <enumeratedValue> in <dimArrayIndex> has a <value> that is not a valid array index: it is greater than or equal to <dim>. svdconv drops that enumeratedValue.

## Fix

Use values from 0 to dim-1 in <dimArrayIndex>, or raise <dim> if the array has more elements.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:582-603`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1431-1452`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:450-470`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:97`
