---
id: "ts-svdconv-m232"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M232: Tag <…> name '…' must not have specifier '…'. Ignoring entry."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M232"
symptoms: ["M232", "Tag <%TAG%> name '%NAME%' must not have specifier '%CHAR%'. Ignoring entry."]
symptom_regex: "^Tag <.+?> name '.+?' must not have specifier '.+?'\\. Ignoring entry\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "A <peripheral> or <cluster> has a <headerStructName> that contains '%' (e.g. copied from a %s or [%s] name). svdconv ignores the headerStructName."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1512-1521", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:575-580", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:99"]
---

## Symptom

`M232`
`Tag <%TAG%> name '%NAME%' must not have specifier '%CHAR%'. Ignoring entry.`

## Cause

A <peripheral> or <cluster> has a <headerStructName> that contains '%' (e.g. copied from a %s or [%s] name). svdconv ignores the headerStructName.

## Fix

Use a plain C identifier in <headerStructName>, e.g. <headerStructName>TIMER</headerStructName>, without %s or [%s].

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1512-1521`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:575-580`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:99`
