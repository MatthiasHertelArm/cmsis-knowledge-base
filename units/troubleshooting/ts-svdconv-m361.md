---
id: "ts-svdconv-m361"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M361: … … '…': 'RESERVED' items must not be defined."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M361"
symptoms: ["M361", "%LEVEL% %ITEM% '%NAME%': 'RESERVED' items must not be defined."]
symptom_regex: "^.+? .+? '.+?': 'RESERVED' items must not be defined\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD input defines an item whose name is RESERVED, so svdconv flags it as a warning."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M361`
`%LEVEL% %ITEM% '%NAME%': 'RESERVED' items must not be defined.`

## Cause

The SVD input defines an item whose name is RESERVED, so svdconv flags it as a warning. The message wording suggests the tool treats a RESERVED-named element or register as a reserved placeholder that should not appear in the device description. The %LEVEL%, %ITEM% and %NAME% placeholders are the level (for example peripheral or register), the item kind and the offending name taken from the SVD.

## Fix

Open the SVD file, find the element whose name is RESERVED (the message gives its level and name), and remove it or rename it to a real register or peripheral name. Then rerun svdconv on the corrected file.

## Note

Source lines were not available, so the trigger condition is inferred from the message text alone; the exact check and the README wording were not verified against the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
