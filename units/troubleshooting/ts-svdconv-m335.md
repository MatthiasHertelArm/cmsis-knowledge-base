---
id: "ts-svdconv-m335"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M335: Value '…:…' does not fit into field '…' …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M335"
symptoms: ["M335", "Value '%NAME%:%NUM%' does not fit into field '%NAME2%' %BITRANGE%."]
symptom_regex: "^Value '.+?:.+?' does not fit into field '.+?' .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a register field value in the SVD file that is wider than the bit range the field declares."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in this clone; message text only)"]
---

## Symptom

`M335`
`Value '%NAME%:%NUM%' does not fit into field '%NAME2%' %BITRANGE%.`

## Cause

svdconv found a register field value in the SVD file that is wider than the bit range the field declares. The message names the offending value (%NAME%:%NUM%), the field (%NAME2%) and its bit range (%BITRANGE%). The SVD description is inconsistent: the value written for the field, typically an enumerated value or a reset value, needs more bits than the field's bitWidth or bit offset allows.

## Fix

Open the SVD file at the named peripheral, register and field, and compare the value with the field's bitOffset and bitWidth. Either correct the value so it fits the bit range, or widen the field's bitWidth if the hardware really uses more bits. Then rerun svdconv.

## Note

Cause and fix are inferred from the message text and the README entry; the source lines around the trigger were not available, so the exact check could not be confirmed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in this clone; message text only)`
