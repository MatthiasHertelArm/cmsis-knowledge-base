---
id: "ts-svdconv-m129"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M129: Option unknown: …'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M129"
symptoms: ["M129", "Option unknown: %OPT%'"]
symptom_regex: "^Option unknown: .+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check given option 'OPT'."
summary: "svdconv was given a command-line option it does not recognise."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M129, source lines not available in this review)"]
---

## Symptom

`M129`
`Option unknown: %OPT%'`

## Cause

svdconv was given a command-line option it does not recognise. The variable part of the message, %OPT%, is the option name as the user typed it. The README cause is only 'Check given option', so the exact trigger could not be confirmed from source here.

## Fix

Run svdconv with --help to list the valid options, then correct or remove the option named in the message and run the command again.

## Note

Source lines were not available, so the trigger and the --help suggestion are inferred from the message text and the README rather than confirmed in code. The message text ends with a stray single quote after the variable; the README cause names the option as 'OPT'. The fix assumes --help lists the options, which was not checked.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M129, source lines not available in this review)`
