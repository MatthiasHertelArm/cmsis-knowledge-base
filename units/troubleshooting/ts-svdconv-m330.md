---
id: "ts-svdconv-m330"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M330: Interrupt '…' Number not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M330"
symptoms: ["M330", "Interrupt '%NAME%' Number not set."]
symptom_regex: "^Interrupt '.+?' Number not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints this error when an interrupt entry in the SVD file has a name but no interrupt number."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M330`
`Interrupt '%NAME%' Number not set.`

## Cause

svdconv prints this error when an interrupt entry in the SVD file has a name but no interrupt number. The interrupt name is substituted for %NAME%. The number is required, so the device description is incomplete for that interrupt.

## Fix

Open the SVD file and find the <interrupt> element named %NAME%. Add a <value> child with the numeric IRQ number, for example <interrupt><name>NAME</name><value>10</value></interrupt>, then rerun svdconv.

## Note

Source lines were not available in this session, so the trigger and the cause are inferred from the message text and the README entry only. The exact XML element and the README wording were not checked against the source.
