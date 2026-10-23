---
id: "ts-svdconv-m353"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M353: Peripheral group name '…' should not end with '_'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M353"
symptoms: ["M353", "Peripheral group name '%NAME%' should not end with '_'"]
symptom_regex: "^Peripheral group name '.+?' should not end with '_'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A peripheral's <groupName> ends with an underscore."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1554", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1555", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:172"]
---

## Symptom

`M353`
`Peripheral group name '%NAME%' should not end with '_'`

## Cause

A peripheral's <groupName> ends with an underscore.

## Fix

Remove the trailing '_' from <groupName>, for example <groupName>UART</groupName>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1554`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1555`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:172`
