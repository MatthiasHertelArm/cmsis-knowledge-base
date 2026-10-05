---
id: "ts-svdconv-m205"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M205: Tag <…> empty"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M205"
symptoms: ["M205", "Tag <%TAG%> empty"]
symptom_regex: "^Tag <.+?> empty$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Assign value to tag."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:1082-1087", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:72"]
---

## Symptom

`M205`
`Tag <%TAG%> empty`

## Cause

An element whose value svdconv converts (a number, boolean, access, usage or other token, an enumeratedValue <value>) is present but empty, e.g. <resetValue></resetValue> or <access/>. The element is treated as not set.

## Fix

Give the element a value, or remove it so the inherited or default value applies.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdUtils.cpp:1082-1087`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:72`
