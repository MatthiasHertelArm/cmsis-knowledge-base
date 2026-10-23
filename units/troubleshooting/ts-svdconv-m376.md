---
id: "ts-svdconv-m376"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M376: … '…' (<enumeratedValues> '…'): '…' container already defined in …."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M376"
symptoms: ["M376", "%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): '%USAGE%' container already defined in %LINE%."]
symptom_regex: "^.+? '.+?' \\(<enumeratedValues> '.+?'\\): '.+?' container already defined in .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "A <field> has two <enumeratedValues> containers with the same usage."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:554-566", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdEnum.cpp:74-82", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:193-197"]
---

## Symptom

`M376`
`%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): '%USAGE%' container already defined in %LINE%.`

## Cause

A <field> has two <enumeratedValues> containers with the same usage. A container without <usage> counts as read-write, so two containers that both omit <usage>, or both say read (or both write), collide; the second one is ignored.

## Fix

Merge the two containers into one, or set <usage>read</usage> on one and <usage>write</usage> on the other.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:554-566`
- `tools/svdconv/SVDModel/src/SvdEnum.cpp:74-82`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:193-197`
