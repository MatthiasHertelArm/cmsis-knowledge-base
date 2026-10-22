---
id: "ts-svdconv-m379"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M379: XBin Number '…' too large, skipping evaluation."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M379"
symptoms: ["M379", "XBin Number '%NAME%' too large, skipping evaluation."]
symptom_regex: "^XBin Number '.+?' too large, skipping evaluation\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An <enumeratedValue> <value> uses binary don't-care notation (0b... or #... with x digits) with more than 8 'x' characters. svdconv expands every x into all combinations and refuses more than 8 (256 values), so the value is rejected with …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:533-548", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdEnum.cpp:133-139", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:144-158", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:200", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:256"]
---

## Symptom

`M379`
`XBin Number '%NAME%' too large, skipping evaluation.`

## Cause

An <enumeratedValue> <value> uses binary don't-care notation (0b... or #... with x digits) with more than 8 'x' characters. svdconv expands every x into all combinations and refuses more than 8 (256 values), so the value is rejected with M202 and the enumeratedValue is dropped.

## Fix

Use at most 8 x digits in one <value>: split it into several <enumeratedValue>s, or cover the remaining values with one <enumeratedValue> that has <isDefault>true</isDefault> instead of a <value>.

## Note

Logged without a line number; the M202 for <value> that follows carries it. Error under --strict.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:533-548`
- `tools/svdconv/SVDModel/src/SvdEnum.cpp:133-139`
- `tools/svdconv/test/unittests/src/SvdUtilsConversionTest.cpp:144-158`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:200`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:256`
