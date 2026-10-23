---
id: "ts-packchk-m396"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M396: Release … not consecutive (newest first): '…', '…' (prev.: '…', '…', see Line …)"
status: "draft"
tool: "packchk"
severity: "error"
code: "M396"
symptoms: ["M396", "Release %TAG% not consecutive (newest first): '%RELEASEVER%', '%RELEASEDATE%' (prev.: '%LATESTVER%', '%LATESTDATE%', see Line %LINE%)"]
symptom_regex: "^Release .+? not consecutive \\(newest first\\): '.+?', '.+?' \\(prev\\.: '.+?', '.+?', see Line .+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Package releases shall be entered in consecutive way: newest release version and latest date first. Rearrange the releases in the list or correct values for the returned 'TAG' attributes (version or date). Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release)."
summary: "The <release> elements are not ordered newest first by version: a release has a version equal to or higher than the release listed before it."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:215", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:477-489", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:407-451", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:230"]
---

## Symptom

`M396`
`Release %TAG% not consecutive (newest first): '%RELEASEVER%', '%RELEASEDATE%' (prev.: '%LATESTVER%', '%LATESTDATE%', see Line %LINE%)`

## Cause

The <release> elements are not ordered newest first by version: a release has a version equal to or higher than the release listed before it. Only versions are compared, not dates; %TAG% is always 'Version'.

## Fix

Order the releases by strictly decreasing version, newest first, and remove duplicate version entries.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:215`
- `tools/packchk/src/ValidateSyntax.cpp:477-489`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:407-451`
- `tools/packchk/README.md:230`
