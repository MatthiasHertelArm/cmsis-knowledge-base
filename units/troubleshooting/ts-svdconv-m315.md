---
id: "ts-svdconv-m315"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M315: Address Block: <size> is zero."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M315"
symptoms: ["M315", "Address Block: <size> is zero."]
symptom_regex: "^Address Block: <size> is zero\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <addressBlock> has <size> 0."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:133", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:134", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:123", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:134"]
---

## Symptom

`M315`
`Address Block: <size> is zero.`

## Cause

An <addressBlock> has <size> 0. The block is dropped.

## Fix

Set <size> to the number of bytes the block spans (for example 0x400), or remove the block.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:133`
- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:134`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:123`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:134`
