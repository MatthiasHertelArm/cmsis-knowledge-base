---
id: "ts-packchk-m329"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M329: Description not set for Release Information"
status: "draft"
tool: "packchk"
severity: "error"
code: "M329"
symptoms: ["M329", "Description not set for Release Information '%VER%'"]
symptom_regex: "^Description not set for Release Information '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M329`
`Description not set for Release Information '%VER%'`

## Cause

The release defined through the version _'VER'_ needs a description. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release).

## Fix

_siehe Cause_
