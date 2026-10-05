---
id: "ts-packchk-m394"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M394: Not Semantic Versioning, ignoring version"
status: "draft"
tool: "packchk"
severity: "error"
code: "M394"
symptoms: ["M394", "Not Semantic Versioning, ignoring version: '%RELEASEVER%'"]
symptom_regex: "^Not Semantic Versioning, ignoring version: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M394`
`Not Semantic Versioning, ignoring version: '%RELEASEVER%'`

## Cause

Package version does not follow expected [semantic versioning](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#VersionType). Correct the value specified for the version attribute using correct semantic. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release).

## Fix

_siehe Cause_
