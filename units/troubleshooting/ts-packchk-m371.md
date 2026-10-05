---
id: "ts-packchk-m371"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M371: Feature for"
status: "draft"
tool: "packchk"
severity: "error"
code: "M371"
symptoms: ["M371", "%SECTION% Feature for '%MCU%': '%FEATURE%' unknown."]
symptom_regex: "^.+? Feature for '.+?': '.+?' unknown\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M371`
`%SECTION% Feature for '%MCU%': '%FEATURE%' unknown.`

## Cause

This feature _'FEATURE'_ is unknwon to the specified _'MCU'_. Correct the feature ([/package/devices/family/.../feature](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature)) if this is a typo.

## Fix

_siehe Cause_
