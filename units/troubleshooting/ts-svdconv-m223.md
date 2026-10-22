---
id: "ts-svdconv-m223"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M223: Input File Name '…' does not match the tag <name> in the <device> section: '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M223"
symptoms: ["M223", "Input File Name '%INFILE%' does not match the tag <name> in the <device> section: '%NAME%'"]
symptom_regex: "^Input File Name '.+?' does not match the tag <name> in the <device> section: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct the MCU name."
summary: "svdconv compares the name of the input SVD file with the text of the <name> element in the <device> section of that file and prints this warning when they differ."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M223 text only; clone not available for trigger lines)"]
---

## Symptom

`M223`
`Input File Name '%INFILE%' does not match the tag <name> in the <device> section: '%NAME%'`

## Cause

svdconv compares the name of the input SVD file with the text of the <name> element in the <device> section of that file and prints this warning when they differ. The %INFILE% placeholder is the input file name and %NAME% is the device name read from the SVD. The file name and the device name are not the same string, so the tool reports the mismatch.

## Fix

Make the device name in the SVD's <device> <name> element match the input file name (or rename the SVD file to match the <name> value), then rerun svdconv. The README's cause, that the MCU name is wrong, is consistent with this: correct the MCU name so both agree.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and the README; the exact comparison (case sensitivity, extension handling) is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M223 text only; clone not available for trigger lines)`
