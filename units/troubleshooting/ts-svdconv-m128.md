---
id: "ts-svdconv-m128"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M128: SfrCC2 reports warnings!"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M128"
symptoms: ["M128", "SfrCC2 reports warnings!"]
symptom_regex: "^SfrCC2 reports warnings!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check SVD file."
summary: "With --generate=sfr, SfrCC2.exe compiled the generated .sfd file and exited with code 1, i.e. it reported warnings."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:99-117", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:55", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:58"]
---

## Symptom

`M128`
`SfrCC2 reports warnings!`

## Cause

With --generate=sfr, SfrCC2.exe compiled the generated .sfd file and exited with code 1, i.e. it reported warnings. Its own output is printed just before, in the M125 'SfrCC2 report' block.

## Fix

Read the SfrCC2 report (M125) printed before this message and correct the SVD elements it points to; the .sfr file is still produced.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:99-117`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:55`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:58`
