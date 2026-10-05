---
id: "ts-packchk-m378"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M378: but does not attribute 'Capiversion' specifying the version it impleme"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M378"
symptoms: ["M378", "Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, implements the API defined in '%NAME%' but does not attribute 'Capiversion' specifying the version it implements."]
symptom_regex: "^Component 'Cclass=.+?, Cgroup=.+?, Csub=.+?, Cversion=.+?, implements the API defined in '.+?' but does not attribute 'Capiversion' specifying the version it implements\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M378`
`Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, implements the API defined in '%NAME%' but does not attribute 'Capiversion' specifying the version it implements.`

## Cause

Add attribute Capiversion specifying the API version that is implemented in the component described in the message. Refer to [/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component).

## Fix

_siehe Cause_
