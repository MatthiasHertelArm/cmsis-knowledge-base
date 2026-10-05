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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Set the date to the future. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:205", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:417-475", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:224"]
---

## Symptom

`M386`
`Release date is in future: '%RELEASEDATE%' (today: %TODAYDATE%)`

## Cause

The date attribute of a <release> is later than today's date on the machine that runs packchk. The README advice 'Set the date to the future' is inverted.

## Fix

Set date to the actual release date, today or earlier, in YYYY-MM-DD form.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:205`
- `tools/packchk/src/ValidateSyntax.cpp:417-475`
- `tools/packchk/README.md:224`
