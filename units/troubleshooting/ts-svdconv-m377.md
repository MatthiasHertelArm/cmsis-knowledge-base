---
id: "ts-svdconv-m377"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M377: … '…' (<enumeratedValues> '…'): '…' container conflicts with '…' …."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M377"
symptoms: ["M377", "%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): '%USAGE%' container conflicts with '%NAME3%' %LINE%."]
symptom_regex: "^.+? '.+?' \\(<enumeratedValues> '.+?'\\): '.+?' container conflicts with '.+?' .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdField.cpp:570-586", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdEnum.cpp:74-82", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:193-198"]
---

## Symptom

`M377`
`%LEVEL% '%NAME%' (<enumeratedValues> '%NAME2%'): '%USAGE%' container conflicts with '%NAME3%' %LINE%.`

## Cause

A <field> has a read-write <enumeratedValues> container (explicit <usage>read-write</usage> or no <usage>) together with a read or a write container. The read-write container already covers both directions, so the read or write container is ignored.

## Fix

Keep a single container for all values, or split them into exactly one <usage>read</usage> and one <usage>write</usage> container; add the missing <usage> to the container that has none.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdField.cpp:570-586`
- `tools/svdconv/SVDModel/src/SvdEnum.cpp:74-82`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:193-198`
