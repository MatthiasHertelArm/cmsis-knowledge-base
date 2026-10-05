---
id: "ts-packchk-m367"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M367: found, see Line"
status: "draft"
tool: "packchk"
severity: "error"
code: "M367"
symptoms: ["M367", "Redefined %TYPE% '%NAME%' found, see Line %LINE%"]
symptom_regex: "^Redefined .+? '.+?' found, see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M367`
`Redefined %TYPE% '%NAME%' found, see Line %LINE%`

## Cause

Remove duplicate device/variant entries. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device).

## Fix

_siehe Cause_
