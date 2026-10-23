---
id: "ts-svdconv-m237"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M237: Nameless … must have <…>."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M237"
symptoms: ["M237", "Nameless %LEVEL% must have <%TAG%>."]
symptom_regex: "^Nameless .+? must have <.+?>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "A <cluster> named just %s (a nameless dim cluster whose instances are named by <dimIndex>) has no <dimName>. svdconv needs <dimName> as the generated type name and drops the cluster."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:596-602", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:104"]
---

## Symptom

`M237`
`Nameless %LEVEL% must have <%TAG%>.`

## Cause

A <cluster> named just %s (a nameless dim cluster whose instances are named by <dimIndex>) has no <dimName>. svdconv needs <dimName> as the generated type name and drops the cluster.

## Fix

Add <dimName> to the cluster, e.g. <name>%s</name><dim>2</dim><dimIncrement>0x10</dimIncrement><dimIndex>TX,RX</dimIndex><dimName>CHANNEL</dimName>, or give the cluster a real name such as CH%s.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDimension.cpp:596-602`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:104`
