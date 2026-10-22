---
id: "ts-svdconv-m362"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M362: … … '…': 'RESERVED' items must not be defined."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M362"
symptoms: ["M362", "%LEVEL% %ITEM% '%NAME%': 'RESERVED' items must not be defined."]
symptom_regex: "^.+? .+? '.+?': 'RESERVED' items must not be defined\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv warns when an SVD description contains an item whose name is the reserved word 'RESERVED', so the tool flags a placeholder that was left in the device description instead of a real peripheral, register, or field name."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M362`
`%LEVEL% %ITEM% '%NAME%': 'RESERVED' items must not be defined.`

## Cause

svdconv warns when an SVD description contains an item whose name is the reserved word 'RESERVED', so the tool flags a placeholder that was left in the device description instead of a real peripheral, register, or field name. The %LEVEL%, %ITEM% and %NAME% parts show which level of the SVD hierarchy (for example a peripheral or register) carries the reserved name. The source lines were not available, so this reading comes from the message text alone.

## Fix

Open the SVD file at the item named in the message and either give it a real name or remove the item if it is only a placeholder. Then rerun svdconv on the corrected SVD.

## Note

Source lines were not provided, so the trigger condition and the exact handling could not be checked against the code. The README is documented as having a cause and fix for this message, but that text was not supplied here to compare against.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
