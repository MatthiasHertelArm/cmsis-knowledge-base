---
id: "ts-svdconv-m359"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M359: Address Block: <usage> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M359"
symptoms: ["M359", "Address Block: <usage> not set."]
symptom_regex: "^Address Block: <usage> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <addressBlock> has no <usage>, and no derivedFrom source supplies one."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:138", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:139", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:111", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:178"]
---

## Symptom

`M359`
`Address Block: <usage> not set.`

## Cause

An <addressBlock> has no <usage>, and no derivedFrom source supplies one. The block is dropped.

## Fix

Add <usage>registers</usage> (or buffer, or reserved) to the block.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:138`
- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:139`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:111`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:178`
