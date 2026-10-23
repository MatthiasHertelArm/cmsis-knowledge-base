---
id: "ts-svdconv-m109"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M109: Cannot find '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M109"
symptoms: ["M109", "Cannot find '%NAME%'"]
symptom_regex: "^Cannot find '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check specified file."
summary: "With --generate=sfr on Windows, svdconv looks for SfrCC2.exe in the directory of svdconv.exe and did not find it at the path shown."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:43-69", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:47-50", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:46"]
---

## Symptom

`M109`
`Cannot find '%NAME%'`

## Cause

With --generate=sfr on Windows, svdconv looks for SfrCC2.exe in the directory of svdconv.exe and did not find it at the path shown. This is the only place svdconv raises M109.

## Fix

Put SfrCC2.exe (from Keil MDK/uVision) into the same directory as svdconv.exe, or generate --generate=sfd instead, which needs no SfrCC2.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:43-69`
- `tools/svdconv/SVDConv/README.md:47-50`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:46`
