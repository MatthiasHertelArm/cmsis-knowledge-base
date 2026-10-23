---
id: "ts-svdconv-m127"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M127: SfrCC2 reports errors!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M127"
symptoms: ["M127", "SfrCC2 reports errors!"]
symptom_regex: "^SfrCC2 reports errors!$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check SVD file."
summary: "With --generate=sfr, SfrCC2.exe compiled the generated .sfd file and exited with code 2 or higher, i.e. it found errors."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:99-116", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:55", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:57"]
---

## Symptom

`M127`
`SfrCC2 reports errors!`

## Cause

With --generate=sfr, SfrCC2.exe compiled the generated .sfd file and exited with code 2 or higher, i.e. it found errors. Its own output is printed just before, in the M125 'SfrCC2 report' block.

## Fix

Read the SfrCC2 report (M125) printed before this message, correct the SVD element that produced the reported .sfd line, and regenerate.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:99-116`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:55`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:57`
