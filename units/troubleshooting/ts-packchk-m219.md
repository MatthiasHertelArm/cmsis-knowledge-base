---
id: "ts-packchk-m219"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M219: Unable to find specified schema file '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M219"
symptoms: ["M219", "Unable to find specified schema file '%PATH%'"]
symptom_regex: "^Unable to find specified schema file '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk could not locate the XML schema file it needs to validate a PDSC file, so the path shown in the message does not exist or is not readable from the tool's schema lookup location."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger, source lines not available in this session)"]
---

## Symptom

`M219`
`Unable to find specified schema file '%PATH%'`

## Cause

packchk could not locate the XML schema file it needs to validate a PDSC file, so the path shown in the message does not exist or is not readable from the tool's schema lookup location. The message is printed when the schema file named by %PATH% cannot be found, which typically means the tool installation or the schema directory it searches is incomplete or was moved.

## Fix

Check that the schema file named in the message exists at the printed path and is readable. If it is missing, reinstall or update the CMSIS tools that provide packchk so the schema files are restored, then rerun the pack check.

## Note

Answered from the message text alone because the clone was not available; the trigger condition and the exact schema lookup logic were not verified against the source, so the cause is an inference from the message wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger, source lines not available in this session)`
