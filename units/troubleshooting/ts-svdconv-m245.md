---
id: "ts-svdconv-m245"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M245: C Expression: Level '…' not supported, change expression: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M245"
symptoms: ["M245", "C Expression: Level '%LEVEL%' not supported, change expression: '%NAME%'"]
symptom_regex: "^C Expression: Level '.+?' not supported, change expression: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:112"]
---

## Symptom

`M245`
`C Expression: Level '%LEVEL%' not supported, change expression: '%NAME%'`

## Cause

_open: to be written in the review_

## Fix

_open: to be written in the review_

## Note

No LogMsg call for this code exists in svdconv at 30f5e81; the code is only defined in the message table, so this version cannot print it. Not listed in the README either.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:112`
