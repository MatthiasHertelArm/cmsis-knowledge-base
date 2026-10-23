---
id: "ts-svdconv-m350"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M350: Peripheral '…' (@…) is not 4Byte-aligned."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M350"
symptoms: ["M350", "Peripheral '%NAME%' (@%ADDR%) is not 4Byte-aligned."]
symptom_regex: "^Peripheral '.+?' \\(@.+?\\) is not 4Byte\\-aligned\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A peripheral's base address is not a multiple of 4."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:551", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:552", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:553", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:169"]
---

## Symptom

`M350`
`Peripheral '%NAME%' (@%ADDR%) is not 4Byte-aligned.`

## Cause

A peripheral's base address is not a multiple of 4.

## Fix

Check <baseAddress>; Cortex-M peripherals normally start on a 4-byte boundary. If the address is right, the warning can be accepted.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:551`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:552`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:553`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:169`
