---
id: "ts-packchk-m338"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M338: No releases found!"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M338"
symptoms: ["M338", "No releases found!"]
symptom_regex: "^No releases found!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M338`
`No releases found!`

## Cause

The PDSC file is missing release information. Add `<release>` information to the file. Refer to [/package/releases element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html).

## Fix

_siehe Cause_
