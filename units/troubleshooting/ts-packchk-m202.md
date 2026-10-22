---
id: "ts-packchk-m202"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M202: No PDSC input file specified"
status: "draft"
tool: "packchk"
severity: "error"
code: "M202"
symptoms: ["M202", "No PDSC input file specified"]
symptom_regex: "^No PDSC input file specified$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct the command line. **packchk** expects a *.pdsc file name as input."
summary: "packchk was started without a PDSC file name on its command line, so there is no pack description to check."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (source lines not available; message id M202 and its trigger taken from the message text and README only)"]
---

## Symptom

`M202`
`No PDSC input file specified`

## Cause

packchk was started without a PDSC file name on its command line, so there is no pack description to check. The README states that packchk expects a *.pdsc file as its input.

## Fix

Run packchk again with the path to the pack's .pdsc file as the input argument, for example: packchk <path-to-pack>/<PackName>.pdsc

## Note

The source clone was not available, so the trigger condition was not read from code; the cause rests on the message text and the README. Exact packchk option syntax was not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (source lines not available; message id M202 and its trigger taken from the message text and README only)`
