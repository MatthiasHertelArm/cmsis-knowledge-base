---
id: "ts-packchk-m306"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M306: No package description found in the PDSC file. Add the <description> t"
status: "draft"
tool: "packchk"
severity: "error"
code: "M306"
symptoms: ["M306", "No package description found in the PDSC file. Add the <description> tag and provide a descriptive text. For example: <description>Device Family Pack for  ...</description>."]
symptom_regex: "^No package description found in the PDSC file\\. Add the <description> tag and provide a descriptive text\\. For example: <description>Device Family Pack for  \\.\\.\\.</description>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M306`
`No package description found in the PDSC file. Add the <description> tag and provide a descriptive text. For example: <description>Device Family Pack for  ...</description>.`

## Cause

Package description is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element add the tag `<description>` and briefly describe the package content. Refer to [/package/description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_description).

## Fix

_siehe Cause_
