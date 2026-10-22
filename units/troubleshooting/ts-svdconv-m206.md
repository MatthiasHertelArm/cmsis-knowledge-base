---
id: "ts-svdconv-m206"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M206: DerivedFrom not found: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M206"
symptoms: ["M206", "DerivedFrom not found: '%NAME%'"]
symptom_regex: "^DerivedFrom not found: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check derivate."
summary: "The derivedFrom attribute names an element svdconv cannot find."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDerivedFrom.cpp:67-98", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:267-285", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/include/SvdItem.h:256-321", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:450-463", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:821-861", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:44-47", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:73"]
---

## Symptom

`M206`
`DerivedFrom not found: '%NAME%'`

## Cause

The derivedFrom attribute names an element svdconv cannot find. The source must be of the same kind (peripheral from peripheral, register from register, ...), must appear earlier in the file because derivedFrom is resolved while parsing, and is looked up among the siblings first and otherwise by a dotted path from the peripheral level (PERIPH.REG). The deriving element is dropped.

## Fix

Correct the spelling (case-sensitive) of the derivedFrom value, move the source element above the deriving one, and use the dotted path (e.g. derivedFrom="TIMER0.CR1") when the source lies in another peripheral or register.

## Note

NAME is printed with '%' characters removed. For a <dim> source the lookup compares the <name> as written, including %s or [%s] (SvdItem.cpp:450-463).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDerivedFrom.cpp:67-98`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:267-285`
- `tools/svdconv/SVDModel/include/SvdItem.h:256-321`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:450-463`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:821-861`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:44-47`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:73`
