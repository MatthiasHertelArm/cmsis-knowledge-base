---
id: "ts-svdconv-m218"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M218: Unsupported ESC sequence found in '…' : …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M218"
symptoms: ["M218", "Unsupported ESC sequence found in '%NAME%' : %CHAR%."]
symptom_regex: "^Unsupported ESC sequence found in '.+?' : .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct escape sequence."
summary: "svdconv found a backslash escape sequence in the text of an SVD element (named %NAME%) that it does not recognise; %CHAR% is the offending character following the backslash."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)"]
---

## Symptom

`M218`
`Unsupported ESC sequence found in '%NAME%' : %CHAR%.`

## Cause

svdconv found a backslash escape sequence in the text of an SVD element (named %NAME%) that it does not recognise; %CHAR% is the offending character following the backslash. The SVD description or name text contains an escape the tool does not support, so the message is printed as a warning for that element.

## Fix

Open the SVD file at the element named in the message and correct the escape sequence so it uses only characters the tool accepts, removing or rewriting the stray backslash before the character shown in the message. Then rerun svdconv.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and the README; the README cause 'Correct escape sequence' is terse and was only expanded from the message wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)`
