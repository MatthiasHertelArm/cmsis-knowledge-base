---
id: "ts-packchk-m377"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M377: must have 'attr=\"config"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M377"
symptoms: ["M377", "File '%NAME%' %TYPE% must have 'attr=\"config\"'"]
symptom_regex: "^File '.+?' .+? must have 'attr=\"config\"'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M377`
`File '%NAME%' %TYPE% must have 'attr="config"'`

## Cause

The category _'TYPE'_ of the file _'NAME'_ requires it to be defined as a configuration file. Add the attribute attr="config" to the `<file>` element that defines the file. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

_siehe Cause_
