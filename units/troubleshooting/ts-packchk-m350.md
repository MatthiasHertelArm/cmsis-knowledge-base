---
id: "ts-packchk-m350"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M350: component found for ["
status: "draft"
tool: "packchk"
severity: "warning"
code: "M350"
symptoms: ["M350", "No '%COMP%' component found for [%VENDOR%] '%MCU%' (Compiler: %COMPILER% [%OPTION%])"]
symptom_regex: "^No '.+?' component found for \\[.+?\\] '.+?' \\(Compiler: .+? \\[.+?\\]\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M350`
`No '%COMP%' component found for [%VENDOR%] '%MCU%' (Compiler: %COMPILER% [%OPTION%])`

## Cause

The package ([/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package)) defines a Vendor-MCU combination for which no component was defined. Define a component ([/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component)) or verify the _'VENDOR'_ - _'MCU'_ settings.

## Fix

_siehe Cause_
