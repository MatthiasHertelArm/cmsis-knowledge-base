---
id: "ts-svdconv-m228"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M228: Enumerated Value Container: Only one Item allowed on this Level!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M228"
symptoms: ["M228", "Enumerated Value Container: Only one Item allowed on this Level!"]
symptom_regex: "^Enumerated Value Container: Only one Item allowed on this Level!$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Remove additional items."
summary: "The SVD file contains an enumeratedValues container with more than one enumeratedValue item, but the tool accepts only one at that level."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not inspected: clone not available)"]
---

## Symptom

`M228`
`Enumerated Value Container: Only one Item allowed on this Level!`

## Cause

The SVD file contains an enumeratedValues container with more than one enumeratedValue item, but the tool accepts only one at that level. Without the source lines the exact trigger cannot be confirmed; the README states the cause as additional items being present.

## Fix

Open the SVD file, find the enumeratedValues element that svdconv reports, and remove the extra enumeratedValue entries so that only one remains at that level, then run svdconv again.

## Note

Message text and README cause/fix were taken as given; the source trigger was not checked, so the wording of the cause is not confirmed against the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not inspected: clone not available)`
