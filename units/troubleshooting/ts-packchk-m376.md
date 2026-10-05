---
id: "ts-packchk-m376"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M376: Schema Version not set!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M376"
symptoms: ["M376", "Schema Version not set!"]
symptom_regex: "^Schema Version not set!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M376`
`Schema Version not set!`

## Cause

Set a valid schema version in the PDSC file. Refer to schemaVersion attribute in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package).

## Fix

_siehe Cause_
