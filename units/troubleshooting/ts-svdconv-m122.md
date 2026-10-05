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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check specified command."
summary: "An '@', which introduces a command file of options, was given on the svdconv command line without a file name after it."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/ParseOptions.cpp:403-430", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:52"]
---

## Symptom

`M122`
`Name of command file should follow '@'`

## Cause

An '@', which introduces a command file of options, was given on the svdconv command line without a file name after it.

## Fix

Put the command file name after '@' (e.g. @options.txt) or pass the options directly on the command line.

## Note

Not raised anywhere in svdconv at 30f5e81: the code appears only in the message table (SVDConv_Msgs.cpp:52) and the README (README.md:231). The cxxopts parser in this version has no '@' command-file handling.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDConv/src/ParseOptions.cpp:403-430`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:52`
