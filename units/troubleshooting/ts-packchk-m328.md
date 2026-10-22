---
id: "ts-packchk-m328"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M328: Version not set for Release Information '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M328"
symptoms: ["M328", "Version not set for Release Information '%DESCR%'"]
symptom_regex: "^Version not set for Release Information '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The release defined through the description _'DESCR'_ requires the attribute `<version>`. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release)."
summary: "A release entry in the PDSC file under /package/releases/release has no version attribute. packchk reports the release by its description text, which is the value substituted for %DESCR%."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M328`
`Version not set for Release Information '%DESCR%'`

## Cause

A release entry in the PDSC file under /package/releases/release has no version attribute. packchk reports the release by its description text, which is the value substituted for %DESCR%. The PDSC spec requires each release to carry a version.

## Fix

Open the PDSC file, find the <release> element whose description matches the reported text, and add a version attribute, for example <release version="1.2.3" date="YYYY-MM-DD">. Then rerun packchk.

## Note

The source clone was not available, so the trigger and handling were not checked in code. The cause and fix come from the message text and the README only. The README wording about the description _'DESCR'_ is taken as given.
