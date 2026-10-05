---
id: "ts-svdconv-m225"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M225: Upper/lower case mismatch: '…', should be '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M225"
symptoms: ["M225", "Upper/lower case mismatch: '%NAME%', should be '%NAME2%'"]
symptom_regex: "^Upper/lower case mismatch: '.+?', should be '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Update SVD file."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:290-380", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:677-720", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:722-790", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:818-858", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:906-1030", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdSauRegion.cpp:116-118", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:220-245", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:301-336", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:92", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:224"]
---

## Symptom

`M225`
`Upper/lower case mismatch: '%NAME%', should be '%NAME2%'`

## Cause

A token value has the right letters but the wrong case, e.g. <access>Read-Write</access>, <usage>Registers</usage>, <endian>Little</endian>, <modifiedWriteValues>OneToClear</modifiedWriteValues> or <protection>S</protection>. svdconv accepts the value with a warning, except for <protection> and SAU values, which it also rejects with M202.

## Fix

Use the exact spelling shown as NAME2, which is the CMSIS-SVD.xsd token, e.g. read-write, registers, little, oneToClear, s/n/p.

## Note

Error under --strict.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:290-380`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:677-720`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:722-790`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:818-858`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:906-1030`
- `tools/svdconv/SVDModel/src/SvdSauRegion.cpp:116-118`
- `tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:220-245`
- `tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:301-336`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:92`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:224`
