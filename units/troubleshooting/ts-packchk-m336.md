---
id: "ts-packchk-m336"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M336: which shall contain device specific components.   The referenced condi"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M336"
symptoms: ["M336", "Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%, condition=%COND%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   The referenced condition id does not contain a rule filtering for a device or set of devices."]
symptom_regex: "^Component 'Cclass=.+?, Cgroup=.+?, Cversion=.+?, condition=.+?' is member of the Cclass='.+?' which shall contain device specific components\\.   The referenced condition id does not contain a rule filtering for a device or set of devices\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M336`
`Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%, condition=%COND%' is member of the Cclass='%CCLASS%' which shall contain device specific components.   The referenced condition id does not contain a rule filtering for a device or set of devices.`

## Cause

Define the device [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device) or correct the information about the device in the reference.

## Fix

_siehe Cause_
