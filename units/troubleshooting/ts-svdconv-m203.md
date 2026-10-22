---
id: "ts-svdconv-m203"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M203: Value already set: <…> = '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M203"
symptoms: ["M203", "Value already set: <%TAG%> = '%VALUE%'"]
symptom_regex: "^Value already set: <.+?> = '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check tag/value."
summary: "svdconv reports M203 when it tries to set a tag in the SVD/PDSC handling and that tag already holds a value, so the second assignment is refused."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M203`
`Value already set: <%TAG%> = '%VALUE%'`

## Cause

svdconv reports M203 when it tries to set a tag in the SVD/PDSC handling and that tag already holds a value, so the second assignment is refused. The <%TAG%> names the element that was already set and '%VALUE%' is the value it already has. The README only says to check the tag and value, and the source lines were not available to confirm which input produces the duplicate.

## Fix

Search the SVD input for a second occurrence of the named element (the one shown in the message) under the same parent and remove or merge the duplicate so each element is given one value. If the duplicate came from an include or a generated file, fix it at the source of that element.

## Note

Source lines were unavailable, so the trigger condition is inferred from the message text and README only; the 'duplicate element' reading is not verified against the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
