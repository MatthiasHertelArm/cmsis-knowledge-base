---
id: "ts-packchk-m386"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M386: Release date is in future"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M386"
symptoms: ["M386", "Release date is in future: '%RELEASEDATE%' (today: %TODAYDATE%)"]
symptom_regex: "^Release date is in future: '.+?' \\(today: .+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M386`
`Release date is in future: '%RELEASEDATE%' (today: %TODAYDATE%)`

## Cause

Set the date to the future. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release).

## Fix

_siehe Cause_
