---
id: "ts-packchk-m394"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M394: Not Semantic Versioning, ignoring version: '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M394"
symptoms: ["M394", "Not Semantic Versioning, ignoring version: '%RELEASEVER%'"]
symptom_regex: "^Not Semantic Versioning, ignoring version: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Package version does not follow expected [semantic versioning](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#VersionType)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:213", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:449-455", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:407-451", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:228"]
---

## Symptom

`M394`
`Not Semantic Versioning, ignoring version: '%RELEASEVER%'`

## Cause

Package version does not follow expected [semantic versioning](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#VersionType). Correct the value specified for the version attribute using correct semantic. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release).

## Fix

Use MAJOR.MINOR.PATCH with optional -prerelease and +build parts, e.g. version="1.2.0" or version="1.2.0-rc1".

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:213`
- `tools/packchk/src/ValidateSyntax.cpp:449-455`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:407-451`
- `tools/packchk/README.md:228`
