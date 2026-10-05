---
id: "ts-packchk-m304"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M304: No package URL (<url>-tag and/or value) found in PDSC file!"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M304"
symptoms: ["M304", "No package URL (<url>-tag and/or value) found in PDSC file!"]
symptom_regex: "^No package URL \\(<url>\\-tag and/or value\\) found in PDSC file!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M304`
`No package URL (<url>-tag and/or value) found in PDSC file!`

## Cause

Package URL is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element enter the tag `<url>` and add the URL that should be used to download the package. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url).

## Fix

_siehe Cause_
