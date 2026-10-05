---
id: "ts-packchk-m342"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M342: must not have category"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M342"
symptoms: ["M342", "File with attribute '%ATTR%' must not have category '%CAT%': '%PATH%'"]
symptom_regex: "^File with attribute '.+?' must not have category '.+?': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M342`
`File with attribute '%ATTR%' must not have category '%CAT%': '%PATH%'`

## Cause

File _'PATH'_ is defined with the attribute attr set to _'ATTR'_. This conflicts with the file category _'CAT'_ specified in category attribute. For example attr=config and category=include are not allowed for the same file. Correct the file attribute or the file category. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

_siehe Cause_
