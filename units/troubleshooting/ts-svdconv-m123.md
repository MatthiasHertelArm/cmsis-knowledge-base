---
id: "ts-svdconv-m123"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M123: File/Path not found: '…'!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M123"
symptoms: ["M123", "File/Path not found: '%PATH%'!"]
symptom_regex: "^File/Path not found: '.+?'!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check speficied path."
summary: "A path given on the command line does not exist: the input SVD file, or the output directory of -o/--outdir when --create-folder is not given."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SvdOptions.cpp:278-293", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SvdOptions.cpp:320-339", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv.cpp:202-206", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:53"]
---

## Symptom

`M123`
`File/Path not found: '%PATH%'!`

## Cause

A path given on the command line does not exist: the input SVD file, or the output directory of -o/--outdir when --create-folder is not given. Relative paths are resolved against the current working directory.

## Fix

Correct the path of the .svd file or of the -o directory, or add --create-folder so svdconv creates the output directory.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDConv/src/SvdOptions.cpp:278-293`
- `tools/svdconv/SVDConv/src/SvdOptions.cpp:320-339`
- `tools/svdconv/SVDConv/src/SVDConv.cpp:202-206`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:53`
