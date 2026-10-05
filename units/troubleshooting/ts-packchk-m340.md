---
id: "ts-packchk-m340"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M340: must end with '/"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M340"
symptoms: ["M340", "Include Path '%PATH%' must end with '/'"]
symptom_regex: "^Include Path '.+?' must end with '/'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M340`
`Include Path '%PATH%' must end with '/'`

## Cause

Include paths must end with a slash or backslash. Verify and correct the path name. Refer to [/package/.../files/file](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html#element_file).

## Fix

_siehe Cause_
