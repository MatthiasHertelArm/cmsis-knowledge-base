---
id: "ts-svdconv-m349"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M349: Alternate … '…' is equal to … name '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M349"
symptoms: ["M349", "Alternate %LEVEL% '%NAME%' is equal to %LEVEL% name '%NAME2%'"]
symptom_regex: "^Alternate .+? '.+?' is equal to .+? name '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An element's <alternatePeripheral>, <alternateCluster> or <alternateRegister> names the element itself."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:744", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:747", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:509", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:511", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1543", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1545", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:168", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:249"]
---

## Symptom

`M349`
`Alternate %LEVEL% '%NAME%' is equal to %LEVEL% name '%NAME2%'`

## Cause

An element's <alternatePeripheral>, <alternateCluster> or <alternateRegister> names the element itself. Warning by default, error with --strict.

## Fix

Set it to the name of the other element that shares the address, or remove it if there is none.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:744`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:747`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:509`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:511`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1543`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1545`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:168`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:249`
