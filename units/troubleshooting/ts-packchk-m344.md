---
id: "ts-packchk-m344"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M344: File shall have condition containing"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M344"
symptoms: ["M344", "File shall have condition containing '%COND%': '%PATH%'"]
symptom_regex: "^File shall have condition containing '.+?': '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M344`
`File shall have condition containing '%COND%': '%PATH%'`

## Cause

File definition for _'PATH'_ shall contain a condition _'COND'_. Add attribute condition with the _'COND'_ in the `<file>` tag that defines the _'PATH'_ file. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

_siehe Cause_
