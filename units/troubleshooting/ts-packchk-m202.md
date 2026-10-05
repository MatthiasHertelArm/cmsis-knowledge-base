---
id: "ts-packchk-m202"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M202: No PDSC input file specified"
status: "draft"
tool: "packchk"
severity: "error"
code: "M202"
symptoms: ["M202", "No PDSC input file specified"]
symptom_regex: "^No PDSC input file specified$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M202`
`No PDSC input file specified`

## Cause

Correct the command line. **packchk** expects a *.pdsc file name as input.

## Fix

_siehe Cause_
