---
id: "ts-svdconv-m226"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M226: SFD Code generation error: …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M226"
symptoms: ["M226", "SFD Code generation error: %MSG%"]
symptom_regex: "^SFD Code generation error: .*$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:93", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:272"]
---

## Symptom

`M226`
`SFD Code generation error: %MSG%`

## Cause

_open: to be written in the review_

## Fix

_open: to be written in the review_

## Note

No LogMsg call for this code exists in svdconv at 30f5e81; the code is only defined in the message table, so this version cannot print it. Problems during SFD generation are reported as M227 and M516 to M518.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:93`
- `tools/svdconv/SVDConv/README.md:272`
