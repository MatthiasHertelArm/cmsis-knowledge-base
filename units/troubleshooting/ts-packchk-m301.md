---
id: "ts-packchk-m301"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M301: Checking Pack URL of PDSC file failed:   Expected URL"
status: "draft"
tool: "packchk"
severity: "error"
code: "M301"
symptoms: ["M301", "Checking Pack URL of PDSC file failed:   Expected URL : '%URL1%'   Package  URL : '%URL2%'"]
symptom_regex: "^Checking Pack URL of PDSC file failed:   Expected URL : '.+?'   Package  URL : '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M301`
`Checking Pack URL of PDSC file failed:   Expected URL : '%URL1%'   Package  URL : '%URL2%'`

## Cause

The URL specified in the package does not match the value entered for comparison in option `-u`. Check for possible misspellings in both URLs. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url).

## Fix

_siehe Cause_
