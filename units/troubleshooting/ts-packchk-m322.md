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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:138", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:350-362", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:424-444"]
---

## Symptom

`M322`
`Associated File/Path not found: '%PATH%'`

## Cause

An <example> has an <environment name="DS5"> whose load points to a '.project' file, but the matching '.cproject' file next to it is missing from the pack; %PATH% is the full path packchk looked for.

## Fix

Add the Eclipse .cproject file beside the .project file in the example folder, or correct the load path.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:138`
- `tools/packchk/src/CheckFiles.cpp:350-362`
- `tools/packchk/src/CheckFiles.cpp:424-444`
