---
id: "ts-svdconv-m221"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M221: Input filename must end with .svd: '…"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M221"
symptoms: ["M221", "Input filename must end with .svd: '%NAME%"]
symptom_regex: "^Input filename must end with \\.svd: '.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct input filename extension."
summary: "svdconv was given an input file whose name does not end in .svd."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M221`
`Input filename must end with .svd: '%NAME%`

## Cause

svdconv was given an input file whose name does not end in .svd. The %NAME% in the message is the offending file name as passed on the command line. The README gives the same cause in one line, but the source lines were not available to confirm the exact check.

## Fix

Rename the input file so that it ends with .svd (for example, rename a file named device.xml to device.svd) and run svdconv again with the renamed file.

## Note

Trigger was inferred from the message text and README only; the source lines were not available, so the exact check is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
