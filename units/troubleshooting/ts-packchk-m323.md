---
id: "ts-packchk-m323"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M323: . Check correct spelling."
status: "draft"
tool: "packchk"
severity: "error"
code: "M323"
symptoms: ["M323", "File/Path not found: '%PATH%'. Check correct spelling."]
symptom_regex: "^File/Path not found: '.+?'\\. Check correct spelling\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M323`
`File/Path not found: '%PATH%'. Check correct spelling.`

## Cause

The file or path _'PATH'_ entered in the PDSC file could not be found. Verify the path information.

## Fix

_siehe Cause_
