---
id: "ts-svdconv-m246"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M246: C Expression: Only one Item allowed!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M246"
symptoms: ["M246", "C Expression: Only one Item allowed!"]
symptom_regex: "^C Expression: Only one Item allowed!$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this error when a C expression that is used in an SVD field or register context, such as a computed value or array-related expression, contains more than one item where only one is accepted."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M246 text only; trigger lines not available)"]
---

## Symptom

`M246`
`C Expression: Only one Item allowed!`

## Cause

svdconv prints this error when a C expression that is used in an SVD field or register context, such as a computed value or array-related expression, contains more than one item where only one is accepted. The exact construct in the user's SVD cannot be confirmed from the trigger lines, since the clone is not available.

## Fix

Open the SVD file at the element whose expression is reported and simplify it so that it holds a single item, for example a single value or a single reference rather than a list or multiple comma-separated parts. Then run svdconv again on the corrected file.

## Note

Source lines were not available, so the trigger condition and the exact construct are inferred from the message text alone. The message is not documented in the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M246 text only; trigger lines not available)`
