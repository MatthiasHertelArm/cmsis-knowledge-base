---
id: "ts-svdconv-m221"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M221: Input filename must end with .svd: '…"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M221"
symptoms: ["M221", "Input filename must end with .svd: '%NAME%"]
symptom_regex: "^Input filename must end with \\.svd: '.*$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct input filename extension."
summary: "The input file's extension is not .svd (case is ignored), e.g. .xml. svdconv takes the text after the last '.' of the full path, so an extensionless file inside a directory with a '.' in its name is reported …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:927-937", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SvdOptions.cpp:285-286", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv.cpp:243", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:88"]
---

## Symptom

`M221`
`Input filename must end with .svd: '%NAME%`

## Cause

The input file's extension is not .svd (case is ignored), e.g. .xml. svdconv takes the text after the last '.' of the full path, so an extensionless file inside a directory with a '.' in its name is reported here too.

## Fix

Rename the input file to <device name>.svd, matching <device><name>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:927-937`
- `tools/svdconv/SVDConv/src/SvdOptions.cpp:285-286`
- `tools/svdconv/SVDConv/src/SVDConv.cpp:243`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:88`
