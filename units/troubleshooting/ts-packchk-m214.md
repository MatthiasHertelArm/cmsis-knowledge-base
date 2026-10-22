---
id: "ts-packchk-m214"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M214: Invalid argument: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M214"
symptoms: ["M214", "Invalid argument: %OPT%"]
symptom_regex: "^Invalid argument: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk was started with a command-line argument it does not recognise."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (source not available; trigger inferred from message text only)"]
---

## Symptom

`M214`
`Invalid argument: %OPT%`

## Cause

packchk was started with a command-line argument it does not recognise. The %OPT% placeholder is the offending option text as the user typed it on the command line.

## Fix

Run packchk with its help option to list the valid arguments, then correct or remove the option named in the message and run it again.

## Note

Derived from the message wording and the absence of source lines, not from the code; the exact trigger condition in PackChk_Msgs.cpp was not checked. Not documented in the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (source not available; trigger inferred from message text only)`
