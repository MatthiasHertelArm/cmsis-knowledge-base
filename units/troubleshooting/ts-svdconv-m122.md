---
id: "ts-svdconv-m122"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M122: Name of command file should follow '@'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M122"
symptoms: ["M122", "Name of command file should follow '@'"]
symptom_regex: "^Name of command file should follow '@'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check specified command."
summary: "svdconv was given an '@' argument for a command file but no file name follows the '@' on the command line, so the tool cannot read the command file it was asked to load."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M122`
`Name of command file should follow '@'`

## Cause

svdconv was given an '@' argument for a command file but no file name follows the '@' on the command line, so the tool cannot read the command file it was asked to load. The README only says to check the specified command, which matches this reading, but the source lines were not available to confirm the exact parsing.

## Fix

Check the svdconv command line and make sure the '@' is immediately followed by the path of the command file, for example '@commands.txt' rather than a bare '@' or '@' separated from its file name by a space. Then run svdconv again.

## Note

Source lines were not available, so the trigger and the handling are inferred from the message text and the README only; the exact condition in the code is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
