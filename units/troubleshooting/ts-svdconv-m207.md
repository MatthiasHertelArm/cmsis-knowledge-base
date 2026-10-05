---
id: "ts-svdconv-m207"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M207: Expression marker found but no <dim> specified"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M207"
symptoms: ["M207", "Expression marker found but no <dim> specified: '%NAME%'"]
symptom_regex: "^Expression marker found but no <dim> specified: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M207`
`Expression marker found but no <dim> specified: '%NAME%'`

## Cause

Specify dimension.

## Fix

_siehe Cause_
