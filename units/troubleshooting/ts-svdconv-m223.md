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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct the MCU name."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:939-961", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SvdGenerator.cpp:69-73", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:90", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:223"]
---

## Symptom

`M223`
`Input File Name '%INFILE%' does not match the tag <name> in the <device> section: '%NAME%'`

## Cause

The SVD file name without path and extension differs from <device><name>; the comparison is case-sensitive (e.g. stm32f4.svd for <name>STM32F4</name>).

## Fix

Rename the file to exactly <device><name> plus .svd, or change <device><name> to match the file; the generated header is named after <device><name>.

## Note

Error under --strict.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:939-961`
- `tools/svdconv/SVDGenerator/src/SvdGenerator.cpp:69-73`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:90`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:223`
