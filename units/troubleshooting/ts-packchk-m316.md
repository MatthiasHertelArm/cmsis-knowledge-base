---
id: "ts-packchk-m316"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M316: URL must end with slash '/"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M316"
symptoms: ["M316", "URL must end with slash '/': '%URL%'"]
symptom_regex: "^URL must end with slash '/': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M316`
`URL must end with slash '/': '%URL%'`

## Cause

Correct package URL _'URL'_. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url).

## Fix

_siehe Cause_
