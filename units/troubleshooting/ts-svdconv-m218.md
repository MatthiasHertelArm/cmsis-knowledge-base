---
id: "ts-svdconv-m218"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M218: Unsupported ESC sequence found in"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M218"
symptoms: ["M218", "Unsupported ESC sequence found in '%NAME%' : %CHAR%."]
symptom_regex: "^Unsupported ESC sequence found in '.+?' : .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M218`
`Unsupported ESC sequence found in '%NAME%' : %CHAR%.`

## Cause

Correct escape sequence.

## Fix

_siehe Cause_
