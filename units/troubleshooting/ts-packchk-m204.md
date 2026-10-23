---
id: "ts-packchk-m204"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M204: File not found: '…'!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M204"
symptoms: ["M204", "File not found: '%PATH%'!"]
symptom_regex: "^File not found: '.+?'!$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The specified PDSC file could not be found in the _PATH_ displayed in the message."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:88", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackOptions.cpp:171-188", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:101-106", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:89-108", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:133"]
---

## Symptom

`M204`
`File not found: '%PATH%'!`

## Cause

The specified PDSC file could not be found in the _PATH_ displayed in the message. Correct the path or the filename.

## Fix

Correct the path or name of the PDSC on the command line; a relative path is resolved against the current working directory.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:88`
- `tools/packchk/src/PackOptions.cpp:171-188`
- `tools/packchk/src/CreateModel.cpp:101-106`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:89-108`
- `tools/packchk/README.md:133`
