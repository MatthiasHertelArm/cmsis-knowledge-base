---
id: "ts-svdconv-m213"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M213: Expression for '…' incomplete, <…> missing."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M213"
symptoms: ["M213", "Expression for '%NAME%' incomplete, <%TAG%> missing."]
symptom_regex: "^Expression for '.+?' incomplete, <.+?> missing\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Add tag."
summary: "svdconv found an expression in an SVD file whose XML element is missing a required tag; the %NAME% is the item the expression belongs to and %TAG% is the tag that was expected but absent."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M213`
`Expression for '%NAME%' incomplete, <%TAG%> missing.`

## Cause

svdconv found an expression in an SVD file whose XML element is missing a required tag; the %NAME% is the item the expression belongs to and %TAG% is the tag that was expected but absent. The exact expression element is not visible in the lines provided, so the specific SVD construct cannot be confirmed.

## Fix

Open the SVD file at the element named in the message and add the missing <%TAG%> element inside it, following the SVD schema for that element, then rerun svdconv. The README's stated fix is simply to add the tag.

## Note

The clone was unavailable, so the trigger condition and the exact element type were not read from source; the cause is inferred from the message text and the README. The README cause 'Add tag.' is terse and does not name the element or tag.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
