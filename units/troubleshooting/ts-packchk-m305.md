---
id: "ts-packchk-m305"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M305: No releases (\"<release>\" elements in a <releases>-tag) found in PDSC f"
status: "draft"
tool: "packchk"
severity: "error"
code: "M305"
symptoms: ["M305", "No releases (\"<release>\" elements in a <releases>-tag) found in PDSC file!"]
symptom_regex: "^No releases \\(\"<release>\" elements in a <releases>\\-tag\\) found in PDSC file!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M305`
`No releases ("<release>" elements in a <releases>-tag) found in PDSC file!`

## Cause

At least one package release shall be specified in the PDSC file, but none was not found. Use `<release>` tag to specify release information in `<releases>` element. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release).

## Fix

_siehe Cause_
