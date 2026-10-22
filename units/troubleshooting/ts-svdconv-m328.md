---
id: "ts-svdconv-m328"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M328: … '…' has no Registers, ignoring …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M328"
symptoms: ["M328", "%LEVEL% '%NAME%' has no Registers, ignoring %LEVEL%."]
symptom_regex: "^.+? '.+?' has no Registers, ignoring .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A peripheral or cluster (LEVEL) contains no registers or clusters, and no derivedFrom source supplies any. svdconv drops the element."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1483", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1489", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1490", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:515", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:517", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDerivedFrom.cpp:119", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:147"]
---

## Symptom

`M328`
`%LEVEL% '%NAME%' has no Registers, ignoring %LEVEL%.`

## Cause

A peripheral or cluster (LEVEL) contains no registers or clusters, and no derivedFrom source supplies any. svdconv drops the element.

## Fix

Add the registers to the peripheral's <registers> or into the <cluster>, derive the element from one that has them (derivedFrom="NAME"), or remove the empty element.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1483`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1489`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1490`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:515`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:517`
- `tools/svdconv/SVDModel/src/SvdDerivedFrom.cpp:119`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:147`
