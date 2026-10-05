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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:60-100", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:137-148", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:251-257", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:107"]
---

## Symptom

`M240`
`Tag <%TAG%> unknown or not allowed on %LEVEL2%:%LEVEL%.`

## Cause

A dim element (any tag whose name contains 'dim') is not accepted on this level by svdconv: <dimIndex> or <dimName> on a <peripheral>, <dimName> on a <register>, <dimArrayIndex> on a <field>, or any dim element on an <interrupt>. Misspelled tags containing 'dim' land here too. svdconv drops the parent element.

## Fix

Remove the element or move it to a level that takes it: peripherals take <dim>, <dimIncrement>, <dimArrayIndex>; clusters also <dimIndex> and <dimName>; registers <dim>, <dimIncrement>, <dimIndex>, <dimArrayIndex>; fields <dim>, <dimIncrement>, <dimIndex>, <dimName>. Check the tag spelling.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDimension.cpp:60-100`
- `tools/svdconv/SVDModel/src/SvdDimension.cpp:137-148`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:251-257`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:107`
