---
id: "ts-svdconv-m202"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M202: Parse error: <…> = '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M202"
symptoms: ["M202", "Parse error: <%TAG%> = '%VALUE%'"]
symptom_regex: "^Parse error: <.+?> = '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check tag/value."
summary: "svdconv cannot convert the element's value: a number that is not plain decimal, 0x hex or 0b/# binary, a boolean other than true/false/1/0, or a token outside the allowed list (e.g."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1082-1097", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:467-531", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:220-244", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:104-115", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:133-145", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:195-205", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:69"]
---

## Symptom

`M202`
`Parse error: <%TAG%> = '%VALUE%'`

## Cause

svdconv cannot convert the element's value: a number that is not plain decimal, 0x hex or 0b/# binary, a boolean other than true/false/1/0, or a token outside the allowed list (e.g. <usage>, <endian>, <modifiedWriteValues>, <readAction>, <protection>). A leading '+' and the k/M/G/T scale suffix are rejected although the CMSIS-SVD schema pattern allows them.

## Fix

Write the value in a form svdconv parses: decimal (4096), hex (0x1000) or binary (0b1010) numbers, true or false for flags, and the exact schema token for enumerated values. Replace scaled values such as 4k with 0x1000.

## Note

Empty values give M205 and <access> values give M233 instead. scaledNonNegativeInteger in CMSIS-SVD.xsd 1.3.9 is '[+]?(0x|0X|#)?[0-9a-fA-F]+[kmgtKMGT]?'.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1082-1097`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:467-531`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:220-244`
- `tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:104-115`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:133-145`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:195-205`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:69`
