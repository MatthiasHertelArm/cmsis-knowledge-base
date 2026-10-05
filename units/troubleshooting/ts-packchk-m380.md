---
id: "ts-packchk-m380"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M380: No description found for ["
status: "draft"
tool: "packchk"
severity: "warning"
code: "M380"
symptoms: ["M380", "No description found for [%VENDOR%] '%MCU%'"]
symptom_regex: "^No description found for \\[.+?\\] '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M380`
`No description found for [%VENDOR%] '%MCU%'`

## Cause

No description was found for the device _'MCU'_ from _'VENDOR'_. Use description attribute to provide information about the device, its subfamily, or family. Refer to [/package/devices/family/.../description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_description).

## Fix

_siehe Cause_
