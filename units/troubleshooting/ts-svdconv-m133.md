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
summary: "SVDConv prints M133 when SFR generation is requested on a host where the SfrCC2.exe helper is not available, which the message states is only supported on Windows."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M133`
`SFR generation is only supported on Windows (requires SfrCC2.exe).`

## Cause

SVDConv prints M133 when SFR generation is requested on a host where the SfrCC2.exe helper is not available, which the message states is only supported on Windows. The SFR output is produced by running SfrCC2.exe, so the request fails on Linux or macOS and on Windows installs that lack that executable next to SVDConv.

## Fix

Run the SFR generation on Windows with SfrCC2.exe installed alongside SVDConv, or request SFD output instead with --generate=sfd, as the README suggests.

## Note

Source lines were not available, so the trigger is taken from the message text and the README only; the exact check that raises M133 was not verified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
