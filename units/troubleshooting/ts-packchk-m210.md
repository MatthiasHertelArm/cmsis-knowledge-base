---
id: "ts-packchk-m210"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M210: Only one input file to be checked is allowed."
status: "draft"
tool: "packchk"
severity: "error"
code: "M210"
symptoms: ["M210", "Only one input file to be checked is allowed."]
symptom_regex: "^Only one input file to be checked is allowed\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M210`
`Only one input file to be checked is allowed.`

## Cause

You can only check one PDSC file at a time.

## Fix

_siehe Cause_
