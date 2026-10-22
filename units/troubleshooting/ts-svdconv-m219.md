---
id: "ts-svdconv-m219"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M219: C Code generation error: …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M219"
symptoms: ["M219", "C Code generation error: %MSG%"]
symptom_regex: "^C Code generation error: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The CMSIS header or partition generator (--generate=header, --generate=partition) met a layout it cannot express in C, wrote '#error \"MSG\"' into the generated file and reports it here; MSG names the problem."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:654", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:657", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_Register.cpp:123", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:608", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_Peripheral.cpp:130", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_EnumValues.cpp:354", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/PartitionData.cpp:239", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/PartitionData.cpp:884", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:255", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:283"]
---

## Symptom

`M219`
`C Code generation error: %MSG%`

## Cause

The CMSIS header or partition generator (--generate=header, --generate=partition) met a layout it cannot express in C, wrote '#error "MSG"' into the generated file and reports it here; MSG names the problem. Typical texts are 'Unaligned Registers are not supported', 'Cannot generate Register or Cluster ...: Address ... is lower than actual address in struct' (overlapping members), 'Peripheral size ... greater than <dimIncrement>', 'Enumerated Value ... already defined as Value ...' and 'SAU Regions Config / SAU Setup: Number of SAU regions not set'.

## Fix

Fix the element MSG points to: place a register at an address that is a multiple of its <size>; remove overlaps by correcting <addressOffset>, <size> or the peripheral array's <dimIncrement>; give each <enumeratedValue> a unique <name>; set <sauNumRegions> in <cpu> (1 to 255) before generating the partition file. Look at the validation messages printed earlier (for example M339, M364), which usually name the same cause.

## Note

Test CheckSauNumRegions_Errors expects two M219 after M364 when generating the partition file.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:654`
- `tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:657`
- `tools/svdconv/SVDGenerator/src/HeaderData_Register.cpp:123`
- `tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:608`
- `tools/svdconv/SVDGenerator/src/HeaderData_Peripheral.cpp:130`
- `tools/svdconv/SVDGenerator/src/HeaderData_EnumValues.cpp:354`
- `tools/svdconv/SVDGenerator/src/PartitionData.cpp:239`
- `tools/svdconv/SVDGenerator/src/PartitionData.cpp:884`
- `tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:255`
- `tools/svdconv/test/integtests/src/SvdConvIntegTests.cpp:283`
