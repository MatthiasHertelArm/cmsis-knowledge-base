---
id: "ts-svdconv-m220"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M220: C Code generation warning: …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M220"
symptoms: ["M220", "C Code generation warning: %MSG%"]
symptom_regex: "^C Code generation warning: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this warning when its C code generator reports a non-fatal problem while writing the device header or source files; the %MSG% part carries the generator's own detail text, which is the specific item to look at."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message id M220 only)"]
---

## Symptom

`M220`
`C Code generation warning: %MSG%`

## Cause

svdconv prints this warning when its C code generator reports a non-fatal problem while writing the device header or source files; the %MSG% part carries the generator's own detail text, which is the specific item to look at. The source lines were not available, so this cause is inferred from the message text and the README entry only.

## Fix

Read the text after the colon in the message to identify the element or value it names, correct that entry in the SVD file, and rerun svdconv. If the detail text is unclear, check the generated output for the affected item.

## Note

Source lines were unavailable, so the trigger and handling could not be confirmed; the cause and fix rest on the message wording and the README claim that it is documented. The %MSG% detail varies, so the specific remedy depends on it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message id M220 only)`
