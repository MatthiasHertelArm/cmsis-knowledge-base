---
id: "ts-svdconv-m230"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M230: out of Range for"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M230"
symptoms: ["M230", "Value '%NAME%:%NUM%' out of Range for %LEVEL% '%NAME2%[%NUM2%]'."]
symptom_regex: "^Value '.+?:.+?' out of Range for .+? '.+?\\[.+?\\]'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M230`
`Value '%NAME%:%NUM%' out of Range for %LEVEL% '%NAME2%[%NUM2%]'.`

## Cause

Correct SVD.

## Fix

_siehe Cause_
