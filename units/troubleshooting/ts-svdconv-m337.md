---
id: "ts-svdconv-m337"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M337: … '…' already defined …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M337"
symptoms: ["M337", "%LEVEL% '%NAME%' already defined %LINE%"]
symptom_regex: "^.+? '.+?' already defined .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "Two <enumeratedValue>s in the same <enumeratedValues> container have the same <name>; this applies to field enumerations and to the <dimArrayIndex> enumeration of a register, cluster or peripheral array."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:416", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:423", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:620", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:552", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1401", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:422", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:156", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:243"]
---

## Symptom

`M337`
`%LEVEL% '%NAME%' already defined %LINE%`

## Cause

Two <enumeratedValue>s in the same <enumeratedValues> container have the same <name>; this applies to field enumerations and to the <dimArrayIndex> enumeration of a register, cluster or peripheral array. The later one is dropped. Warning by default, error with --strict.

## Fix

Give each enumeratedValue in a container a unique <name>, or delete the duplicate.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:416`
- `tools/svdconv/SVDModel/src/SvdField.cpp:423`
- `tools/svdconv/SVDModel/src/SvdField.cpp:620`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:552`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1401`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:422`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:156`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:243`
