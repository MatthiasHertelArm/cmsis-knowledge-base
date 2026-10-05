---
id: "ts-packchk-m600"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M600: Attribute '…' on '…' is deprecated."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M600"
symptoms: ["M600", "Attribute '%ATTR%' on '%TAG%' is deprecated."]
symptom_regex: "^Attribute '.+?' on '.+?' is deprecated\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A <file> element uses attr=\"copy\", which packchk reports as deprecated."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:235", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:189-207", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1105-1131", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/FileAttributeDeprecated/TestVendor.FileAttributeDeprecated.pdsc:35"]
---

## Symptom

`M600`
`Attribute '%ATTR%' on '%TAG%' is deprecated.`

## Cause

A <file> element uses attr="copy", which packchk reports as deprecated.

## Fix

Remove attr="copy" from the <file>; if users are meant to get an editable copy in their project, use attr="config" with a version attribute instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:235`
- `tools/packchk/src/CheckFiles.cpp:189-207`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1105-1131`
- `tools/packchk/test/data/FileAttributeDeprecated/TestVendor.FileAttributeDeprecated.pdsc:35`
