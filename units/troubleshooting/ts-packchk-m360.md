---
id: "ts-packchk-m360"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M360: Subfamily has no Device(s)"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M360"
symptoms: ["M360", "Subfamily has no Device(s): '%SUBFAMILY%"]
symptom_regex: "^Subfamily has no Device\\(s\\): '.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M360`
`Subfamily has no Device(s): '%SUBFAMILY%`

## Cause

Add the missing information. Refer to [/package/devices/family/subFamily](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_subFamily).

## Fix

_siehe Cause_
