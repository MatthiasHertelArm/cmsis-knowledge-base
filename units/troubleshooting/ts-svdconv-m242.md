---
id: "ts-svdconv-m242"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M242: … '…' <dimArrayIndex> found, but no <dim>"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M242"
symptoms: ["M242", "%LEVEL% '%NAME%' <dimArrayIndex> found, but no <dim>"]
symptom_regex: "^.+? '.+?' <dimArrayIndex> found, but no <dim>$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1524-1539", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:543-559", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:109"]
---

## Symptom

`M242`
`%LEVEL% '%NAME%' <dimArrayIndex> found, but no <dim>`

## Cause

A <peripheral> or <cluster> has <dimArrayIndex> but no <dim>; svdconv also reports M229.

## Fix

Make it an array with <dim>, <dimIncrement> and a <name> ending in [%s], or remove the <dimArrayIndex>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1524-1539`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:543-559`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:109`
