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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct name."
summary: "svdconv found a character in a name field (the %NAME% placeholder, such as a register or field name in the SVD file) that is not allowed in the identifiers it generates."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)"]
---

## Symptom

`M216`
`Unsupported character found in '%NAME%' : %HEX%.`

## Cause

svdconv found a character in a name field (the %NAME% placeholder, such as a register or field name in the SVD file) that is not allowed in the identifiers it generates. The %HEX% placeholder gives the byte value of that character. The README only says 'Correct name', and the source is not available to confirm which characters are rejected.

## Fix

Open the SVD file, find the element whose name contains the reported character (search for the name in the message), and replace that character with a plain letter, digit or underscore, then rerun svdconv.

## Note

Cause and fix are inferred from the message text and the README's 'Correct name' only, since the clone was not available. The exact set of allowed characters is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)`
