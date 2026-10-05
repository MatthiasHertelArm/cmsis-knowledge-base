---
id: "ts-svdconv-m518"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M518: SFD Code generation: Unsupported ESC sequence found in '…' : …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M518"
symptoms: ["M518", "SFD Code generation: Unsupported ESC sequence found in '%NAME%' : %CHAR%."]
symptom_regex: "^SFD Code generation: Unsupported ESC sequence found in '.+?' : .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "During SFD generation a description contains a backslash followed by a character other than 'n' (e.g. \\t, \\r, \\\\ or a Windows path)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1302-1317", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:218"]
---

## Symptom

`M518`
`SFD Code generation: Unsupported ESC sequence found in '%NAME%' : %CHAR%.`

## Cause

During SFD generation a description contains a backslash followed by a character other than 'n' (e.g. \t, \r, \\ or a Windows path). Only \n is supported; svdconv drops the character after the backslash.

## Fix

Remove the backslash or rewrite the text: use \n for a line break, write paths with '/', and use no other C escape sequences in <description>.

## Note

Source FIXME (SvdUtils.cpp:1310) notes the conversion mangles such sequences.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1302-1317`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:218`
