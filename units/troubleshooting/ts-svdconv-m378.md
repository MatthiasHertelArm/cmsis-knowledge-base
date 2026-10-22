---
id: "ts-svdconv-m378"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M378: Register Array: Register '…' size (…Bit) does not match <dimIncrement> (…Bit)."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M378"
symptoms: ["M378", "Register Array: Register '%NAME%' size (%NUM%Bit) does not match <dimIncrement> (%NUM2%Bit)."]
symptom_regex: "^Register Array: Register '.+?' size \\(.+?Bit\\) does not match <dimIncrement> \\(.+?Bit\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A register array (a <register> with <dim> and a <name> ending in [%s]) has a <dimIncrement> that is not exactly its size in bytes: svdconv requires dimIncrement*8 to equal the register <size> in bits, because the array is generated …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:715-735", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1501-1503", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:168-175", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/include/SvdPeripheral.h:104", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:199"]
---

## Symptom

`M378`
`Register Array: Register '%NAME%' size (%NUM%Bit) does not match <dimIncrement> (%NUM2%Bit).`

## Cause

A register array (a <register> with <dim> and a <name> ending in [%s]) has a <dimIncrement> that is not exactly its size in bytes: svdconv requires dimIncrement*8 to equal the register <size> in bits, because the array is generated as a contiguous C array; the register is dropped. svdconv also raises M378 for a <peripheral> whose <baseAddress> is missing or unparsable, and the text then still speaks of a register array.

## Fix

Make <dimIncrement> equal to the register size in bytes, e.g. <size>32</size> with <dimIncrement>4</dimIncrement>. If the registers are spaced further apart, use a %s list instead (<name>CH%s</name>) or put the register into a <cluster> array that carries the larger <dimIncrement>. If NAME is a peripheral, give it a valid <baseAddress>.

## Note

Misleading reuse: SvdPeripheral.cpp:1502 logs M378 (register-array text, NUM/NUM2 unset) for a peripheral without a valid <baseAddress>. M366 is the related check that the increment is not smaller than the register.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:715-735`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1501-1503`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:168-175`
- `tools/svdconv/SVDModel/include/SvdPeripheral.h:104`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:199`
