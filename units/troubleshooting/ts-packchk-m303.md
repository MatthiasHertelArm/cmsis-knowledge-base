---
id: "ts-packchk-m303"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M303: No package name found in the PDSC file. Add the <name> tag and provide the package name. For …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M303"
symptoms: ["M303", "No package name found in the PDSC file. Add the <name> tag and provide the package name. For example: <name>MCU-Name_DFP</name>."]
symptom_regex: "^No package name found in the PDSC file\\. Add the <name> tag and provide the package name\\. For example: <name>MCU\\-Name_DFP</name>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:114-115", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:285-289", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:335-341", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:152"]
---

## Symptom

`M303`
`No package name found in the PDSC file. Add the <name> tag and provide the package name. For example: <name>MCU-Name_DFP</name>.`

## Cause

Package name is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element enter the tag `<name>` and add the package name. For example `<name>MCU-Name_DFP</name>`. Refer to [/package/name](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_name).

## Fix

Add <name>MyPack</name> under <package>; it must equal the second part of the PDSC file name (<vendor>.<name>.pdsc).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:114-115`
- `tools/packchk/src/ValidateSyntax.cpp:285-289`
- `tools/packchk/src/ValidateSyntax.cpp:335-341`
- `tools/packchk/README.md:152`
