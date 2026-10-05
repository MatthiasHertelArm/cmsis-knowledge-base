---
id: "ts-packchk-m348"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M348: Feature redefined for"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M348"
symptoms: ["M348", "Feature redefined for '%MCU%', see Line %LINE%: '%PROP%'"]
symptom_regex: "^Feature redefined for '.+?', see Line .+?: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M348`
`Feature redefined for '%MCU%', see Line %LINE%: '%PROP%'`

## Cause

This feature _'FEATURE'_ has been defined already on the same level in line _'REF\_LINE'_. The feature characteristics defined on line _'LINE'_ overwrite those from _'REF\_LINE'_. Correct the feature ([/package/devices/family/.../feature](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature)).

## Fix

_siehe Cause_
