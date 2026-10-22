---
id: "ts-svdconv-m326"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M326: Endianess is not set, using default (little)"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M326"
symptoms: ["M326", "Endianess is not set, using default (little)"]
symptom_regex: "^Endianess is not set, using default \\(little\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file being converted does not contain an <endian> element at device level, so svdconv falls back to its default byte order, little endian."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M326`
`Endianess is not set, using default (little)`

## Cause

The SVD file being converted does not contain an <endian> element at device level, so svdconv falls back to its default byte order, little endian. The message reports that default being applied; it is informational about the input, not a failure of the conversion itself.

## Fix

Add an <endian>little</endian> or <endian>big</endian> element to the device description in the SVD file, matching the target hardware, to silence the message. If the device is little endian, which is the usual case for Cortex-M, no functional change is needed.

## Note

Source lines were not available, so the trigger condition and the severity mapping are unverified. The message is listed as severity error, which may be worth checking against the code that emits it, since the text reads like a warning about a default being used.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
