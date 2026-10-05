---
id: "ts-svdconv-m107"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M107: Lost xml file stream."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M107"
symptoms: ["M107", "Lost xml file stream."]
symptom_regex: "^Lost xml file stream\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:44", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:225"]
---

## Symptom

`M107`
`Lost xml file stream.`

## Cause

Check SVD file.

## Fix

_see Cause_

## Note

Not raised anywhere in svdconv at 30f5e81: the code appears only in the message table (SVDConv_Msgs.cpp:44) and the README (README.md:225). A file that is not well-formed XML ends in M111 'Reading SVD File failed!' (SVDConv.cpp:213-218).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:44`
- `tools/svdconv/SVDConv/README.md:225`
