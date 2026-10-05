---
id: "ts-svdconv-m336"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M336: … '…' already defined …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M336"
symptoms: ["M336", "%LEVEL% '%NAME%' already defined %LINE%"]
symptom_regex: "^.+? '.+?' already defined .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:800", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:819", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:529", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:201", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:540", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:284", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:155"]
---

## Symptom

`M336`
`%LEVEL% '%NAME%' already defined %LINE%`

## Cause

Two elements in the same scope have the same name; LEVEL says which: registers or clusters with the same <name> (and <alternateGroup>) in one peripheral or cluster, fields with the same <name> in one register, two <interrupt>s with the same <name> but different <value>s, or the same index twice in a <dimIndex> list. Except for <dimIndex>, the later element is dropped.

## Fix

Rename or delete one of the two elements (LINE gives the first one). Registers that share a name on purpose need different <alternateGroup>s; an interrupt shared by two peripherals must have the same <value> in both.

## Note

The 'Enumerated Values Container' variant (SvdField.cpp:440) is not reached: its only caller is commented out (SvdField.cpp:596).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:800`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:819`
- `tools/svdconv/SVDModel/src/SvdRegister.cpp:529`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:201`
- `tools/svdconv/SVDModel/src/SvdDimension.cpp:540`
- `tools/svdconv/test/unittests/src/SvdModelValidationTest.cpp:284`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:155`
