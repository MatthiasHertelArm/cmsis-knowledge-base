---
id: "ts-svdconv-m341"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M341: More than one devices found, only one is allowed per SVD File."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M341"
symptoms: ["M341", "More than one devices found, only one is allowed per SVD File."]
symptom_regex: "^More than one devices found, only one is allowed per SVD File\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The parsed input holds more than one <device> element at the top level. svdconv reads one file per run and an XML document has a single root element, so this does not normally occur."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdModel.cpp:83", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdModel.cpp:87", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdModel.cpp:88", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv.cpp:210", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:160"]
---

## Symptom

`M341`
`More than one devices found, only one is allowed per SVD File.`

## Cause

The parsed input holds more than one <device> element at the top level. svdconv reads one file per run and an XML document has a single root element, so this does not normally occur.

## Fix

Keep exactly one <device> per .svd file and describe further devices in files of their own.

## Note

Not reachable with one well-formed input file.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdModel.cpp:83`
- `tools/svdconv/SVDModel/src/SvdModel.cpp:87`
- `tools/svdconv/SVDModel/src/SvdModel.cpp:88`
- `tools/svdconv/SVDConv/src/SVDConv.cpp:210`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:160`
