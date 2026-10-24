---
id: "ts-svdconv-m132"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M132: SfrCC2 report: … SfrCC2 report end."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M132"
symptoms: ["M132", "SfrCC2 report: %MSG% SfrCC2 report end."]
symptom_regex: "^SfrCC2 report:$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:62", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:240", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:108", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:119"]
---

## Symptom

`M132`
`SfrCC2 report: %MSG% SfrCC2 report end.`

## Cause

_open: to be written in the review_

## Fix

_open: to be written in the review_

## Note

No LogMsg call for this code exists in svdconv at 30f5e81; the code is only defined in the message table, so this version cannot print it. The SfrCC2 interface reports through M109, M124, M125, M127, M128 and, on hosts other than Windows, M133.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:62`
- `tools/svdconv/SVDConv/README.md:240`
- `tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:108`
- `tools/svdconv/SVDGenerator/src/SfrccInterface.cpp:119`
