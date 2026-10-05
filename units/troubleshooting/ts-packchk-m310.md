---
id: "ts-packchk-m310"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M310: Filename mismatch (case sensitive):   PDSC name"
status: "draft"
tool: "packchk"
severity: "error"
code: "M310"
symptoms: ["M310", "Filename mismatch (case sensitive):   PDSC name : '%PDSC%'   Filename  : '%SYSTEM%'"]
symptom_regex: "^Filename mismatch \\(case sensitive\\):   PDSC name : '.+?'   Filename  : '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M310`
`Filename mismatch (case sensitive):   PDSC name : '%PDSC%'   Filename  : '%SYSTEM%'`

## Cause

Filenames are case sensitive. Correct spelling.

## Fix

_siehe Cause_
