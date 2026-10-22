---
id: "ts-svdconv-m366"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M366: Register '…' size (…Bit) is greater than <dimIncrement> * <addressBitsUnits> (…Bit)."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M366"
symptoms: ["M366", "Register '%NAME%' size (%NUM%Bit) is greater than <dimIncrement> * <addressBitsUnits> (%NUM2%Bit)."]
symptom_regex: "^Register '.+?' size \\(.+?Bit\\) is greater than <dimIncrement> \\* <addressBitsUnits> \\(.+?Bit\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD register's size in bits (the %NUM% value) is larger than the address span allotted to each array element, which is <dimIncrement> multiplied by <addressBitsUnits> (the %NUM2% value)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M366`
`Register '%NAME%' size (%NUM%Bit) is greater than <dimIncrement> * <addressBitsUnits> (%NUM2%Bit).`

## Cause

The SVD register's size in bits (the %NUM% value) is larger than the address span allotted to each array element, which is <dimIncrement> multiplied by <addressBitsUnits> (the %NUM2% value). In a register array the elements are spaced by dimIncrement, so a register wider than that spacing would overlap its neighbours in the generated address map. The check is inferred from the message text alone because the source lines were not available.

## Fix

Open the SVD file, find the register named %NAME% and its dim group, and make dimIncrement at least as large as the register size in bytes (or set addressBitsUnits to match the device's addressable unit). Then rerun svdconv.

## Note

Trigger not verified in source; cause and fix are inferred from the message wording and the README-documented meaning of the two bit values.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
