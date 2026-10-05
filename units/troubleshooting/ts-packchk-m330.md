---
id: "ts-packchk-m330"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M330: , already defined in Line"
status: "draft"
tool: "packchk"
severity: "error"
code: "M330"
symptoms: ["M330", "Condition redefined: '%COND%', already defined in Line %LINE%"]
symptom_regex: "^Condition redefined: '.+?', already defined in Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M330`
`Condition redefined: '%COND%', already defined in Line %LINE%`

## Cause

The condition has been defined already in a previous line. Correct the condition name, or remove the duplicate. Refer to [/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition).

## Fix

_siehe Cause_
