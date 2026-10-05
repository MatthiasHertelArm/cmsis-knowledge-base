---
id: "ts-svdconv-m314"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M314: Address Block: <offset> or <size> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M314"
symptoms: ["M314", "Address Block: <offset> or <size> not set."]
symptom_regex: "^Address Block: <offset> or <size> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:116", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:128", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:129", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:102", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:133"]
---

## Symptom

`M314`
`Address Block: <offset> or <size> not set.`

## Cause

An <addressBlock> lacks <offset> or <size>, and no derivedFrom source supplies it. The block is dropped.

## Fix

Give every address block all three elements: <offset> relative to the peripheral's <baseAddress>, <size> in bytes and <usage>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:116`
- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:128`
- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:129`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:102`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:133`
