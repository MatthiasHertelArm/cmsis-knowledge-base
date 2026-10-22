---
id: "ts-packchk-m386"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M386: Release date is in future: '…' (today: …)"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M386"
symptoms: ["M386", "Release date is in future: '%RELEASEDATE%' (today: %TODAYDATE%)"]
symptom_regex: "^Release date is in future: '.+?' \\(today: .+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Set the date to the future. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release)."
summary: "packchk found a release entry in the PDSC whose date is later than the current system date."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M386`
`Release date is in future: '%RELEASEDATE%' (today: %TODAYDATE%)`

## Cause

packchk found a release entry in the PDSC whose date is later than the current system date. The message shows the release date from the release element as %RELEASEDATE% and the date packchk considers today as %TODAYDATE%.

## Fix

Correct the date attribute of the offending <release> element in the PDSC so it is not in the future, or set the date to the actual release date. Refer to the CMSIS Pack specification for the release element: https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release

## Note

Source lines were not available; cause and fix come from the message text and the README only. The README cause is terse, so the fix is inferred from the message wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
