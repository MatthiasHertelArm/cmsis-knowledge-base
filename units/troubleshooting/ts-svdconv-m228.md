---
id: "ts-svdconv-m228"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M228: Enumerated Value Container: Only one Item allowed on this Level!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M228"
symptoms: ["M228", "Enumerated Value Container: Only one Item allowed on this Level!"]
symptom_regex: "^Enumerated Value Container: Only one Item allowed on this Level!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Remove additional items."
summary: "A <peripheral>, <cluster> or <register> contains more than one <dimArrayIndex>; only the first is used and the others are ignored."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:181-189", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:224-232", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:105-113", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:95"]
---

## Symptom

`M228`
`Enumerated Value Container: Only one Item allowed on this Level!`

## Cause

A <peripheral>, <cluster> or <register> contains more than one <dimArrayIndex>; only the first is used and the others are ignored.

## Fix

Keep one <dimArrayIndex> per array and put all its <enumeratedValue> entries into it.

## Note

Logged without a line number.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:181-189`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:224-232`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:105-113`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:95`
