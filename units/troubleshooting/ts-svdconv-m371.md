---
id: "ts-svdconv-m371"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M371: … '…' <headerStructName> is equal to hierarchical name"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M371"
symptoms: ["M371", "%LEVEL% '%NAME%' <headerStructName> is equal to hierarchical name"]
symptom_regex: "^.+? '.+?' <headerStructName> is equal to hierarchical name$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:569", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:570", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:571", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:497", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:190", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:254"]
---

## Symptom

`M371`
`%LEVEL% '%NAME%' <headerStructName> is equal to hierarchical name`

## Cause

A cluster's <headerStructName> equals the name svdconv derives from the hierarchy anyway (the names of peripheral and enclosing clusters joined with '_', for example TIM1_CH). svdconv drops the redundant headerStructName. Warning by default, error with --strict.

## Fix

Remove <headerStructName> from the cluster, or set it to a different type name if a specific one is wanted.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCluster.cpp:569`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:570`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:571`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:497`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:190`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:254`
