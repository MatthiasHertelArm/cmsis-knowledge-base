---
id: "ts-svdconv-m105"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M105: Cannot add Register to group sorter: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M105"
symptoms: ["M105", "Cannot add Register to group sorter: '%NAME%'"]
symptom_regex: "^Cannot add Register to group sorter: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:29", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:42", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:43", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:61", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:62", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/include/HeaderData.h:31", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_Register.cpp:49", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDGenerator/src/HeaderData_Register.cpp:130", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:42"]
---

## Symptom

`M105`
`Cannot add Register to group sorter: '%NAME%'`

## Cause

While generating the CMSIS device header, svdconv puts all registers and clusters of a peripheral or cluster that start in the same 32-bit word (address with the two low bits cleared) into one union, and that union holds at most 32 members per access size. NAME is the register that did not fit (for 32-bit registers the message already appears from the 31st member on), so far too many registers share one word address, usually through wrong <addressOffset> values or many alternate registers at one address.

## Fix

Give each register its correct <addressOffset> so that only intended aliases share an address, and keep intentional aliases (<alternateRegister>, <alternateGroup>) at one word address well below 30. The overlap messages M339/M365 name the registers that collide.

## Note

Only raised with --generate=header. The guard 'regItems > MAX_REGS' lets a 33rd entry be written into a 32-entry array (off by one).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:29`
- `tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:42`
- `tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:43`
- `tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:61`
- `tools/svdconv/SVDGenerator/src/HeaderData_RegStructure.cpp:62`
- `tools/svdconv/SVDGenerator/include/HeaderData.h:31`
- `tools/svdconv/SVDGenerator/src/HeaderData_Register.cpp:49`
- `tools/svdconv/SVDGenerator/src/HeaderData_Register.cpp:130`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:42`
