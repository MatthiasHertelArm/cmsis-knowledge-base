---
id: "ts-svdconv-m218"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M218: Unsupported ESC sequence found in '…' : …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M218"
symptoms: ["M218", "Unsupported ESC sequence found in '%NAME%' : %CHAR%."]
symptom_regex: "^Unsupported ESC sequence found in '.+?' : .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct escape sequence."
summary: "A <name>, <description> or register <displayName> contains a backslash followed by a character other than 'n' (e.g. \\t, \\r, \\\\ or a Windows path)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1220-1232", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:217-235", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:85"]
---

## Symptom

`M218`
`Unsupported ESC sequence found in '%NAME%' : %CHAR%.`

## Cause

A <name>, <description> or register <displayName> contains a backslash followed by a character other than 'n' (e.g. \t, \r, \\ or a Windows path). Only \n is supported in SVD texts.

## Fix

Remove the backslash, use \n for a line break, and write paths with '/'.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1220-1232`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:217-235`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:85`
