---
id: "ts-packchk-m347"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M347: Generator ID in Component 'Cclass="
status: "draft"
tool: "packchk"
severity: "warning"
code: "M347"
symptoms: ["M347", "Generator ID in Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is undefined: '%GENID%'"]
symptom_regex: "^Generator ID in Component 'Cclass=.+?, Cgroup=.+?, Cversion=.+?' is undefined: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M347`
`Generator ID in Component 'Cclass=%CCLASS%, Cgroup=%CGROUP%, Cversion=%CVER%' is undefined: '%GENID%'`

## Cause

The generator ID used in the component could not be found. Verify and correct the generator ID ([/package/components/.../component](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_component)), or define the generator ID (ref [/package/generators/generator](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html#element_generator)).

## Fix

_siehe Cause_
