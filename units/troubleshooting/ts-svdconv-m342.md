---
id: "ts-svdconv-m342"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M342: Dim-extended … '…' must not have <headerStructName>"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M342"
symptoms: ["M342", "Dim-extended %LEVEL% '%NAME%' must not have <headerStructName>"]
symptom_regex: "^Dim\\-extended .+? '.+?' must not have <headerStructName>$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:582", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCluster.cpp:591", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:161"]
---

## Symptom

`M342`
`Dim-extended %LEVEL% '%NAME%' must not have <headerStructName>`

## Cause

A cluster that is a dim list (name with %s, expanded into separately named clusters) also has a <headerStructName>; svdconv would ignore the header struct name.

## Fix

Remove <headerStructName> from clusters that are dim lists.

## Note

The only raise site is inside '#if 0' (SvdCluster.cpp:582), so svdconv at 30f5e81 never prints M342; cause and fix come from that disabled code and apply to older builds.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCluster.cpp:582`
- `tools/svdconv/SVDModel/src/SvdCluster.cpp:591`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:161`
