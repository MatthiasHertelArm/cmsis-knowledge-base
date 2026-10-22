---
id: "ts-svdconv-m109"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M109: Cannot find '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M109"
symptoms: ["M109", "Cannot find '%NAME%'"]
symptom_regex: "^Cannot find '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check specified file."
summary: "svdconv prints this when a name it was asked to look up cannot be found in the input it is processing."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M109`
`Cannot find '%NAME%'`

## Cause

svdconv prints this when a name it was asked to look up cannot be found in the input it is processing. The %NAME% placeholder is the identifier that was not found. The source lines were not available, so the exact lookup cannot be confirmed; the README only says to check the specified file.

## Fix

Check the file you passed to svdconv and confirm that the named item (the %NAME% in the message) exists in it, spelled exactly as in the message. If the name refers to another file or resource, check that it is present at the path svdconv was given.

## Note

Trigger and lookup were not visible in the provided material, so the cause is inferred from the message text and the README. The README cause is generic; treat the fix as a check, not a confirmed remedy.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
