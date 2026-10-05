---
id: "ts-svdconv-m216"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M216: Unsupported character found in '…' : …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M216"
symptoms: ["M216", "Unsupported character found in '%NAME%' : %HEX%."]
symptom_regex: "^Unsupported character found in '.+?' : .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct name."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1155-1215", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:217-235", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:83"]
---

## Symptom

`M216`
`Unsupported character found in '%NAME%' : %HEX%.`

## Cause

A <name>, <description>, register <displayName> or enumerated-value name contains a character svdconv does not support: a byte outside printable ASCII 0x20..0x7E (UTF-8 letters such as ä or µ, ©, typographic quotes or dashes, non-breaking spaces; each byte is reported) or a double quote. HEX shows the byte; line breaks and tabs are accepted.

## Fix

Replace the character with plain ASCII (e.g. 'u' for µ, ' instead of typographic quotes, - instead of an en dash) and remove double quotes from the text.

## Note

The text is kept unchanged in the model; only the SFD generator later drops such bytes (M516).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1155-1215`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:217-235`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:83`
