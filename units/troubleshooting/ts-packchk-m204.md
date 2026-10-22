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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The specified PDSC file could not be found in the _PATH_ displayed in the message. Correct the path or the filename."
summary: "packchk was given a path to a PDSC file that does not exist or cannot be opened."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the clone; message id M204 and text 'File not found' taken from the message as printed)"]
---

## Symptom

`M204`
`File not found: '%PATH%'!`

## Cause

packchk was given a path to a PDSC file that does not exist or cannot be opened. The %PATH% in the message is the path as packchk received it, so the path on the command line or the pack directory it was pointed at is the value to check. The README gives the same cause: the PDSC file is not at the displayed location.

## Fix

Check the path printed in the message. Correct the directory or the file name passed to packchk so it points to an existing .pdsc file, for example by running packchk on the full path of the PDSC file in the pack root.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and the README rather than read from the code. The exact check that raises M204 is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the clone; message id M204 and text 'File not found' taken from the message as printed)`
