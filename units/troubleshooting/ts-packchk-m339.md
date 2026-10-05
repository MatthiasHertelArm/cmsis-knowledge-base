---
id: "ts-packchk-m339"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M339: must not be a file!"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M339"
symptoms: ["M339", "Include Path '%PATH%' must not be a file!"]
symptom_regex: "^Include Path '.+?' must not be a file!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M339`
`Include Path '%PATH%' must not be a file!`

## Cause

The path specified contains a filename. Correct the path infomation and remove the filename. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

_siehe Cause_
