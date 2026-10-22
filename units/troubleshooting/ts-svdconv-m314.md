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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file has a <addressBlock> element inside a peripheral or device that is missing its <offset> or <size> child element, or has them empty."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M314`
`Address Block: <offset> or <size> not set.`

## Cause

The SVD file has a <addressBlock> element inside a peripheral or device that is missing its <offset> or <size> child element, or has them empty. SVDConv needs both values to lay out the address block and reports M314 with the placeholder replaced by the missing element name. The exact trigger line was not available in this review, so this reading comes from the message text alone.

## Fix

Open the SVD file at the reported peripheral and add the missing <offset> and <size> elements inside each <addressBlock>, for example <addressBlock><offset>0x0</offset><size>0x400</size><usage>registers</usage></addressBlock>, using the real offset and size of the block from the device reference manual. Then rerun svdconv.

## Note

Source lines around the trigger were not provided, so the trigger condition and the README text were not checked against the code. The README is reported to document this message, but its cause and fix were not supplied here.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
