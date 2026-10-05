---
id: "ts-packchk-m205"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M205: Cannot create Pack Name file"
status: "draft"
tool: "packchk"
severity: "error"
code: "M205"
symptoms: ["M205", "Cannot create Pack Name file '%PATH%'"]
symptom_regex: "^Cannot create Pack Name file '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M205`
`Cannot create Pack Name file '%PATH%'`

## Cause

Check the disk space or your permissions. Correct the path name.

## Fix

_siehe Cause_
