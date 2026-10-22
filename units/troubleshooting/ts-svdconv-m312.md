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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file describes a peripheral that has no <addressBlock> element, so svdconv cannot determine the register address range of that peripheral."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M312`
`Address Block missing for Peripheral '%NAME%'`

## Cause

The SVD file describes a peripheral that has no <addressBlock> element, so svdconv cannot determine the register address range of that peripheral. The name in the message is the peripheral named in the SVD. This reading comes from the message text alone, since the source lines were not available.

## Fix

Open the SVD file and add an <addressBlock> with <offset>, <size> and <usage> under the named peripheral, or inherit it from a derivedFrom peripheral that already has one. Then run svdconv again.

## Note

The README documents this message, but its cause and fix text was not provided here, so the fix above is inferred from the message rather than confirmed against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
