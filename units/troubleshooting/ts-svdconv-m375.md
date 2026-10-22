---
id: "ts-svdconv-m375"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M375: … '…' (<enumeratedValues> '…'): Too many <enumeratedValues> container specified."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M375"
symptoms: ["M375", "%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): Too many <enumeratedValues> container specified."]
symptom_regex: "^.+? '.+?' \\(<enumeratedValues> '.+?'\\): Too many <enumeratedValues> container specified\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD input has more than one <enumeratedValues> container for the same field (or register/peripheral level named by %LEVEL% and %NAME%)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text M375 used)"]
---

## Symptom

`M375`
`%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): Too many <enumeratedValues> container specified.`

## Cause

The SVD input has more than one <enumeratedValues> container for the same field (or register/peripheral level named by %LEVEL% and %NAME%). The SVD schema and svdconv accept only one <enumeratedValues> per field, so the extra container is reported with the enclosing item name in %NAME% and the enumeratedValues name in %NAME2%.

## Fix

Open the SVD file at the element named in the message and merge the duplicate <enumeratedValues> blocks into a single <enumeratedValues> element containing all the <enumeratedValue> entries, or delete the redundant container. Then rerun svdconv.

## Note

Cause and fix are inferred from the message text and the README entry; the source lines for the trigger were not available, so the exact condition could not be checked.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text M375 used)`
