---
id: "ts-svdconv-m518"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M518: SFD Code generation: Unsupported ESC sequence found in '…' : …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M518"
symptoms: ["M518", "SFD Code generation: Unsupported ESC sequence found in '%NAME%' : %CHAR%."]
symptom_regex: "^SFD Code generation: Unsupported ESC sequence found in '.+?' : .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SFD code generator met an escape sequence it does not support in a string it was writing out, so it reports the name of the affected item (%NAME%) and the offending character (%CHAR%)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M518`
`SFD Code generation: Unsupported ESC sequence found in '%NAME%' : %CHAR%.`

## Cause

The SFD code generator met an escape sequence it does not support in a string it was writing out, so it reports the name of the affected item (%NAME%) and the offending character (%CHAR%). The input is likely an SVD description text (for example a description or name field) containing a backslash sequence that the generator cannot translate into its output.

## Fix

Find the element named in the message in the SVD file and remove or replace the unsupported backslash escape or special character in its text, then run svdconv again. The source lines for this trigger were not available, so the exact set of supported escapes could not be checked.

## Note

Written from the message text and the README entry only; the trigger lines were not available in the clone, so the cause is inferred and the list of supported escapes is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
