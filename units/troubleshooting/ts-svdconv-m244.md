---
id: "ts-svdconv-m244"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M244: C Expression: Referenced item '…' not found from: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M244"
symptoms: ["M244", "C Expression: Referenced item '%NAME%' not found from: '%MSG%'"]
symptom_regex: "^C Expression: Referenced item '.+?' not found from: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this when an expression in the SVD (for example a derivedFrom reference, or a value written as an expression that refers to another named item) points to an item name that does not exist in the device …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; clone not available)"]
---

## Symptom

`M244`
`C Expression: Referenced item '%NAME%' not found from: '%MSG%'`

## Cause

svdconv prints this when an expression in the SVD (for example a derivedFrom reference, or a value written as an expression that refers to another named item) points to an item name that does not exist in the device description it is evaluating. The variable part %NAME% is the item name it could not resolve, and %MSG% gives the context in which the reference was made. This is inferred from the message text only, since the source lines were not available.

## Fix

Open the SVD file at the location named in the message context and check that the referenced name matches an existing peripheral, register or field name exactly (names are case-sensitive). Correct the spelling or add the missing item, then run svdconv again.

## Note

Not documented in the README. Cause and fix are inferred from the message wording and the name of the message category, not verified against the trigger code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; clone not available)`
