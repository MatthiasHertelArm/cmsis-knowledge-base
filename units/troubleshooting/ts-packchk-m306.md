---
id: "ts-packchk-m306"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M306: No package description found in the PDSC file. Add the <description> tag and provide a descriptive …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M306"
symptoms: ["M306", "No package description found in the PDSC file. Add the <description> tag and provide a descriptive text. For example: <description>Device Family Pack for  ...</description>."]
symptom_regex: "^No package description found in the PDSC file\\. Add the <description> tag$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Package description is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:118-120", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:317-320", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:952-986", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:155"]
---

## Symptom

`M306`
`No package description found in the PDSC file. Add the <description> tag and provide a descriptive text. For example: <description>Device Family Pack for  ...</description>.`

## Cause

Package description is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element add the tag `<description>` and briefly describe the package content. Refer to [/package/description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_description).

## Fix

Add <description>Device Family Pack for ...</description> under <package>; keep it to plain ASCII on one line, within 128 characters, to avoid M387 and M388.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:118-120`
- `tools/packchk/src/ValidateSyntax.cpp:317-320`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:952-986`
- `tools/packchk/README.md:155`
