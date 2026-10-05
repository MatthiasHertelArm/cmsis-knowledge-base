---
id: "ts-packchk-m332"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M332: Condition undefined"
status: "draft"
tool: "packchk"
severity: "error"
code: "M332"
symptoms: ["M332", "Condition undefined: '%COND%'"]
symptom_regex: "^Condition undefined: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M332`
`Condition undefined: '%COND%'`

## Cause

A condition has been used but not defined. Correct the name of the condition or define the missing condition. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition).

## Fix

_siehe Cause_
