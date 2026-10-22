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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found more than one device element in the SVD file it was given."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text for M341; trigger lines not available in this session)"]
---

## Symptom

`M341`
`More than one devices found, only one is allowed per SVD File.`

## Cause

svdconv found more than one device element in the SVD file it was given. The tool accepts one device per SVD file, so an SVD that contains several <device> entries triggers this error.

## Fix

Split the SVD so that each file describes exactly one device, then pass each single-device file to svdconv separately. Check the input with a text search for <device> to confirm there is only one occurrence.

## Note

Source lines were not available, so the trigger is inferred from the message text only. The README's cause and fix were not provided to me in this session and were not checked.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text for M341; trigger lines not available in this session)`
