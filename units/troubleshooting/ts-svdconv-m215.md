---
id: "ts-svdconv-m215"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M215: Size of <dim> is only one element for"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M215"
symptoms: ["M215", "Size of <dim> is only one element for '%NAME%', is this intended?"]
symptom_regex: "^Size of <dim> is only one element for '.+?', is this intended\\?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M215`
`Size of <dim> is only one element for '%NAME%', is this intended?`

## Cause

Check single element.

## Fix

_siehe Cause_
