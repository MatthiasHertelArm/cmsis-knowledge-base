---
id: "ts-svdconv-m311"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M311: Field '…': Calculation: MSB or LSB == -1"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M311"
symptoms: ["M311", "Field '%NAME%': Calculation: MSB or LSB == -1"]
symptom_regex: "^Field '.+?': Calculation: MSB or LSB == \\-1$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv prints M311 when a field's bit-range calculation produces an MSB or LSB value of -1 for the field named in the message."
cause_origin: "source-analysis"
confidence: "low"
---

## Symptom

`M311`
`Field '%NAME%': Calculation: MSB or LSB == -1`

## Cause

svdconv prints M311 when a field's bit-range calculation produces an MSB or LSB value of -1 for the field named in the message. This points to a field whose bit offset or width in the SVD (bitOffset/bitWidth, or lsb/msb) is inconsistent so that the computed most or least significant bit falls outside the valid range, typically from a mismatched or negative offset or width in the input description. The exact input condition could not be confirmed from source here, since the clone was not available.

## Fix

Open the SVD and locate the field named in the message; check its bitOffset and bitWidth (or lsb and msb) for negative values, a zero or missing width, or a combination that yields an out-of-range bit position, then correct them and re-run svdconv.

## Note

Source lines were not provided, so the trigger condition and the exact input pattern are unverified; the cause is inferred from the message text only. The README states it is documented, but its cause and fix text was not supplied for comparison.
