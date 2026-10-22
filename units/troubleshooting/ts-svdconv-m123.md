---
id: "ts-svdconv-m123"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M123: File/Path not found: '…'!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M123"
symptoms: ["M123", "File/Path not found: '%PATH%'!"]
symptom_regex: "^File/Path not found: '.+?'!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check speficied path."
summary: "svdconv prints this error when a path it was asked to open, most likely the SVD input file or an include or output location given on the command line or in the project, does not exist at the given location."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M123 'File/Path not found'; trigger lines not available in this review)"]
---

## Symptom

`M123`
`File/Path not found: '%PATH%'!`

## Cause

svdconv prints this error when a path it was asked to open, most likely the SVD input file or an include or output location given on the command line or in the project, does not exist at the given location. The %PATH% placeholder is the path as svdconv received it. The README gives only the cause 'Check specified path', and the source lines were not available to confirm which path argument triggers it.

## Fix

Check the spelling and location of the path shown in the message, relative to the current working directory from which svdconv was started. Correct the path in the command line or project file, or create the missing file or directory, and run svdconv again.

## Note

The README cause text 'Check speficied path.' contains a typo ('speficied'). Source lines were not available, so the trigger and which input produces the path were not verified; confidence is capped at medium accordingly.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M123 'File/Path not found'; trigger lines not available in this review)`
