---
id: "ts-packchk-m397"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M397: File extension '.pdsc' must be lowercase: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M397"
symptoms: ["M397", "File extension '.pdsc' must be lowercase: '%PATH%'"]
symptom_regex: "^File extension '\\.pdsc' must be lowercase: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The PDSC file shall have lowercase extension `.pdsc` Correct extension of the PDSC file _'PATH'_."
summary: "packchk found a PDSC file whose extension is not all lowercase, for example 'Device.PDSC' instead of 'Device.pdsc'."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text M397 | File extension '.pdsc' must be lowercase: '%PATH%', source lines not available)"]
---

## Symptom

`M397`
`File extension '.pdsc' must be lowercase: '%PATH%'`

## Cause

packchk found a PDSC file whose extension is not all lowercase, for example 'Device.PDSC' instead of 'Device.pdsc'. The %PATH% in the message is the path of that file. The README states the rule: the pack description file must use the lowercase extension .pdsc. The source itself was not available, so this reading comes from the message text and the README.

## Fix

Rename the file so its extension is lowercase '.pdsc', for example from 'Device.PDSC' to 'Device.pdsc', then run packchk again. Update any references to the old name, such as in the pack's index or build scripts.

## Note

Trigger and handling were not verified in the source because the clone was not available; cause and fix rest on the message text and the README. The README cause text contains a quoting artifact ('PATH' instead of %PATH%).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text M397 | File extension '.pdsc' must be lowercase: '%PATH%', source lines not available)`
