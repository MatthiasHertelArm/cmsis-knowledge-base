---
id: "ts-svdconv-m102"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M102: MFC initialization failed"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M102"
symptoms: ["M102", "MFC initialization failed"]
symptom_regex: "^MFC initialization failed$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:39", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:220"]
---

## Symptom

`M102`
`MFC initialization failed`

## Cause

Please contact support.

## Fix

_see Cause_

## Note

Not raised anywhere in svdconv at 30f5e81: the code appears only in the message table (SVDConv_Msgs.cpp:39) and the README (README.md:220).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:39`
- `tools/svdconv/SVDConv/README.md:220`
