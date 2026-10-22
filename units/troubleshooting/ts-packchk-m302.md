---
id: "ts-packchk-m302"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M302: No vendor tag found in the PDSC file. Add the <vendor> tag and provide the vendor name. For …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M302"
symptoms: ["M302", "No vendor tag found in the PDSC file. Add the <vendor> tag and provide the vendor name. For example: <vendor>Keil</vendor>."]
symptom_regex: "^No vendor tag found in the PDSC file\\. Add the <vendor> tag and provide the vendor name\\. For example: <vendor>Keil</vendor>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Vendor name is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element enter the tag `<vendor>` and add the vendor name. For example: `<vendor>Keil</vendor>`. Refer to [/package/vendor](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_vendor)."
summary: "packchk checks the PDSC file's top-level package description and found no <vendor> element inside the <package> element."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M302`
`No vendor tag found in the PDSC file. Add the <vendor> tag and provide the vendor name. For example: <vendor>Keil</vendor>.`

## Cause

packchk checks the PDSC file's top-level package description and found no <vendor> element inside the <package> element. The vendor name is required there, so the check fails. The source lines were not available, so this is taken from the message and the README rather than the code.

## Fix

Open the PDSC file and, inside the root <package> element, add a <vendor> element containing the vendor name, for example: <vendor>Keil</vendor>. Then rerun packchk on the pack.

## Note

Source lines were not provided, so the trigger location in tools/packchk/src/PackChk_Msgs.cpp could not be checked and no line references are given. The cause and fix follow the message text and the README.
