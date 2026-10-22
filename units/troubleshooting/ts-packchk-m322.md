---
id: "ts-packchk-m322"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M322: Associated File/Path not found: '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M322"
symptoms: ["M322", "Associated File/Path not found: '%PATH%'"]
symptom_regex: "^Associated File/Path not found: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk checks that every file or path referenced by the PDSC is present in the pack directory."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M322`
`Associated File/Path not found: '%PATH%'`

## Cause

packchk checks that every file or path referenced by the PDSC is present in the pack directory. The message is printed when a path referenced in the PDSC, such as a file entry or an associated file, does not exist at the location the PDSC names relative to the pack root. The '%PATH%' placeholder is the referenced path as written in the PDSC.

## Fix

Open the PDSC, find the entry whose path matches the value printed in the message, and either add the missing file at that location in the pack or correct the path in the PDSC so it points to the existing file. Then rerun packchk.

## Note

Written from the message text and the id alone, since the clone was not available; the trigger condition was not read from source. Check the exact check in PackChk_Msgs.cpp before relying on the wording of the cause.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
