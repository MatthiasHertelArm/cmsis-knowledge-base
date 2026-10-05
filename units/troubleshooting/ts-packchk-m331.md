---
id: "ts-packchk-m331"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M331: Condition unused"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M331"
symptoms: ["M331", "Condition unused: '%COND%'"]
symptom_regex: "^Condition unused: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M331`
`Condition unused: '%COND%'`

## Cause

The condition has been defined but not used further. Remove the condition or add condition rules. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition).

## Fix

_siehe Cause_
