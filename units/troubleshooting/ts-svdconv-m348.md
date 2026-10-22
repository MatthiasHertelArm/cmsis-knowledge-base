---
id: "ts-svdconv-m348"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M348: Alternate … '…' does not exist at … address (@…)"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M348"
symptoms: ["M348", "Alternate %LEVEL% '%NAME%' does not exist at %LEVEL% address (@%ADDR%)"]
symptom_regex: "^Alternate .+? '.+?' does not exist at .+? address \\(@.+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this warning when an SVD register or field declares an alternate (alternateRegister or alternateGroup) whose name cannot be resolved at the reported level and address."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M348`
`Alternate %LEVEL% '%NAME%' does not exist at %LEVEL% address (@%ADDR%)`

## Cause

svdconv prints this warning when an SVD register or field declares an alternate (alternateRegister or alternateGroup) whose name cannot be resolved at the reported level and address. The %LEVEL% and %NAME% are the alternate's level and name taken from the SVD, and %ADDR% is the address where the lookup was made. This usually means the SVD references an alternate that is not defined in the same peripheral or at that address.

## Fix

Open the SVD at the named peripheral and address, and check that the alternateRegister or alternateGroup name matches an existing register or group spelled exactly the same way. Correct the name or add the missing alternate definition, then re-run svdconv.

## Note

The clone was not available, so the trigger and handling are inferred from the message text and the README entry only; the exact condition in the source was not checked.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
