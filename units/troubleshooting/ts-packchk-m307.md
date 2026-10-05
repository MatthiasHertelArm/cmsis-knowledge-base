---
id: "ts-packchk-m307"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M307: must be specified for 'memory"
status: "draft"
tool: "packchk"
severity: "error"
code: "M307"
symptoms: ["M307", "Either attribute '%TAG%' or '%TAG2%' + '%TAG3%' must be specified for 'memory'"]
symptom_regex: "^Either attribute '.+?' or '.+?' \\+ '.+?' must be specified for 'memory'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M307`
`Either attribute '%TAG%' or '%TAG2%' + '%TAG3%' must be specified for 'memory'`

## Cause

`<memory>` element requires that either attribute id or attributes name and access are specified, but none of those were found. Specify the expected attributes. Refer to [/package/devices/family/.../memory](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_memory).

## Fix

_siehe Cause_
