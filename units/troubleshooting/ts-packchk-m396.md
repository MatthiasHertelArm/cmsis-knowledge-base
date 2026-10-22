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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Package releases shall be entered in consecutive way: newest release version and latest date first. Rearrange the releases in the list or correct values for the returned 'TAG' attributes (version or date). Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release)."
summary: "packchk checks the <releases> list of a PDSC: consecutive entries must be ordered newest first, with version and date both decreasing."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text M396; trigger and handling lines not available in this clone)"]
---

## Symptom

`M396`
`Release %TAG% not consecutive (newest first): '%RELEASEVER%', '%RELEASEDATE%' (prev.: '%LATESTVER%', '%LATESTDATE%', see Line %LINE%)`

## Cause

packchk checks the <releases> list of a PDSC: consecutive entries must be ordered newest first, with version and date both decreasing. The message is printed when the release '%RELEASEVER%' dated '%RELEASEDATE%' is not consecutive to the previous entry '%LATESTVER%' dated '%LATESTDATE%' at line %LINE%, meaning the release order or the date/version attributes of the releases do not follow each other.

## Fix

Open the PDSC at the reported line and check the <release version=... date=...> entries: move the releases so the newest comes first, or correct the version or date attribute of the release named in the message so that the order is consistent. Refer to the release element of the Open-CMSIS-Pack specification for the expected format.

## Note

Source lines unavailable; the cause and fix are based on the message text and the README, not on the trigger code. The message wording says the release is 'not consecutive', which may also be triggered by an out-of-order date alone.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text M396; trigger and handling lines not available in this clone)`
