---
id: "ts-svdconv-m124"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M124: Cannot execute SfrCC2: '…'!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M124"
symptoms: ["M124", "Cannot execute SfrCC2: '%PATH%'!"]
symptom_regex: "^Cannot execute SfrCC2: '.+?'!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check path to SfrCC2."
summary: "svdconv runs the external SfrCC2 compiler to generate the register-description output, and the executable at the path shown in the message could not be started."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M124`
`Cannot execute SfrCC2: '%PATH%'!`

## Cause

svdconv runs the external SfrCC2 compiler to generate the register-description output, and the executable at the path shown in the message could not be started. The %PATH% in the message is the location svdconv tried to execute, so the SfrCC2 binary is missing there or is not runnable by the current user.

## Fix

Check that SfrCC2 is installed and that the path shown in the message points to the actual executable; run that path directly to confirm it starts. If it is not on the expected location, correct the install or the path svdconv is configured to use, then re-run svdconv.

## Note

The clone was not available, so the trigger and the handling were not read from the source lines; the cause and fix rest on the message text and the README's 'Check path to SfrCC2' only. The exact conditions that select this message were not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
