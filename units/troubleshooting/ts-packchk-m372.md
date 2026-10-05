---
id: "ts-packchk-m372"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M372: misspelled, did you mean"
status: "draft"
tool: "packchk"
severity: "error"
code: "M372"
symptoms: ["M372", "%SECTION% Feature for '%MCU%': '%FEATURE%' misspelled, did you mean '%KNOWNFEATURE%' (%DESCR%)."]
symptom_regex: "^.+? Feature for '.+?': '.+?' misspelled, did you mean '.+?' \\(.+?\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M372`
`%SECTION% Feature for '%MCU%': '%FEATURE%' misspelled, did you mean '%KNOWNFEATURE%' (%DESCR%).`

## Cause

This feature _'FEATURE'_ resembles the feature _'KNOWNFEATURE'_. Correct the feature ([/package/devices/family/.../feature](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature)) if this is a typo.

## Fix

_siehe Cause_
