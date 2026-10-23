---
id: "ts-svdconv-m222"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M222: Input filename has no extension: '…"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M222"
symptoms: ["M222", "Input filename has no extension: '%NAME%"]
symptom_regex: "^Input filename has no extension: '.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct input filename extension."
summary: "Meant for an input file name without extension."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:927-937", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv.cpp:154-160", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:89"]
---

## Symptom

`M222`
`Input filename has no extension: '%NAME%`

## Cause

Meant for an input file name without extension. In svdconv 30f5e81 it cannot appear: with no '.' anywhere in the absolute path svdconv aborts with a critical M104 exception, and with a '.' in a directory name it reports M221 instead.

## Fix

Rename the input file to <device name>.svd.

## Note

Bug: inputFileName.substr(pos) with pos == npos (SvdDevice.cpp:929) throws std::out_of_range before the M222 test runs.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:927-937`
- `tools/svdconv/SVDConv/src/SVDConv.cpp:154-160`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:89`
