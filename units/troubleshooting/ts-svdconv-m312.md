---
id: "ts-svdconv-m312"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M312: Address Block missing for Peripheral '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M312"
symptoms: ["M312", "Address Block missing for Peripheral '%NAME%'"]
symptom_regex: "^Address Block missing for Peripheral '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1505", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1507", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:378", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:868", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:131"]
---

## Symptom

`M312`
`Address Block missing for Peripheral '%NAME%'`

## Cause

A peripheral has no <addressBlock>, neither its own nor one inherited through derivedFrom. Without it svdconv cannot check that the registers lie in the peripheral's address range (M344) or that peripherals do not overlap (M352); the peripheral itself is kept.

## Fix

Add an address block that covers the peripheral's registers, for example <addressBlock><offset>0x0</offset><size>0x400</size><usage>registers</usage></addressBlock>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1505`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1507`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:378`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:868`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:131`
