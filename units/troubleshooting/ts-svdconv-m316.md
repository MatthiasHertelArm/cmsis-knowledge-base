---
id: "ts-svdconv-m316"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M316: … <name> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M316"
symptoms: ["M316", "%LEVEL% <name> not set."]
symptom_regex: "^.+? <name> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "An element that needs a name has no <name> or an empty one; LEVEL says which (device, peripheral, cluster, register, field, enumeratedValue, cpu or interrupt)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:644", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1186", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1189", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:1193", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:135"]
---

## Symptom

`M316`
`%LEVEL% <name> not set.`

## Cause

An element that needs a name has no <name> or an empty one; LEVEL says which (device, peripheral, cluster, register, field, enumeratedValue, cpu or interrupt). Registers, clusters and fields that are dim lists are exempt. The element is dropped.

## Fix

Add a <name> that is a C identifier to the element at the reported line, for example <name>CTRL</name>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdItem.cpp:644`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1186`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1189`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:1193`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:135`
