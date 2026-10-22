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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Package version does not follow expected [semantic versioning](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#VersionType). Correct the value specified for the version attribute using correct semantic. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release)."
summary: "packchk found a release version string in the PDSC that is not valid Semantic Versioning, so it cannot use that release entry's version."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M394`
`Not Semantic Versioning, ignoring version: '%RELEASEVER%'`

## Cause

packchk found a release version string in the PDSC that is not valid Semantic Versioning, so it cannot use that release entry's version. The %RELEASEVER% in the message is the version attribute value from the /package/releases/release element that was read. The README says the version must follow the Semantic Versioning form expected by the PDSC specification.

## Fix

Open the PDSC, find the release element whose version attribute is shown in the message, and change it to a valid semantic version such as MAJOR.MINOR.PATCH (for example 1.2.0), then rerun packchk. Check the element against the link in the README for /package/releases/release.

## Note

The source lines were not available, so the trigger and handling could not be checked; the cause is taken from the message text and the README. The message says 'ignoring version', so the tool may skip the release rather than fail the whole package. The README wording is generic and does not give the exact accepted format.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
