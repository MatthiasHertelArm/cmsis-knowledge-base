---
id: "ts-svdconv-m301"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M301: Interrupt number '… : …' already defined: … …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M301"
symptoms: ["M301", "Interrupt number '%NUM% : %NAME%' already defined: %NAME2% %LINE%"]
symptom_regex: "^Interrupt number '.+? : .+?' already defined: .+? .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found two peripheral interrupt entries in the SVD that use the same interrupt number, so the number %NUM% is assigned to both %NAME% and %NAME2%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M301`
`Interrupt number '%NUM% : %NAME%' already defined: %NAME2% %LINE%`

## Cause

svdconv found two peripheral interrupt entries in the SVD that use the same interrupt number, so the number %NUM% is assigned to both %NAME% and %NAME2%. An SVD file must give each interrupt a unique number, and the duplicate is usually a copy-paste or generation mistake in the device description. The source lines were not available, so this reading is based on the message text and the README note only.

## Fix

Open the SVD file at the location referenced by the message (the line %LINE% shows where the second definition occurs) and change the <value> of one of the two <interrupt> entries so that each interrupt number is used once. Then rerun svdconv.

## Note

Trigger and handling were not checked against the source; the cause and fix rely on the message text and the README. The clone was unavailable, so the exact trigger condition is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
