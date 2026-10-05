---
id: "ts-packchk-m204"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M204: File not found"
status: "draft"
tool: "packchk"
severity: "error"
code: "M204"
symptoms: ["M204", "File not found: '%PATH%'!"]
symptom_regex: "^File not found: '.+?'!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M204`
`File not found: '%PATH%'!`

## Cause

The specified PDSC file could not be found in the _PATH_ displayed in the message. Correct the path or the filename.

## Fix

_siehe Cause_
