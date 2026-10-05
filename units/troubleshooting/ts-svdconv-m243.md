---
id: "ts-svdconv-m243"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M243: … '…' <dimArrayIndex> found, but <dim> does not describe an array"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M243"
symptoms: ["M243", "%LEVEL% '%NAME%' <dimArrayIndex> found, but <dim> does not describe an array"]
symptom_regex: "^.+? '.+?' <dimArrayIndex> found, but <dim> does not describe an array$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "A <peripheral> or <cluster> has <dim> and <dimArrayIndex>, but its <name> uses %s instead of ending with [%s], so it is not an array; svdconv also reports M229."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1524-1539", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:543-559", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:110"]
---

## Symptom

`M243`
`%LEVEL% '%NAME%' <dimArrayIndex> found, but <dim> does not describe an array`

## Cause

A <peripheral> or <cluster> has <dim> and <dimArrayIndex>, but its <name> uses %s instead of ending with [%s], so it is not an array; svdconv also reports M229.

## Fix

End the <name> with [%s] (e.g. UART[%s]) or remove the <dimArrayIndex>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1524-1539`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:543-559`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:110`
