---
id: "ts-svdconv-m204"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M204: Parse Error: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M204"
symptoms: ["M204", "Parse Error: '%VALUE%'"]
symptom_regex: "^Parse Error: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check value."
summary: "svdconv prints this message when it fails to parse a value in the SVD input; the value that could not be parsed is shown in place of %VALUE%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M204`
`Parse Error: '%VALUE%'`

## Cause

svdconv prints this message when it fails to parse a value in the SVD input; the value that could not be parsed is shown in place of %VALUE%. The README only says to check the value, and without the source lines the exact field that holds the value cannot be confirmed.

## Fix

Find the quoted value in the SVD file and correct it to the form the SVD schema expects for that element (for example a plain decimal or 0x-prefixed hexadecimal number where a numeric field is required), then rerun svdconv.

## Note

Source lines were not available, so the trigger condition and the exact set of accepted formats are not verified; the fix is inferred from the message text and the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
