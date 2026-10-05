---
id: "ts-svdconv-m130"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M130: Cannot create file '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M130"
symptoms: ["M130", "Cannot create file '%NAME%'"]
symptom_regex: "^Cannot create file '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check user rights."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/FileIo.cpp:44-56", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SvdGenerator.cpp:69-73", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SvdGenerator.cpp:103-108", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:60"]
---

## Symptom

`M130`
`Cannot create file '%NAME%'`

## Cause

svdconv could not open an output file (header, partition, SFD or listing) for writing. The file name is built from the output directory and <device><name>; the directory is not writable, an existing file is read-only or locked, or the name is not a valid file name.

## Fix

Choose a writable output directory with -o, close programs that hold the file open, remove a read-only attribute, and check that <device><name> contains only characters valid in file names.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/FileIo.cpp:44-56`
- `tools/svdconv/SVDGenerator/src/SvdGenerator.cpp:69-73`
- `tools/svdconv/SVDGenerator/src/SvdGenerator.cpp:103-108`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:60`
