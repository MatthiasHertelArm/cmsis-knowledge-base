---
id: "ts-svdconv-m233"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M233: Parse error: <…> = '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M233"
symptoms: ["M233", "Parse error: <%TAG%> = '%VALUE%'"]
symptom_regex: "^Parse error: <.+?> = '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "svdconv parses the SVD file and found an element whose value could not be interpreted, so the parser reports the tag name and the offending value."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M233`
`Parse error: <%TAG%> = '%VALUE%'`

## Cause

svdconv parses the SVD file and found an element whose value could not be interpreted, so the parser reports the tag name and the offending value. The README attributes this to an incorrect SVD file. The exact tag and value are the variable parts of the message and identify which element of the SVD is malformed.

## Fix

Open the SVD file and locate the element named by the tag in the message, then check that its value is valid for that element (for example a number where a number is required, with the expected format). Correct the value and rerun svdconv.

## Note

Source lines were not available, so the trigger and handling were not verified; the cause is inferred from the message text and the README entry, which only says 'Correct SVD.'

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
