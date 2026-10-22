---
id: "ts-svdconv-m361"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M361: … … '…': 'RESERVED' items must not be defined."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M361"
symptoms: ["M361", "%LEVEL% %ITEM% '%NAME%': 'RESERVED' items must not be defined."]
symptom_regex: "^.+? .+? '.+?': 'RESERVED' items must not be defined\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An element's <name>, or a register's <displayName>, is 'reserved' (in any case)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1210", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1211", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1240", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1241", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_Cluster.cpp:94", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:180", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:253"]
---

## Symptom

`M361`
`%LEVEL% %ITEM% '%NAME%': 'RESERVED' items must not be defined.`

## Cause

An element's <name>, or a register's <displayName>, is 'reserved' (in any case). Reserved space must not be described as an element, so svdconv drops it. Warning by default, error with --strict.

## Fix

Delete the element. Unused addresses and bits need no description; the header generator fills gaps with reserved members on its own.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdItem.cpp:1210`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1211`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1240`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1241`
- `tools/svdconv/SVDGenerator/src/HeaderData_Cluster.cpp:94`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:180`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:253`
