---
id: "ts-packchk-m345"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M345: URL not found"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M345"
symptoms: ["M345", "URL not found: '%URL%'"]
symptom_regex: "^URL not found: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M345`
`URL not found: '%URL%'`

## Cause

The specified URL could not be found. Correct the URL. Refer to [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package).

## Fix

_siehe Cause_
