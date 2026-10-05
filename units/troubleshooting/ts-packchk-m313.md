---
id: "ts-packchk-m313"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M313: Associated File/Path is outside PACK root: '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M313"
symptoms: ["M313", "Associated File/Path is outside PACK root: '%PATH%'"]
symptom_regex: "^Associated File/Path is outside PACK root: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:129", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:483-502", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:343-348", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:622-647", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/TestPackRoot/Pack/TestVendor.TestPackRoot.pdsc:31"]
---

## Symptom

`M313`
`Associated File/Path is outside PACK root: '%PATH%'`

## Cause

A file or folder referenced in the PDSC resolves to a location outside the folder that contains the PDSC (the pack root), typically through '../' segments in its path.

## Fix

Move the file into the pack folder tree and reference it with a path relative to the PDSC that stays inside it, e.g. name="Source/test2.c" instead of name="../ExtFiles/test2.c".

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:129`
- `tools/packchk/src/CheckFiles.cpp:483-502`
- `tools/packchk/src/CheckFiles.cpp:343-348`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:622-647`
- `tools/packchk/test/data/TestPackRoot/Pack/TestVendor.TestPackRoot.pdsc:31`
