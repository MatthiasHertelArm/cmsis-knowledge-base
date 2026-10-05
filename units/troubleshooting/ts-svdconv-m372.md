---
id: "ts-svdconv-m372"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M372: … <…> '…' already defined …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M372"
symptoms: ["M372", "%LEVEL% <%TAG%> '%NAME%' already defined %LINE%"]
symptom_regex: "^.+? <.+?> '.+?' already defined .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A name that must be unique across the whole device is used twice; TAG says which: a peripheral <name>, a peripheral or cluster <headerStructName>, a cluster's derived type name, or an <enumeratedValues> <headerEnumName>."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:381", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:390", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:398", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:415", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:440", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:446", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:480", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:191"]
---

## Symptom

`M372`
`%LEVEL% <%TAG%> '%NAME%' already defined %LINE%`

## Cause

A name that must be unique across the whole device is used twice; TAG says which: a peripheral <name>, a peripheral or cluster <headerStructName>, a cluster's derived type name, or an <enumeratedValues> <headerEnumName>. An element derived from the first one (derivedFrom) is exempt. The later element is dropped.

## Fix

Rename one of the two (LINE gives the first), or use derivedFrom when the second element is meant to reuse the first one's definition.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:381`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:390`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:398`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:415`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:440`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:446`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:480`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:191`
