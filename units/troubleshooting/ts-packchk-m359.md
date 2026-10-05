---
id: "ts-packchk-m359"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M359: Family has no Device(s) or Subfamilies"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M359"
symptoms: ["M359", "Family has no Device(s) or Subfamilies: '%FAMILY%"]
symptom_regex: "^Family has no Device\\(s\\) or Subfamilies: '.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M359`
`Family has no Device(s) or Subfamilies: '%FAMILY%`

## Cause

The device family has no devices or subfamilies. Add the missing information ([/package/devices/family](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_family)).

## Fix

_siehe Cause_
