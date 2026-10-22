---
id: "ts-svdconv-m240"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M240: Tag <…> unknown or not allowed on …:…."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M240"
symptoms: ["M240", "Tag <%TAG%> unknown or not allowed on %LEVEL2%:%LEVEL%."]
symptom_regex: "^Tag <.+?> unknown or not allowed on .+?:.+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "svdconv found an XML tag in the SVD file that its schema does not allow at the given position."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M240`
`Tag <%TAG%> unknown or not allowed on %LEVEL2%:%LEVEL%.`

## Cause

svdconv found an XML tag in the SVD file that its schema does not allow at the given position. The %TAG% is the offending element name, and %LEVEL2%:%LEVEL% names the parent element and the level where it appeared, so the tag is either misspelled, placed under the wrong parent, or not valid in this SVD schema version.

## Fix

Open the SVD file at the element named in the message and check the tag spelling and its parent. Compare it against the CMSIS-SVD schema for the SVD version in use and remove or move the tag so it sits where the schema allows it.

## Note

Source lines were not available, so the trigger and handling are not verified; the cause is inferred from the message text and the README's 'Correct SVD' cause, which is vague.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
