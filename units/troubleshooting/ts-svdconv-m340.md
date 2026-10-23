---
id: "ts-svdconv-m340"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M340: No Devices found."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M340"
symptoms: ["M340", "No Devices found."]
symptom_regex: "^No Devices found\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The input has no <device> root element: the root element has another name, or the XML could not be parsed at all (then XML errors and M111 'Reading SVD File failed' come first)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdModel.cpp:46", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdModel.cpp:84", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdModel.cpp:85", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv.cpp:214", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv.cpp:218", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv.cpp:245", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:159"]
---

## Symptom

`M340`
`No Devices found.`

## Cause

The input has no <device> root element: the root element has another name, or the XML could not be parsed at all (then XML errors and M111 'Reading SVD File failed' come first).

## Fix

Pass an SVD file whose root element is <device schemaVersion="1.3">, and repair any XML syntax errors reported before this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdModel.cpp:46`
- `tools/svdconv/SVDModel/src/SvdModel.cpp:84`
- `tools/svdconv/SVDModel/src/SvdModel.cpp:85`
- `tools/svdconv/SVDConv/src/SVDConv.cpp:214`
- `tools/svdconv/SVDConv/src/SVDConv.cpp:218`
- `tools/svdconv/SVDConv/src/SVDConv.cpp:245`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:159`
