---
id: "ts-packchk-m362"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M362: Not all Component Dependencies for 'Cclass="
status: "draft"
tool: "packchk"
severity: "warning"
code: "M362"
symptoms: ["M362", "Not all Component Dependencies for 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%' can be resolved.%MSG%"]
symptom_regex: "^Not all Component Dependencies for 'Cclass=.+?, Cgroup=.+?, Csub=.+?, Cversion=.+?, Capiversion=.+?' can be resolved\\..+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M362`
`Not all Component Dependencies for 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%' can be resolved.%MSG%`

## Cause

Some of the component dependencies could not be resolved. The message might contain additional information. Verify and correct component definition and dependency information. Refer to [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component) attribute _condition_.

## Fix

_siehe Cause_
