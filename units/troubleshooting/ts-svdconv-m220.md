---
id: "ts-svdconv-m220"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M220: C Code generation warning: …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M220"
symptoms: ["M220", "C Code generation warning: %MSG%"]
symptom_regex: "^C Code generation warning: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "While generating the CMSIS header, the bit mask computed for a field came out even."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:660", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:663", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:784", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:846", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_PosMask.cpp:224", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:173", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:491"]
---

## Symptom

`M220`
`C Code generation warning: %MSG%`

## Cause

While generating the CMSIS header, the bit mask computed for a field came out even. That happens when the field width is 0 (for example <bitWidth>0</bitWidth>, or <lsb> exactly one above <msb>) and can also happen for a 64-bit field; svdconv adds the comment 'Even number for MASK detected!' next to the field's _Msk define.

## Fix

Correct the field's bit position so that it is at least one bit wide, for example <bitRange>[7:4]</bitRange> with the most significant bit first, or a <bitWidth> of 1 or more.

## Note

The other source of M220 ('Peripheral unaligned address', HeaderData_RegStructure.cpp:753) is unreachable because 'unaligned' is always 0 (line 37). The field check M313 only rejects negative widths, so a zero-width field reaches the generator.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:660`
- `tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:663`
- `tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:784`
- `tools/svdconv/SVDGenerator/src/HeaderGenerator.cpp:846`
- `tools/svdconv/SVDGenerator/src/HeaderData_PosMask.cpp:224`
- `tools/svdconv/SVDModel/src/SvdField.cpp:173`
- `tools/svdconv/SVDModel/src/SvdField.cpp:491`
