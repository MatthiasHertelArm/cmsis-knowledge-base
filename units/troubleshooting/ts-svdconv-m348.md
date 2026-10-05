---
id: "ts-svdconv-m348"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M348: Alternate … '…' does not exist at … address (@…)"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M348"
symptoms: ["M348", "Alternate %LEVEL% '%NAME%' does not exist at %LEVEL% address (@%ADDR%)"]
symptom_regex: "^Alternate .+? '.+?' does not exist at .+? address \\(@.+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:578", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:579", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:671", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:729", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:167", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:248"]
---

## Symptom

`M348`
`Alternate %LEVEL% '%NAME%' does not exist at %LEVEL% address (@%ADDR%)`

## Cause

A peripheral with <alternatePeripheral>, or a register with <alternateRegister>, shares its address with another element, but no element at that address has the name given. svdconv then also reports the overlap itself (M343 for peripherals, M339 or M365 for registers). Warning by default, error with --strict.

## Fix

Set <alternatePeripheral> or <alternateRegister> to the <name> of the element that occupies the same address (shown in the overlap message that follows), or correct the address if the two should not overlap.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:578`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:579`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:671`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:729`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:167`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:248`
