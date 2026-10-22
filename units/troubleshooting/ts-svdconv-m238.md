---
id: "ts-svdconv-m238"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M238: … must not have <…>."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M238"
symptoms: ["M238", "%LEVEL% must not have <%TAG%>."]
symptom_regex: "^.+? must not have <.+?>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:105", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:284"]
---

## Symptom

`M238`
`%LEVEL% must not have <%TAG%>.`

## Cause

Correct SVD.

## Fix

_see Cause_

## Note

Not raised anywhere in svdconv at 30f5e81: the code appears only in the message table (SVDConv_Msgs.cpp:105) and the README (README.md:284).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:105`
- `tools/svdconv/SVDConv/README.md:284`
