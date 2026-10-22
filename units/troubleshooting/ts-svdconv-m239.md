---
id: "ts-svdconv-m239"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M239: Dim-ed … '…' must have an expression."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M239"
symptoms: ["M239", "Dim-ed %LEVEL% '%NAME%' must have an expression."]
symptom_regex: "^Dim\\-ed .+? '.+?' must have an expression\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "The SVD file declares a dimensioned element (a register, field or cluster with a dim tag) whose dim value or dim-index expression is missing, so svdconv cannot expand the array. %LEVEL% is the kind of element (register, field, cluster) …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not inspected; clone not available)"]
---

## Symptom

`M239`
`Dim-ed %LEVEL% '%NAME%' must have an expression.`

## Cause

The SVD file declares a dimensioned element (a register, field or cluster with a dim tag) whose dim value or dim-index expression is missing, so svdconv cannot expand the array. %LEVEL% is the kind of element (register, field, cluster) and %NAME% is the element's name.

## Fix

Open the SVD file, find the element named in the message, and add the missing dim expression (for example a dim value and dimIndex or the dim tag contents) so the array can be expanded. Then rerun svdconv.

## Note

Answered from the message text and the README cause only, since the source clone was not available. The README cause 'Correct SVD.' is generic; the specific missing element is named by %LEVEL% and %NAME%. The exact accepted dim syntax was not verified against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not inspected; clone not available)`
