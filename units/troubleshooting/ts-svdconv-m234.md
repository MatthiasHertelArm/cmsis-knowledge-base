---
id: "ts-svdconv-m234"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M234: No valid items found for … '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M234"
symptoms: ["M234", "No valid items found for %LEVEL% '%NAME%'"]
symptom_regex: "^No valid items found for .+? '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "svdconv prints this warning when a peripheral, cluster or register group in the input SVD contains no usable child items, so the entry named by %LEVEL% and %NAME% gives nothing to generate."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M234`
`No valid items found for %LEVEL% '%NAME%'`

## Cause

svdconv prints this warning when a peripheral, cluster or register group in the input SVD contains no usable child items, so the entry named by %LEVEL% and %NAME% gives nothing to generate. The README attributes it to an incorrect SVD file, which fits this reading, but the source lines were not available to confirm the exact condition.

## Fix

Open the SVD file at the element named in the message and check that it actually contains the child elements it should (for example registers under a peripheral or fields under a register). Correct the SVD, or remove the empty element if it is not needed, then rerun svdconv.

## Note

The source clone was not available, so the trigger condition and the exact meaning of %LEVEL% were not checked against code; the cause is inferred from the message text and the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
