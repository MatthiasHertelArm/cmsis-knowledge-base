---
id: "ts-svdconv-m369"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M369: Enumerated Value '…': <value> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M369"
symptoms: ["M369", "Enumerated Value '%NAME%': <value> not set."]
symptom_regex: "^Enumerated Value '.+?': <value> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this when an enumeratedValue entry in the input SVD, inside a field's enumeratedValues list, has neither a value nor a bitfield-valued element set for the named enumerated value %NAME%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M369`
`Enumerated Value '%NAME%': <value> not set.`

## Cause

svdconv prints this when an enumeratedValue entry in the input SVD, inside a field's enumeratedValues list, has neither a value nor a bitfield-valued element set for the named enumerated value %NAME%. The enumerated value is therefore unusable, because svdconv cannot map it to a numeric value. Exact element handling could not be verified from source, since the clone was not provided.

## Fix

Open the SVD file, find the enumeratedValue named %NAME% under its field, and add a <value> element (for example <value>0x1</value>) or a <isDefault>true</isDefault> element with a valid value. Then rerun svdconv on the corrected file.

## Note

Source lines were not available, so the trigger condition and the handling are inferred from the message text only. The README documents this message, but its cause and fix text was not supplied for comparison. Verify the exact element that must be set against the trigger in SVDConv_Msgs.cpp before relying on the fix.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
