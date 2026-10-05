---
id: "ts-packchk-m361"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M361: Generator ID in Taxonomy 'Cclass="
status: "draft"
tool: "packchk"
severity: "warning"
code: "M361"
symptoms: ["M361", "Generator ID in Taxonomy 'Cclass=%CCLASS%, Cgroup=%CGROUP%' is undefined: '%GENID%'"]
symptom_regex: "^Generator ID in Taxonomy 'Cclass=.+?, Cgroup=.+?' is undefined: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M361`
`Generator ID in Taxonomy 'Cclass=%CCLASS%, Cgroup=%CGROUP%' is undefined: '%GENID%'`

## Cause

The generator ID used in the taxonomy is not defined. Define or correct the generator ID ([/package/taxonomy element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_taxonomy.html)).

## Fix

_siehe Cause_
