---
id: "ts-svdconv-m360"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M360: Address Block: found <…> (…) > …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M360"
symptoms: ["M360", "Address Block: found <%TAG%> (%HEXNUM%) > %HEXNUM2%."]
symptom_regex: "^Address Block: found <.+?> \\(.+?\\) > .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <addressBlock>'s <offset> or <size> (TAG) is larger than 0x1000000 (16 MiB). svdconv treats such a number as probably miscalculated but keeps it."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:14", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:49", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:65", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:147", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:179", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:252"]
---

## Symptom

`M360`
`Address Block: found <%TAG%> (%HEXNUM%) > %HEXNUM2%.`

## Cause

An <addressBlock>'s <offset> or <size> (TAG) is larger than 0x1000000 (16 MiB). svdconv treats such a number as probably miscalculated but keeps it. Warning by default, error with --strict.

## Fix

Check the value: <offset> is relative to the peripheral's <baseAddress>, not an absolute address, and <size> is the block length in bytes.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:14`
- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:49`
- `tools/svdconv/SVDModel/src/SvdAddressBlock.cpp:65`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:147`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:179`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:252`
