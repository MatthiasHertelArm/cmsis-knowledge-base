---
id: "ts-packchk-m323"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M323: File/Path not found: '…'. Check correct spelling."
status: "draft"
tool: "packchk"
severity: "error"
code: "M323"
symptoms: ["M323", "File/Path not found: '%PATH%'. Check correct spelling."]
symptom_regex: "^File/Path not found: '.+?'\\. Check correct spelling\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The file or path _'PATH'_ entered in the PDSC file could not be found."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:139", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:424-451", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:589-620", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:164"]
---

## Symptom

`M323`
`File/Path not found: '%PATH%'. Check correct spelling.`

## Cause

The file or path _'PATH'_ entered in the PDSC file could not be found. Verify the path information.

## Fix

Correct the path (relative to the PDSC folder, forward slashes, matching letter case) or add the missing file to the pack; %PATH% is the full path packchk looked for.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:139`
- `tools/packchk/src/CheckFiles.cpp:424-451`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:589-620`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247`
- `tools/packchk/README.md:164`
