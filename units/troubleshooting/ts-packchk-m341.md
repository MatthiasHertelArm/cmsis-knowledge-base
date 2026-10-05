---
id: "ts-packchk-m341"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M341: dependency must have extension"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M341"
symptoms: ["M341", "File with '%COMP%' dependency must have extension '%EXT%': '%PATH%'"]
symptom_regex: "^File with '.+?' dependency must have extension '.+?': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M341`
`File with '%COMP%' dependency must have extension '%EXT%': '%PATH%'`

## Cause

The file _'PATH'_ with dependency on component _'COMP'_ must have a specific extension _'EXT'_. Verify the dependency and correct the file extension. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

_siehe Cause_
