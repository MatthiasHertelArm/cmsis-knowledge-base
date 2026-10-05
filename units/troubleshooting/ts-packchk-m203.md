---
id: "ts-packchk-m203"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M203: Error reading PDSC file(s)"
status: "draft"
tool: "packchk"
severity: "error"
code: "M203"
symptoms: ["M203", "Error reading PDSC file(s) '%PATH%'!"]
symptom_regex: "^Error reading PDSC file\\(s\\) '.+?'!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M203`
`Error reading PDSC file(s) '%PATH%'!`

## Cause

Verify the PDSC file for consistency.

## Fix

_siehe Cause_
