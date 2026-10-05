---
id: "ts-packchk-m104"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M104: Path empty when searching for other PDSC files"
status: "draft"
tool: "packchk"
severity: "error"
code: "M104"
symptoms: ["M104", "Path empty when searching for other PDSC files"]
symptom_regex: "^Path empty when searching for other PDSC files$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M104`
`Path empty when searching for other PDSC files`

## Cause

Execute the check in verbose mode and try to identify the PDSC file intended for use. Correct the PDSC.

## Fix

_siehe Cause_
