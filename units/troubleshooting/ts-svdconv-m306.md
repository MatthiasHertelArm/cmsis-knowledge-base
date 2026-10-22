---
id: "ts-svdconv-m306"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M306: Schema Version not set for <device>."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M306"
symptoms: ["M306", "Schema Version not set for <device>."]
symptom_regex: "^Schema Version not set for <device>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this warning when the input SVD file does not declare a schema version for the device, so the tool cannot tell which CMSIS-SVD schema revision the description follows."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M306`
`Schema Version not set for <device>.`

## Cause

svdconv prints this warning when the input SVD file does not declare a schema version for the device, so the tool cannot tell which CMSIS-SVD schema revision the description follows. The <device> placeholder is the device name taken from the SVD. The exact trigger condition could not be checked because the source lines were not available.

## Fix

Add a schema version to the device element in the SVD file, for example by setting the schemaVersion attribute on <device>, so the description states which SVD schema it follows. Then rerun svdconv on the corrected file.

## Note

Source lines were unavailable; the cause and fix are inferred from the message text and the README statement that the message is documented, not confirmed against the trigger code. The exact attribute name should be checked against the SVD schema before use.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
