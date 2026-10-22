---
id: "ts-svdconv-m120"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M120: Invalid arguments!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M120"
symptoms: ["M120", "Invalid arguments!"]
symptom_regex: "^Invalid arguments!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Provide a list of valid arguments."
summary: "svdconv was started with a command-line argument it does not accept, or with an argument combination it cannot process."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M120`
`Invalid arguments!`

## Cause

svdconv was started with a command-line argument it does not accept, or with an argument combination it cannot process. The README gives only the generic cause that a list of valid arguments is needed, and the source lines were not available to confirm the exact trigger.

## Fix

Run svdconv with no arguments or with --help to list the valid options for your version, then correct the failing command line to use only those options.

## Note

The source lines were not available, so the trigger condition is inferred from the message text and README only. The fix relies on svdconv printing its option list when run with --help; this has not been verified against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
