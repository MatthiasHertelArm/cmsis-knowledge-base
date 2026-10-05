---
id: "ts-packchk-m302"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M302: No vendor tag found in the PDSC file. Add the <vendor> tag and provide"
status: "draft"
tool: "packchk"
severity: "error"
code: "M302"
symptoms: ["M302", "No vendor tag found in the PDSC file. Add the <vendor> tag and provide the vendor name. For example: <vendor>Keil</vendor>."]
symptom_regex: "^No vendor tag found in the PDSC file\\. Add the <vendor> tag and provide the vendor name\\. For example: <vendor>Keil</vendor>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M302`
`No vendor tag found in the PDSC file. Add the <vendor> tag and provide the vendor name. For example: <vendor>Keil</vendor>.`

## Cause

Vendor name is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element enter the tag `<vendor>` and add the vendor name. For example: `<vendor>Keil</vendor>`. Refer to [/package/vendor](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_vendor).

## Fix

_siehe Cause_
