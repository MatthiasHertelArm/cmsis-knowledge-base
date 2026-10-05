---
id: "ts-packchk-m392"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M392: Redefined Device or Variant"
status: "draft"
tool: "packchk"
severity: "error"
code: "M392"
symptoms: ["M392", "Redefined Device or Variant '%NAME%': %MSG%"]
symptom_regex: "^Redefined Device or Variant '.+?': .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M392`
`Redefined Device or Variant '%NAME%': %MSG%`

## Cause

Multiple defitions of device or variant _'NAME'_ are found. Use unique names for the devices listed in the message _'MSG'_. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device) and [/package/devices/family/.../device/variant](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_variant)

## Fix

_siehe Cause_
