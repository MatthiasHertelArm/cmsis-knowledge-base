---
id: "ts-packchk-m334"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M334: Config File has no version"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M334"
symptoms: ["M334", "Config File has no version: '%PATH%'"]
symptom_regex: "^Config File has no version: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M334`
`Config File has no version: '%PATH%'`

## Cause

Specified file 'PATH' does not contain version information. It is recommended to specify versions for configuration files. Add attribute version with the file version in the `<file>` tag that defines the _'PATH'_ file in the PDSC. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

_siehe Cause_
