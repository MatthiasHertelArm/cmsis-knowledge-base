---
id: "ts-packchk-m210"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M210: Only one input file to be checked is allowed."
status: "draft"
tool: "packchk"
severity: "error"
code: "M210"
symptoms: ["M210", "Only one input file to be checked is allowed."]
symptom_regex: "^Only one input file to be checked is allowed\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "You can only check one PDSC file at a time."
summary: "packchk was invoked with more than one input file, but it accepts only a single PDSC file per run."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M210`
`Only one input file to be checked is allowed.`

## Cause

packchk was invoked with more than one input file, but it accepts only a single PDSC file per run. The README states that only one PDSC file can be checked at a time. The source lines were not available, so this is taken from the message text and the README rather than from the trigger code.

## Fix

Run packchk once per PDSC file, passing exactly one input file on each command line, for example: packchk path/to/first.pdsc, then packchk path/to/second.pdsc.

## Note

Trigger code was not available for review; the cause and fix rest on the message text and the README. Check the argument parsing in PackChk_Msgs.cpp or the packchk entry point before relying on the exact wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
