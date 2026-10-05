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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The release defined through the version _'VER'_ needs a description."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:145", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:303-314", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:407-451", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:170"]
---

## Symptom

`M329`
`Description not set for Release Information '%VER%'`

## Cause

The release defined through the version _'VER'_ needs a description. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release).

## Fix

Write the release notes as text of the <release>, e.g. <release version="1.2.0" date="2026-01-31">Added USB driver</release>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:145`
- `tools/packchk/src/ValidateSyntax.cpp:303-314`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:407-451`
- `tools/packchk/README.md:170`
