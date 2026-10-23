---
id: "ts-svdconv-m212"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M212: Address Block <usage> parse error: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M212"
symptoms: ["M212", "Address Block <usage> parse error: '%NAME%'"]
symptom_regex: "^Address Block <usage> parse error: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct address block."
summary: "An <addressBlock> <usage> is not one of registers, buffer or reserved. svdconv also reports M202 for that line and leaves the usage unset."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:722-757", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:77-81", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:133-145", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:79"]
---

## Symptom

`M212`
`Address Block <usage> parse error: '%NAME%'`

## Cause

An <addressBlock> <usage> is not one of registers, buffer or reserved. svdconv also reports M202 for that line and leaves the usage unset.

## Fix

Use <usage>registers</usage>, <usage>buffer</usage> or <usage>reserved</usage> in each <addressBlock>.

## Note

M212 carries no line number; the M202 that follows does.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:722-757`
- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:77-81`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:133-145`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:79`
