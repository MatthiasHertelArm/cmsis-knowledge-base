---
id: "ts-svdconv-m313"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M313: Field '…': LSB > MSB: BitWith calculates to …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M313"
symptoms: ["M313", "Field '%NAME%': LSB > MSB: BitWith calculates to %NUM%"]
symptom_regex: "^Field '.+?': LSB > MSB: BitWith calculates to .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD input defines a peripheral field whose bit offset (LSB) is greater than its most significant bit (MSB), so the derived bit width (BitWith, computed as MSB minus LSB plus one) comes out zero or negative."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M313`
`Field '%NAME%': LSB > MSB: BitWith calculates to %NUM%`

## Cause

The SVD input defines a peripheral field whose bit offset (LSB) is greater than its most significant bit (MSB), so the derived bit width (BitWith, computed as MSB minus LSB plus one) comes out zero or negative. The %NAME% is the field name from the SVD and %NUM% is the computed width.

## Fix

Open the SVD file, find the field named in the message, and correct its bitOffset/bitWidth or lsb/msb values so that the least significant bit is not above the most significant bit. Then rerun svdconv on the corrected SVD.

## Note

Source lines were not available, so the trigger condition and the field-width formula are inferred from the message text and README rather than confirmed in the code. The exact XML element names to edit are also not verified against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
