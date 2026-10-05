---
id: "ts-svdconv-m224"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M224: Deprecated: '…' Use '…' instead"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M224"
symptoms: ["M224", "Deprecated: '%NAME%' Use '%NAME2%' instead"]
symptom_regex: "^Deprecated: '.+?' Use '.+?' instead$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Update SVD file."
summary: "An <access> value uses the deprecated token read or write. svdconv maps it to read-only or write-only."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:706-716", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:91"]
---

## Symptom

`M224`
`Deprecated: '%NAME%' Use '%NAME2%' instead`

## Cause

An <access> value uses the deprecated token read or write. svdconv maps it to read-only or write-only.

## Fix

Write <access>read-only</access> instead of read and <access>write-only</access> instead of write.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:706-716`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:91`
