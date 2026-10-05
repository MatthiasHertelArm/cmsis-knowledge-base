---
id: "ts-packchk-m315"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M315: Invalid URL / Paths to Drives are not allowed in Package URL"
status: "draft"
tool: "packchk"
severity: "error"
code: "M315"
symptoms: ["M315", "Invalid URL / Paths to Drives are not allowed in Package URL: '%URL%'"]
symptom_regex: "^Invalid URL / Paths to Drives are not allowed in Package URL: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M315`
`Invalid URL / Paths to Drives are not allowed in Package URL: '%URL%'`

## Cause

Correct package URL _'URL'_. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url).

## Fix

_siehe Cause_
