---
id: "ts-svdconv-m101"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M101: Unknown error!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M101"
symptoms: ["M101", "Unknown error!"]
symptom_regex: "^Unknown error!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:38", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:219", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv.cpp:154-167"]
---

## Symptom

`M101`
`Unknown error!`

## Cause

Please contact support.

## Fix

_see Cause_

## Note

Not raised anywhere in svdconv at 30f5e81: the code appears only in the message table (SVDConv_Msgs.cpp:38) and the README (README.md:219). Unexpected exceptions are reported as M104 ('STL exception occurred: ...' or 'Unknown exception occurred!') instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:38`
- `tools/svdconv/SVDConv/README.md:219`
- `tools/svdconv/SVDConv/src/SVDConv.cpp:154-167`
