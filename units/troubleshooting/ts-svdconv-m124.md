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
summary: "With --generate=sfr on Windows, svdconv could not start SfrCC2.exe (opening the pipe to the command failed); PATH shows the command it tried."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:63-92", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:54"]
---

## Symptom

`M124`
`Cannot execute SfrCC2: '%PATH%'!`

## Cause

With --generate=sfr on Windows, svdconv could not start SfrCC2.exe (opening the pipe to the command failed); PATH shows the command it tried.

## Fix

Check that SfrCC2.exe exists next to svdconv.exe and can be started from a command prompt; otherwise use --generate=sfd.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:63-92`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:54`
