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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:719", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:722", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:723", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:304", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:312", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:185"]
---

## Symptom

`M366`
`Register '%NAME%' size (%NUM%Bit) is greater than <dimIncrement> * <addressBitsUnits> (%NUM2%Bit).`

## Cause

In a register array or list (<dim>), the register's <size> is larger than the distance between instances, <dimIncrement> times the device's <addressUnitBits> (the message calls it 'addressBitsUnits'), so consecutive instances would overlap. The register is dropped.

## Fix

Set <dimIncrement> to the address distance between instances in address units (bytes on Cortex-M), for example <dimIncrement>4</dimIncrement> for 32-bit registers, or correct the register's <size>.

## Note

The message names 'addressBitsUnits', which is not an SVD element; the schema element is <addressUnitBits> under <device>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:719`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:722`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:723`
- `tools/svdconv/SVDModel/src/SvdDimension.cpp:304`
- `tools/svdconv/SVDModel/src/SvdDimension.cpp:312`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:185`
