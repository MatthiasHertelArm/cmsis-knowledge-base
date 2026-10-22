---
id: "ts-packchk-m345"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M345: URL not found: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M345"
symptoms: ["M345", "URL not found: '%URL%'"]
symptom_regex: "^URL not found: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The specified URL could not be found. Correct the URL. Refer to [/package](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#element_package)."
summary: "packchk prints this warning when a URL taken from the PDSC is checked and cannot be found, for example the URL attribute of a release or the package URL in the .pdsc file points to a location that does …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M345`
`URL not found: '%URL%'`

## Cause

packchk prints this warning when a URL taken from the PDSC is checked and cannot be found, for example the URL attribute of a release or the package URL in the .pdsc file points to a location that does not exist. The %URL% placeholder is the URL string that failed the check. The source lines were not available, so this is taken from the message text and the README.

## Fix

Open the .pdsc file, find the URL reported in the message and correct it so that it points to the actual location of the resource; then run packchk again. Check the URL in a browser or with curl to confirm it resolves.

## Note

Source lines were not available for the trigger, so the exact PDSC element that carries the URL is not confirmed; the README text is the only support for the fix. The README points to the package element documentation for the URL attribute.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
