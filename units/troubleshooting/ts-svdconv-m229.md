---
id: "ts-svdconv-m229"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M229: Register '…' is not an array, <dimArrayIndex> is not applicable"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M229"
symptoms: ["M229", "Register '%NAME%' is not an array, <dimArrayIndex> is not applicable"]
symptom_regex: "^Register '.+?' is not an array, <dimArrayIndex> is not applicable$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "A <register>, <cluster> or <peripheral> has <dimArrayIndex> but is not an array: it has no <dim>, or its <name> does not end with [%s]."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdRegister.cpp:562-580", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1411-1429", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:430-448", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:96"]
---

## Symptom

`M229`
`Register '%NAME%' is not an array, <dimArrayIndex> is not applicable`

## Cause

A <register>, <cluster> or <peripheral> has <dimArrayIndex> but is not an array: it has no <dim>, or its <name> does not end with [%s]. The text always says 'Register', and NAME is the name of the <dimArrayIndex> container (often empty), not of the element.

## Fix

Make the element an array (<name>X[%s]</name> with <dim> and <dimIncrement>) or remove the <dimArrayIndex>.

## Note

For peripherals and clusters M242 or M243 is reported as well.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdRegister.cpp:562-580`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1411-1429`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:430-448`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:96`
