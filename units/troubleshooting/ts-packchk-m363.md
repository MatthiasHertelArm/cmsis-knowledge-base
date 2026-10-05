---
id: "ts-packchk-m363"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M363: No API defined for Component 'Cclass="
status: "draft"
tool: "packchk"
severity: "warning"
code: "M363"
symptoms: ["M363", "No API defined for Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%'"]
symptom_regex: "^No API defined for Component 'Cclass=.+?, Cgroup=.+?, Csub=.+?, Cversion=.+?, Capiversion=.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M363`
`No API defined for Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Csub=%CSUB%, Cversion=%CVER%, Capiversion=%APIVER%'`

## Cause

The package is missing the API information for the specified component. Refer to [/package/apis](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_apis_pg.html#element_apis).

## Fix

_siehe Cause_
