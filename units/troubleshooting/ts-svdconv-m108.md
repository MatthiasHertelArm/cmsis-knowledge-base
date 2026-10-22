---
id: "ts-svdconv-m108"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M108: SfrDis not supported."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M108"
symptoms: ["M108", "SfrDis not supported."]
symptom_regex: "^SfrDis not supported\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:45", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:226"]
---

## Symptom

`M108`
`SfrDis not supported.`

## Cause

_open: to be written in the review_

## Fix

_open: to be written in the review_

## Note

No LogMsg call for this code exists in svdconv at 30f5e81; the code is only defined in the message table, so this version cannot print it. There is no SfrDis (disassembly) code in this tree; packchk's M108 ('Reading PDSC File failed!') is unrelated.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:45`
- `tools/svdconv/SVDConv/README.md:226`
