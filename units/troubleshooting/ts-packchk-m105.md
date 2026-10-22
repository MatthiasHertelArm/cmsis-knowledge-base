---
id: "ts-packchk-m105"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M105: Error while parsing command arguments"
status: "draft"
tool: "packchk"
severity: "error"
code: "M105"
symptoms: ["M105", "Error while parsing command arguments"]
symptom_regex: "^Error while parsing command arguments$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk printed its generic command-line parsing error, meaning an argument passed to packchk was not accepted by its option parser."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available in this session; message text M105 'Error while parsing command arguments' only)"]
---

## Symptom

`M105`
`Error while parsing command arguments`

## Cause

packchk printed its generic command-line parsing error, meaning an argument passed to packchk was not accepted by its option parser. The offending argument is not named in the message itself, so the exact cause has to be read from the command line that was run.

## Fix

Run packchk with --help to list the accepted options, then correct the invalid or misspelled option and any missing option value in the command line, and run it again.

## Note

Source lines were not available, so the cause is inferred from the message text alone. The README does not document this message. Confirm the exact trigger in PackChk_Msgs.cpp before relying on this entry.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available in this session; message text M105 'Error while parsing command arguments' only)`
