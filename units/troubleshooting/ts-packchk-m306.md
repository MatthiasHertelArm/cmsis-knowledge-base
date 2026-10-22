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
symptom_regex: "^No package description found in the PDSC file\\. Add the <description> tag and provide a descriptive text\\. For example: <description>Device Family Pack for  \\.\\.\\.</description>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Package description is mandatory required in the package description but was not found in the [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package) element in the PDSC file. Within the parent `<package>` element add the tag `<description>` and briefly describe the package content. Refer to [/package/description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_description)."
summary: "packchk found no <description> element under the root <package> element of the PDSC file, so the package has no descriptive text."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M306`
`No package description found in the PDSC file. Add the <description> tag and provide a descriptive text. For example: <description>Device Family Pack for  ...</description>.`

## Cause

packchk found no <description> element under the root <package> element of the PDSC file, so the package has no descriptive text. The README states the description is required and must be a child of <package>. The source lines were not available, so this rests on the message text and the README.

## Fix

Open the PDSC file, add a <description> child inside the root <package> element with a short text describing the pack content, for example <description>Device Family Pack for ...</description>, and rerun packchk.

## Note

Source lines were unavailable; the trigger location in tools/packchk/src/PackChk_Msgs.cpp could not be checked, so the cause is taken from the message text and the README.
