---
id: "ts-svdconv-m133"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M133: SFR generation is only supported on Windows (requires SfrCC2.exe)."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M133"
symptoms: ["M133", "SFR generation is only supported on Windows (requires SfrCC2.exe)."]
symptom_regex: "^SFR generation is only supported on Windows \\(requires SfrCC2\\.exe\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Generate SFR output on Windows with SfrCC2.exe installed alongside SVDConv, or use `--generate=sfd` for SFD output."
summary: "--generate=sfr was used on Linux or macOS."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:118-121", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:215-234", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:47-50", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:63"]
---

## Symptom

`M133`
`SFR generation is only supported on Windows (requires SfrCC2.exe).`

## Cause

--generate=sfr was used on Linux or macOS. SFR generation runs SfrCC2.exe, which exists only on Windows, so svdconv stops after the intermediate .sfd file and exits with code 2.

## Fix

Use --generate=sfd on Linux and macOS, or run --generate=sfr on Windows with SfrCC2.exe (from Keil MDK/uVision) in the same directory as svdconv.exe.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:118-121`
- `tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:215-234`
- `tools/svdconv/SVDConv/README.md:47-50`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:63`
