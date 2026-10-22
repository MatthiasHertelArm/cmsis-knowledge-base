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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The PDSC file is missing release information. Add `<release>` information to the file. Refer to [/package/releases element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html)."
summary: "packchk prints this warning when the PDSC file has no release information, so the package does not declare any version history."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message M338 text; trigger lines not provided)"]
---

## Symptom

`M338`
`No releases found!`

## Cause

packchk prints this warning when the PDSC file has no release information, so the package does not declare any version history. The README attributes it to a missing <release> entry under the package's <releases> element. The source lines were not available, so this is taken from the message text and the README, not from the code.

## Fix

Add a <releases> element to the PDSC file with at least one <release version="x.y.z" date="YYYY-MM-DD"/> entry describing the current package version, then rerun packchk. See the /package/releases element in the CMSIS Pack specification.

## Note

Source lines were unavailable; the trigger condition is inferred from the message text and README only. The README cause and fix were not checked against code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message M338 text; trigger lines not provided)`
