---
id: "ts-svdconv-m363"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M363: CPU: <sauNumRegions> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M363"
symptoms: ["M363", "CPU: <sauNumRegions> not set."]
symptom_regex: "^CPU: <sauNumRegions> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file describes a Cortex-M CPU block (the CPU element) but does not give a value for the sauNumRegions element, which is the number of regions in the Security Attribution Unit. svdconv prints M363 with that element name …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in clone; message text only)"]
---

## Symptom

`M363`
`CPU: <sauNumRegions> not set.`

## Cause

The SVD file describes a Cortex-M CPU block (the CPU element) but does not give a value for the sauNumRegions element, which is the number of regions in the Security Attribution Unit. svdconv prints M363 with that element name when it needs the value and the SVD omits it.

## Fix

Open the SVD file and add a <sauNumRegions> element inside the <cpu> block, with the number of SAU regions the device has (0 if the device has no SAU), then run svdconv again. The exact value must come from the device reference manual or the vendor SVD.

## Note

Reasoned from the message text and the element name only, because the clone was not available; the trigger condition itself was not read. The README documents the message as well, but its text was not supplied here to compare against.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in clone; message text only)`
