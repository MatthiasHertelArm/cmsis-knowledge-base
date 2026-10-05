---
id: "ts-packchk-m337"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M337: has wrong extension"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M337"
symptoms: ["M337", "File with category '%CAT%' has wrong extension '%EXT%': '%PATH%'%MSG%"]
symptom_regex: "^File with category '.+?' has wrong extension '.+?': '.+?'.+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M337`
`File with category '%CAT%' has wrong extension '%EXT%': '%PATH%'%MSG%`

## Cause

The extension of the file does not match the file category _'CAT'_ specified in the category attribute. Verify the extension to match the category. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

_siehe Cause_
