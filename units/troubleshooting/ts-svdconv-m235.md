---
id: "ts-svdconv-m235"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M235: … '…' cannot be an array."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M235"
symptoms: ["M235", "%LEVEL% '%NAME%' cannot be an array."]
symptom_regex: "^.+? '.+?' cannot be an array\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "svdconv prints this when an SVD element named by %NAME% (at the %LEVEL% level, for example a peripheral, register or cluster) is declared as an array, but the tool does not accept an array at that level."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)"]
---

## Symptom

`M235`
`%LEVEL% '%NAME%' cannot be an array.`

## Cause

svdconv prints this when an SVD element named by %NAME% (at the %LEVEL% level, for example a peripheral, register or cluster) is declared as an array, but the tool does not accept an array at that level. The SVD input declares a dim/dimIncrement (or similar array form) on that element where the tool expects a plain, single instance.

## Fix

Open the SVD file at the element named in the message and remove the dim and dimIncrement (and dimIndex/dimName if present) from it, or expand the array into individual entries with explicit names and addresses. Then run svdconv again.

## Note

Cause and fix are inferred from the message text and the README cause 'Correct SVD', since the clone with the trigger lines was not available. Verify against the trigger condition in SVDConv_Msgs.cpp before relying on the specific fix wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)`
