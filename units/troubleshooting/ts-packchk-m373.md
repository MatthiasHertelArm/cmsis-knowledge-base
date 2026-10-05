---
id: "ts-packchk-m373"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M373: Unsupported Schema Version"
status: "draft"
tool: "packchk"
severity: "error"
code: "M373"
symptoms: ["M373", "Unsupported Schema Version: '%VER%'"]
symptom_regex: "^Unsupported Schema Version: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M373`
`Unsupported Schema Version: '%VER%'`

## Cause

The schema version is not supported. Verify the attribute schemaVersion of the element [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package).

## Fix

_siehe Cause_
