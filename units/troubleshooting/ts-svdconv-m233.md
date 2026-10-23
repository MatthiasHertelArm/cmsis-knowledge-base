---
id: "ts-svdconv-m233"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M233: Parse error: <…> = '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M233"
symptoms: ["M233", "Parse error: <%TAG%> = '%VALUE%'"]
symptom_regex: "^Parse error: <.+?> = '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "An <access> value is not one of read-only, write-only, read-write, writeOnce or read-writeOnce (or the deprecated read/write). svdconv treats the access as not set on that element; this is the <access> form of M202."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1089-1091", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:677-720", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdTypes.cpp:19-26", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:100", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:227"]
---

## Symptom

`M233`
`Parse error: <%TAG%> = '%VALUE%'`

## Cause

An <access> value is not one of read-only, write-only, read-write, writeOnce or read-writeOnce (or the deprecated read/write). svdconv treats the access as not set on that element; this is the <access> form of M202.

## Fix

Use one of the schema tokens in exact spelling, e.g. <access>read-write</access>.

## Note

Error under --strict.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1089-1091`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:677-720`
- `tools/svdconv/SVDModel/src/SvdTypes.cpp:19-26`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:100`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:227`
