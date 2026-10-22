---
id: "ts-svdconv-m222"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M222: Input filename has no extension: '…"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M222"
symptoms: ["M222", "Input filename has no extension: '%NAME%"]
symptom_regex: "^Input filename has no extension: '.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct input filename extension."
summary: "svdconv was given an input file whose name has no extension, so it cannot tell which input format it is reading."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M222`
`Input filename has no extension: '%NAME%`

## Cause

svdconv was given an input file whose name has no extension, so it cannot tell which input format it is reading. The variable part of the message is the file name as passed on the command line.

## Fix

Rename the input file so it carries the expected extension (for example .svd for a CMSIS-SVD device description) and run svdconv again with the renamed file.

## Note

Source lines were not available; the cause and fix rely on the message text and the README's one-line cause. The exact extension svdconv expects is not confirmed from source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
