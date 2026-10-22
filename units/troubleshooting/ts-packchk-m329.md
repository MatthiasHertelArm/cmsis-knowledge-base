---
id: "ts-packchk-m329"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M329: Description not set for Release Information '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M329"
symptoms: ["M329", "Description not set for Release Information '%VER%'"]
symptom_regex: "^Description not set for Release Information '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The release defined through the version _'VER'_ needs a description. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release)."
summary: "The PDSC file has a <release> element under <releases> whose version is VER but which has no text content describing the release. packchk emits M329 for each release entry that lacks a description; the %VER% placeholder is the version …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M329`
`Description not set for Release Information '%VER%'`

## Cause

The PDSC file has a <release> element under <releases> whose version is VER but which has no text content describing the release. packchk emits M329 for each release entry that lacks a description; the %VER% placeholder is the version attribute of that release.

## Fix

Open the PDSC file, find the <release> element with version="VER" inside <releases>, and add a description as the element's text content, for example <release version="1.0.0" date="2024-01-01">Initial release</release>. Then rerun packchk.

## Note

Source lines were not available; cause and fix come from the message text and the README entry, which points to the /package/releases/release element of the Pack Specification. Exact wording of the description requirement is not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
