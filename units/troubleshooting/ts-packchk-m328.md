---
id: "ts-packchk-m328"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M328: Version not set for Release Information"
status: "draft"
tool: "packchk"
severity: "error"
code: "M328"
symptoms: ["M328", "Version not set for Release Information '%DESCR%'"]
symptom_regex: "^Version not set for Release Information '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M328`
`Version not set for Release Information '%DESCR%'`

## Cause

The release defined through the description _'DESCR'_ requires the attribute `<version>`. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release).

## Fix

_siehe Cause_
