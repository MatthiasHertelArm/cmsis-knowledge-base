---
id: "ts-packchk-m333"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M333: Component has no condition: 'Cclass="
status: "draft"
tool: "packchk"
severity: "warning"
code: "M333"
symptoms: ["M333", "Component has no condition: 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%'"]
symptom_regex: "^Component has no condition: 'Cclass=.+?, Cgroup=.+?, Csub=.+?, Cversion=.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M333`
`Component has no condition: 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%'`

## Cause

The component defined has no condition. If the component has restrictions, then add a condition to the component definition. Refer to [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component).

## Fix

_siehe Cause_
