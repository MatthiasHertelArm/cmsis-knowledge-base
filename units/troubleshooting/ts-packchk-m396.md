---
id: "ts-packchk-m396"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M396: not consecutive (newest first)"
status: "draft"
tool: "packchk"
severity: "error"
code: "M396"
symptoms: ["M396", "Release %TAG% not consecutive (newest first): '%RELEASEVER%', '%RELEASEDATE%' (prev.: '%LATESTVER%', '%LATESTDATE%', see Line %LINE%)"]
symptom_regex: "^Release .+? not consecutive \\(newest first\\): '.+?', '.+?' \\(prev\\.: '.+?', '.+?', see Line .+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M396`
`Release %TAG% not consecutive (newest first): '%RELEASEVER%', '%RELEASEDATE%' (prev.: '%LATESTVER%', '%LATESTDATE%', see Line %LINE%)`

## Cause

Package releases shall be entered in consecutive way: newest release version and latest date first. Rearrange the releases in the list or correct values for the returned 'TAG' attributes (version or date). Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release).

## Fix

_siehe Cause_
