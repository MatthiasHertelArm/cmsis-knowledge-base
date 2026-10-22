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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Package URL is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:116", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:502-511", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:153"]
---

## Symptom

`M304`
`No package URL (<url>-tag and/or value) found in PDSC file!`

## Cause

Package URL is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element enter the tag `<url>` and add the URL that should be used to download the package. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url).

## Fix

Add <url> under <package> with the location the pack is downloaded from, ending in '/', e.g. <url>https://www.myvendor.com/pack/</url>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:116`
- `tools/packchk/src/ValidateSyntax.cpp:502-511`
- `tools/packchk/README.md:153`
