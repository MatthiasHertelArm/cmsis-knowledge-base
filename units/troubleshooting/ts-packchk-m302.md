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
summary: "Vendor name is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:112-113", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:279-283", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:335-341", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:151"]
---

## Symptom

`M302`
`No vendor tag found in the PDSC file. Add the <vendor> tag and provide the vendor name. For example: <vendor>Keil</vendor>.`

## Cause

Vendor name is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element enter the tag `<vendor>` and add the vendor name. For example: `<vendor>Keil</vendor>`. Refer to [/package/vendor](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_vendor).

## Fix

Add <vendor>MyVendor</vendor> under <package>; the value is also the first part of the PDSC file name (<vendor>.<name>.pdsc).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:112-113`
- `tools/packchk/src/ValidateSyntax.cpp:279-283`
- `tools/packchk/src/ValidateSyntax.cpp:335-341`
- `tools/packchk/README.md:151`
