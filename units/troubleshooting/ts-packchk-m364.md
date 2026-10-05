---
id: "ts-packchk-m364"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M364: No Devices for Condition"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M364"
symptoms: ["M364", "No Devices for Condition '%COND% [%VENDOR%] %MCU%' available."]
symptom_regex: "^No Devices for Condition '.+? \\[.+?\\] .+?' available\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M364`
`No Devices for Condition '%COND% [%VENDOR%] %MCU%' available.`

## Cause

The specified condition refers to a device that does not exist. Define the device ([/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device)) or correct the information for the condition ([/package/conditions/condition](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_conditions_pg.html#element_condition)).

## Fix

_siehe Cause_
