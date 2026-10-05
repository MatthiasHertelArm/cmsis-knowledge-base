---
id: "ts-packchk-m374"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M374: While checking Feature for"
status: "draft"
tool: "packchk"
severity: "error"
code: "M374"
symptoms: ["M374", "While checking Feature for '%MCU%': Pname '%CPU%' not found."]
symptom_regex: "^While checking Feature for '.+?': Pname '.+?' not found\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M374`
`While checking Feature for '%MCU%': Pname '%CPU%' not found.`

## Cause

The processor could not be found for the specified device. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device) and [/package/devices/family/.../processor](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_processor).

## Fix

_siehe Cause_
