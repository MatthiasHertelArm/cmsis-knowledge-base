---
id: "ts-svdconv-m202"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M202: Parse error: <…> = '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M202"
symptoms: ["M202", "Parse error: <%TAG%> = '%VALUE%'"]
symptom_regex: "^Parse error: <.+?> = '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check tag/value."
summary: "svdconv failed to parse an SVD XML element whose tag and value it could not interpret; the message names the offending element as <%TAG%> and its text content as %VALUE%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M202`
`Parse error: <%TAG%> = '%VALUE%'`

## Cause

svdconv failed to parse an SVD XML element whose tag and value it could not interpret; the message names the offending element as <%TAG%> and its text content as %VALUE%. The README only says to check the tag and value. Without the source lines the exact trigger condition cannot be confirmed.

## Fix

Open the SVD file at the element named in the message and check that its tag is spelled as the SVD schema expects and that its value has the correct type and format (for example a number written in a supported form). Correct the value, then rerun svdconv.

## Note

Source lines were not available, so the trigger was not checked; the cause is taken from the message text and the README. The message format string is only partially known.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
