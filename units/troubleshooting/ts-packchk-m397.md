---
id: "ts-packchk-m397"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M397: File extension '.pdsc' must be lowercase"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M397"
symptoms: ["M397", "File extension '.pdsc' must be lowercase: '%PATH%'"]
symptom_regex: "^File extension '\\.pdsc' must be lowercase: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M397`
`File extension '.pdsc' must be lowercase: '%PATH%'`

## Cause

The PDSC file shall have lowercase extension `.pdsc` Correct extension of the PDSC file _'PATH'_.

## Fix

_siehe Cause_
